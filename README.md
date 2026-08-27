# 🚀 Cola Skill Library (跨平台 AI Agent 技能庫全集)

> 專為 **Google Antigravity**、**Claude Code**、**Codex CLI**、**OpenCode** 設計的跨平台通用 Agent 技能與教學懶人包集合。
> 支援與 **Obsidian 第二大腦** 雙向連通，並相容最新 **Agent Skills 開放標準**。

---

## 📂 資料夾結構

```
Cola-Skill-Library/
├── README.md               # 專案總導覽與安裝指南
├── SKILL.md                # 技能庫主安裝/呼叫入口
├── AGENTS.md               # Agent 安全規範與工作原則
│
├── workflow-skills/        # 🧠 高階獨立與專家思維工作流技能
│   ├── minerva-thinking/   # 密涅瓦大學 100+ HCs 思考模塊與決策引導
│   ├── humanizer-zh-tw/    # 繁中去 AI 腔與人性化寫作 (融合 24 條語病與瓦基人味雙核心)
│   ├── grill-me/           # 嚴格質詢與思維壓力測試 (Grill-Me / Grilling)
│   ├── ui-ux-pro-max/      # 旗艦級 UI/UX 設計系統與元件庫
│   ├── brainstorming/      # 蘇格拉底式創意與需求深度探索引導
│   ├── skill-creator/      # 技能開發、評測與自動優化工作台
│   ├── video-spec-builder/ # 影音分鏡、TTS 與多模態影片規格生成器
│   ├── yourself-skill/     # 數位孿生 / 數位分身建構工具
│   ├── persona-coach/      # 多角色顧問諮詢教練 (Noah, Rose, Mark, Lucas...)
│   ├── meta-prompt/        # YAML 結構化 Prompt 與系統指令架構師
│   ├── presentation-coach/ # 簡報骨架與結構化教練
│   ├── resume-builder/     # 極簡風格無文字履歷圖卡產生器
│   ├── habit-tracker/      # 習慣追蹤與短影音規格產出
│   ├── 00_cola_ergo/       # Noah 人因小管家圖卡與對比圖產生器
│   ├── academic-deep-research/  # 13-agent 學術研究團隊
│   ├── academic-paper/     # 12-agent 學術論文寫作管線
│   ├── academic-paper-reviewer/ # 5 位審稿人模擬評審
│   ├── academic-pipeline/  # 研究→出版 10 階段總管線
│   ├── article-noah/       # Noah 人因部落格文章 HTML 撰寫
│   ├── cola-uiux-game-design/   # UI/UX 與遊戲設計引導
│   ├── draw/               # AI 生圖 (gpt-image-2)
│   ├── project-init/       # 新專案初始化
│   ├── startup/            # 開工流程
│   ├── shutdown/           # 收工流程
│   └── 職場人因文案專家/     # 職場人因工程社群文案
│
├── engineering-skills/     # ⚙️ 工程與寫作技能集 (Matt Pocock 系列, 41 個)
│
├── lazy-packs/             # 🛠️ MCP 串接與環境一鍵安裝懶人包 (00~13)
│   ├── 00-env-setup/       # 基礎環境建置 (Git, Node, uv, GitHub CLI)
│   ├── 00-install-all/     # 一鍵安裝所有懶人包
│   ├── 01-notebooklm/      # 連接 NotebookLM MCP
│   ├── 02-essentials/      # 初學者必裝 Skills 與 Plugins
│   ├── 03-github/          # 連接 GitHub CLI 與 Pages 上線
│   ├── 04-github-obsidian/ # GitHub + Obsidian 整合設定
│   ├── 05-obsidian/        # 連接 Obsidian MCP (MCPVault)
│   ├── 06-second-brain/    # 第二大腦三層結構工作流
│   ├── 07-supabase/        # 連接 Supabase 雲端資料庫 MCP
│   ├── 08-firebase/        # 連接 Firebase / Firestore MCP
│   ├── 09-ollama/          # 安裝本地 AI Ollama
│   ├── 10-gemini/          # 設定 Gemini 免費 API
│   ├── 11-workspace/       # 專案開工/收工與初始化工作模式
│   ├── 12-draw/            # ChatGPT Image 2.0 / 生圖技能
│   └── 13-chezmoi/         # chezmoi 多電腦環境同步
│
├── docs/                   # 📖 教學文件與詳細操作手冊 (00-環境建置 ~ 08-生圖)
└── _archive/               # 📦 歷史設定與備份檔案
```

