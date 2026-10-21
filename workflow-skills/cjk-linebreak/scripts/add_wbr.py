"""在 HTML 可見的中文文字裡，於詞與詞之間加上 <wbr> 換行點。

搭配 CSS 的 `word-break: keep-all`，瀏覽器只會在 <wbr>、空白和標點換行，
避免把「自己」「血壓」這類詞拆成兩行。

用法（修改文案後重新執行即可，可重複執行）：
    pip install budoux==0.9.3
    python add_wbr.py site/index.html [其他.html ...] [--terms protected-terms.txt] [--show]

--terms  專案自己的保護詞彙檔，一行一個詞，# 開頭為註解，會加在內建清單之後。
--show   印出每段文字的切詞結果（以「｜」分隔），方便逐句檢查。
"""

import argparse
import pathlib
import re

import budoux

# 整個詞不可拆開。BudouX 的繁體中文模型常拆錯專有名詞和常用詞，
# 專案自己的品牌詞與人工檢查發現的詞，放在 --terms 指定的檔案。
COMMON_TERMS = [
    # 健康與專業用語
    "物理治療師", "物理治療", "人體工學", "心理諮商", "體適能", "肌耐力", "中高齡",
    "血壓紀錄", "血壓", "上班族", "使用者",
    # BudouX 常拆錯的常用詞
    "自己", "日常", "生活", "理解", "了解", "數位", "紀錄", "取代", "下載", "微小",
    "個人", "每日", "每天", "情境", "連結", "創造", "成效", "數字", "工具", "真的",
    "不只", "不是", "而是", "哪裡", "並非", "下一步", "做得到", "用得上", "放進",
    "把關", "有跡可循", "身心", "有限公司", "健康科技",
    # 數量詞
    "五分鐘", "一次", "一下", "一件", "一個", "一天", "一步", "一點", "一間", "一筆",
]

CJK = re.compile(r"[㐀-鿿豈-﫿]")
LATIN = re.compile(r"[A-Za-z0-9]")
TAG = re.compile(r"(<[^>]+>)")
SKIP_BLOCKS = ("script", "style", "title", "textarea", "pre", "code")


def load_terms(path):
    terms = list(COMMON_TERMS)
    if path:
        for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                terms.append(line)
    # 長的詞優先，避免只保護到一部分
    return sorted(set(terms), key=len, reverse=True)


def protected_spans(text, terms):
    spans = []
    for term in terms:
        for match in re.finditer(re.escape(term), text):
            spans.append((match.start(), match.end()))
    return spans


def add_breaks(text, parser, terms, show):
    if not CJK.search(text):
        return text
    segments = parser.parse(text)
    boundaries = []
    position = 0
    for segment in segments[:-1]:
        position += len(segment)
        boundaries.append(position)
    spans = protected_spans(text, terms)
    allowed = [
        b for b in boundaries
        if not any(start < b < end for start, end in spans)
        # 標點和空白本來就能換行，不需要再加 <wbr>
        and not text[b - 1].isspace() and not text[b].isspace()
        # 英文單字與數字不可拆開
        and not (LATIN.match(text[b - 1]) and LATIN.match(text[b]))
    ]
    pieces = []
    previous = 0
    for b in allowed:
        pieces.append(text[previous:b])
        previous = b
    pieces.append(text[previous:])
    if show and text.strip():
        print("  " + "｜".join(piece.strip() for piece in pieces if piece.strip()))
    return "<wbr>".join(pieces)


def process(html, parser, terms, show):
    html = html.replace("<wbr>", "")
    body_start = html.find("<body")
    if body_start < 0:
        body_start = 0
    head, body = html[:body_start], html[body_start:]
    parts = TAG.split(body)
    skipping = None
    for index, part in enumerate(parts):
        if part.startswith("<"):
            name = re.match(r"</?\s*([a-zA-Z0-9]+)", part)
            if name:
                tag = name.group(1).lower()
                if part.startswith("</") and tag == skipping:
                    skipping = None
                elif skipping is None and not part.startswith("</") and tag in SKIP_BLOCKS and not part.endswith("/>"):
                    skipping = tag
            continue
        if skipping is None and part:
            parts[index] = add_breaks(part, parser, terms, show)
    return head + "".join(parts)


def main():
    arg_parser = argparse.ArgumentParser(description="在中文詞與詞之間加上 <wbr>")
    arg_parser.add_argument("files", nargs="+", help="要處理的 HTML 檔案")
    arg_parser.add_argument("--terms", help="專案保護詞彙檔（一行一個詞）")
    arg_parser.add_argument("--show", action="store_true", help="印出切詞結果供逐句檢查")
    args = arg_parser.parse_args()

    parser = budoux.load_default_traditional_chinese_parser()
    terms = load_terms(args.terms)
    for file in args.files:
        path = pathlib.Path(file)
        if args.show:
            print(f"{path}:")
        original = path.read_text(encoding="utf-8")
        updated = process(original, parser, terms, args.show)
        path.write_text(updated, encoding="utf-8", newline="")
        print(f"{path.name}: <wbr> {updated.count('<wbr>')}")


if __name__ == "__main__":
    main()
