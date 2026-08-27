# COLA SKILL 總盤點

> 建立日期：2026-06-18
> 通用於：OpenCode / Codex / Antigravity 三平台
> 原則：**不移動、不刪除原始檔案**，只在 `_docs/` 新增整理文件

---

## 目錄

1. [SKILL 三大來源](#1-skill-三大來源)
2. [全部 SKILL 一覽表](#2-全部-skill-一覽表)
3. [跨平台安裝方式](#3-跨平台安裝方式)
4. [來源檔案歸類對照](#4-來源檔案歸類對照)
5. [你真正有在用的 10 個 SKILL](#5-你真正有在用的-10-個-skill)

---

## 1. SKILL 三大來源

| 來源 | 作者 | 內容 | 檔案前綴 |
|------|------|------|----------|
| **Claude Code 懶人包** | Math Ruffian | 環境建置、MCP 串接、工具安裝指引 | 00- ~ 08- 編號檔 |
| **Skill 技能包** | Anthropic / 社群 | 可安裝的 AI 工作流程 (SKILL.md) | 目錄名如 brainstorming/ |
| **雷蒙 MCP 推薦** | Raymond Hou | Firecrawl / Playwright / Filesystem MCP 安裝指引 | 04-mcp-essentials |
| **你的自建文件** | COLA | 環境盤點、安全規則、論文 prompt | COLA.md / AGENTS.md 等 |

---

## 2. 全部 SKILL 一覽表

### 2-A 🔧 基礎環境類

| # | SKILL 名稱 | 用途 | 來源目錄 |
|---|-----------|------|---------|
| 00 | **codex-env-setup** | 安裝 Git、Node.js、GitHub CLI、uv 等開發工具 | `00-env-setup/` |
| 00i | **codex-install-all** | 批次安裝所有 14 個懶人包技能 | `00-install-all/` |
| 13 | **codex-chezmoi** | 用 chezmoi 同步設定到多台電腦 | `13-chezmoi/` |

### 2-B 🔗 MCP / 服務連接類

| # | SKILL 名稱 | 用途 | 來源目錄 |
|---|-----------|------|---------|
| 01 | **codex-notebooklm** | 連接 Google NotebookLM MCP | `01-notebooklm/` |
| 02 | **codex-github** | 設定 GitHub CLI 登入與 Git 配置 | `03-github/` |
| 03 | **codex-obsidian** | 連接 Obsidian 筆記庫 (MCPVault) | `05-obsidian/` |
| 04 | **codex-github-obsidian** | GitHub + Obsidian 整合安裝 | `04-github-obsidian/` |
| 06 | **codex-supabase** | 連接 Supabase 雲端資料庫 MCP | `07-supabase/` |
| 07 | **codex-firebase** | 連接 Firebase 資料庫 MCP | `08-firebase/` |
| 08 | **codex-ollama** | 安裝本地 AI Ollama | `09-ollama/` |
| 09 | **codex-gemini** | 設定 Gemini 免費 API Key | `10-gemini/` |

### 2-C 🧠 知識管理類

| # | SKILL 名稱 | 用途 | 來源目錄 |
|---|-----------|------|---------|
| 05 | **codex-second-brain** | 建立 Obsidian 三層結構（日記/創作/知識庫） | `06-second-brain/` |
| 10 | **codex-workspace** | 初始化專案：AGENTS.md + Git + Obsidian 筆記 | `11-workspace/` |

### 2-D 🎨 創作類

| # | SKILL 名稱 | 用途 | 來源目錄 |
|---|-----------|------|---------|
| 11 | **codex-draw** | 生圖指引（內建 Image Gen + 進階 API） | `12-draw/` |
| 01.5 | **codex-essentials** | 初學者必裝 Skills 與 Plugins 檢查 | `02-essentials/` |

### 2-E 🧩 社群 Skills（你已安裝的 10 個）

| # | SKILL 名稱 | 用途 | 來源目錄 |
|---|-----------|------|---------|
| S01 | **brainstorming** | 創意工作前的需求釐清與設計流程 | `14-codex-skills/user-installed/brainstorming/` |
| S02 | **skill-creator** | 建立/修改/評測 AI Skill（附量化評估框架） | `14-codex-skills/user-installed/skill-creator/` |
| S03 | **ui-ux-pro-max** | UI/UX 設計系統（50+風格、色彩、字體、UX指南） | `14-codex-skills/user-installed/ui-ux-pro-max/` |
| S04 | **habit-tracker** | 習慣追蹤 → 輸出 Veo 風格影片規格 | `(已安裝於 opencode 但不在 00_SKILL 子目錄)` |
| S05 | **meta-prompt** | 需求描述 → YAML 結構化系統指令 | `(已安裝於 opencode 但不在 00_SKILL 子目錄)` |
| S06 | **persona-coach** | 6 位專業教練角色（Noah/Rose/Mark 等）提供諮詢 | `(已安裝於 opencode 但不在 00_SKILL 子目錄)` |
| S07 | **presentation-coach** | 簡報/PDF → YAML 簡報骨架 | `(已安裝於 opencode 但不在 00_SKILL 子目錄)` |
| S08 | **resume-builder** | 個人經歷 → 極簡風格履歷圖卡 | `(已安裝於 opencode 但不在 00_SKILL 子目錄)` |
| S09 | **video-spec-builder** | 影片需求 → 標準化 video-spec.md | `(已安裝於 opencode 但不在 00_SKILL 子目錄)` |
| S10 | **yourself-skill** | 數位分身：從聊天/日記/照片建立可執行的自我 | `14-codex-skills/user-installed/yourself-skill/` |

### 2-F ⚙️ Codex 系統 Skills（備用參考）

| # | SKILL 名稱 | 用途 | 來源目錄 |
|---|-----------|------|---------|
| Sys1 | **skill-installer** | 從 GitHub 或精選清單安裝 Codex skills | `14-codex-skills/system/.system/skill-installer/` |
| Sys2 | **plugin-creator** | 建立 Codex 外掛程式目錄結構 | `14-codex-skills/system/.system/plugin-creator/` |
| Sys3 | **openai-docs** | 查詢 OpenAI / Codex 官方開發文件 | `14-codex-skills/system/.system/openai-docs/` |
| Sys4 | **imagegen** | 用 Codex 內建工具或 gpt-image-1.5 生成圖像 | `14-codex-skills/system/.system/imagegen/` |

### 2-G 📄 獨立文件（非 SKILL，但重要）

| 檔案 | 類型 | 用途 |
|------|------|------|
| `00-環境建置.md` | 安裝指引 | Codex 懶人包 EP03：安裝 Git/Node.js/uv 等（手動閱讀用） |
| `01-連接-NotebookLM.md` | 安裝指引 | Codex 懶人包：連接 NotebookLM MCP |
| `01.5-Codex必裝Skills與Plugins.md` | 安裝指引 | 初學者必裝外掛與技能檢查 |
| `02-連接-GitHub.md` | 安裝指引 | 連接 GitHub + Pages 上線 |
| `03-建立第二大腦-Obsidian.md` | 安裝指引 | Obsidian + MCP 連接 + GDrive 同步 |
| `04-第二大腦設定指南.md` | 安裝指引 | 三層結構 + CLAUDE.md + 模板 |
| `04-連接-Supabase-資料庫.md` | 安裝指引 | 雲端資料庫連接 |
| `04.5-連接-Firebase-資料庫.md` | 安裝指引 | Firebase 資料庫（老師友善版） |
| `04-mcp-essentials(兩個網路爬文MCP).md` | 安裝指引 | 雷蒙推薦 Firecrawl + Playwright MCP |
| `05-安裝本地AI-Ollama.md` | 安裝指引 | 本地 AI Ollama 安裝 |
| `06-設定Gemini免費API.md` | 安裝指引 | Gemini 免費 API 設定 |
| `07-初始化班級工具工作模式.md` | 安裝指引 | 老師建專案模式 |
| `08-安裝gpt-image-2生圖.md` | 安裝指引 | ChatGPT Image 2.0 安裝 |
| `00-Skill Creator(Antropics).md` | 安裝指引 | Anthropic 官方 Skill Creator 說明（已轉成 skill） |
| `wiki卡_prompt.txt` | Prompt | 學術論文 → Obsidian Wiki 格式轉換提示詞 |
| `COLA.md` | 個人盤點 | Codex 環境準備清單（含 MCP / Skills / 驗證） |
| `COLAOPENCODE.md` | 個人盤點 | opencode 環境建置總覽（最完整版） |
| `cola_opencodeskill.md` | 個人盤點 | opencode 環境建置 + 技能盤點 |
| `00-AGENTS.md` | 安全規則 | Workspace 安全規則（刪除/安裝限制） |
| `README.md` | 說明文件 | Claude Code 懶人包全集 README |
| `CLAUDE.md` | 工作規則 | 雙倉同步規則（Obsidian ↔ GitHub） |
| `SKILL.md` | 主入口 | 懶人包安裝入口（給 AI agent 用） |

---

## 3. 跨平台安裝方式

### 通用格式（三平台皆適用）

每個 SKILL 的本質是一個目錄，內含 `SKILL.md`（YAML frontmatter + Markdown 指令）。

```
skill-name/
├── SKILL.md       ← 必備（含 name + description + 指令）
├── scripts/       ← 選用（可執行程式碼）
├── references/    ← 選用（參考文件）
└── assets/        ← 選用（模板、圖示等）
```

### 安裝到各平台

#### OpenCode (Claude Code)

| 方式 | 指令 |
|------|------|
| 目錄位置 | `%USERPROFILE%\.config\opencode\skills\<skill-name>\` |
| 手動安裝 | `Copy-Item -Path <source> -Destination "$env:USERPROFILE\.config\opencode\skills\<name>" -Recurse` |
| MCP 設定 | 編輯 `%USERPROFILE%\.config\opencode\opencode.jsonc` |
| 驗證 | 重啟 opencode，說關鍵字觸發 skill |

#### Codex

| 方式 | 指令 |
|------|------|
| 目錄位置 | `%USERPROFILE%\.codex\skills\<skill-name>\` |
| npm 安裝 | `npx skills add <repo> --skill <name> -g -y` |
| 手動安裝 | `Copy-Item -Path <source> -Destination "$env:USERPROFILE\.codex\skills\<name>" -Recurse` |
| 驗證 | `Get-ChildItem "$env:USERPROFILE\.codex\skills"` |

#### Antigravity

> ⚠️ 若 Antigravity 同樣支援 SKILL.md 格式（YAML frontmatter + description 觸發），
> 則通用安裝方式為：將 SKILL 目錄複製到 Antigravity 的 skills 路徑。
> 待確認 Antigravity 的具體 skills 目錄位置後可補上。

### 跨平台通用安裝腳本

```powershell
# 參數設定
$sourceDir = "E:\COKECOLA\00_SKILL\<skill-dir>"
$skillName = "<skill-name>"

# 依平台安裝
switch ($env:COLA_AI_PLATFORM) {
  "opencode" {
    $target = "$env:USERPROFILE\.config\opencode\skills\$skillName"
  }
  "codex" {
    $target = "$env:USERPROFILE\.codex\skills\$skillName"
  }
  "antigravity" {
    $target = "$env:USERPROFILE\.antigravity\skills\$skillName"
  }
  default {
    Write-Host "請設定 `$env:COLA_AI_PLATFORM = opencode / codex / antigravity"
    exit
  }
}

Copy-Item -Path $sourceDir -Destination $target -Recurse -Force
Write-Host "✅ $skillName 已安裝到 $target"
```

---

## 4. 來源檔案歸類對照

### 懶人包編號 vs 實際 SKILL 目錄 vs 原始 .md 說明檔

| 編號 | SKILL 目錄 | 對應 .md 說明檔 |
|------|-----------|----------------|
| 00 | `00-env-setup/` | `00-環境建置.md` |
| 01 | `01-notebooklm/` | `01-連接-NotebookLM.md` |
| 01.5 | `02-essentials/` | `01.5-Codex必裝Skills與Plugins.md` |
| 02 | `03-github/` | `02-連接-GitHub.md` |
| 03 | `05-obsidian/` | `03-建立第二大腦-Obsidian.md` |
| 04 | `06-second-brain/` | `04-第二大腦設定指南.md` |
| 05 | `04-github-obsidian/` | (無對應 .md) |
| 06 | `07-supabase/` | `04-連接-Supabase-資料庫.md` |
| 07 | `08-firebase/` | `04.5-連接-Firebase-資料庫.md` |
| 08 | `09-ollama/` | `05-安裝本地AI-Ollama.md` |
| 09 | `10-gemini/` | `06-設定Gemini免費API.md` |
| 10 | `11-workspace/` | `07-初始化班級工具工作模式.md` |
| 11 | `12-draw/` | `08-安裝gpt-image-2生圖.md` |
| 12 | `13-chezmoi/` | (無對應 .md) |

> **⚠️ 注意：** 編號不一致原因：目錄是依實際安裝順序命名（00-13），
> 而 .md 說明檔是依影片集數命名（00-08，中間有 01.5、04.5 等）。
> 兩者都是 Math Ruffian 的懶人包系列，只是角度不同。

---

## 5. 你真正有在用的 10 個 SKILL

根據 `COLAOPENCODE.md`，你目前在 **opencode** 上已安裝的 10 個 SKILL：

```
C:\Users\COLA\.config\opencode\skills\
├── brainstorming/       → 創意需求釐清
├── skill-creator/       → 技能建立/修改/評測
├── ui-ux-pro-max/       → UI/UX 設計系統
├── habit-tracker/       → 習慣→影片規格
├── meta-prompt/         → 需求→YAML 系統指令
├── persona-coach/       → 6 位專業教練諮詢
├── presentation-coach/  → 簡報→YAML 骨架
├── resume-builder/      → 履歷圖卡
├── video-spec-builder/  → 影片規格製作
└── yourself-skill/      → 數位分身
```

這 10 個才是你日常會用到的核心技能。
其他 Math Ruffian 的懶人包 skills（00-env-setup ~ 13-chezmoi 共 14 個）
屬於「一次性安裝工具」，裝完環境後通常不會再觸發。

---

## 快速參考：給 Agent 的安裝指令

### 從這個目錄安裝 SKILL 到指定平台

```powershell
# 安裝 brainstorming 到 OpenCode
Copy-Item -Path "E:\COKECOLA\00_SKILL\14-codex-skills\user-installed\brainstorming" `
          -Destination "$env:USERPROFILE\.config\opencode\skills\brainstorming" `
          -Recurse -Force

# 安裝到 Codex
Copy-Item -Path "E:\COKECOLA\00_SKILL\14-codex-skills\user-installed\brainstorming" `
          -Destination "$env:USERPROFILE\.codex\skills\brainstorming" `
          -Recurse -Force
```

### 從 GitHub 安裝社群 SKILL

```powershell
# Codex 專用
npx skills add <github-repo> --skill <name> -g -y

# 通用（手動 clone 後複製）
git clone <repo-url> /tmp/skills
Copy-Item -Path "/tmp/skills/skills/<name>" -Destination "<target-dir>" -Recurse
```
