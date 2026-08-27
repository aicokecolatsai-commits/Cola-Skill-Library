#!/usr/bin/env python3
"""
notebooklm_patch_wiki.py

讀取剪貼簿中的 NotebookLM 自我核對結果，
解析每個 [引用來源] 區塊，比對對應的 wiki 卡，
並將查證紀錄回填至每張卡的「查證記錄」section。
"""

import re
import sys
import io
import subprocess
from datetime import datetime
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

WIKI_DIR = Path(r"E:\99_vault\aca_vault\mybrand\wiki")
SECTION_HEADER = "## 查證記錄（NotebookLM）"


# ── 讀取剪貼簿 ────────────────────────────────────────────────────────────────

def get_clipboard() -> str:
    result = subprocess.run(
        ["powershell", "-NoProfile", "-command", "Get-Clipboard -Raw"],
        capture_output=True, text=True, encoding="utf-8"
    )
    return result.stdout.strip()


# ── 解析驗證結果文字 ──────────────────────────────────────────────────────────

def parse_blocks(text: str) -> list[dict]:
    """把 NotebookLM 輸出切成 list of dict，每個 dict 是一個引用區塊。"""
    # 移除開頭的 [自我核對] 標題（若有）
    text = re.sub(r"^\[自我核對\]\s*", "", text.strip())

    raw_blocks = re.split(r"\[引用來源\]", text)
    blocks = []

    for raw in raw_blocks:
        raw = raw.strip()
        if not raw:
            continue

        block: dict = {}

        # 引用來源：從開頭到第一個 [ 欄位標籤
        src_match = re.match(
            r"^(.*?)(?=\[段落中的主張\]|\[文獻中的實際論述\]|\[驗證結果\]|\[說明\]|$)",
            raw, re.DOTALL
        )
        if src_match:
            block["引用來源"] = src_match.group(1).strip()

        for field in ["段落中的主張", "文獻中的實際論述", "驗證結果", "說明"]:
            pattern = (
                rf"\[{field}\]\s*(.*?)"
                rf"(?=\[(?:段落中的主張|文獻中的實際論述|驗證結果|說明)\]|$)"
            )
            m = re.search(pattern, raw, re.DOTALL)
            if m:
                block[field] = m.group(1).strip()

        if block.get("引用來源"):
            blocks.append(block)

    return blocks


# ── 從引用來源字串萃取 (姓氏, 年份) ──────────────────────────────────────────

def extract_citations(source_str: str) -> list[tuple[str, str]]:
    """
    "Aguirre-Rodriguez et al. (2012); Sirgy (1982)"
    → [("Aguirre-Rodriguez", "2012"), ("Sirgy", "1982")]
    """
    citations = []
    for part in re.split(r";\s*", source_str):
        m = re.match(
            r"^([A-Za-zÀ-ÿ\-]+(?:\s+(?:et\s+al\.?|and\s+[A-Za-z]+))?)\s*\((\d{4}[a-z]?)\)",
            part.strip()
        )
        if m:
            last_name = m.group(1).strip().split()[0].rstrip(",")
            year = m.group(2)
            citations.append((last_name, year))
    return citations


# ── 找對應的 wiki 卡 ──────────────────────────────────────────────────────────

def find_wiki_card(last_name: str, year: str) -> Path | None:
    # 嘗試精確 glob：LastName_Year_*.md
    matches = list(WIKI_DIR.glob(f"{last_name}_{year}_*.md"))
    if matches:
        return matches[0]
    # 不分大小寫 fallback
    prefix = f"{last_name.lower()}_{year}"
    for f in WIKI_DIR.iterdir():
        if f.name.lower().startswith(prefix):
            return f
    return None


# ── 將查證記錄寫入 wiki 卡 ────────────────────────────────────────────────────

def build_entry(block: dict, entry_index: int) -> str:
    lines = [f"\n**【論點 {entry_index}】**"]
    if block.get("段落中的主張"):
        lines.append(f"- **主張：** {block['段落中的主張']}")
    if block.get("文獻中的實際論述"):
        lines.append(f"- **文獻原述：** {block['文獻中的實際論述']}")
    result = block.get("驗證結果", "")
    emoji = {"正確": "✅", "部分正確": "⚠️", "錯誤": "❌"}.get(result, "")
    lines.append(f"- **驗證結果：** {emoji} {result}")
    if block.get("說明"):
        lines.append(f"- **說明：** {block['說明']}")
    return "\n".join(lines)


def patch_card(card_path: Path, entries: list[dict]) -> None:
    content = card_path.read_text(encoding="utf-8")
    today = datetime.now().strftime("%Y-%m-%d")

    new_section_lines = []

    if SECTION_HEADER not in content:
        new_section_lines.append(f"\n\n---\n\n{SECTION_HEADER}\n")
        new_section_lines.append(f"\n### {today}\n")
    else:
        new_section_lines.append(f"\n### {today}（補充）\n")

    for i, block in enumerate(entries, 1):
        new_section_lines.append(build_entry(block, i))

    content += "\n".join(new_section_lines) + "\n"
    card_path.write_text(content, encoding="utf-8")


# ── 主流程 ────────────────────────────────────────────────────────────────────

def main():
    print("讀取剪貼簿中的 NotebookLM 查證結果...")
    text = get_clipboard()
    if not text:
        print("❌ 剪貼簿是空的，請先複製 NotebookLM 的查證結果。")
        sys.exit(1)

    blocks = parse_blocks(text)
    if not blocks:
        print("❌ 找不到任何 [引用來源] 區塊，請確認格式是否正確。")
        sys.exit(1)

    print(f"✅ 解析到 {len(blocks)} 個引用區塊\n")

    # 以 wiki 卡為單位，聚合所有相關 block
    card_to_blocks: dict[Path, list[dict]] = {}
    unmatched: list[str] = []

    for block in blocks:
        source_str = block.get("引用來源", "")
        citations = extract_citations(source_str)

        if not citations:
            unmatched.append(source_str)
            continue

        for last_name, year in citations:
            card = find_wiki_card(last_name, year)
            if card:
                card_to_blocks.setdefault(card, []).append(block)
            else:
                unmatched.append(f"{last_name} ({year})")

    # 回填每張 wiki 卡
    if card_to_blocks:
        print("回填以下 wiki 卡：")
        for card, blks in card_to_blocks.items():
            patch_card(card, blks)
            result_emoji = {"正確": "✅", "部分正確": "⚠️", "錯誤": "❌"}
            results = [result_emoji.get(b.get("驗證結果", ""), "？") for b in blks]
            print(f"  {'  '.join(results)}  {card.name}  ({len(blks)} 筆)")
    else:
        print("⚠️  沒有成功比對到任何 wiki 卡。")

    if unmatched:
        print("\n⚠️  以下引用找不到對應的 wiki 卡：")
        for u in unmatched:
            print(f"   - {u}")

    print("\n完成。")


if __name__ == "__main__":
    main()
