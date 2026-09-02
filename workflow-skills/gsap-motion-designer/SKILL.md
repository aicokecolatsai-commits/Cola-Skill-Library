---
name: gsap-motion-designer
description: GSAP 3 專業網頁動效、ScrollTrigger 滾動觸發、時間軸編排與互動微動效專家（GSAP Motion & ScrollTrigger Expert）。當使用者提到「GSAP」、「網頁動效」、「滾動動畫」、「ScrollTrigger」、「時間軸」、「微互動」、「平滑滾動」、「Lenis」、「文字逐字滑入」、「磁吸按鈕」時載入。
---

# ⚡ GSAP Motion Designer: 網頁動效與時間軸編排專家

> 專注於將靜態網頁提升至 **Awwwards / FWA 得獎級** 動態質感的 GSAP 動效專家。涵蓋 GSAP 3 核心 API、ScrollTrigger 滾動視差驅動、SplitType 文字編排、Lenis 平滑滾動與高流暢微互動。

---

## 🎯 核心能力矩陣

1. **GSAP 3 核心時間軸 (Timelines & Stagger)**：精準排定連續動畫次序與物理緩動曲線。
2. **ScrollTrigger 滾動觸發 (Scrollytelling & Parallax)**：Pin 固定視角、Scrub 滾動同步、進出場視差。
3. **Typography 文字動效 (SplitType)**：標題逐字 (Chars)、逐詞 (Words)、逐行 (Lines) 上浮滑入。
4. **高階微互動 (Micro-interactions)**：磁吸按鈕 (Magnetic Buttons)、自訂跟隨光圈游標 (Custom Cursor)、SVG 描邊路徑 (DrawSVG)。
5. **平滑滾動整合 (Lenis Smooth Scroll)**：消除瀏覽器原生滾動生硬頓挫感。

---

## 🛠️ 最佳實踐與實作範例

### 1. 現代前端引入標準 (Next.js / React / Vite)
```javascript
import { useEffect, useRef } from 'react';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);
```

### 2. 經典 Hero 區塊入場時間軸 (Entrance Timeline)
```javascript
const tl = gsap.timeline({ defaults: { ease: 'power3.out', duration: 1 } });

tl.from('.hero-badge', { y: -20, opacity: 0, duration: 0.6 })
  .from('.hero-title span', { y: 60, opacity: 0, stagger: 0.1 }, '-=0.3')
  .from('.hero-desc', { y: 30, opacity: 0, duration: 0.8 }, '-=0.5')
  .from('.hero-cta', { scale: 0.9, opacity: 0, duration: 0.6 }, '-=0.4')
  .from('.hero-mockup', { y: 80, opacity: 0, duration: 1.2, ease: 'power4.out' }, '-=0.6');
```

### 3. ScrollTrigger 滾動釘選與橫向滾動 (Pin & Horizontal Scroll)
```javascript
gsap.to('.horizontal-container', {
  xPercent: -100 * (sections.length - 1),
  ease: 'none',
  scrollTrigger: {
    trigger: '.pin-section',
    pin: true,
    scrub: 1, // 平滑滾動阻尼
    snap: 1 / (sections.length - 1),
    end: () => '+=' + document.querySelector('.horizontal-container').offsetWidth
  }
});
```

### 4. 磁吸按鈕 (Magnetic Hover Effect)
```javascript
const btn = document.querySelector('.magnetic-btn');
btn.addEventListener('mousemove', (e) => {
  const rect = btn.getBoundingClientRect();
  const x = e.clientX - rect.left - rect.width / 2;
  const y = e.clientY - rect.top - rect.height / 2;
  gsap.to(btn, { x: x * 0.35, y: y * 0.35, duration: 0.3, ease: 'power2.out' });
});
btn.addEventListener('mouseleave', () => {
  gsap.to(btn, { x: 0, y: 0, duration: 0.6, ease: 'elastic.out(1, 0.4)' });
});
```

---

## ⚠️ 動效效能與防呆鐵律

1. **僅對 `transform` 與 `opacity` 進行動畫**：
   - 嚴禁直接動畫 `top`、`left`、`width`、`height`（會觸發重排 Reflow，導致掉幀）。
   - 一律使用 `x`, `y`, `scale`, `rotation`, `autoAlpha`。
2. **記憶體釋放與清理**：
   - 在 React / Vue 元件卸載時，必須呼叫 `ScrollTrigger.getAll().forEach(t => t.kill())` 或使用 `gsap.context()` 清理。
3. **無障礙與防暈眩 (Prefers-Reduced-Motion)**：
   - 必須偵測 `window.matchMedia('(prefers-reduced-motion: reduce)')`，當使用者開啟防眩暈時，自動將所有動效 duration 設為 0 或直接停用。