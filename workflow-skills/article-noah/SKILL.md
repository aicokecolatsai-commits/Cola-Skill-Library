---
name: article-noah
description: 人因小管家部落格文章撰寫技能。將原始內容轉換為符合 V8 主題風格的 clean HTML，包含 Noah 角色元件、JSON-LD Article Schema 與 AI SEO 優化。
---

# 人因小管家 — 部落格文章撰寫技能

將原始、混亂的部落格草稿（Markdown 匯出、舊 Blogger 內嵌樣式等）轉換為符合 V8 主題風格的 clean HTML。

---

## 輸出規範

- 使用 V8 設計語言的 CSS 變數與色系
- 嵌入 JSON-LD Article Schema 提供 AI SEO
- <strong style="color:red;">全程使用繁體中文</strong>，禁止出現任何簡體中文用字（如「头」→「頭」、「专」→「專」、「发」→「發」等），輸出後須全文掃描確認無簡體字
- 適時插入 Noah 角色互動元件
- 移除所有外站編輯器的垃圾屬性（`cid`、`mdtype`、`white-space` 等）
- 保留原始圖片並確保 `loading="lazy"` 與描述性 `alt`
- 圖片使用 `border-radius: 8px`、滿寬、置中

---

## V8 色系參照

```css
--ergopt-text: #242826;
--ergopt-muted: #6b736f;
--ergopt-border: #dde5df;
--ergopt-accent: #147d75;
--ergopt-accent-soft: #e7f3ef;
--ergopt-warm: #f3eadb;
```

---

## SEO 結構

每篇文章必須嵌入 JSON-LD Article Schema：

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "文章標題（包含人因小管家／Noah 品牌字）",
  "description": "搜尋結果顯示的描述，50-80 字，包含關鍵字",
  "author": { "@type": "Person", "name": "人因小管家 Noah" },
  "image": "首圖網址",
  "keywords": ["人因工程", "關鍵字1", "關鍵字2", "Noah人因小管家"]
}
</script>
```

---

## 文章佈局元件

所有元件共用一個包裹容器：

```html
<div class="article-wrap">
  <!-- 內容放這裡 -->
