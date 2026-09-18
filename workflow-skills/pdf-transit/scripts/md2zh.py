"""Markdown -> 中文精煉萃取 (Groq 免費 API)
用法:
  md2zh <input.md | 目錄> [-o 輸出目錄] [--model llama-3.3-70b-versatile] [--dry-run]
輸出:
  <同檔名>_中文精煉萃取.md — 每節: 精煉摘要 bullets 在前, 中文翻譯在後, 英文原文折疊保留.
  表格原文結構保留(內容中譯), 圖片連結原樣保留 + 中文圖說.
流程: 按 ## 標題分塊(表不切斷) -> Groq 逐塊翻譯+摘要 -> 組回原結構.
     免費額度 30 RPM, 預設每塊間隔 2.5 秒; 逐塊快取在 .cache/md2zh, 中斷可續跑.
前置: 到 https://console.groq.com 免費申請 key, 不需信用卡, 然後
  PowerShell: $env:GROQ_API_KEY="gsk_..."  (僅當次有效)
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import time
import urllib.request
from pathlib import Path

API_URL = "https://api.groq.com/openai/v1/chat/completions"
DEFAULT_MODEL = "qwen/qwen3.8-27b"
# Groq 前有 Cloudflare, 擋 Python-urllib 預設 UA (error 1010), 需偽裝瀏覽器
BROWSER_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
MAX_CHARS = 4000  # 每塊上限(配合免費 TPM 8K/min), 表格不切斷
SLEEP_SEC = 30.0  # 免費 TPM 約 8K/min, 每塊 input+output 約 4-5K tokens, 保守間隔
PROMPT_VERSION = "v1"

SYSTEM_PROMPT = """你是學術/專業文件的中文翻譯與精煉摘要助手。把使用者給的 Markdown 章節轉成繁體中文輸出, 嚴格遵守格式與規則。

輸出格式(照順序, 不可少):
### <中文標題>(原文標題可附後)
**精煉摘要**
- (3-6 條 bullets: 只寫關鍵發現/數據/結論, 每條一行, 數據保留原文數字)
**中文翻譯**
(忠實翻譯本節全文, 保留原文段落與小標題結構)

規則:
1. 專業術語首次出現用「中文(English)」, 之後直接用中文。
2. Markdown 表格必須完整保留(欄列不可刪), 儲存格內容譯成中文, 數字/單位/縮寫保留原文。
3. `![](...)` 圖片行原樣保留一行, 另起一行寫「圖說:<中文描述>」(依上下文 caption 推斷, 不要編造圖中數據)。
4. 不要省略、不要總結式跳段, 翻譯覆蓋率 100%。只輸出上述格式, 不加開場白。"""

CACHE_DIRNAME = ".cache/md2zh"


def split_frontmatter(text: str) -> tuple[str, str]:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[: end + 5], text[end + 5 :]
    return "", text


def split_sections(body: str, max_chars: int = MAX_CHARS) -> list[tuple[str, str]]:
    """按 ##(含#) 標題切塊; 單塊超長再按 ###/段落切, 不切斷表格. 回傳 (標題路徑, 內容)."""
    lines = body.splitlines()
    chunks: list[tuple[str, str]] = []
    cur_title = "前言"
    cur: list[str] = []

    def flush():
        if cur and "".join(cur).strip():
            chunks.append((cur_title, "\n".join(cur).strip()))

    for ln in lines:
        m = re.match(r"^(#{1,2})\s+(.*)", ln)
        if m and cur and "".join(cur).strip():
            flush()
            cur_title = m.group(2).strip()
            cur = [ln]
        else:
            cur.append(ln)
    flush()

    # 過長塊再切(避開表格列)
    out: list[tuple[str, str]] = []
    for title, content in chunks:
        if len(content) <= max_chars:
            out.append((title, content))
            continue
        parts: list[str] = []
        buf: list[str] = []
        for ln in content.splitlines():
            buf.append(ln)
            is_table = ln.strip().startswith("|")
            if len("\n".join(buf)) >= max_chars and not is_table and not ln.strip().startswith("|") and ln.strip() == "" or (
                len("\n".join(buf)) >= max_chars and not is_table and re.match(r"^#{3,4}\s+", ln)
            ):
                parts.append("\n".join(buf).strip())
                buf = []
        if buf and "".join(buf).strip():
            parts.append("\n".join(buf).strip())
        for i, p in enumerate(parts):
            out.append((f"{title} ({i+1}/{len(parts)})", p))
    return out


def cache_key(model: str, title: str, content: str) -> str:
    h = hashlib.md5((PROMPT_VERSION + model + title + content).encode("utf-8")).hexdigest()
    return h


