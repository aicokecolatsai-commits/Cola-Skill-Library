---
name: audio-to-srt
description: 音訊/影片檔自動生成乾淨 SRT 字幕檔。當使用者要「把音訊轉字幕」「做 SRT」「語音轉文字+時間碼」「影片上字幕」時使用。預設走 Groq Whisper-large-v3-turbo（雲端、word-level 時間碼），備援本地 Whisper medium。
---

# audio-to-srt：音訊 → 乾淨 SRT

## 兩條路線

| 路線 | 模型 | 時間碼粒度 | 速度 | 隱私 | 適用 |
|------|------|------------|------|------|------|
| **A. Groq（預設）** | whisper-large-v3-turbo | **word-level** | 快 | 上雲 | 一般情境 |
| B. 本地 Whisper | medium | segment-level | 慢 | 完全本地 | 敏感內容、無網路 |

## 核心原則
1. **時間碼神聖不可侵犯**：清字過程 SRT 時間碼行完全不准改動
2. **段落邊界不可動**：不得合併/拆分/新增/刪除段落
3. **只改文字，不改語意**：修錯字、加標點、順語感

## 路線 A：Groq 流程（預設）

### 環境檢查
```bash
echo $GROQ_API_KEY
ls ~/.groq_api_key
ffmpeg -version
```

### 呼叫腳本
```bash
python "$HOME/.config/opencode/skills/audio-to-srt/scripts/transcribe_groq.py" "輸入檔.mp3" --out _subtitles/輸入檔.groq.json
python "$HOME/.config/opencode/skills/audio-to-srt/scripts/resegment.py" _subtitles/輸入檔.groq.json --out _subtitles/輸入檔.raw.srt
python "$HOME/.config/opencode/skills/audio-to-srt/scripts/apply_vocab.py" _subtitles/輸入檔.raw.srt --out _subtitles/輸入檔.vocab.srt
python "$HOME/.config/opencode/skills/audio-to-srt/scripts/validate_srt.py" --raw _subtitles/輸入檔.vocab.srt --clean _subtitles/輸入檔.clean.srt
python "$HOME/.config/opencode/skills/audio-to-srt/scripts/srt_to_txt.py" _subtitles/輸入檔.clean.srt --out 輸入檔.txt
```

## 檔案結構
```
audio-to-srt/
├── SKILL.md
├── scripts/
│   ├── transcribe_groq.py
│   ├── resegment.py
│   ├── apply_vocab.py
│   ├── srt_to_txt.py
│   └── validate_srt.py
└── references/
    ├── cleanup_rules.md
    └── vocabulary.md
```