---

## 🌟 高階工作流技能 (Workflow Skills)

| 技能名稱 | 目錄路徑 | 觸發關鍵字 | 核心功能 |
| :--- | :--- | :--- | :--- |
| **密涅瓦思考模式** | `workflow-skills/minerva-thinking` | 密涅瓦, HC分析, 思考模式, 決策評估, 批判思考 | 基於 Minerva University 100+ HCs，提供四階段決策重構與深層盲點檢驗 |
| **UI/UX Pro Max** | `workflow-skills/ui-ux-pro-max` | UI設計, 介面優化, 前端設計, 配色, Tailwind | 包含 50+ 風格、161 配色、React/Vue/Tailwind 模板的完整設計系統 |
| **Brainstorming** | `workflow-skills/brainstorming` | 腦力激盪, 發想, 需求探索, 設計規劃 | 在實作任何功能前進行蘇格拉底式追問與架構定義 |
| **Skill Creator** | `workflow-skills/skill-creator` | 建立技能, 優化技能, 技能評測 | Agent 技能開發、測試、benchmark 評測與自動最佳化工具 |
| **Video Spec Builder** | `workflow-skills/video-spec-builder` | 做影片, 宣傳片, 分鏡, 字幕, 3D shader | 追問收集影片需求，產出標準化可渲染的 `video-spec.md` |
| **Yourself Skill** | `workflow-skills/yourself-skill` | 數位分身, 數位永生, 蒸餾自己 | 將對話紀錄、日記解構為可運行的數位分身 |
| **Persona Coach** | `workflow-skills/persona-coach` | 教練, 顧問, Noah, Rose, Mark, Lucas | 六大專業顧問群角色切換與結構化建議輸出 |
| **Meta Prompt** | `workflow-skills/meta-prompt` | prompt, 系統指令, 提示詞, 性格分析 | 產出 YAML 結構化高階系統指令與溝通策略 |
| **Presentation Coach** | `workflow-skills/presentation-coach` | 簡報, PPT, 投影片, presentation | 吃簡報材料或 PDF，產出 YAML 簡報骨架 |
| **Resume Builder** | `workflow-skills/resume-builder` | 做履歷, 履歷圖卡, resume | 個人經歷轉成一張極簡風格無文字履歷圖卡 |
| **Habit Tracker** | `workflow-skills/habit-tracker` | 習慣追蹤, 工作流影片, Veo, habit | 習慣描述轉成 30-90 秒 Veo 風格影片規格 |
| **Noah 人因圖卡** | `workflow-skills/00_cola_ergo` | 人因圖卡, 對比圖 | Noah 人因小管家圖卡與對比圖產生器 |
| **Academic Deep Research** | `workflow-skills/academic-deep-research` | 深度研究, 文獻回顧, 系統性回顧 | 13-agent 學術研究團隊，8 模式（PRISMA、後設分析、事實查核等） |
| **Academic Paper** | `workflow-skills/academic-paper` | 寫論文, 學術論文, 論文大綱 | 12-agent 論文寫作管線，11 模式，5 種引用格式，輸出 LaTeX/PDF/DOCX |
| **Academic Paper Reviewer** | `workflow-skills/academic-paper-reviewer` | 審查論文, 同行評審, referee report | 模擬主編 + 3 審稿人 + 魔鬼代言人的多視角評審 |
| **Academic Pipeline** | `workflow-skills/academic-pipeline` | 論文管線, 研究到出版 | 研究→出版 10 階段總管線，整合 deep-research/paper/reviewer |
| **Article Noah** | `workflow-skills/article-noah` | 人因部落格, 文章撰寫 | 產出 V8 風格 clean HTML，含 Noah 元件、JSON-LD Schema 與 AI SEO |
| **Cola UIUX Game Design** | `workflow-skills/cola-uiux-game-design` | 畫面不好看, 設計 UI, 開發遊戲 | 引導高品質 UI/UX 與遊戲設計，現代感、微動畫與優質人機互動 |
| **Draw 生圖** | `workflow-skills/draw` | 畫一張, 生成圖片, 生圖 | 用 OpenAI gpt-image-2 生成圖片 |
| **Project Init** | `workflow-skills/project-init` | 初始化專案 | AGENTS.md + Git + GitHub + Obsidian 初始化 |
| **Startup 開工** | `workflow-skills/startup` | 開工, 開始工作, 上次做到哪 | 讀取 Obsidian 工作筆記 + 檢查 Git 狀態 + 建議下一步 |
| **Shutdown 收工** | `workflow-skills/shutdown` | 收工, 結束了, 該同步的同步 | Git commit/push + Obsidian 工作筆記更新 + 三方同步 |
| **職場人因文案專家** | `workflow-skills/職場人因文案專家` | 人因工程, 人體工學, 職場文案, 中高齡職場 | 吃情境或痛點描述，產出繁體中文職場人因工程社群文案 (300-500字) |