</div>
```

### 元件 CSS（完整引入）

```css
.article-wrap {
  max-width: 760px; margin: 0 auto;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans TC", "Microsoft JhengHei", Arial, sans-serif;
  color: #242826; line-height: 1.85; font-size: 1.08rem; letter-spacing: .02em;
}
.article-wrap * { box-sizing: border-box; }
.article-wrap .featured-img { width: 100%; border-radius: 8px; margin: 0 0 24px; display: block; }
.article-wrap p { margin: 0 0 1.18em; color: #242826; }
.article-wrap h2 { font-size: 1.55rem; font-weight: 700; color: #242826; margin: 1.85em 0 .7em; line-height: 1.35; padding-bottom: 6px; border-bottom: 2px solid #e7f3ef; }
.article-wrap h3 { font-size: 1.28rem; font-weight: 700; color: #242826; margin: 1.5em 0 .6em; line-height: 1.35; }
.article-wrap strong { color: #147d75; }
.article-wrap ul, .article-wrap ol { margin: 0 0 1.35em 1.4em; padding: 0; }
.article-wrap li { margin: .35em 0; }

.noah-callout {
  background: #e7f3ef; border-left: 4px solid #147d75;
  border-radius: 0 8px 8px 0; padding: 18px 22px; margin: 1.5em 0;
}
.noah-callout .label { font-size: .82rem; font-weight: 700; color: #147d75; letter-spacing: .06em; text-transform: uppercase; margin-bottom: 4px; }
.noah-callout p { margin: 0; color: #242826; }

.ng-box {
  background: #fbfaf7; border: 1px solid #dde5df; border-left: 4px solid #e8a838;
  border-radius: 0 8px 8px 0; padding: 16px 20px; margin: 1em 0;
}
.ng-box .label { font-size: .82rem; font-weight: 700; color: #b8860b; letter-spacing: .06em; text-transform: uppercase; margin-bottom: 4px; }
.ng-box p { margin: 0; color: #4a524e; }

.tip-card {
  background: #f7f8f6; border: 1px solid #dde5df;
  border-radius: 8px; padding: 18px 20px; margin: 1em 0;
}
.tip-card .num {
  display: inline-block; font-size: .78rem; font-weight: 700; color: #fff; background: #147d75;
  border-radius: 999px; padding: 0 10px; line-height: 1.7; margin-bottom: 4px;
}
.tip-card h3 { font-size: 1.1rem; font-weight: 700; color: #242826; margin: 4px 0 6px; }
.tip-card p { margin: 0; color: #4a524e; font-size: 1rem; }

.check-card {
  background: #f7f8f6; border: 1px solid #dde5df;
  border-radius: 8px; padding: 18px 20px; margin: 1em 0;
}
.check-card .num {
  display: inline-block; font-size: .78rem; font-weight: 700; color: #fff; background: #147d75;
  border-radius: 999px; padding: 0 10px; line-height: 1.7; margin-bottom: 4px;
}
.check-card h3 { font-size: 1.1rem; font-weight: 700; color: #242826; margin: 4px 0 6px; }
.check-card p { margin: 0 0 6px; color: #4a524e; font-size: 1rem; }
.check-card .note { font-size: .88rem; color: #6b736f; margin: 0; padding-left: 12px; border-left: 2px solid #dde5df; }

.article-divider {
  border: none; height: 1px;
  background: linear-gradient(90deg, transparent, #dde5df, transparent);
  margin: 2.2em 0;
}

@media (max-width: 700px) {
  .article-wrap { font-size: 1.04rem; }
}
```

---

## 元件使用時機

| 元件 | 用途 | 時機 |
|------|------|------|
| `noah-callout` | Noah 提醒／叮嚀 | 開場引言、結語總結 |
| `ng-box` | NG 姿勢｜錯誤觀念｜地雷 | 列舉常見錯誤時 |
| `tip-card` | 正確步驟｜教學｜技巧 | 列出 numbered 步驟時 |
| `check-card` | 自我檢查項目 | 讀者可自行檢查的項目（如睡姿、姿勢） |
| `pillow-hint` | 挑選指標｜簡潔提示 | 快速參考資訊（如拳度指標） |
| `article-divider` | 段落分隔線 | 每個大段落之間 |

---

## 文章結構模板

```html
<!-- 文章標題（V8 + Noah） -->
<script type="application/ld+json">{/* Article Schema */}</script>
<style>{/* 引入上方 CSS */}</style>

<div class="article-wrap">

  <img class="featured-img" src="..." alt="..." loading="lazy">

  <!-- 開場 1-2 段鋪陳 -->

  <p>...</p>

  <!-- Noah 提醒框（選擇性） -->
  <div class="noah-callout">
    <div class="label">Noah 溫暖提醒</div>
    <p>...</p>
  </div>

  <hr class="article-divider">

  <h2>主題一：人因工程解析</h2>
  <p>...</p>

  <hr class="article-divider">

  <h2>主題二：錯誤姿勢／地雷</h2>
  <div class="ng-box">...</div>
  <div class="ng-box">...</div>

  <hr class="article-divider">

  <h2>主題三：正確做法</h2>
  <div class="tip-card"><div class="num">1</div><h3>...</h3><p>...</p></div>
  <div class="tip-card"><div class="num">2</div><h3>...</h3><p>...</p></div>
  <div class="tip-card"><div class="num">3</div><h3>...</h3><p>...</p></div>

  <hr class="article-divider">

  <h2>Noah 的貼心叮嚀</h2>
  <p>...</p>

  <div class="noah-callout">
    <div class="label">Noah 小管家</div>
    <p>...</p>
  </div>

</div>
```

---

## 命名規則

文章檔案命名：`文章範例_<主題>.html`
Schema headline：結尾包含「人因小管家／Noah」品牌識別
keywords 陣列：最後一項固定為 `"Noah人因小管家"`
圖片 alt：中文描述性文字，不超過 15 字
