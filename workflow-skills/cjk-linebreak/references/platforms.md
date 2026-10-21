# 各平台套用指南

原則都一樣：**禁止瀏覽器在字與字之間換行（`keep-all`），再在詞與詞之間標出可以換行的位置（`<wbr>`）**。不同平台只差在「能不能放程式」和「能不能改 CSS」。

## 先選做法

| 平台能做什麼 | 做法 | 使用的檔案 |
|---|---|---|
| 可以放 `<script>`（Blogger、WordPress 自架、Wix 自訂程式碼、一般網站） | **網頁載入後切詞**：貼一段腳本就好 | `scripts/cjk-wbr.js` |
| 可以跑建置腳本（靜態網站、Hugo、Jekyll、Astro、VitePress） | **事先切詞**：建置後處理輸出的 HTML | `scripts/add_wbr.py` |
| React、Next.js、Vue 管理的畫面 | **元件切詞** | `templates/CjkText.tsx`、`cjkWordBreak.ts` |
| 不能放程式、也不能改 CSS（Notion、Medium、Google 協作平台） | 只能手動控制換行 | 見「無法套用的平台」 |
| 不是網頁（Word、簡報、海報、圖片） | 手動換行加人工檢查 | 見「非網頁內容」 |

> **React／Vue 的畫面不要用 `cjk-wbr.js`**：這類框架自己管理畫面上的元素，外部腳本改動文字節點後，框架更新畫面時可能出錯（例如 `removeChild` 錯誤）或把 `<wbr>` 洗掉。請改用 `CjkText` 元件。

## Google Blogger（可以套用）

Blogger 的文章是伺服器產生的一般 HTML，可以直接用 `cjk-wbr.js`。

### 方法 A：放進主題（建議，所有頁面都生效）

1. 先備份：Blogger 後台 →「主題」→ 主題右邊的下拉選單 →「備份」。
2. 同一個下拉選單 →「編輯 HTML」。
3. 搜尋 `</body>`，在它**前面**貼上以下內容。Blogger 的主題是 XML，腳本一定要包在 `CDATA` 裡：

```html
<script>
//<![CDATA[
window.CJK_WBR = {
  selector: ".post-body, .post-title",  // 文章內文和標題
  terms: ["你的品牌名稱", "專有名詞"],     // 不可拆開的詞
}
/* 這裡貼上 scripts/cjk-wbr.js 的完整內容 */
//]]>
</script>
```

4. 儲存後，用手機打開任一篇文章檢查。

### 方法 B：用小工具（不想動主題時）

「版面配置」→「新增小工具」→「HTML/JavaScript」，貼上同一段 `<script>…</script>`（這裡不需要 `CDATA`）。缺點是有些主題的手機版不會顯示小工具，所以手機上要特別檢查。

### 找出文章內文的 class

大部分 Blogger 主題（Contempo、Soho、Emporio、Notable 等）的內文是 `.post-body`，標題是 `.post-title`。不確定的話，在文章上按右鍵 →「檢查」，看包住內文的元素是哪個 class。

### Blogger 的注意事項

- **留言區、相關文章**如果是之後才載入的，設定 `observe: true`。
- **不要在文章編輯器裡手動插入 `<wbr>`**：編輯器切換「撰寫／HTML」模式時可能會整理掉，而且以後改文章很難維護。用主題腳本自動處理比較可靠。
- 驗證：打開文章頁，用 `scripts/check_linebreaks.js` 在 360 和 390px 寬度各跑一次。

## WordPress

- **自架 WordPress**：用外掛（例如 WPCode）或子主題的 `footer.php`，在 `</body>` 前面插入和 Blogger 一樣的腳本（不用 `CDATA`），`selector` 通常是 `.entry-content, .entry-title`。
- **WordPress.com 免費方案**不能放自訂 JavaScript。可以先用 `add_wbr.py` 處理文章 HTML，再貼進「自訂 HTML」區塊。

## Wix、Squarespace、Shopify

這三個平台都有「自訂程式碼」或「Code Injection」的設定（部分需要付費方案），把腳本放在頁尾（body end），`selector` 依實際的版面 class 設定。

## 靜態網站與文件網站

Hugo、Jekyll、Astro、Eleventy、VitePress、Docusaurus 等：

- **建議**：建置完成後，對輸出資料夾裡的 HTML 執行 `add_wbr.py`，例如 `python add_wbr.py public/**/*.html --terms protected-terms.txt`（Windows 的 shell 不會展開 `**`，可以改用 `find` 或 PowerShell 列出檔案）。
- **最簡單**：在版型的 `</body>` 前面放 `cjk-wbr.js`。
- VitePress、Docusaurus 的畫面由 Vue／React 管理，事先處理（`add_wbr.py`）比較安全。

## 電子報、EDM

- 電子郵件不能執行 JavaScript，只能用 `add_wbr.py` 事先插入 `<wbr>`。
- 各家收信軟體對 `<wbr>` 和 `keep-all` 的支援不一致，特別是電腦版 Outlook。寄送前要用 Gmail（手機與電腦）、Apple Mail、Outlook 實際測試。
- 標題、按鈕這類短文字，直接用 `<br>` 手動決定換行位置最保險。

## 手機 App

- **WebView 或網頁做的 App**（例如動齡）：跟網頁一樣，依框架選擇 `CjkText` 或 `add_wbr.py`。
- **Android 原生**：Android 13 以後的 `TextView` 有 `android:lineBreakWordStyle="phrase"`，但官方說明以日文和韓文為主，繁體中文要實際測試才能使用。不支援時，重要文字由設計決定換行位置。
- **iOS 原生**：目前沒有可靠的中文分詞換行設定，重要文字要手動決定換行位置。

## 無法套用的平台

Notion、Medium、Google 協作平台、大部分社群貼文，都不能放程式也不能改 CSS：

- 段落文字只能接受瀏覽器的預設換行。
- 標題、按鈕、圖片說明這類短文字，盡量控制在一行以內，或改寫成不容易斷在詞中間的長度。
- Google 協作平台的「嵌入」是 iframe，裡面的腳本影響不到頁面本身的文字。

## 非網頁內容

Word、PowerPoint、Google 文件、Canva、海報、圖片沒有 `<wbr>` 可以用，做法改成「人工決定換行位置，再逐行檢查」：

1. **標題、海報、簡報**：用 Shift+Enter（換行不換段）手動在詞與詞之間換行。
2. **Word**：「段落」→「中文印刷樣式」勾選「依照東亞語言的規則控制首尾字元」，可以避免標點出現在行首；但詞還是可能被拆開，重要段落仍然要檢查。
3. **逐行檢查**：把每一行的最後兩個字和下一行的開頭兩個字列出來，看有沒有把詞拆開。
4. **改了字級、字型或框的寬度之後要重新檢查**，因為換行位置會跟著改變。

## 未來的瀏覽器原生支援

CSS 的 `word-break: auto-phrase` 可以讓瀏覽器自己依詞換行，但目前（2026 年）只在 Chrome 系瀏覽器、而且只對日文（`lang="ja"`）有效，繁體中文還不能用。等瀏覽器支援繁體中文後，可以改成只寫 CSS，不必再插入 `<wbr>`。
