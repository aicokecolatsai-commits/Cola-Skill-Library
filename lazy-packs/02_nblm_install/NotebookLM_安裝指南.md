# NotebookLM Prompt 產生器 — 新電腦安裝指南

## 資料夾內容（共 3 個檔案）

```
NotebookLM_Prompts.bat        ← 雙擊這個啟動
NotebookLM_Prompts.ps1        ← 主程式
notebooklm_patch_wiki.py      ← 選項 5 使用
```

> 三個檔案放在同一個資料夾即可，路徑不限。

---

## 安裝步驟

### 第一步：複製資料夾到新電腦

把整個資料夾複製到新電腦任意位置，例如：
- `C:\NotebookLM\`
- `D:\工具\NotebookLM\`

路徑不重要，放哪裡都能運作。

---

### 第二步：安裝 Python

> 如果只使用選項 1–4B，可跳過此步驟。選項 5 才需要 Python。

1. 前往 https://www.python.org/downloads/
2. 下載並安裝最新版本
3. **安裝時務必勾選「Add Python to PATH」**
4. 安裝後開啟 PowerShell 確認：
   ```
   python --version
   ```
   出現版本號即成功。

---

### 第三步：允許 PowerShell 執行腳本

開啟 PowerShell，執行：

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

出現提示時輸入 `Y` 確認。

> 這個設定只需要做一次，之後不需要重複。

---

### 第四步：測試

雙擊 `NotebookLM_Prompts.bat`，出現選單畫面即安裝成功。

---

## 常見問題

**Q：雙擊 bat 後閃一下就關掉？**
A：第三步的 PowerShell 執行原則還沒設定，重新執行第三步。

**Q：出現「無法載入檔案」錯誤？**
A：同上，執行第三步。

**Q：選項 5 出錯？**
A：確認 Python 已安裝（第二步），且三個檔案在同一個資料夾內。
