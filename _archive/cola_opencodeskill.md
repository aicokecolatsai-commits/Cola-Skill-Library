# COLA opencode 環境建置與技能盤點

> 建立日期：2026-06-17
> Workspace：`E:\02_OPENCODE`
> 對應軟體：opencode (Claude Code CLI/Desktop)

---

## 1. 基礎工具

```text
Node.js: v24.16.0
Git: 2.54.0.windows.1
GitHub CLI: 2.93.0 (帳號: snoocola)
uv: 0.11.17
PowerShell: 5.1.19041
OS: Windows 10 (19045)
```

### 安裝指令

```powershell
# Git
winget install --id Git.Git --accept-source-agreements --accept-package-agreements
# 加入 PATH
$env:PATH += ";C:\Program Files\Git\cmd"

# GitHub CLI
winget install --id GitHub.cli --accept-source-agreements --accept-package-agreements
# 加入 PATH
$env:PATH += ";C:\Program Files\GitHub CLI"

# uv
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# 加入 PATH
$env:PATH += ";$env:USERPROFILE\.local\bin"
```

### Git 設定（登入 GitHub 後）

```powershell
git config --global user.name "snoocola"
git config --global user.email "snoocola@gmail.com"
```

---

## 2. opencode 設定檔

**路徑：** `C:\Users\COLA\.config\opencode\opencode.jsonc`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "playwright": {
      "type": "local",
      "command": ["npx.cmd", "-y", "@playwright/mcp"]
    },
    "firecrawl": {
      "type": "local",
      "command": ["npx.cmd", "-y", "firecrawl-mcp"],
      "environment": {
        "FIRECRAWL_API_KEY": "fc-02ad54118eac42f2a469b2a6ff075f20"
      }
    }
  }
}
```

---

## 3. MCP 伺服器

| 名稱 | 命令 | 用途 |
|:---|---:|:----|
| **playwright** | `npx.cmd -y @playwright/mcp` | 操作瀏覽器、截圖、互動頁面 |
| **firecrawl** | `npx.cmd -y firecrawl-mcp` | 網頁內容抓取、整理成乾淨文字 |

---

## 4. 技能清單（共 10 個）

安裝路徑：`C:\Users\COLA\.config\opencode\skills\`

| 技能 | 說明 | 觸發關鍵字 |
|:---|---|:---|
| **brainstorming** | 創意工作前的需求釐清與設計流程 | 設計、規劃、想功能 |
| **skill-creator** | 建立/修改/優化 skill，含評測框架 | 技能、skill |
| **ui-ux-pro-max** | UI/UX 設計系統，50+ 風格、色彩、字體、UX 指南 | UI、設計、介面 |
| **habit-tracker** | 習慣追蹤 → Veo 風格影片規格 | 習慣、Veo、habit |
| **meta-prompt** | 需求 → YAML 結構化系統指令 | prompt、系統指令、提示詞 |
| **persona-coach** | 6 位專業教練諮詢 | 教練、coach、Noah、Rose 等 |
| **presentation-coach** | 簡報/PDF → YAML 簡報骨架 | 簡報、PPT、presentation |
| **resume-builder** | 個人經歷 → 極簡履歷圖卡 | 履歷、resume |
| **video-spec-builder** | 影片規格製作 | 影片規格 |
| **yourself-skill** | 數位分身 / 自我 skill | 自我、分身 |

### 快速安裝指令（從 Codex 同步到 opencode）

```powershell
$codex = "C:\Users\COLA\.codex\skills"
$oc = "C:\Users\COLA\.config\opencode\skills"
$skills = @("brainstorming","skill-creator","ui-ux-pro-max","video-spec-builder","yourself-skill")
foreach ($s in $skills) {
    Copy-Item -LiteralPath "$codex\$s" -Destination "$oc\$s" -Recurse -Force
}
```

---

## 5. GitHub 連接

```powershell
# 登入
gh auth login --web --git-protocol https
# 或使用 token
gh auth login --with-token

# 確認狀態
gh auth status

# 建立 repo 並推送
gh repo create <repo-name> --public --source=. --push

# 開啟 GitHub Pages
gh api repos/<owner>/<repo>/pages -X POST -f build_type=workflow -f source.branch=<branch> -f source.path=/
```

---

## 6. 驗證清單

```text
[ ] Node.js 可用 (node --version)
[ ] Git 可用 (git --version)
[ ] GitHub CLI 可用 (gh --version)
[ ] uv 可用 (uv --version)
[ ] gh 已登入 (gh auth status)
[ ] Git 使用者資訊已設定 (git config --global user.name)
[ ] opencode.jsonc 含 playwright MCP
[ ] opencode.jsonc 含 firecrawl MCP (含 API Key)
[ ] brainstorming 已安裝
[ ] skill-creator 已安裝
[ ] ui-ux-pro-max 已安裝
[ ] habit-tracker 已安裝
[ ] meta-prompt 已安裝
[ ] persona-coach 已安裝
[ ] presentation-coach 已安裝
[ ] resume-builder 已安裝
[ ] video-spec-builder 已安裝
[ ] yourself-skill 已安裝
```

---

## 7. 對應原始文件

- `00-環境建置.md` — 基礎工具安裝指引
- `02-連接-GitHub.md` — GitHub 帳號註冊與連接
- `COLA.md` — 完整環境準備清單（含 Codex）
