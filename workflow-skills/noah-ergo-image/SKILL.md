---
name: noah-ergo-image
description: >-
  Noah 人因小管家社群對比圖完整產圖＋文案工作流。
  吃一個人因主題（如「拖地板」「穿鞋襪」），產出 FB 橫版對比大圖、IG/Threads 正確與錯誤姿勢卡片（共 5 張圖）＋三平台社群文案（共 3 份 txt）。
  當使用者提到「人因圖片」「正確vs錯誤姿勢圖」「Noah 社群圖」「人因工程對比圖」「做人因主題」「產出人因」「ergo image」時，必須使用此技能。
  也可被其他工作流串接呼叫——只要傳入主題名稱與參考圖即可啟動完整管線。
---

# Noah 人因小管家 — 社群對比圖產圖工作流

> 一條「給主題 → 五步驟固定流程 → 輸出 8 個檔案」的可重複工作流。
> **固定的是流程＋規格，浮動的是每次的主題材料。**

---

## 🔗 串接介面（供其他工作流呼叫）

本技能可被其他工作流串接呼叫。呼叫方只需提供：

```yaml
# 必要輸入
topic_name: "穿鞋襪的正確人因姿勢"   # 主題中文名稱
topic_number: 34                      # 編號（流水號）
reference_image: "<path>"             # 參考圖路徑（可選）

# 可選輸入
slug: "shoes"                         # 英文短代碼（未指定則自動推斷）
project_root: "<path>"                # 專案根目錄（未指定則用預設位置）
```

**輸出**：`output/<編號>_<主題名稱>/` 資料夾，內含 5 張圖 + 3 份文案 txt。

---

## 📌 核心角色與語氣

- **角色**：貼心人因小管家 Noah，語氣溫暖貼心，以日常生活小助手角度切入。
- **去醫療化**：將醫療學術語白話化（例如「神經被壓到手麻麻的」、「肌肉在發炎抗議喔」），避免過度醫療化。
- **語言**：回應與所有產出一律使用**繁體中文**。

---

## 🔧 前置需求

### 專案結構

```
<專案根目錄>/
├── input/
│   └── new2.png              # LOGO 去背透明圖檔 (必要)
├── fonts/
│   ├── GenSenRounded2-H.ttc  # 源泉圓體 Heavy (大標題)
│   ├── GenSenRounded2-B.ttc  # 源泉圓體 Bold (標籤/副標)
│   └── GenSenRounded2-M.ttc  # 源泉圓體 Medium (內文)
├── scripts/
│   └── compose_noah_photo_infographic.py  # 合成腳本
└── output/
    └── <編號>_<主題名稱>/     # 每個主題一個子資料夾
```

### Python 環境

```bash
pip install Pillow
```

---

## 🚀 完整工作流程（五步驟）

### 步驟一：確認主題與文案方向

使用者會提供：
1. **主題名稱**（例如「擦拭地板拖地板」「穿鞋襪的正確人因姿勢」）
2. **參考圖**（可選，用來理解正確/錯誤姿勢的差異）

根據主題分析出：
- 錯誤姿勢的具體動作描述
- 正確姿勢的具體動作描述
- 人因風險重點（腰椎壓力、肌肉拉伸、跌倒風險等）

---

### 步驟二：生成底圖（逐張確認）

> ⚠️ **鐵律：必須先生成底圖讓使用者確認 OK，才能進入合成步驟。嚴禁跳過確認直接合成。**

使用 `generate_image` 分別生成**正確姿勢**與**錯誤姿勢**各一張底圖。

#### 生圖參數規範

| 參數 | 規範 |
|------|------|
| AspectRatio | `3:4`（直式，確保人物全身入鏡） |
| 人物族裔 | **必須**指定為 Taiwanese 或 Asian |
| 構圖 | 側面全身照，eye-level，人物從頭到腳完整入鏡不可裁切 |
| 場景 | 與主題匹配的真實居家/辦公室環境 |
| 風格 | `realistic photograph, professional photography, clean composition, soft natural light` |

#### Prompt 模板

**正確姿勢**：
```
A realistic full-body photograph of a Taiwanese Asian [man/woman]
in [場景], [動作描述] CORRECTLY.
[正確姿勢的具體細節].
His/Her entire body from head to feet is fully visible and well-framed.
[服裝]. [場景細節].
Side view, eye-level camera angle.
Professional photography, clean composition, plenty of space around the subject,
soft natural indoor light.
```

**錯誤姿勢**：
```
A realistic full-body photograph of a Taiwanese Asian [man/woman]
in [場景], [動作描述] INCORRECTLY.
[錯誤姿勢的具體細節].
His/Her face shows discomfort and strain.
His/Her entire body from head to feet is fully visible and well-framed.
[服裝]. [場景細節].
Side view, eye-level camera angle.
Professional photography, clean composition, plenty of space around the subject,
soft natural indoor light.
```

#### 確認流程

生成後展示兩張底圖，詢問使用者確認。若要求修改，以 `_v2`、`_v3` 版號重新生成，**嚴禁覆蓋原圖**。

