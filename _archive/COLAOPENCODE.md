# COLA opencode 環境建置總覽

> 建立日期：2026-06-17
> Workspace：`E:\02_OPENCODE`
> 對應軟體：opencode (Claude Code CLI/Desktop)

---

## 1. 基礎工具

| 工具 | 版本 | 狀態 |
|:---|---:|:----:|
| Node.js | v24.16.0 | ✅ |
| Git | 2.54.0.windows.1 | ✅ |
| GitHub CLI | 2.93.0 | ✅ |
| uv | 0.11.21 | ✅ |
| Python | 3.11.15 / 3.12 | ✅ |

**PATH 設定：**
```
C:\Program Files\Git\cmd
C:\Program Files\GitHub CLI
%USERPROFILE%\.local\bin      (uv)
%USERPROFILE%\AppData\Local\Programs\Python\Python312
```

---

## 2. GitHub 連接

| 項目 | 狀態 |
|:---|---:|
| GitHub 帳號 | `snoocola` ✅ |
| gh 已登入 | ✅ |
| Git 使用者 | `snoocola` / `snoocola@gmail.com` ✅ |

**登入指令：**
```powershell
gh auth login --web --git-protocol https
# 或用 token
gh auth login --with-token
```

---

## 3. MCP 伺服器（opencode.jsonc）

路徑：`C:\Users\COLA\.config\opencode\opencode.jsonc`

```json
{
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

| MCP | 用途 |
|:---|---|
| **playwright** | 瀏覽器操作、截圖、互動頁面 |
| **firecrawl** | 網頁抓取、整理成乾淨文字 |

---

## 4. 已安裝 Skills（共 10 個）

路徑：`C:\Users\COLA\.config\opencode\skills\`

| 技能 | 說明 | 關鍵字 |
|:---|---|:---|
| **brainstorming** | 創意需求釐清與設計流程 | 設計、規劃 |
| **skill-creator** | 技能建立/修改/評測 | 技能、skill |
| **ui-ux-pro-max** | UI/UX 設計系統（50+風格、色彩、字體） | UI、設計、介面 |
| **habit-tracker** | 習慣追蹤 → Veo 影片規格 | 習慣、habit |
| **meta-prompt** | 需求 → YAML 系統指令 | prompt、指令 |
| **persona-coach** | 6位專業教練諮詢 | 教練、coach |
| **presentation-coach** | 簡報 → YAML 骨架 | 簡報、PPT |
| **resume-builder** | 個人經歷 → 極簡履歷圖卡 | 履歷、resume |
| **video-spec-builder** | 影片規格製作 | 影片規格 |
| **yourself-skill** | 數位分身 | 自我、分身 |

**一鍵同步（從 Codex → opencode）：**
```powershell
$codex = "C:\Users\COLA\.codex\skills"
$oc = "C:\Users\COLA\.config\opencode\skills"
$skills = @("brainstorming","skill-creator","ui-ux-pro-max","video-spec-builder","yourself-skill")
foreach ($s in $skills) {
    Copy-Item -LiteralPath "$codex\$s" -Destination "$oc\$s" -Recurse -Force
}
```

---

## 5. SKILL 備份

路徑：`E:\02_OPENCODE\SKILL\`

內含全部 10 個技能 + 設定檔，共 12 項：
```
SKILL/
├── brainstorming/
├── habit-tracker/
├── meta-prompt/
├── persona-coach/
├── presentation-coach/
├── resume-builder/
├── skill-creator/
├── ui-ux-pro-max/
├── video-spec-builder/
├── yourself-skill/
├── opencode.jsonc        (MCP 設定)
└── cola_opencodeskill.md  (本文件)
```

---

## 6. 知識庫（sensebar-knowledge-vault）

路徑：`E:\02_OPENCODE\sensebar-knowledge-vault\`

```
sensebar-knowledge-vault/
├── Clipping/     ← 36 部字幕（原始資料，勿修改）
├── 創作庫/       ← 你的教案/筆記（目前空）
└── 知識庫/       ← Agent 整理後知識（目前空）
```

來源 repo：`E:\02_OPENCODE\sensebar-agent-knowledge-vault-builder\`

**更新指令：**
```powershell
# 1. 重新抓取影片清單
& "C:\Users\COLA\AppData\Local\Programs\Python\Python312\python.exe" extract_videos.py

# 2. 下載新字幕
& "C:\Users\COLA\AppData\Local\Programs\Python\Python312\python.exe" download_all_subs.py
```

---

## 7. 驗證清單

```text
[ ] node --version                → v24.16.0
[ ] git --version                 → 2.54.0
[ ] gh --version                  → 2.93.0
[ ] uv --version                  → 0.11.21
[ ] gh auth status                → snoocola 已登入
[ ] git config --global user.name → snoocola
[ ] opencode.jsonc 含 playwright  → ✅
[ ] opencode.jsonc 含 firecrawl   → ✅
[ ] 10 個 skills 已安裝            → ✅
[ ] SKILL 備份資料夾               → ✅ (E:\02_OPENCODE\SKILL)
[ ] 知識庫 Clipping 有資料         → ✅ (36 部字幕)
```

---

## 8. 快速啟動指令

```powershell
# 設定完整 PATH
$env:PATH += ";C:\Program Files\Git\cmd;C:\Program Files\GitHub CLI;$env:USERPROFILE\.local\bin"

# 用 Python 3.12 執行指令
$py = "C:\Users\COLA\AppData\Local\Programs\Python\Python312\python.exe"

# 更新知識庫
cd E:\02_OPENCODE\sensebar-agent-knowledge-vault-builder
& $py extract_videos.py
& $py download_all_subs.py
```