---

## ⚙️ 工程與寫作技能集 (Engineering Skills)

來源：`~/.agents/skills`（Matt Pocock 工程技能系列），完整收錄於 `engineering-skills/`。

| 技能名稱 | 核心功能 |
| :--- | :--- |
| `engineering-skills/ask-matt` | 技能路由：判斷哪個 skill/flow 適合目前情境 |
| `engineering-skills/batch-grill-me` | 一輪問完所有前沿問題的密集面試 |
| `engineering-skills/claude-handoff` | 交接給全新背景 agent 立即接手 |
| `engineering-skills/code-review` | 沿兩軸（標準/規格）平行審查分支、PR 或 WIP |
| `engineering-skills/codebase-design` | Deep module 設計共享詞彙 |
| `engineering-skills/design-an-interface` | 平行子 agent 產生多種介面設計方案 |
| `engineering-skills/diagnosing-bugs` | 困難 bug 與效能回歸的診斷迴圈 |
| `engineering-skills/domain-modeling` | 建構與打磨專案領域模型、術語表 |
| `engineering-skills/edit-article` | 重組章節、提升清晰度與精煉文章 |
| `engineering-skills/git-guardrails-claude-code` | 建立 Claude Code hooks 阻擋危險 git 指令 |
| `engineering-skills/grill-me` | 密集面試以銳化計畫或設計 |
| `engineering-skills/grill-with-docs` | 密集面試並同步產出 ADR 與術語表 |
| `engineering-skills/grilling` | 對計畫、決定或想法進行密集壓力測試 |
| `engineering-skills/handoff` | 將對話壓縮成交接文件 |
| `engineering-skills/implement` | 依 spec/票單實作工作 |
| `engineering-skills/improve-codebase-architecture` | 掃描深度化機會，輸出 HTML 報告並面試挑選 |
| `engineering-skills/loop-me` | 針對想建構的工作流規格進行密集面試 |
| `engineering-skills/migrate-to-shoehorn` | 測試檔 `as` 斷言遷移至 @total-typescript/shoehorn |
| `engineering-skills/obsidian-vault` | 搜尋、建立、管理 Obsidian 筆記（wikilinks 與索引筆記） |
| `engineering-skills/prototype` | 一次性 prototype 驗證設計問題 |
| `engineering-skills/qa` | 互動式 QA：口語回報 bug，agent 建 GitHub issue |
| `engineering-skills/request-refactor-plan` | 訪談產出小型 commit 重構計畫並建 issue |
| `engineering-skills/research` | 對高信賴一手來源做研究並存成 Markdown |
| `engineering-skills/resolving-merge-conflicts` | 解決進行中的 git merge/rebase 衝突 |
| `engineering-skills/scaffold-exercises` | 建立通過 lint 的練習目錄結構 |
| `engineering-skills/setup-matt-pocock-skills` | 配置本 repo 的 issue tracker 與領域文件 |
| `engineering-skills/setup-pre-commit` | 設定 Husky pre-commit hooks（Prettier/typecheck/tests） |
| `engineering-skills/setup-ts-deep-modules` | 用 dependency-cruiser 將套件包成 deep module |
| `engineering-skills/tdd` | 測試驅動開發（red-green-refactor、整合測試） |
| `engineering-skills/teach` | 在此 workspace 內教學新技能或概念 |
| `engineering-skills/to-questionnaire` | 把無法回答的決策轉成問卷 |
| `engineering-skills/to-spec` | 把對話綜合成 spec 並發布到 issue tracker |
| `engineering-skills/to-tickets` | 把計畫拆成 tracer-bullet 票單（含 blocking 邊界） |
| `engineering-skills/triage` | 用角色狀態機分類、驗證、撰寫 agent-ready briefs |
| `engineering-skills/ubiquitous-language` | 從對話萃取 DDD 術語表並存成 UBIQUITOUS_LANGUAGE.md |
| `engineering-skills/wayfinder` | 把大型工作切成決策票單地圖，逐一解決 |
| `engineering-skills/wizard` | 產生互動式 bash wizard 引導人工程序 |
| `engineering-skills/writing-beats` | 寫作：將素材組裝成節拍旅程 |
| `engineering-skills/writing-fragments` | 寫作：挖掘原始片段，尚無結構 |
| `engineering-skills/writing-great-skills` | 技能寫作參考：可預測技能的字彙與原則 |
| `engineering-skills/writing-shape` | 寫作：把素材塑形成文章，逐段推進 |

