---
name: cjk-linebreak
description: 中文斷詞換行技能（CJK line break / 中文不斷詞）。讓網頁上的中文只在詞與詞之間換行，不會出現「自｜己」「血｜壓」這種把詞拆成兩行的情況，電腦和手機都一樣。當使用者提到「斷詞」「斷行」「換行」「字被拆開」「詞被切斷」「中文換行很怪」「keep-all」「wbr」，或要建立、修改中文網頁、App 畫面、官網文案時載入。支援純靜態 HTML（事先插入 <wbr>）與 React／Next.js（畫面顯示時切詞）。
---

# 中文斷詞換行技能

中文沒有空格，瀏覽器預設可以在任何兩個字之間換行，所以常把詞拆成兩行，例如「自｜己」「血｜壓」「福聚｜徠」。這種錯誤很容易被看到，也很傷專業感，**做中文網頁一定要處理**。

## 核心原則（不論哪種網站都一樣）

1. **先禁止瀏覽器隨便換行**：中文文字套用 `word-break: keep-all`。
2. **再標出可以換行的位置**：在詞與詞之間插入 `<wbr>`。瀏覽器就只會在 `<wbr>`、空白和標點換行。
3. **斷詞工具會切錯**：一定要搭配「保護詞彙表」，表上的詞一律不拆，並且逐句檢查結果。
4. **標點跟著前一個詞**：結尾標點（。，、」）不可以出現在行首，開頭標點（「（）不可以出現在行尾。
5. **英文和數字不可拆開**：例如 `Google Play`、`SBIR`、`2026`。
6. **一定要在瀏覽器實際檢查**：測試通過不代表畫面正確。

### CSS 規則

```css
/* 中文文字的容器 */
.cjk {
  word-break: keep-all;        /* 只在 <wbr>、空白和標點換行 */
  overflow-wrap: break-word;   /* 只有單一個詞比整行還寬時才強制換行 */
  line-break: strict;          /* 避免標點出現在行首 */
}
```

**禁止使用**：
- `word-break: break-all`：任意兩個字之間都能換行，等於沒處理。
- `overflow-wrap: anywhere`：瀏覽器計算最小寬度時會把每個字都當成可以換行的位置。在 flex 或 grid 版面裡，容器可能因此縮得很窄，讓詞又被拆開。需要保底的話，改用 `break-word`。

## 步驟 1：判斷網站類型，選擇做法

| 網站類型 | 做法 | 使用的檔案 |
|---|---|---|
| 純靜態 HTML（官網、活動頁、單頁網站） | **事先產生**：用 BudouX 斷詞，直接把 `<wbr>` 寫進 HTML | `scripts/add_wbr.py` |
| React、Next.js、Vue 等（文案在程式裡，或由 API 回傳） | **畫面顯示時切詞**：用瀏覽器內建的 `Intl.Segmenter`，由元件插入 `<wbr>` | `templates/cjkWordBreak.ts`、`templates/CjkText.tsx` |
| Markdown 或 CMS 產生的頁面 | 建置完成後，對輸出的 HTML 執行 `add_wbr.py` | `scripts/add_wbr.py` |

### 1A. 純靜態 HTML

```bash
pip install budoux==0.9.3
python scripts/add_wbr.py site/index.html --terms tools/protected-terms.txt
```

- 腳本只處理 `<body>` 裡看得到的文字，不會動 `<head>`、`<script>`、`<style>`、`<title>` 和 HTML 屬性。
- 可以重複執行：每次會先移除舊的 `<wbr>` 再重新產生。**只要改了文案，就要重新執行。**
- `--terms` 指向專案自己的保護詞彙檔，一行一個詞，`#` 開頭是註解。通用詞彙已經內建在腳本裡。
- 建議把腳本複製到專案的 `tools/`，並把執行方式寫進專案的 `AGENTS.md`，讓其他 agent 也知道。

### 1B. React／Next.js

1. 把 `templates/cjkWordBreak.ts` 複製到 `lib/`，把 `templates/CjkText.tsx` 複製到共用元件資料夾。
2. 在 `PROTECTED_TERMS` 補上專案的品牌詞和專業用語。
3. 在全域 CSS 加上 `.cjk` 規則（見上方「CSS 規則」）。
4. 使用方式：

```tsx
<p className="cjk"><CjkText>每一次完成，都是照顧自己的累積。</CjkText></p>
```

- `CjkText` 只接受純文字字串。文字裡有連結或粗體時，把每一段純文字分別包起來。
- 舊瀏覽器沒有 `Intl.Segmenter` 時，會把整段當成一個詞，不會出錯，但也就不會插入換行點。
- `templates/cjkWordBreak.test.ts` 是 Vitest 測試範例，新增保護詞彙時也要把詞加進測試。

