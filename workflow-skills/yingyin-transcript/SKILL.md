---
name: yingyin-transcript
description: 影音轉運站專用：影片/Podcast/課程轉逐字稿＋精煉筆記＋密涅瓦萃取。當使用者提到「轉逐字稿」「影片轉mp3」「SRT」「逐字稿md」「v2 心法/觀念/行動」「精煉筆記」「密涅瓦萃取」「PressPlay/Hahow/知識衛星/親子天下/Webinar/podcast/youtube轉」或在00_影音轉運站放素材時，必須使用此 skill。
---

# 影音轉運站：素材 → 三種輸出

## 0. 路徑變數（每次執行先確認）

- 素材區：`O:\我的雲端硬碟\AI_Project\03_opencode_project\00_影音轉運站\`
  - `youtube轉/`、`podcast轉/`、`其他方式轉/`（PressPlay、Hahow、知識衛星、親子天下、Webinar、本機mp4/mp3 全丟對應夾）
- 第二大腦：`O:\我的雲端硬碟\AI_Project\00_colabrain\ColaBrain\專業領域\02_重新整理與分類(含密涅瓦)\`
  - 底下 14 主題（人生經營、工作流與生產力、房產投資、思考方法、財務思維、健康照護、業務銷售、遊戲化設計、管理領導、寫作變現、親子理財、總體經濟、簡報表達、AI生產力）→ 按主題再存
- 三種輸出（檔名後綴區分）：
  1. `NN-標題.md` ＝ 逐字稿（原始）
  2. `NN-標題-v2.md` ＝ 精煉筆記（15系預設、40系深挖）
  3. `NN-標題-密涅瓦.md` ＝ 密涅瓦萃取（需要才產）

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
| YouTube | `yt-dlp.exe --no-update --list-subs` 有就下字幕，無才 `-x --audio-format mp3` | 中間檔用 ASCII 檔名避 cp950 亂碼 |
| Podcast（Apple/Spotify/SoundOn/YT） | firecrawl 抓 Apple 頁拿標題+SoundOn 連結 → SoundOn player 頁拿 `og:audio`（302 真 mp3）→ 找不到才找同集 YT 版 | Spotify/Apple 中文集幾乎無內建稿，不浪費時間找 |
| PressPlay | Playwright 登入（認 `dtx_Cola`）→ iframe `src^="/vp/"` → 找 `^\d{2}:\d{2}$` 時間碼，parent last-child 即字幕 → `[{time,text}]` | 出現 iframe 立刻抓（會自動跳轉）；<200筆/10分或顯示同步中＝失敗重抓 |
| Hahow | 開 classroom → 先讀左側單元一覽回報章/集 → 逐集單線程：evaluate 找標題往上找 `cursor=pointer` 父元素點入 → 點「逐字稿」tab → `querySelectorAll('p')` 過濾 `offsetParent!==null` | 無稿顯示「尚未提供」才走 jwplayer HLS：`jwplayer().getPlaylist()[0].sources[0].file` 立刻 ffmpeg 下 mp3（簽章時效短）；導讀缺稿記缺集不硬湊；特殊符號用短關鍵字 |
| 知識衛星 sat.cool | `page.evaluate()` 抓 h6（跳過課前準備/章節標題）→ `page.on('response')` 監聽 `captions.cloud.vimeo.com` .vtt → evaluate 點 h6、等3秒、點播放 → 抓到立刻 Invoke-WebRequest（時效短）→ 去 WEBVTT/時間碼/純數字行轉 MD | 禁用 locator.click()（會跳轉）；中文路徑用 Write tool 寫 .js 跑，不用 node -e；按官網順序 01~NN 編號 |
| 親子天下 learning.parenting | Playwright 登入（Google+手機2FA等 OK）→ 列單元確認集數 → network 找 `kaik.io/.../playback_info` 取 playback_id/token → `ffmpeg -headers "Referer: https://player.loopix.com/"` 下 m3u8 | token 約6hr，時效內下完；下完 `ffmpeg -i -f null -` 驗 moov；失敗重進拿新 token |
| Webinar replay | 進 replay URL，被導 /login 就 snapshot 認姓名+Email 表單請使用者給 → 認 Video Player/Remaining Time/Progress Bar → network `static=true filter \.(mp4\|m3u8)` 找 CloudFront MP4（206 正常） | 找不到改 filter `video\|stream\|media`；過期重 navigate 刷新；只用官方登入+可見 URL |

## 4. Whisper 轉寫（無字幕才用）

先載入 `audio-to-srt` skill。腳本：`C:\Users\COLA\.config\opencode\skills\audio-to-srt\scripts\`。

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

### A. 逐字稿 `NN-標題.md`

```md
---
title: [完整標題]
date: [YYYY-MM-DD]
tags: [主題tag, 逐字稿]
source: [URL或原始檔名]
instructor: [講師，可空]
chapter: [章節，可空]
---

