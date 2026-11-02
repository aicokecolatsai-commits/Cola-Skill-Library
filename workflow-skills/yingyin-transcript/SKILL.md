---
name: yingyin-transcript
description: 影音轉運站專用：影片/Podcast/課程轉逐字稿＋精煉筆記＋密涅瓦萃取。當使用者提到「轉逐字稿」「影片轉mp3」「SRT」「逐字稿md」「v2 心法/觀念/行動」「精煉筆記」「密涅瓦萃取」「PressPlay/Hahow/知識衛星/親子天下/Webinar/podcast/youtube轉」或在00_影音轉運站放素材時，必須使用此 skill。
title: 影音轉運站技能
date: 2026-09-18
updated: 2026-11-02
tags:
  - Skill
  - 影音轉運站
  - 逐字稿
  - 精煉筆記
  - 密涅瓦萃取
source: 00_影音轉運站/SKILL.md 統整版（9組prompt合一）
---

# 影音轉運站技能：素材 → 三種輸出

> 來源統整：PressPlay iframe、親子天下四階段、知識衛星 VTT、Hahow SOP、Webinar replay、podcast-to-summary、video-to-mp3 v2、faster-whisper 本機、密涅瓦萃取，共 9 組。
> 雙向關聯：[[02_外部學習/02_大師課程/專家概念總索引|專家概念總索引]]、[[07_智能技能/01_核心技能/密涅瓦思考模式技能/SKILL|密涅瓦思考模式技能]]、[[07_智能技能/03_影音技能/PressPlay逐字稿擷取技能/SKILL|PressPlay逐字稿擷取技能]]

## 0. 先讀規範，再確認路徑（每次執行）

**存放位置、資料夾、檔名、frontmatter 一律以 ColaBrain 的 `AGENTS.md` 為準**（「外部學習分類規則」「外部學習命名規則」「檔案類型規則」三段）。本技能只管「怎麼做」，不重複寫規則；兩邊衝突時以 `AGENTS.md` 為準。

