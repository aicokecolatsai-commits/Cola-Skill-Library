# COLA 初始環境準備清單

> 建立日期：2026-06-03  
> Workspace：`E:\COKECOLA\CODEX`

這份文件整理 COLA workspace 初始環境需要準備的內容，包含基礎工具、Codex 設定、MCP 工具與已安裝 skills。之後換機、重灌或重新建立 workspace 時，可以照這份清單檢查。

---

## 1. Workspace 基礎文件

確認 `00_SKILL` 內已有這些初始化文件：

- `E:\COKECOLA\CODEX\00_SKILL\00-環境建置.md`
  - Codex Desktop app、Node.js、Git、GitHub CLI、uv 的建置指引。
  - 讀取時請使用 UTF-8，避免 PowerShell 預設編碼造成中文亂碼。
- `E:\COKECOLA\CODEX\00_SKILL\AGENTS.md`
  - Workspace 安全規則。
  - 包含刪除、移動、安裝、網路存取、Windows PowerShell 的操作限制。
- `E:\COKECOLA\CODEX\00_SKILL\04-mcp-essentials(兩個網路爬文MCP).md`
  - Firecrawl 與 Playwright MCP 的安裝來源。

---

## 2. 基礎工具

目前已確認可用：

```text
Node.js: v24.16.0
Git: 2.54.0.windows.1
GitHub CLI: 2.93.0
uv: 0.11.17
```

檢查指令：

```powershell
node --version
git --version
gh --version
uv --version
```

注意：Windows PowerShell 可能會擋 `npx.ps1`，因此 MCP 設定中使用 `npx.cmd`。

---

## 3. Codex 設定檔

主要設定檔：

```text
C:\Users\COLA\.codex\config.toml
```

已建立備份：

```text
C:\Users\COLA\.codex\config.toml.bak-before-mcp-essentials
```

目前 workspace 已設為 trusted：

```toml
[projects.'e:\cokecola\codex']
trust_level = "trusted"
```

---

## 4. 已安裝 MCP

### Playwright MCP

用途：

- 操作瀏覽器
- 打開網站
- 截圖
- 處理需要互動、點擊、滾動或登入後才能看的頁面

Codex 設定：

```toml
[mcp_servers.playwright]
command = "npx.cmd"
args = ["-y", "@playwright/mcp"]
```

已執行：

```powershell
npx.cmd -y playwright install chromium
npx.cmd -y @playwright/mcp --help
```

### Firecrawl MCP

用途：

- 抓取網頁內容
- 將網頁整理成乾淨文字
- 摘要文章
- 比較多個網頁資料

Codex 設定：

```toml
[mcp_servers.firecrawl]
command = "npx.cmd"
args = ["-y", "firecrawl-mcp"]

[mcp_servers.firecrawl.env]
FIRECRAWL_API_KEY = "***已設定，勿公開***"
```

注意：

- Firecrawl 需要 API Key 才能啟用。
- 不要把 API Key 貼到公開文件、GitHub、截圖或聊天紀錄中。

---

## 5. 已安裝 Skills

使用者 skills 目錄：

```text
C:\Users\COLA\.codex\skills
```

workspace 內的整理備份：

```text
E:\COKECOLA\CODEX\00_SKILL\14-codex-skills
```

備份結構：

```text
14-codex-skills
├─ user-installed
└─ system
```

目前已安裝：

```text
brainstorming
skill-creator
ui-ux-pro-max
yourself-skill
```

### skill-creator

來源：

```text
https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
```

本機位置：

```text
C:\Users\COLA\.codex\skills\skill-creator\SKILL.md
```

用途：

- 建立新的 skill
- 修改與優化既有 skill
- 設計測試 prompts
- 評估 skill 表現

### brainstorming

來源：

```text
https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md
```

本機位置：

```text
C:\Users\COLA\.codex\skills\brainstorming\SKILL.md
```

用途：

- 在開始做功能、設計、元件或行為調整前，先釐清需求
- 把想法整理成設計與規格
- 避免還沒想清楚就直接實作

### yourself-skill

來源：

```text
https://github.com/notdog1998/yourself-skill
```

本機位置：

```text
C:\Users\COLA\.codex\skills\yourself-skill\SKILL.md
```

實際 skill 名稱：

```text
create-yourself
```

用途：

- 建立自己的數位分身 / 自我 skill
- 從聊天紀錄、日記、照片等資料整理個人風格
- 後續可透過追加資料更新自我 skill

### ui-ux-pro-max

來源：

```text
https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
```

本機位置：

```text
C:\Users\COLA\.codex\skills\ui-ux-pro-max\SKILL.md
```

實際 skill 名稱：

```text
ui-ux-pro-max
```

用途：

- UI/UX 設計決策與品質檢查
- 網站、landing page、dashboard、admin panel、SaaS、mobile app 的介面規劃
- 色彩、字體、排版、間距、互動狀態、響應式與 accessibility 建議
- 搭配內建資料與 `scripts/search.py` 查詢設計系統、產品型態、UX guideline 與技術 stack 建議

---

## 6. 安裝後必做

每次新增 MCP 或 skill 後，請重啟 Codex。

重啟後檢查：

- 用 `/mcp` 確認是否看到：
  - `playwright`
  - `firecrawl`
- 確認 skills 是否可被觸發：
  - `brainstorming`
  - `skill-creator`
  - `ui-ux-pro-max`
  - `create-yourself`

---

## 7. 安全注意事項

- 不要公開 Firecrawl API Key。
- 修改 `C:\Users\COLA\.codex\config.toml` 前，先備份。
- 不要隨意刪除 workspace 檔案；需要清理時優先移到 `.trash/`。
- 安裝工具、下載套件、修改使用者層級設定時，要先確認來源。
- 在 Windows PowerShell 中，優先使用 `npx.cmd`，避免被 `npx.ps1` 的執行政策卡住。

---

## 8. 快速驗證清單

```text
[ ] Codex 已重啟
[ ] /mcp 看得到 playwright
[ ] /mcp 看得到 firecrawl
[ ] Node.js 可用
[ ] Git 可用
[ ] GitHub CLI 可用
[ ] uv 可用
[ ] skill-creator 已安裝
[ ] brainstorming 已安裝
[ ] ui-ux-pro-max 已安裝
[ ] create-yourself 已安裝
```