# [完整標題]

[全文，PressPlay 格式為 [{time}]\n{text} 每筆空一行]
```

### B. 精煉筆記 `NN-標題-v2.md`（預設 15系）

```md
---
title: [課程名稱]
date: [YYYY-MM-DD]
tags: [主題tag, 精煉筆記]
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
- 變體：深挖版 40系（三節各恰好40條：40心法/40觀念/40行動，每條1-3行、忠於稿）。
- 集數多用 Task 平行（每批4-5集，PressPlay 8-12篇），每批都要足數。
- 驗證：txt>5000字才算成功；md 必含 15+15+15（或40+40+40），缺一段重補。
- 可選：多集 `綜合摘要-v2.md`（15+15+15＋全課程流程總覽）＋ Word 整合（python-docx、A4、微軟正黑體、封面＋目錄＋每集分頁，Heading1 18pt、Heading2 14pt、內文11pt）。

### C. 密涅瓦 `NN-標題-密涅瓦.md`（需要才產）

四鏡頭固定結構：批判性（核心問題＋證據L1-L5表＋4條件限制＋3具名偏誤）→ 創意思考（類比映射表＋4邊界＋設計思考五階段表）→ 有效溝通（受眾分層表＋4-7條七字金句＋多模態文字/圖表/行動）→ 有效互動（利害關係人圖譜＋增強/平衡雙迴路＋槓桿點＋個體差異）。
鐵律：句句有據，缺出處標 L4/L5 提醒查證；檔名內容不符加註；截斷標未完整版。

## 6. 工作目錄規範＋回報

### 檔名對照規則（檔名必須一看即知內容）
- 中間檔（`_mp3/`、`_subtitles/`）用 ASCII 代號（如 ep1245）避 cp950 亂碼。
- 最終三種輸出 local 檔一律用中文原標：
  `{NN}-{中文標題}.md`／`{NN}-{中文標題}-v2.md`／`{NN}-{中文標題}-密涅瓦.md`
  （例：`郝聲音1245_量化求職一生受用的求職方法-v2.md`，禁止只留 ep1245 這種代號）。
- frontmatter 的 `title:` 必須與檔名中文標題一致；`source:` 註明來源 URL 或原始素材檔名。
- 每次建對照表：ASCII 代號 ↔ 中文檔名 ↔ 原始素材名，回報時附上。

- 單課一資料夾：`videos/ 逐字稿/ 精煉筆記/ _subtitles/ _mp3/ _transcripts/ _v2/`（Hahow 用 `ch01 ch02…`，知識衛星用 `01~NN`，小課用 `NN-標題`）。
- 每集存檔成功才做下一集（Hahow 強制單線程）； finishes 回報筆數/bytes/末段文字/檔案大小/頁數＋缺集清單。
- 批次結束統計：逐字稿數、v2數、密涅瓦數、缺漏表。