- 素材區（工作目錄）：`O:\我的雲端硬碟\AI_Project\03_opencode_project\00_影音轉運站\`
  - `youtube轉/`、`podcast轉/`、`其他方式轉/`（PressPlay、Hahow、知識衛星、親子天下、Webinar、本機mp4/mp3 全丟對應夾）
- 第二大腦 vault：`O:\我的雲端硬碟\AI_Project\00_colabrain\ColaBrain\`（只放精煉摘要、密涅瓦萃取）
- 素材庫：`O:\我的雲端硬碟\AI_Project\00_colabrain\ColaBrain_素材庫\`（放逐字稿、講義、原始檔，路徑跟 vault 一模一樣）
- 先判斷 `media`，決定「系列容器」放哪裡（細節見 `AGENTS.md`）：
  - `course`（有章節的系列課）→ `02_外部學習/02_大師課程/<NN_主題>/<平台>_<課程名>/`
  - `youtube` → `02_外部學習/04_影音訪談/01_YouTube/<頻道名>/`
  - `podcast` → `02_外部學習/04_影音訪談/02_Podcast/<節目名>/`
- 三種輸出（容器內固定子資料夾，檔名 `<編號>_<標題>_<產出類型>.md`）：
  1. `01_原始逐字稿/<編號>_<標題>_逐字稿.md` → **放素材庫**
  2. `02_精煉摘要/<編號>_<標題>_精煉摘要.md` → 放 vault（15系預設、40系深挖、短片精簡版）
  3. `03_密涅瓦萃取/<編號>_<標題>_密涅瓦.md` → 放 vault（需要才產）
- 編號：課程用原本章節（`1-2`、`CH13`）；YouTube 用發布日 `2026-11-02`（`yt-dlp --print "%(upload_date)s"` 可查）；Podcast 用 `EP0894`（補到 4 位數）；全課程綜合用 `00`。
- 平台、頻道名查不到或分不出 `media` 時，停下來問使用者，不要自己編。

## 1. 鐵律：只能另存新檔，禁覆寫

1. 寫檔前先檢查目標路徑是否已存在同名檔。
2. 已存在 → 依序改名：`_new` → `_new_YYYYMMDD-HHmm` → 獨立子資料夾。
3. 全程不用覆蓋寫入；會撞名就停下來改名再存。

## 2. 輸入判斷（素材各式來源都吃）

1. 資料夾已有 mp3/mp4 → 跳到 §4 轉寫。
2. 有平台內建逐字稿/字幕 → 走 §3 平台直抓（免費、最準）。
3. 無字幕才走 Whisper：
   - 預設 Groq `whisper-large-v3-turbo`（快、word-level，需 GROQ_API_KEY）
   - 備援本地 faster-whisper `medium int8 CPU`（敏感/無網路/省錢）

## 3. 平台直抓法（有字幕優先，省 Whisper）

| 平台 | 抓法 | 關鍵點 |
|------|------|--------|
| YouTube | `yt-dlp.exe --no-update --list-subs` 有就下字幕，無才 `-x --audio-format mp3` | 中間檔用 ASCII 檔名避 cp950 亂碼；yt-dlp.exe 若無法執行改用 `python -m yt_dlp`（參數相同）；音檔 403 加 `--extractor-args "youtube:player_client=android"`；en-orig 列出卻抓不到時改抓 auto `en`；`--print "%(channel)s\|%(upload_date)s"` 取頻道名與發布日 |
| Podcast（Apple/Spotify/SoundOn/YT） | firecrawl 抓 Apple 頁拿標題+SoundOn 連結 → SoundOn player 頁拿 `og:audio`（302 真 mp3）→ 找不到才找同集 YT 版 | Spotify/Apple 中文集幾乎無內建稿，不浪費時間找 |
| PressPlay | Playwright 登入（認 `dtx_Cola`）→ iframe `src^="/vp/"` → 找 `^\d{2}:\d{2}$` 時間碼，parent last-child 即字幕 → `[{time,text}]` | 出現 iframe 立刻抓（會自動跳轉）；<200筆/10分或顯示同步中＝失敗重抓 |
| Hahow | 開 classroom → 先讀左側單元一覽回報章/集 → 逐集單線程：evaluate 找標題往上找 `cursor=pointer` 父元素點入 → 點「逐字稿」tab → `querySelectorAll('p')` 過濾 `offsetParent!==null` | 無稿顯示「尚未提供」才走 jwplayer HLS：`jwplayer().getPlaylist()[0].sources[0].file` 立刻 ffmpeg 下 mp3（簽章時效短）；導讀缺稿記缺集不硬湊；特殊符號用短關鍵字 |
| 知識衛星 sat.cool | `page.evaluate()` 抓 h6（跳過課前準備/章節標題）→ `page.on('response')` 監聽 `captions.cloud.vimeo.com` .vtt → evaluate 點 h6、等3秒、點播放 → 抓到立刻 Invoke-WebRequest（時效短）→ 去 WEBVTT/時間碼/純數字行轉 MD | 禁用 locator.click()（會跳轉）；中文路徑用 Write tool 寫 .js 跑，不用 node -e；按官網順序 01~NN 編號 |
| 親子天下 learning.parenting | Playwright 登入（Google+手機2FA等 OK）→ 列單元確認集數 → network 找 `kaik.io/.../playback_info` 取 playback_id/token → `ffmpeg -headers "Referer: https://player.loopix.com/"` 下 m3u8 | token 約6hr，時效內下完；下完 `ffmpeg -i -f null -` 驗 moov；失敗重進拿新 token |
| Webinar replay | 進 replay URL，被導 /login 就 snapshot 認姓名+Email 表單請使用者給 → 認 Video Player/Remaining Time/Progress Bar → network `static=true filter \.(mp4\|m3u8)` 找 CloudFront MP4（206 正常） | 找不到改 filter `video\|stream\|media`；過期重 navigate 刷新；只用官方登入+可見 URL |

## 4. Whisper 轉寫（無字幕才用）

先載入 `audio-to-srt` skill。腳本：`~\.config\opencode\skills\audio-to-srt\scripts\`（`~` 是目前使用者的家目錄）。

### 4a. Groq 預設管線（推薦）

```powershell
$env:GROQ_API_KEY = Get-Content ~\.groq_api_key -Raw | ForEach-Object { $_.Trim() }
ffmpeg -i $in -vn -ac 1 -ar 16000 -b:a 32k -y _mp3/<base>.mp3
python transcribe_groq.py _mp3/<base>.mp3 --out _subtitles/<base>.groq.json   # 已存在就 SKIP
python resegment.py _subtitles/<base>.groq.json --out _subtitles/<base>.raw.srt
python apply_vocab.py _subtitles/<base>.raw.srt --out _subtitles/<base>.vocab.srt
Copy-Item -LiteralPath _subtitles/<base>.vocab.srt _subtitles/<base>.clean.srt  # validate 不會自己產 clean，一定要先 copy
python validate_srt.py --raw _subtitles/<base>.vocab.srt --clean _subtitles/<base>.clean.srt
python srt_to_txt.py _subtitles/<base>.clean.srt --out _transcripts/<base>.md
```

- mp4 轉 mp3 用 `-vn -ac 1 -ar 16000 -b:a 32k`；大檔自動壓，驗收 mp3>0KB。
- 路徑有 `[]` 一律 `-LiteralPath`、全路徑操作不 cd；中文檔名 PowerShell 易亂碼，用 Get-ChildItem 掃目錄取檔，先 `$env:PYTHONIOENCODING="utf-8"`。
- 1hr 節目約 55-70MB / 13k-17k 詞；上下集分開轉最後合併。

### 4b. 本機備援（faster-whisper，不上雲）

`yt-dlp 下載 → ffmpeg 轉 16kHz mono wav → faster-whisper medium int8 CPU → 含時間戳 txt → merge.py（間隔>1.5s 或 >350字切一段）→ 逐字稿.md`

## 5. 三種輸出格式（嚴格執行）

三種輸出共用的 frontmatter 欄位（依 `AGENTS.md`；模板見 `09_標準模板/01_筆記模板/外部學習筆記.md`）：

```yaml
title: "[完整標題]"          # 可以比檔名長
date: "[YYYY-MM-DD]"
type: "source"
media: "course"               # course | youtube | podcast
expert: "[講者]"
domain: [主題1, 主題2]
course: "[<平台>_<課程名>／頻道名／節目名]"
platform: "[知識衛星、HaHow、YouTube…]"
episode: "[章節或集數]"
source_url: "[原始網址]"
tags: [主題tag, 產出類型tag]
```

### A. 逐字稿 `<編號>_<標題>_逐字稿.md`（放素材庫）

```md
---
（共用欄位）
instructor: [講師，可空]
chapter: [章節，可空]
---

