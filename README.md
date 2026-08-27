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
│   ├── noah-ergo-image/    # Noah 人因小管家社群對比圖產圖工作流 (v2)
│   ├── minerva-thinking/   # 密涅瓦大學 76 HCs 思考習慣與多元思維模型引導
│   ├── directing-ai/       # 指揮 AI 四步驟方法論（PRD規格書 / 打造專業分身 / 組隊思考 / RPG陪練）
│   ├── humanizer-zh-tw/    # 繁中去 AI 腔與人性化寫作 (融合 24 條語病與瓦基人味雙核心)
│   ├── grill-me/           # 嚴格質詢與思維壓力測試 (Grill-Me / Grilling)
│   ├── ui-ux-pro-max/      # 旗艦級 UI/UX 設計系統與元件庫
│   ├── brainstorming/      # 蘇格拉底式創意與需求深度探索引導
│   ├── skill-creator/      # 技能開發、評測與自動優化工作台
│   ├── video-spec-builder/ # 影音分鏡、TTS 與多模態影片規格生成器
│   ├── yourself-skill/     # 數位孿生 / 數位分身建構工具
│   ├── persona-coach/      # 多角色顧問諮詢教練
│   ├── meta-prompt/        # YAML 結構化 Prompt 與系統指令架構師
│   ├── presentation-coach/ # 簡報骨架與結構化教練
│   ├── resume-builder/     # 極簡風格無文字履歷圖卡產生器
│   ├── habit-tracker/      # 習慣追蹤與短影音規格產出
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
│   ├── 12-draw/            # ChatGPT Image 2.0 生圖
│   └── 13-chezmoi/         # chezmoi 多電腦環境同步
│
├── docs/                   # 📖 教學文件與詳細操作手冊 (00-環境建置 ~ 08-生圖)
└── _archive/               # 📦 歷史設定與備份檔案
```

---

## 🌟 高階工作流技能 (Workflow Skills)

| 技能名稱 | 目錄路徑 | 觸發關鍵字 | 核心功能 |
| :--- | :--- | :--- | :--- |
| **Noah 人因對比圖 v2** | `workflow-skills/noah-ergo-image` | 人因圖片, 正確vs錯誤姿勢圖, Noah 社群圖, 做人因主題 | 吃主題產出 FB/IG/Threads 對比圖×5 + 文案×3，含串接介面可供其他工作流呼叫 |
| **密涅瓦思考模式** | `workflow-skills/minerva-thinking` | 密涅瓦, HC分析, 思考模式, 決策評估, 批判思考 | 基於 Minerva University 100+ HCs，提供四階段決策重構與深層盲點檢驗 |
| **UI/UX Pro Max** | `workflow-skills/ui-ux-pro-max` | UI設計, 介面優化, 前端設計, 配色, Tailwind | 包含 50+ 風格、161 配色、React/Vue/Tailwind 模板的完整設計系統 |
| **Brainstorming** | `workflow-skills/brainstorming` | 腦力激盪, 發想, 需求探索, 設計規劃 | 在實作任何功能前進行蘇格拉底式追問與架構定義 |
| **Skill Creator** | `workflow-skills/skill-creator` | 建立技能, 優化技能, 技能評測 | Agent 技能開發、測試、benchmark 評測與自動最佳化工具 |
| **Video Spec Builder** | `workflow-skills/video-spec-builder` | 做影片, 宣傳片, 分鏡, 字幕, 3D shader | 追問收集影片需求，產出標準化可渲染的 video-spec.md |
| **Yourself Skill** | `workflow-skills/yourself-skill` | 數位分身, 數位永生, 蒸餾自己 | 將對話紀錄、日記解構為可運行的數位分身 |
| **Persona Coach** | `workflow-skills/persona-coach` | 教練, 顧問, Noah, Rose, Mark, Lucas | 六大專業顧問群角色切換與結構化建議輸出 |
| **Meta Prompt** | `workflow-skills/meta-prompt` | prompt, 系統指令, 提示詞, 性格分析 | 產出 YAML 結構化高階系統指令與溝通策略 |
| **Presentation Coach** | `workflow-skills/presentation-coach` | 簡報, PPT, 投影片, presentation | 吃簡報材料或 PDF，產出 YAML 簡報骨架 |
| **Resume Builder** | `workflow-skills/resume-builder` | 做履歷, 履歷圖卡, resume | 個人經歷轉成一張極簡風格無文字履歷圖卡 |
| **Habit Tracker** | `workflow-skills/habit-tracker` | 習慣追蹤, 工作流影片, Veo, habit | 習慣描述轉成 30-90 秒 Veo 風格影片規格 |
| **Academic Deep Research** | `workflow-skills/academic-deep-research` | 深度研究, 文獻回顧, 系統性回顧 | 13-agent 學術研究團隊，8 模式（PRISMA、後設分析、事實查核等） |
| **Academic Paper** | `workflow-skills/academic-paper` | 寫論文, 學術論文, 論文大綱 | 12-agent 論文寫作管線，11 模式，5 種引用格式 |
| **Academic Paper Reviewer** | `workflow-skills/academic-paper-reviewer` | 審查論文, 同行評審, referee report | 模擬主編 + 3 審稿人 + 魔鬼代言人的多視角評審 |
| **Academic Pipeline** | `workflow-skills/academic-pipeline` | 論文管線, 研究到出版 | 研究→出版 10 階段總管線 |
| **Article Noah** | `workflow-skills/article-noah` | 人因部落格, 文章撰寫 | 產出 V8 風格 clean HTML，含 Noah 元件、JSON-LD Schema 與 AI SEO |
| **Cola UIUX Game Design** | `workflow-skills/cola-uiux-game-design` | 畫面不好看, 設計 UI, 開發遊戲 | 引導高品質 UI/UX 與遊戲設計 |
| **Draw 生圖** | `workflow-skills/draw` | 畫一張, 生成圖片, 生圖 | 用 OpenAI gpt-image-2 生成圖片 |
| **Project Init** | `workflow-skills/project-init` | 初始化專案 | AGENTS.md + Git + GitHub + Obsidian 初始化 |
| **Startup 開工** | `workflow-skills/startup` | 開工, 開始工作, 上次做到哪 | 讀取 Obsidian 工作筆記 + 檢查 Git 狀態 + 建議下一步 |
| **Shutdown 收工** | `workflow-skills/shutdown` | 收工, 結束了, 該同步的同步 | Git commit/push + Obsidian 工作筆記更新 + 三方同步 |
| **職場人因文案專家** | `workflow-skills/職場人因文案專家` | 人因工程, 人體工學, 職場文案, 中高齡職場 | 吃情境或痛點描述，產出繁體中文職場人因工程社群文案 |

---

## ⚙️ 工程與寫作技能集 (Engineering Skills)

來源：`~/.agents/skills`（Matt Pocock 工程技能系列），完整收錄於 `engineering-skills/`。

| 技能名稱 | 核心功能 |
| :--- | :--- |
| `engineering-skills/ask-matt` | 技能路由：判斷哪個 skill/flow 適合目前情境 |
| `engineering-skills/code-review` | 沿兩軸（標準/規格）平行審查分支、PR 或 WIP |
| `engineering-skills/diagnosing-bugs` | 困難 bug 與效能回歸的診斷迴圈 |
| `engineering-skills/tdd` | 測試驅動開發（red-green-refactor） |
| `engineering-skills/research` | 對高信賴一手來源做研究並存成 Markdown |
| ... | 共 41 個技能，詳見 `engineering-skills/` 目錄 |

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
| 08 | 設定 Gemini 免費 API | `lazy-packs/10-gemini` | [`docs/06-設定Gemini免貽API.md`](docs/06-設定Gemini免貽API.md) |
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
# 範例：將 noah-ergo-image 連結到 Antigravity 全域技能目錄
New-Item -ItemType SymbolicLink -Path "$HOME\.gemini\config\skills\noah-ergo-image" -Target "O:\SNOOCOLA\AI_Project\00_skill\workflow-skills\noah-ergo-image"
```

---

## 📄 授權 (License)

本專案採用 [MIT License](LICENSE) 授權，歡迎自由使用、擴充與分享。
