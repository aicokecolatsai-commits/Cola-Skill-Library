---
name: 00-cola-ergo
description: COLA / Noah 人因小管家共用技能，用於 Codex 與 Antigravity 產出真人照片式人因社群圖、FB/IG/Threads 正確錯誤對比圖、透明壓字版型、透明背景素材支援，以及不覆蓋舊檔的版控輸出。當使用者提到 Noah、人因小管家、人因工程、職安評估、正確錯誤對比圖、真人照片配圖、透明背景圖、Antigravity 共用技能時使用。
---

# 00_cola_ergo

## 定位

這是 COLA / Noah 人因小管家在 Codex 與 Antigravity 共用的技能。用途是把人因工程主題做成溫暖、生活化、去醫療化的社群圖，尤其適合「正確 vs 錯誤」對比圖。

輸出風格以真人照片為主，不使用 SVG 代替照片。人物需符合在地感，優先使用台灣人或亞洲人。若主題聚焦在腳、手、肩頸、腰背等局部風險，照片也應聚焦該部位，不一定要出現整個人。

## 固定原則

- 回應與圖中文字使用繁體中文。
- 文案用日常語氣，不做醫療診斷感的表述。
- 底圖使用真人照片或真實情境照片，不用插畫、SVG、3D 假圖。
- 圖片主標或小標需直接出現「正確」與「錯誤」。
- 不使用白色標題字卡蓋住背景；以透明深色漸層、文字陰影、直接壓字為主。
- 字句要人工斷行，避免最後一行只有 `。`、`，`、`、` 等標點。
- 新圖永遠另存版號，不覆蓋舊圖。已有無版號檔案時，下一版從 `_v2` 開始。
- 若使用透明 PNG 底圖或透明背景素材，腳本可用 `--transparent-output` 保留 alpha。

## Noah 圖片規格

- LOGO：預設使用專案內 `input/new2.png`，必須透明貼上，不加圓形遮罩、不加框線裁切。
- FB 對比圖：`2142x1169`，LOGO 縮放 `450x300`，置中貼在左右分割線。
- IG / Threads：`1080x1080`，LOGO 縮放 `270x180`，貼右下角。
- 字體：優先使用專案 `fonts/GenSenRounded2-*.ttc`。
- 正確色：綠色系；錯誤色：紅色系。不要讓整張圖變成單一色調。

## 產出流程

1. 讀取專案規範：
   - `AGENTS.md`
   - `.agents/skills/health-noah/SKILL.md`
   - `input/` 內的主題材料
2. 生成或選擇兩張 1:1 底圖：
   - `correct_base`：正確或較友善的人因姿勢 / 工具 / 環境。
   - `incorrect_base`：錯誤或較吃力的人因姿勢 / 工具 / 環境。
3. 底圖先存到 `output/[topic]/codex_photo_final/` 或當次指定資料夾。
4. 使用 `scripts/compose_noah_photo_infographic.py` 合成 FB、IG、Threads。
5. 逐張檢查：照片感、主題焦點、文字位置、LOGO、正確/錯誤標示、斷句、版號。

## Antigravity 透明背景注意事項

Antigravity 若提供透明 PNG 作為底圖或局部素材，可以直接交給合成腳本。

- 一般照片輸出：不加 `--transparent-output`，輸出一般 RGB PNG。
- 透明背景輸出：加 `--transparent-output`，輸出 RGBA PNG，保留透明背景與透明素材 alpha。
- 若透明底圖上仍需要文字可讀性，可保留腳本預設漸層；若要後續在其他軟體排版，建議先輸出透明版本，再由 Antigravity 疊到最終背景。

## 腳本用法

從 `02-health-noah` 專案根目錄執行：

```powershell
python "E:\SNOOCOLA\AI_Project\00_skill\00_cola_ergo\scripts\compose_noah_photo_infographic.py" `
  --correct-base "output\04_足底筋膜炎\codex_photo_final\correct_base_photo_final_v3.png" `
  --incorrect-base "output\04_足底筋膜炎\codex_photo_final\incorrect_base_photo_final_v3.png" `
  --out-dir "output\04_足底筋膜炎\codex_photo_final" `
  --slug "plantar" `
  --main-title "足底筋膜炎｜正確 vs 錯誤站法" `
  --correct-title "正確｜腳底別硬撐" `
  --incorrect-title "錯誤｜薄底踩硬地" `
  --correct-label "正確｜腳底有支撐" `
  --incorrect-label "錯誤｜薄底踩硬地" `
  --correct-subtitle "鞋底有支撐，地面也軟一點" `
  --incorrect-subtitle "腳底每天都在加班" `
  --correct-bullet "選有支撐的鞋底" `
  --correct-bullet "腳下加一塊止滑軟墊" `
  --correct-bullet "讓腳底少一點硬碰硬" `
  --incorrect-bullet "薄底鞋直接踩硬地" `
  --incorrect-bullet "腳跟與足弓容易吃力" `
  --incorrect-bullet "久站越久越想換腳站" `
  --fb-correct-line "鞋底穩、地面軟一點" `
  --fb-correct-line "久站時，腳底不用一路硬撐" `
  --fb-incorrect-line "薄底加硬地" `
  --fb-incorrect-line "每一步都讓腳底多吃一點力" `
  --fb-note "Noah 小提醒：先從鞋底支撐與站立地面開始調整"
```

需要透明背景輸出時，在最後加：

```powershell
  --transparent-output
```

腳本會列出所有輸出檔案路徑。以最新列出的 FB / IG / Threads 圖作為本次成品。