# [完整標題]

[全文，PressPlay 格式為 [{time}]\n{text} 每筆空一行]
```

### B. 精煉摘要 `<編號>_<標題>_精煉摘要.md`（放 vault，預設 15系）

```md
---
（共用欄位）
source_file: "[逐字稿在素材庫的相對路徑，例：02_外部學習/02_大師課程/06_財務思維/知識衛星_超級數字力/01_原始逐字稿/2-1_損益表_逐字稿.md]"
version: 1                    # 重做就 +1，不寫進檔名
template: "15系"              # 精簡 | 15系 | 40系
---

# [課程名稱]

## 📌 主要摘要說明
[200-300字核心摘要]

## 📋 本集流程說明
[200-300字教學流程與邏輯]

## 💡 核心內容與心法（15句）
1. [15-25字金句] ...共15句

## 🔑 關鍵觀念與如何執行（15條）
1. **[概念]**：[一句話] → **執行方式**：[一句話] ...共15條

## 🎯 具體行動步驟（15條）
1. [可立即執行] ...共15條
```

- 變體：podcast 版 15觀念用表格 `| # | 觀念 | 執行方式 |`、15行動分5階段x3、加 Mermaid `flowchart TB`＋5-6行說明＋文末 AI 整理聲明。
- 變體：深挖版 40系（三節各恰好40條：40心法/40觀念/40行動，每條1-3行、忠於稿），`template: "40系"`。同一集同時有 15系和 40系時，40系檔名在標題後加 `（40系）`，例：`EP1250_密涅瓦大學核心秘密（40系）_精煉摘要.md`。
- 集數多用 Task 平行（每批4-5集，PressPlay 8-12篇），每批都要足數。
- 驗證：txt>5000字才算成功；md 必含 15+15+15（或40+40+40），缺一段重補。
- 內容量分級：逐字稿 <2000字（Shorts/短片約<2分鐘）走精簡版（摘要＋流程＋5心法＋5觀念＋5行動＋Mermaid，`template: "精簡"`，不硬湊15，**檔名不加後綴**）；≥5000字走標準15系；長課可選40系。英文改算單字數：<1000 words 走精簡版，≥1000 words 走15系。密涅瓦同理：短片只萃取有據部分，L1-L5 從缺留空不硬寫。
- 可選：多集綜合 `00_綜合摘要_精煉摘要.md`（15+15+15＋全課程流程總覽）＋ Word 整合（python-docx、A4、微軟正黑體、封面＋目錄＋每集分頁，Heading1 18pt、Heading2 14pt、內文11pt；Word 檔不進 vault，放素材庫 `04_教材/`）。