def groq_chat(api_key: str, model: str, section_title: str, content: str,
              retries: int = 4) -> str:
    payload = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"## {section_title}\n\n{content}"},
        ],
        "temperature": 0.2,
        "max_completion_tokens": 3500,
    }).encode("utf-8")
    last_err = ""
    for attempt in range(8):
        req = urllib.request.Request(
            API_URL, data=payload,
            headers={"Authorization": f"Bearer {api_key}",
                     "Content-Type": "application/json", "User-Agent": BROWSER_UA},
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                data = json.loads(r.read().decode("utf-8"))
            return data["choices"][0]["message"]["content"].strip()
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "ignore")[:300]
            last_err = f"HTTP {e.code}: {body}"
            if e.code == 429:  # 免費額度撞牆: 讀 Retry-After, 保守等 60s+
                wait = 60 * (attempt + 1)
                m = re.search(r"[Rr]etry-[Aa]fter[\"':\s]+(\d+)", body)
                if m:
                    wait = max(wait, int(m.group(1)) + 5)
                print(f"    429 撞額度, 等待 {wait}s 後重試 ({attempt+1}/8)...")
                time.sleep(wait)
                continue
            time.sleep(10 * (attempt + 1))
        except Exception as e:  # noqa: BLE001 網路錯誤, 退避重試
            last_err = str(e)[:200]
            time.sleep(10 * (attempt + 1))
    raise RuntimeError(f"Groq 呼叫失敗(8次): {last_err}")


def process_one(md_path: Path, out_path: Path, model: str, api_key: str,
                cache_dir: Path, dry_run: bool, sleep_sec: float) -> dict:
    text = md_path.read_text(encoding="utf-8")
    front, body = split_frontmatter(text)
    sections = split_sections(body)
    if dry_run:
        total = sum(len(c) for _, c in sections)
        return {"ok": True, "dry_run": True, "sections": len(sections),
                "chars": total,
                "titles": [t for t, _ in sections][:30]}
    if not api_key:
        return {"ok": False, "reason": "缺少 GROQ_API_KEY (PowerShell: $env:GROQ_API_KEY=\"gsk_...\")"}
    cache_dir.mkdir(parents=True, exist_ok=True)
    parts = [front.rstrip() + "\n" if front else "",
             f"> 來源: `{md_path.name}` | 模型: `{model}` | 格式: 精煉摘要 + 中文翻譯 + 英文原文折疊\n"]
    for i, (title, content) in enumerate(sections, 1):
        print(f"  [{i}/{len(sections)}] {title[:50]} ...")
        key = cache_key(model, title, content)
        hit = cache_dir / (key + ".md")
        if hit.exists():
            zh = hit.read_text(encoding="utf-8")
        else:
            zh = groq_chat(api_key, model, title, content)
            hit.write_text(zh, encoding="utf-8")
            time.sleep(sleep_sec)
        parts.append(f"\n---\n\n{zh}\n\n<details><summary>英文原文: {title}</summary>\n\n{content}\n\n</details>\n")
    out_path.write_text("\n".join(parts), encoding="utf-8")
    return {"ok": True, "sections": len(sections), "md": str(out_path)}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Markdown -> 中文精煉萃取 (Groq 免費 API)")
    ap.add_argument("input", help="單一 .md 或資料夾")
    ap.add_argument("-o", "--output", default="", help="輸出檔/輸出目錄 (預設: 同目錄 <檔名>_中文精煉萃取.md)")
    ap.add_argument("--model", default=DEFAULT_MODEL, help=f"Groq 模型 (預設 {DEFAULT_MODEL})")
    ap.add_argument("--dry-run", action="store_true", help="只顯示切塊結果, 不呼叫 API")
    ap.add_argument("--force", action="store_true", help="忽略快取重跑全部")
    ap.add_argument("--sleep", type=float, default=SLEEP_SEC, help="每塊間隔秒數 (預設 30, 配合免費 TPM)")
    args = ap.parse_args(argv)

    src = Path(args.input)
    if not src.exists():
        print(f"找不到輸入: {src}", file=sys.stderr)
        return 2
    mds = [src] if src.is_file() else sorted(src.glob("*.md"))
    mds = [p for p in mds if "中文精煉萃取" not in p.name and p.is_file()]
    if not mds:
        print("無可處理的 .md", file=sys.stderr)
        return 2

    api_key = os.environ.get("GROQ_API_KEY", "").strip()
    ok = fail = 0
    for md in mds:
        if args.output and args.output.endswith(".md"):
            out = Path(args.output)
        elif args.output:
            out = Path(args.output) / (md.stem + "_中文精煉萃取.md")
        else:
            out = md.parent / (md.stem + "_中文精煉萃取.md")
        out.parent.mkdir(parents=True, exist_ok=True)
        cache_dir = md.parent / CACHE_DIRNAME
        if args.force and cache_dir.exists():
            shutil.rmtree(cache_dir, ignore_errors=True)
        print(f"[md2zh] {md.name} -> {out.name} ({len(mds)} 篇之 {mds.index(md)+1})")
        try:
            res = process_one(md, out, args.model, api_key, cache_dir, args.dry_run, args.sleep)
        except Exception as e:  # noqa: BLE001
            res = {"ok": False, "reason": str(e)[:300]}
        if res.get("ok"):
            ok += 1
            if res.get("dry_run"):
                print(f"  DRY-RUN: {res['sections']} 塊, 共 {res['chars']} 字")
                for t in res["titles"]:
                    print(f"    - {t[:70]}")
            else:
                print(f"  OK: {res['sections']} 節 -> {res['md']}")
        else:
            fail += 1
            print(f"  FAIL: {res.get('reason')}")
    print(f"完成: 成功 {ok}, 失敗 {fail}")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
