# COLA 環境建置清單（通用版）

> 適用平台：OpenCode / Codex / Antigravity
> 更新日期：2026-06-18

---

## 1. 基礎工具

| 工具 | 用途 | 驗證指令 | 安裝方式 (Windows) |
|------|------|---------|-------------------|
| **Git** | 版本控制、commit、push | `git --version` | `winget install --id Git.Git -a` |
| **GitHub CLI** | GitHub 登入、repo、Pages | `gh --version` | `winget install --id GitHub.cli -a` |
| **Node.js** | MCP、npm 套件 | `node --version` | `winget install --id OpenJS.NodeJS -a` |
| **uv** | Python 工具管理 | `uv --version` | `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"` |
| **Python** | 執行腳本 | `python --version` | 官網下載安裝 |

## 2. MCP 伺服器

| MCP | 用途 | 安裝方式 |
|-----|------|---------|
| **playwright** | 瀏覽器操作、截圖 | `npx.cmd -y @playwright/mcp` + `npx playwright install chromium` |
| **firecrawl** | 網頁抓取、摘要 | `npx.cmd -y firecrawl-mcp`（需 API Key） |

## 3. 跨平台 SKILL 安裝位置

| 平台 | SKILL 目錄 | 設定檔位置 |
|------|-----------|-----------|
| **OpenCode** | `%USERPROFILE%\.config\opencode\skills\` | `%USERPROFILE%\.config\opencode\opencode.jsonc` |
| **Codex** | `%USERPROFILE%\.codex\skills\` | `%USERPROFILE%\.codex\config.toml` |
| **Antigravity** | `%USERPROFILE%\.antigravity\skills\`（推測） | 待確認 |

## 4. 驗證清單

```text
[ ] node --version                → v20+
[ ] git --version                 → 已安裝
[ ] gh --version                  → 已安裝
[ ] uv --version                  → 已安裝
[ ] gh auth status                → 已登入 GitHub
[ ] git config user.name          → 已設定
[ ] playwright MCP 已啟用
[ ] firecrawl MCP 已啟用（含 API Key）
[ ] 10 個核心 SKILL 已安裝
```

## 5. 對應原始文件

- 詳細環境建置指引 → `..\00-環境建置.md`（Math Ruffian 版）
- COLA opencode 盤點 → `..\COLAOPENCODE.md`
- COLA codex 盤點 → `..\COLA.md`
