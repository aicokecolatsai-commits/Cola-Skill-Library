---
name: shutdown
description: 收工流程 — Git commit/push + Obsidian 工作筆記更新 + 三方同步。說「收工」、「結束了」、「準備換電腦」、「該同步的同步」、「先到這裡」時載入。
---

# 收工同步助手

對話結束前，把今天的工作完整保存到三個家：
- **GDrive**：自動同步（不用管）
- **Obsidian 工作筆記**：更新「上次做到哪」+「最近更動紀錄」
- **GitHub**：commit + push 本 repo 變動

## 收工 SOP（依序執行）

### 步驟 1：盤點今天做了什麼
從對話歷史摘要：完成的檔案、決策、踩到的新坑。

### 步驟 2：找到工作目錄與工作筆記
- 當前工作目錄：`$PWD`（或從對話脈絡推斷）
- Obsidian vault：`O:\我的雲端硬碟\AI_Project\00_colabrain\ColaBrain`
- Obsidian 工作筆記：`每日筆記/` 下的當日筆記，或專案同名資料夾下的 `工作筆記.md`
- 若 vault 沒對應資料夾 → 提醒使用者，但仍進行 GitHub 同步

### 步驟 3：更新 Obsidian 工作筆記
用 `obsidian_read_note` 讀取現有工作筆記，然後用 `obsidian_patch_note` 或 `obsidian_write_note` 更新：
- 「⏸️ 上次做到哪」段落：最後動作、完成的檔案、對話脈絡
- 「📋 最近更動紀錄」表格最後加一行：今天日期 + 摘要 + GDrive/Obsidian/GitHub 三勾
- 「🕳️ 踩坑筆記」（若有新坑）：依分類加進去

若當日筆記不存在，用 `obsidian_write_note` 在 `每日筆記/` 下建立 `YYYY-MM-DD-工作紀錄.md`。

### 步驟 4：Git commit + push
```bash
cd "<工作目錄>"
git add <今天動到的檔案，不要加 .opencode/ 或 .claude/>
git commit -m "<今天工作摘要的 commit message>"
git push origin <branch>
```

commit message 寫法：
- 標題行：「動詞 + 對象」
- 正文：3-5 條 bullet 描述變動 + 為什麼

### 步驟 5：報告同步狀態
給使用者一個三勾表格：

| 平台 | 動到的檔案 | 狀態 |
|------|------------|------|
| GDrive | （自動同步） | ✅ |
| Obsidian | 工作筆記更新 | ✅ |
| GitHub | commit + push | ✅ |

## 不該做的事
- ❌ 對「沒實質進度」的對話也跑同步（例：使用者只是問問題沒改檔）
- ❌ 把 `.opencode/`、`.claude/` 裡的設定檔 commit 進去
- ❌ commit message 寫「更新」、「修改」這種沒資訊的字