---

## 🛠️ 教學系列懶人包 (Lazy Packs)

| 編號 | 名稱 | 目錄路徑 | 對應教學手冊 |
| :--- | :--- | :--- | :--- |
| 00 | 環境建置 | `lazy-packs/00-env-setup` | [`docs/00-環境建置.md`](docs/00-環境建置.md) |
| 01 | 連接 NotebookLM | `lazy-packs/01-notebooklm` | [`docs/01-連接-NotebookLM.md`](docs/01-連接-NotebookLM.md) |
| 02 | 新手必裝推薦 | `lazy-packs/02-essentials` | [`docs/01.5-Codex必裝Skills與Plugins.md`](docs/01.5-Codex必裝Skills與Plugins.md) |
| 03 | 連接 GitHub | `lazy-packs/03-github` | [`docs/02-連接-GitHub.md`](docs/02-連接-GitHub.md) |
| 04 | 連接 Obsidian | `lazy-packs/05-obsidian` | [`docs/04-第二大腦設定指南.md`](docs/04-第二大腦設定指南.md) |
| 05 | 連接 Supabase | `lazy-packs/07-supabase` | [`docs/04-連接-Supabase-資料庫.md`](docs/04-連接-Supabase-資料庫.md) |
| 06 | 連接 Firebase | `lazy-packs/08-firebase` | [`docs/04.5-連接-Firebase-資料庫.md`](docs/04.5-連接-Firebase-資料庫.md) |
| 07 | 安裝本地 AI Ollama | `lazy-packs/09-ollama` | [`docs/05-安裝本地AI-Ollama.md`](docs/05-安裝本地AI-Ollama.md) |
| 08 | 設定 Gemini 免費 API | `lazy-packs/10-gemini` | [`docs/06-設定Gemini免費API.md`](docs/06-設定Gemini免費API.md) |
| 09 | 專案初始化與收工模式 | `lazy-packs/11-workspace` | [`docs/07-初始化班級工具工作模式.md`](docs/07-初始化班級工具工作模式.md) |
| 10 | ChatGPT Image 2.0 生圖 | `lazy-packs/12-draw` | [`docs/08-安裝gpt-image-2生圖.md`](docs/08-安裝gpt-image-2生圖.md) |

---

## ⚡ 跨平台安裝與使用方式

### 方式一：直接在對話中呼叫 AI 載入
把這個 Repo 網址貼給你的 AI Agent（Antigravity / Claude Code / Codex / OpenCode）：
```text
請讀取 https://github.com/aicokecolatsai-commits/Cola-Skill-Library
並列出所有可用技能，幫我安裝指定的技能。
```

### 方式二：全域軟連結 (一次修改，多端生效)
在 Windows PowerShell 下執行：
```powershell
# 範例：將 minerva-thinking 連結到 Antigravity 全域技能目錄
New-Item -ItemType SymbolicLink -Path "$HOME\.gemini\config\skills\minerva-thinking" -Target "O:\我的雲端硬碟\AI_Project\00_skill\workflow-skills\minerva-thinking"
```

---

## 📄 授權 (License)

本專案採用 [MIT License](LICENSE) 授權，歡迎自由使用、擴充與分享。
