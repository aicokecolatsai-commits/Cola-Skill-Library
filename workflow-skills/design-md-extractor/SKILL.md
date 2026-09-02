---
name: design-md-extractor
description: 網站設計風格逆向提取、Design Tokens 萃取與 DESIGN.md 生成器（Design Extractor & Tokens Generator）。當使用者提到「提取網站風格」、「抓取設計」、「產生 DESIGN.md」、「提取配色」、「提取字體」、「逆向設計」、「Open Design」時載入。
---

# 🌐 Design MD Extractor: 網站設計風格逆向提取器

> 利用瀏覽器 DOM 與 Computed CSS 分析技術，快速逆向解析任何目標網站的**視覺風格、色盤（Color Palette）、字體層級（Typography Scale）、圓角與陰影（Design Tokens）**，並自動輸出標準化 `DESIGN.md` 供前端專案直接套用。

---

## 🎯 提取維度規範

提取一個網站的設計系統時，涵蓋以下 5 大維度：

1. **色彩系統 (Color Palette)**：
   - Primary, Secondary, Background, Surface, Border, Text (Heading/Body/Muted), Accent。
2. **字體系統 (Typography Scale)**：
   - Font Family (Heading & Body), Font Sizes (h1~h6, p, small), Line Heights, Font Weights。
3. **間距與佈局 (Spacing & Layout)**：
   - Max Width (Container), Padding/Margin 基準單位 (4px/8px 網格)。
4. **裝飾與邊框 (Radius & Borders)**：
   - Border Radius (sm, md, lg, full), Border Colors, Border Widths。
5. **陰影與效果 (Shadows & Blurs)**：
   - Box Shadows, Backdrop Blurs (Glassmorphism), Glows。

---

## 📋 標準 DESIGN.md 模板範例

```markdown
# Design System Specification (DESIGN.md)

## 🎨 Color Palette
- **Background**: `#090A0F` (Deep Space Dark)
- **Surface / Card**: `#12151F` (Border: `#1E2335`)
- **Primary / Accent**: `#6366F1` (Indigo 500)
- **Primary Hover**: `#4F46E5` (Indigo 600)
- **Text Primary**: `#F8FAFC` (Slate 50)
- **Text Muted**: `#94A3B8` (Slate 400)
- **Success / Status**: `#10B981` (Emerald 500)

## 🔤 Typography Scale
- **Font Family**: `Inter, system-ui, sans-serif`
- **Display 1**: `font-size: 56px; line-height: 1.1; font-weight: 800; letter-spacing: -0.02em;`
- **Heading 1**: `font-size: 40px; line-height: 1.2; font-weight: 700; letter-spacing: -0.01em;`
- **Heading 2**: `font-size: 28px; line-height: 1.3; font-weight: 600;`
- **Body Regular**: `font-size: 16px; line-height: 1.6; font-weight: 400;`
- **Caption / Small**: `font-size: 13px; line-height: 1.5; font-weight: 500;`

## 📦 Design Tokens
- **Border Radius**: Card: `16px` (`rounded-2xl`), Button: `10px` (`rounded-xl`), Badge: `9999px` (`rounded-full`)
- **Card Shadow**: `0 10px 30px -10px rgba(0, 0, 0, 0.5)`
- **Glow Effect**: `radial-gradient(circle, rgba(99,102,241,0.15) 0%, rgba(0,0,0,0) 70%)`
- **Container Max-Width**: `1200px` (`max-w-7xl`)
```

---

## 🛠️ 如何配合 Playwright 逆向提取？

當需要分析某個網站時，可使用 Playwright 執行以下 JavaScript 代碼提取 Computed Styles：

```javascript
const styles = await page.evaluate(() => {
  const getStyle = (el, prop) => window.getComputedStyle(el).getPropertyValue(prop);
  const body = document.body;
  const h1 = document.querySelector('h1') || body;
  const btn = document.querySelector('button') || document.querySelector('a.btn') || body;

  return {
    bg: getStyle(body, 'background-color'),
    textColor: getStyle(body, 'color'),
    fontFamily: getStyle(body, 'font-family'),
    h1Size: getStyle(h1, 'font-size'),
    h1Weight: getStyle(h1, 'font-weight'),
    btnBg: getStyle(btn, 'background-color'),
    btnRadius: getStyle(btn, 'border-radius'),
  };
});
```