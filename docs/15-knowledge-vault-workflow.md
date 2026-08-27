# COLA Knowledge Vault 工作流

> 建立日期：2026-06-17  
> 參考來源：https://github.com/mathruffian-dot/sensebar-agent-knowledge-vault-builder

這份文件把 `sensebar-agent-knowledge-vault-builder` 的概念整理成適合 COLA workspace 使用的版本。原專案比較像 Agent 操作藍圖與範例腳本，不建議直接照抄執行；COLA 版本的重點是建立可長期維護的知識庫流程。

---

## 1. 適合用途

這個工作流適合用來整理：

- AI Agent / Codex / Claude / OpenCode / MCP 的學習資料
- YouTube 影片字幕與逐字稿
- 網頁文章、技術文件、GitHub README
- 自己的 prompt、課程草稿、操作筆記
- 之後要用於教學、腳本、產品設計或自動化流程的素材

不建議用來取代：

- Codex 初始環境建置
- MCP 安裝流程
- Skill 安裝流程
- GitHub 發佈流程

---

## 2. COLA 本機資料夾

知識庫放在：

```text
E:\COKECOLA\CODEX\04_KNOWLEDGE_VAULT
```

建議三層結構：

```text
04_KNOWLEDGE_VAULT
├─ Clipping
├─ 創作庫
└─ 知識庫
```

### Clipping

外部來源資料。包含影片字幕、網頁擷取、PDF OCR、GitHub README 摘要等。

原則：

- 保留原始來源連結
- 盡量不要直接改寫原文
- 每份資料開頭要標明來源與擷取日期

### 創作庫

自己的原始創作。包含 prompt、課程草稿、腳本、專案想法、文章草稿。

原則：

- 這裡放自己的想法與半成品
- 不要求一開始就整理得很乾淨
- 後續由 Agent 協助分類到知識庫

### 知識庫

整理後的長期知識。由 Agent 協助維護主題、索引、交叉連結與摘要。

建議初始分類：

```text
知識庫
├─ AI工作流
├─ Codex
├─ MCP
├─ Skills
├─ UIUX
├─ 教學素材
├─ 專案靈感
├─ Index.md
└─ Log.md
```

---

## 3. 每次新增資料的流程

1. 把新資料放入 `Clipping` 或 `創作庫`。
2. 每份檔案開頭補上基本資訊：

```markdown
# 標題

- 來源：
- 擷取日期：YYYY-MM-DD
- 類型：YouTube / Web / GitHub / PDF / Note
- 狀態：raw
```

3. 請 Agent 讀取新增檔案。
4. Agent 產生摘要、關鍵字、可行動重點。
5. Agent 把整理後內容寫入 `知識庫` 對應主題。
6. 更新 `知識庫\Index.md`。
7. 更新 `知識庫\Log.md`，記錄這次整理了什麼。

---

## 4. 每週整理任務

建議每週做一次「知識庫重整」。

Agent 任務：

- 掃描 `Clipping` 與 `創作庫` 的新檔案
- 找出尚未整理或狀態為 `raw` 的資料
- 摘要重點、抽取主題、建立關鍵字
- 合併到 `知識庫` 的既有主題
- 發現重複、矛盾、過期內容時記錄到 `Log.md`
- 更新 `Index.md`

建議提示詞：

```text
請掃描 E:\COKECOLA\CODEX\04_KNOWLEDGE_VAULT\Clipping 與 創作庫，
找出尚未整理的新資料，整理成 E:\COKECOLA\CODEX\04_KNOWLEDGE_VAULT\知識庫。

請保留來源連結、建立摘要、關鍵字、可行動重點，
並更新 Index.md 與 Log.md。
```

---

## 5. YouTube 字幕整理

參考 repo 的腳本使用 `yt-dlp` 下載字幕，但原始腳本綁定固定頻道與固定 Windows 路徑，不建議直接使用。

COLA 使用原則：

- 先建立要整理的影片 URL 清單
- 再下載字幕
- 清理 VTT 時移除時間軸、HTML tag、重複字幕行
- 輸出 Markdown 到 `Clipping`
- 每份 Markdown 保留影片標題與 URL

建議輸出格式：

```markdown
# 影片標題

- 來源：YouTube URL
- 擷取日期：YYYY-MM-DD
- 類型：YouTube
- 狀態：raw

---

逐字稿內容...
```

---

## 6. 與目前 COLA 系統的關係

這個工作流應該放在 COLA 系統的「知識沉澱」層：

```text
COLA.md
├─ 初始環境
├─ MCP
├─ Skills
├─ GitHub
└─ Knowledge Vault
```

對應工具：

- Firecrawl MCP：擷取網頁與文章
- Playwright MCP：處理需要瀏覽器互動的頁面
- skill-creator：把成熟流程沉澱成 Codex skill
- brainstorming：整理新主題或創作前先釐清方向
- ui-ux-pro-max：整理 UI/UX 相關知識與設計規範

---

## 7. 安全注意事項

- 不要把 API Key、登入 Cookie、私人帳密放進 `Clipping`。
- 來源資料若有版權限制，只保留摘要與必要短摘錄。
- 從網路下載腳本前，先檢查內容與固定路徑。
- 外部 repo 的腳本要先改成本機 COLA 路徑，再執行。
- 大量下載 YouTube 字幕時，要注意平台規則與頻率限制。

---

## 8. 下一步

建議先做一個小型試跑：

1. 選 3 個 AI Agent 相關 YouTube 影片或 3 篇網頁文章。
2. 放入 `Clipping`。
3. 請 Agent 整理成 `知識庫\AI工作流`。
4. 檢查 `Index.md` 與 `Log.md` 是否有幫助。
5. 確認好用後，再把流程做成正式 Codex skill。