---

### 步驟三：執行合成腳本

底圖確認 OK 後，執行 `compose_noah_photo_infographic.py`。

```powershell
python scripts/compose_noah_photo_infographic.py `
  --correct-base "<正確底圖路徑>" `
  --incorrect-base "<錯誤底圖路徑>" `
  --out-dir "output/<編號>_<主題名稱>" `
  --slug "<英文短代碼>" `
  --logo "input/new2.png" --font-dir "fonts" `
  --main-title "<主標題｜副標>" `
  --ig-topic "<IG 主題文字>" `
  --correct-title "<正確大標>" --incorrect-title "<錯誤大標>" `
  --correct-label "✓ 正確姿勢" --incorrect-label "✗ 錯誤姿勢" `
  --correct-subtitle "<正確副標>" --incorrect-subtitle "<錯誤副標>" `
  --correct-bullet "<重點1>" --correct-bullet "<重點2>" `
  --correct-bullet "<重點3>" --correct-bullet "<重點4>" `
  --incorrect-bullet "<重點1>" --incorrect-bullet "<重點2>" `
  --incorrect-bullet "<重點3>" --incorrect-bullet "<重點4>" `
  --fb-correct-line "✓ <描述1>" --fb-correct-line "✓ <描述2>" `
  --fb-correct-line "✓ <描述3>" `
  --fb-incorrect-line "✗ <描述1>" --fb-incorrect-line "✗ <描述2>" `
  --fb-incorrect-line "✗ <描述3>" `
  --fb-note "💡 Noah 小提醒：<溫暖小提示>"
```

#### 輸出成品（共 5 張圖）

| 檔案 | 尺寸 | 用途 |
|------|------|------|
| `fb_<slug>_photo.png` | 2142×1169 | FB 橫版左右對比大圖 |
| `ig_<slug>_correct.png` | 1080×1080 | IG 正確姿勢卡片 |
| `ig_<slug>_incorrect.png` | 1080×1080 | IG 錯誤姿勢卡片 |
| `threads_<slug>_correct.png` | 1080×1080 | Threads 正確 |
| `threads_<slug>_incorrect.png` | 1080×1080 | Threads 錯誤 |

---

### 步驟四：撰寫三平台社群文案

#### `fb_post.txt`（完整版，200-300 字）
```
<問句開頭，貼近生活>
<錯誤姿勢為什麼傷身，白話化>
<正確方式，列 4 步驟>
Noah 小提醒：<溫暖建議>
#人因工程 #<主題> #<部位保護> #<場景> #Noah人因小管家
```

#### `ig_post.txt`（精簡版，100-150 字）
#### `threads_post.txt`（極短版，50-80 字）

---

### 步驟五：成品展示

建立 walkthrough artifact，嵌入 FB 大圖、carousel 展示 IG 卡片、列出全部 8 個檔案連結。

---

## 🎨 視覺規格速查

### LOGO 規格

| 版型 | LOGO 尺寸 | 位置 |
|------|----------|------|
| FB 橫版 (2142×1169) | 450×300 px | 左右分割線正中央 |
| IG/Threads (1080×1080) | 270×180 px | 卡片右下角 |

### 字體規格（GenSenRounded 源泉圓體）

| 元素 | FB 橫版 | IG/Threads |
|------|---------|-----------|
| 大標題 | 80px Heavy | 60px Heavy |
| 標籤 | 40px Bold | 34px Bold |
| 說明標題 | 36px Bold | 34px Bold |
| 內文 | 28px Medium | 26px Medium |

---

## 📋 白話化對照表

| 醫療用語 | Noah 白話版 |
|---------|----------|
| 腰椎間盤突出 | 腰椎被擠壓到凸出來 |
| 姿勢性低血壓 | 蹲太久突然站起來頭暈暈的 |
| 後腿肌群過度拉伸 | 後面大腿的筋被拉到太緊 |
| 肩頸肌筋膜炎 | 肩膀脖子的肌肉在發炎抗議 |
| 腕隧道症候群 | 神經被壓到手麻麻的 |
| 脊椎中立位 | 背挺直，不要彎也不要太挺 |

---

## 📂 已完成 34 個主題索引

01-滑鼠 | 02-上下床 | 03-螢幕高度 | 04-足底筋膜炎 | 05-背包 | 06-站姿 | 07-枕頭 | 08-開車 | 09-搬東西 | 10-雨天騎車 | 11-沙發 | 12-拿高低物品 | 13-洗碗 | 14-吃飯/洗頭 | 15-上廁所 | 16-看手機 | 17-檯燈光線 | 18-曬衣服 | 19-翹腳 | 20-鍵盤 | 21-筆電 | 22-辦公範圍 | 23-濕滑地板 | 24-開車視線 | 25-夾電話 | 26-雙螢幕 | 27-骨盆椅背 | 28-站姿工作站 | 29-搬運重物 | 30-起床起身 | 31-鍵鼠位置 | 32-工程椅坐姿 | 33-拖地板 | 34-穿鞋襪
