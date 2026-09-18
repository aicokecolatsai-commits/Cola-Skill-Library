"""PDF -> Markdown 免費轉換器 (pymupdf4llm 預設, pdfmux 可選)
用法:
  pdf2md <input.pdf | input_dir> [-o output_dir] [--engine pymupdf4llm|pdfmux]
輸出:
  output/<name>.md + output/assets/<name>-p<page>-<idx>.png
圖表忠實策略: 文字/表格轉 GFM, 圖片落地存檔並在 md 留連結, 不把圖硬轉文字.
"""
from __future__ import annotations
import argparse
import datetime
import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def short_id(name: str, keep: int = 40) -> str:
    """長檔名縮短: 前綴(去特殊字元, 截斷) + hash, 避開 Windows 260 字元路徑上限."""
    slug = re.sub(r"[^\w\-]+", "_", name).strip("_")[:keep].strip("_") or "doc"
    return f"{slug}_{hashlib.md5(name.encode('utf-8')).hexdigest()[:8]}"


def _normalize_img_refs(md_text: str, sid: str, img_files: list[Path]) -> str:
    """把 md 內圖片引用一律改成相對路徑 assets/<sid>/<檔名> (转換器產生的可能是 cwd 相對或絕對路徑)."""
    for f in img_files:
        pat = re.compile(r"!\[[^\]]*\]\([^)]*" + re.escape(f.name) + r"\)")
        md_text = pat.sub(f"![](assets/{sid}/{f.name})", md_text)
    return md_text


def convert_with_pymupdf4llm(pdf: Path, out_md: Path, assets_dir: Path) -> dict:
    import pymupdf4llm

    assets_dir.mkdir(parents=True, exist_ok=True)
    # pymupdf4llm 用輸入檔完整路徑當圖片檔名前綴, 長檔名會超過 Windows 路徑上限,
    # 先複製到短路徑暫存檔再轉
    sid = assets_dir.name
    tmpdir = Path(tempfile.gettempdir()) / "pdf2md" / sid
    tmpdir.mkdir(parents=True, exist_ok=True)
    tmp_pdf = tmpdir / (sid + ".pdf")
    shutil.copyfile(pdf, tmp_pdf)
    try:
        # write_images=True 會把圖存到 image_path, md 內自動引用
        md_text: str = pymupdf4llm.to_markdown(
            str(tmp_pdf),
            write_images=True,
            image_path=str(assets_dir),
            image_format="png",
            embed_images=False,
            page_chunks=False,
        )
    finally:
        try:
            tmp_pdf.unlink(missing_ok=True)
        except OSError:
            pass
    if not md_text or not md_text.strip():
        return {"ok": False, "reason": "empty-output(可能是掃描件, 無文字層)", "images": 0, "empty": True}

    imgs = sorted(assets_dir.glob("*.png")) + sorted(assets_dir.glob("*.jpg"))
    md_text = _normalize_img_refs(md_text, sid, imgs)
    header = (
        "---\n"
        f'title: "{pdf.stem}"\n'
        f"source_pdf: \"{pdf.name}\"\n"
        f"converter: pymupdf4llm\n"
        f"date: {datetime.date.today().isoformat()}\n"
        "---\n\n"
    )
    out_md.write_text(header + md_text, encoding="utf-8")
    return {"ok": True, "images": len(imgs), "chars": len(md_text)}


def convert_with_pdfmux(pdf: Path, out_md: Path, quality: str = "standard") -> dict:
    exe = shutil.which("pdfmux")
    if not exe:
        return {"ok": False, "reason": "找不到 pdfmux CLI, 請 pip install pdfmux"}
    out_md.parent.mkdir(parents=True, exist_ok=True)
    cmd = [exe, "convert", str(pdf), "-o", str(out_md), "-q", quality, "--no-strict", "--quiet"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        return {"ok": False, "reason": (r.stderr or r.stdout)[-500:]}
    if not out_md.exists():
        return {"ok": False, "reason": "pdfmux 未產出檔案"}
    return {"ok": True, "chars": len(out_md.read_text(encoding="utf-8", errors="ignore"))}


def convert_one(pdf: Path, out_dir: Path, engine: str, quality: str) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    assets_dir = out_dir / "assets"
    out_md = out_dir / (pdf.stem + ".md")
    # 批次時把圖集中到 assets/, 用子資料夾前綴避免檔名碰撞: pdfmux 不分圖, 只有 pymupdf4llm 需要
    if engine == "pdfmux":
        res = convert_with_pdfmux(pdf, out_md, quality)
    else:
        # 每份 PDF 獨立 assets 子資料夾; 用短 id 避開 Windows 路徑長度上限
        sid = short_id(pdf.stem)
        per_assets = assets_dir / sid
        res = convert_with_pymupdf4llm(pdf, out_md, per_assets)
    res.update({"pdf": str(pdf), "md": str(out_md), "engine": engine})
    return res


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="免費 PDF -> Markdown (圖/表忠實保留)")
    ap.add_argument("input", help="單一 .pdf 或含 PDF 的資料夾")
    ap.add_argument("-o", "--output", default="output", help="輸出資料夾 (預設 ./output)")
    ap.add_argument("--engine", choices=["pymupdf4llm", "pdfmux"], default="pymupdf4llm",
                    help="pymupdf4llm=最快+圖片落地, pdfmux=表格/閱讀順序最佳")
    ap.add_argument("-q", "--quality", default="standard", help="pdfmux 專用: fast|standard|high")
    args = ap.parse_args(argv)

    src = Path(args.input)
    out_dir = Path(args.output)
    if not src.exists():
        print(f"找不到輸入: {src}", file=sys.stderr)
        return 2

    if src.is_file():
        pdfs = [src]
    else:
        # Windows 檔案系統不分大小寫, *.pdf/*.PDF 會重複, 用 resolve 去重
        seen: dict[str, Path] = {}
        for p in sorted(src.glob("*.pdf")) + sorted(src.glob("*.PDF")):
            seen[str(p.resolve()).lower()] = p
        pdfs = sorted(seen.values())
    if src.is_file() and src.suffix.lower() != ".pdf":
        print("輸入必須是 .pdf 或資料夾", file=sys.stderr)
        return 2
    if not pdfs:
        print(f"資料夾內無 PDF: {src}", file=sys.stderr)
        return 2

    ok, fail = 0, 0
    for pdf in pdfs:
        print(f"[pdf2md:{args.engine}] {pdf.name} ...")
        try:
            res = convert_one(pdf, out_dir, args.engine, args.quality)
        except Exception as e:  # noqa: BLE001
            res = {"ok": False, "reason": str(e)[:300], "pdf": str(pdf)}
        if res.get("ok"):
            ok += 1
            extra = f"images={res.get('images','-')} chars={res.get('chars','-')}"
            print(f"  OK -> {res['md']} ({extra})")
        else:
            fail += 1
            print(f"  FAIL: {res.get('reason')}")
            if res.get("empty"):
                print("  提示: 疑似掃描件(無文字層), 免費解法是 pip install docling 再用 docling 轉, 或先 OCR 加文字層.")
    print(f"完成: 成功 {ok}, 失敗 {fail}, 輸出: {out_dir.resolve()}")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
