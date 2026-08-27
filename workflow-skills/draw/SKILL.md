---
name: draw
description: AI 生圖技能 — 用 OpenAI gpt-image-2 生成圖片。說「畫一張」「生成圖片」「生圖」時載入。
---

# Draw — AI 生圖

當使用者說「畫一張 XXX」時執行：

```bash
python ~/.config/opencode/skills/draw/draw.py "<提示詞>" --name <檔名> --quality low
```

- 提示詞：使用者的描述
- 輸出：`slides/generated/` 或 `generated/` 目錄
- 支援參數：`--size` (預設 1536x1024)、`--quality` (low/medium/high/auto)
