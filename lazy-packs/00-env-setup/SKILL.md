---
name: codex-env-setup
description: Codex 環境建置（Node.js, Codex CLI, Git, GitHub CLI, uv）。說「建置環境」「安裝開發環境」時載入。
---

# Codex 環境建置

檢查：`node --version; codex --version; git --version; gh --version; uv --version`

| 工具 | Windows | macOS | Linux |
|------|---------|-------|-------|
| Node.js | `winget install OpenJS.NodeJS` | `brew install node` | apt install nodejs |
| Codex CLI | `npm install -g @openai/codex` | 同左 | 同左 |
| Git | `winget install Git.Git` | `xcode-select --install` | apt install git |
| GitHub CLI | `winget install GitHub.cli` | `brew install gh` | apt install gh |
| uv | powershell iex script | `curl -LsSf ... \| sh` | 同左 |

最終驗證所有版本。回報：已安裝/已補裝清單 + 版本。