## 步驟 2：建立與維護保護詞彙表

斷詞工具（BudouX、`Intl.Segmenter`）是用一般語料訓練的，常會拆錯以下幾類詞：

- **品牌與產品名稱**：福聚徠、動齡、艾力賀
- **專業用語**：體適能、肌耐力、物理治療、人體工學、常模
- **常用詞**：日常、生活、理解、紀錄、下載、工具、不是、而是
- **數量詞**：一次、一個、一天、五分鐘

通用清單在 `references/protected-terms.md`。每個專案再加上自己的品牌詞，還有人工檢查時發現被拆開的詞。

**比較長的詞要放在前面**，例如「物理治療師」要排在「物理治療」前面，才不會只保護到一部分。

## 步驟 3：逐句檢查斷詞結果

執行斷詞後，不能只看測試是否通過：

1. 把每一句新文案的切詞結果印出來，例如 `日常｜生活｜裡，｜量一次｜血壓`。
2. 看到被拆開的詞，就加進保護詞彙表，再執行一次。
3. 重要的詞也要加進契約測試，避免之後被改回去：

```js
// 檢查 HTML 裡常用詞沒有被 <wbr> 拆開
for (const term of ["自己", "血壓", "動齡"]) {
  const pattern = new RegExp([...term].join("(?:<wbr>)?"), "g")
  for (const match of html.matchAll(pattern)) {
    assert.ok(!match[0].includes("<wbr>"), `「${term}」被 <wbr> 拆開`)
  }
}
```

## 步驟 4：在瀏覽器實際驗證

把 `scripts/check_linebreaks.js` 的內容貼到瀏覽器 DevTools 的 Console，或用 agent 的瀏覽器工具執行。它會找出畫面上**每一個實際換行的位置**，回報：

- `midWordBreaks`：在兩個中文字中間換行、而且那裡沒有 `<wbr>` 的位置（應該是 0）
- `horizontalScroll`：頁面有沒有水平捲動（應該是 false）
- `samples`：前 20 個問題位置，附上前後文

**至少要檢查這 4 種寬度**：360、390、768、1280px。通過標準：每種寬度的 `midWordBreaks` 都是 0，`horizontalScroll` 都是 false。

> 提醒：腳本看的是畫面上的實際換行，所以只能檢查目前畫面上顯示的內容。摺疊選單、分頁或對話框裡的文字，要先打開再執行一次。

## 步驟 5：寫進專案規範

處理完之後，在專案的 `AGENTS.md` 加上一段「中文換行」規則，讓之後修改文案的人（或 agent）知道：

1. 改了文案要重新執行斷詞（靜態網站），或改用 `CjkText` 包住文字（React）。
2. 保護詞彙表放在哪裡，怎麼新增。
3. 禁止使用 `break-all` 和 `overflow-wrap: anywhere`。
4. 合併前要在 360 和 390px 寬度檢查。

## 常見問題

| 狀況 | 原因 | 處理方式 |
|---|---|---|
| 加了 `keep-all`，整段文字卻完全不換行、超出畫面 | 只設了 `keep-all`，沒有插入 `<wbr>` | 執行斷詞，插入 `<wbr>` |
| 手機上某個詞還是被拆開 | 斷詞工具切錯，或那段文字沒有包 `CjkText` | 把詞加進保護詞彙表；確認那段文字有經過處理 |
| 標點出現在行首 | 標點被切成獨立的詞 | 使用模板的標點合併規則，並加上 `line-break: strict` |
| `<title>` 或 meta 描述裡出現 `<wbr>` 字樣 | 處理範圍包到 `<head>` | 腳本只處理 `<body>`；不要手動在屬性裡插入 |
| 搜尋引擎或複製文字時出現奇怪的符號 | 誤用了零寬空白（U+200B） | 改用 `<wbr>`，它不會被複製出來，也不影響搜尋 |

## 附件

- `scripts/add_wbr.py`：靜態 HTML 用的斷詞腳本（BudouX）
- `scripts/check_linebreaks.js`：瀏覽器換行檢查腳本
- `templates/cjkWordBreak.ts`、`templates/CjkText.tsx`、`templates/cjkWordBreak.test.ts`：React／Next.js 模板
- `references/protected-terms.md`：通用保護詞彙與維護方式

## 實際案例

- 福聚徠官網（`bewellfutlife.com`，純靜態）：用 `add_wbr.py` 插入 `<wbr>`，在 360、390、768、1280px 檢查，詞中間換行 0 處。
- 動齡 App（Next.js）：用 `lib/cjkWordBreak.ts` 加上 `CjkText` 元件，從護照和首頁等改版頁面開始，逐頁套用。