### C. 密涅瓦萃取 `<編號>_<標題>_密涅瓦.md`（放 vault，需要才產）

格式、四鏡頭結構與鐵律統一定義在 [[07_智能技能/01_核心技能/密涅瓦思考模式技能/SKILL|密涅瓦思考模式技能]] 的「輸出成檔：密涅瓦萃取」一節，照那裡產出；frontmatter 同 B（`source_file` 指向逐字稿）。

## 6. 工作目錄規範＋回報

### 檔名對照規則（檔名必須一看即知內容）
- 中間檔（`_mp3/`、`_subtitles/`）用 ASCII 代號（如 ep1245）避 cp950 亂碼；中間檔只留在素材區，不進 vault 和素材庫。
- 最終三種輸出一律用 `<編號>_<標題>_<產出類型>.md`，標題用中文原標（英文素材可用英文原標），禁止只留 ep1245 這種代號。
  例：`EP1245_量化求職一生受用的求職方法_精煉摘要.md`、`2026-08-25_WhatIsErgonomics_密涅瓦.md`、`3-7_創業要準備多少錢_逐字稿.md`
- 標題不用半形 `\ / : * ? " < > |`（可用全形 `：｜`），太長縮到 40 字內。
- 每次建對照表：ASCII 代號 ↔ 正式檔名 ↔ 原始素材名，回報時附上。

- 素材區單課一資料夾：`videos/ _subtitles/ _mp3/ _transcripts/ _v2/`（Hahow 用 `ch01 ch02…`，知識衛星用 `01~NN`，小課用 `NN-標題`）。
- youtube轉固定四夾：`_mp3/ _subtitles/ _transcripts/ _v2/`，散檔禁止；單片中間檔（mp3/srt/txt）進對應夾，最終三種才放 _transcripts/_v2。
- 每集存檔成功才做下一集（Hahow 強制單線程）；結束回報筆數/bytes/末段文字/檔案大小/頁數＋缺集清單。
- 批次結束統計：逐字稿數、精煉摘要數、密涅瓦數、缺漏表。

### 兩段式歸檔（先審後歸，不可跳過）
- 三種產出先組裝到 `00_影音轉運站/_待審/<容器名>/`，裡面已照最終結構分好 `01_原始逐字稿/ 02_精煉摘要/ 03_密涅瓦萃取/`＋對照表，不直接進第二大腦。
- 回報待審清單，附上預計的 `media`、主題、容器名稱，等使用者說「可歸檔」（可同時改主題或名稱）才搬：
  - `01_原始逐字稿/` → 素材庫的容器路徑
  - `02_精煉摘要/`、`03_密涅瓦萃取/` → vault 的容器路徑
- 歸檔後執行 `python 10_自動腳本/reindex_experts.py` 更新索引，並追加一筆 `04_核心知識/log.md`。
- 退件就在 _待審內重產（加 `_new`，禁覆寫）；歸檔後刪除該課的 _待審資料夾。

## 7. 英文素材特例

- 轉寫：同 Groq 管線，但**跳過 apply_vocab.py**（它會把 Cloud/cloud 全換成 Claude，英文談雲端即毀稿）；`raw.srt` 直接複製為 `clean.srt` 再 validate。
- 精煉摘要／密涅瓦：照產**繁中**，英文專有名詞保留原文括號附註；Mermaid 節點用英文原文＋中文對照。
- 密涅瓦金句：英文短句每條≤10 words（中文仍十字）。
- 存檔：不另建英文區，照 `media` 放同一套容器；檔名可用英文原標（ASCII 本來就安全）；frontmatter 加 `lang: en`、tags 加 `英文`；逐字稿留英文原文不翻。

## 實戰紀錄

- 2026-09-18：9 組 prompt 統整初版，素材區 `00_影音轉運站/`，輸出 `02_重新整理與分類(含密涅瓦)/` 14 主題。
- 2026-11-02：改照 ColaBrain `AGENTS.md` 的分類與命名規則輸出：逐字稿進素材庫，vault 只放精煉摘要與密涅瓦；檔名 `<編號>_<標題>_<產出類型>.md`，版本與深度改寫 frontmatter；密涅瓦格式移到密涅瓦思考模式技能統一定義。
