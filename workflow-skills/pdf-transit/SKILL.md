---
name: pdf-transit
description: PDF轉運站專用：PDF轉Markdown（標題/表格/圖片忠實保留）＋Groq免費中文精煉萃取＋歸檔第二大腦學習庫。當使用者提到「PDF轉md」「轉markdown」「中文精煉」「pdf轉運站」「論文翻譯摘要」或在00_PDF轉運站放檔案時，必須使用此 skill。
---

# PDF轉運站：PDF → MD → 中文精煉 → 學習庫

## 0. 路徑變數（每次執行先確認）

- 轉運站：`O:\我的雲端硬碟\AI_Project\03_opencode_project\00_PDF轉運站\`
  - `input/` 丟 PDF、`output/` 產出（`*.md`＋`assets/<sid>/`圖片）
- 第二大腦學習庫：`O:\我的雲端硬碟\AI_Project\00_colabrain\ColaBrain\學習庫\`
  - 未來分資料夾也沒問題：每篇圖隔離在自家 `assets/<sid>/`，整包搬移連結不斷
- 腳本：本 skill `scripts/`（`pdf2md.py`、`md2zh.py`，另見全域指令）
- 全域指令（已 `pip install -e`）：`pdf2md`、`md2zh`（任一目錄可用；改腳本直接改轉運站那份，editable 即時生效）

## 1. 鐵律

1. 只能另存新檔，禁覆寫（撞名加 `_new`／日期後綴）。
2. GROQ_API_KEY 只走當次環境變數（`$env:GROQ_API_KEY="gsk_..."`），禁寫檔、禁進 repo。
3. MarkItDown 不用於此流程（無標題、無圖片落地、表格保真 ~0.27、掃描件回空字串）。

## 2. 第一步：PDF → Markdown（免費本機）

```powershell
pdf2md input -o output
# 表格/雙欄爛掉換引擎：pdf2md "財報.pdf" -o output --engine pdfmux -q standard
```

- 預設 `pymupdf4llm`：最快＋圖片落地 `assets/<短id>/`；表格多/雙欄用 `--engine pdfmux`。
- 驗收：標題有 `#` 層級、表格 `|` 行數合理、圖片 `![](assets/...)` 連結對得到實檔。
- 掃描件（轉出空白）→ 明確 FAIL，不靜默丟失；免費解是 `pip install docling` 補 OCR。
- 長檔名 Windows 260 字元上限：腳本已用短 id＋暫存短路徑處理，勿改回全名。

## 3. 第二步：Markdown → 中文精煉萃取（Groq 免費 API）

```powershell
$env:GROQ_API_KEY="gsk_..."   # console.groq.com 免費申請，免信用卡
md2zh output/某篇.md --dry-run   # 先看切塊，不花額度
md2zh output/某篇.md             # 正式跑
# 產出：output/某篇_中文精煉萃取.md（每節：精煉摘要＋中文翻譯＋英文原文折疊）
```

- 預設模型 `qwen/qwen3.8-27b`（中文翻譯品質；`llama-3.3-70b-versatile` 已下架勿用）。
- 按 `##` 分塊（表格不切斷）；免費 TPM 約 8K/min，每塊間隔 30s，20 塊約 10–40 分鐘。
- 逐塊快取在 `.cache/md2zh/`，中斷重跑自動續跑；`--force` 才全重跑。
- 實戰排除表：
  - `error code: 1010`（Cloudflare 擋 urllib）→ 腳本已帶瀏覽器 UA，勿刪。
  - HTTP 429 → 腳本自動退避（60s 起跳×8 次），一直撞就放著跑完。
  - key 相關 403 → 到 console 重產生一把（貼對話的 key 用完即刪）。

## 4. 第三步：歸檔學習庫（第二大腦規範）

1. 檔名：`YYYY-MM-DD-簡短標題-中文精煉.md`。
2. frontmatter：`title/date/tags（含精煉萃取）/source_pdf/converter`。
3. 該篇 `output/assets/<sid>/` 整包拷到 `學習庫/assets/<sid>/`，維持相對連結。
4. 驗：所有 `![](...)` 相對學習庫都解析得到實檔；回報檔名＋bytes＋圖片數。
