---
name: pdf-transit
description: PDF轉運站專用：PDF轉Markdown（標題/表格/圖片忠實保留）＋Groq免費中文精煉萃取＋歸檔第二大腦學習庫。當使用者提到「PDF轉md」「轉markdown」「中文精煉」「pdf轉運站」「論文翻譯摘要」或在00_PDF轉運站放檔案時，必須使用此 skill。
---

# PDF轉運站：PDF → MD → 中文精煉 → 第二大腦

## 0. 先讀規範，再確認路徑（每次執行）

**存放位置、檔名、frontmatter 一律以 ColaBrain 的 `AGENTS.md` 為準**（「外部學習分類規則」「外部學習命名規則」「檔案類型規則」）。本技能只管「怎麼做」；兩邊衝突時以 `AGENTS.md` 為準。

- 轉運站（工作目錄）：`O:\我的雲端硬碟\AI_Project\03_opencode_project\00_PDF轉運站\`
  - `input/` 丟 PDF、`output/` 產出（`*.md`＋`assets/<sid>/`圖片）
- 第二大腦 vault：`O:\我的雲端硬碟\AI_Project\00_colabrain\ColaBrain\`（只放精煉摘要、密涅瓦萃取、被它們內嵌的圖片）
- 素材庫：`O:\我的雲端硬碟\AI_Project\00_colabrain\ColaBrain_素材庫\`（放原始 PDF、全文轉檔 md，路徑跟 vault 一模一樣）
- 先判斷 `media`：
  - `book`（書）→ 系列容器 `02_外部學習/01_書籍文獻/書籍/<分類>/BOOK_<作者>_<書名>/`，分章就一章一檔
  - `paper`（期刊論文）→ 不建容器，直接放 `02_外部學習/01_書籍文獻/文獻/`
  - 講義、投影片（某門課的教材）→ 該課容器的 `04_教材/`，放素材庫
  - 判斷不出來就停下來問使用者
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
- 需要密涅瓦萃取時，照 `密涅瓦思考模式技能`（minerva-thinking）的「輸出成檔：密涅瓦萃取」一節另產一份。

## 4. 第三步：歸檔第二大腦（照 AGENTS.md）

1. **改成正式檔名**（`<編號>_<標題>_<產出類型>.md`）：

   | 產出 | 書（`BOOK_<作者>_<書名>/` 容器內） | 論文（`文獻/` 底下） | 放哪 |
   | :--- | :--- | :--- | :--- |
   | pdf2md 全文 | `01_原始逐字稿/第01章_<章名>_逐字稿.md` | `<發表年>_<第一作者姓>_<短標題>_逐字稿.md` | 素材庫 |
   | md2zh 中文精煉 | `02_精煉摘要/第01章_<章名>_精煉摘要.md` | `<發表年>_<第一作者姓>_<短標題>_精煉摘要.md` | vault |
   | 密涅瓦萃取（選做） | `03_密涅瓦萃取/第01章_<章名>_密涅瓦.md` | `<發表年>_<第一作者姓>_<短標題>_密涅瓦.md` | vault |
   | 原始 PDF | `04_教材/<原檔名>.pdf` | 同路徑 `<原檔名>.pdf` | 素材庫 |

   - 整本不分章就用 `00` 當編號：`00_<書名>_精煉摘要.md`。
   - 例：`2022_Tran_遊戲化服藥遵從_精煉摘要.md`、`第03章_肩關節_精煉摘要.md`。
2. **frontmatter**（`type: source`）：`title`（完整標題）、`date`、`media: book|paper`、`expert`（作者）、`domain`、`course`（書名或期刊名）、`source_file`（全文 md 在素材庫的相對路徑）、`source_pdf`（原始 PDF 在素材庫的相對路徑）、`converter: pdf2md + md2zh`、`version`、`tags`（含 `精煉萃取`）。
3. **圖片**：精煉摘要內嵌的圖片（`output/assets/<sid>/`）整包拷到 vault 的精煉檔旁邊（`02_精煉摘要/assets/<sid>/`；論文就放 `文獻/assets/<sid>/`），維持相對連結。這是 `AGENTS.md` 允許的例外；只有全文 md 用到、精煉摘要沒用到的圖片放素材庫。
4. **驗收**：vault 裡所有 `![](...)` 都解析得到實檔；回報檔名＋bytes＋圖片數＋素材庫路徑。
5. 新增書或論文後，更新 `02_外部學習/01_書籍文獻/index.md`，並追加一筆 `04_核心知識/log.md`。

## 實戰紀錄

- 2026-11-02：歸檔改照 ColaBrain `AGENTS.md`：舊的 `學習庫/` 和 `YYYY-MM-DD-簡短標題-中文精煉.md` 停用；書用 `BOOK_` 容器，論文用 `<發表年>_<第一作者姓>_<短標題>`；全文與 PDF 進素材庫。
