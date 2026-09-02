---
name: cinematic-scrollytelling-ui
description: 電影級敘事視覺、Apple 風格 Scrollytelling 滾動敘事與沉浸式互動設計（Cinematic UI & Narrative Scrollytelling）。當使用者提到「電影感」、「敘事UI」、「Apple風格」、「Scrollytelling」、「沉浸式」、「視差滾動」、「Dark Luxury」、「故事性視覺」時載入。
---

# 🎬 Cinematic Scrollytelling UI: 電影級敘事視覺與沉浸式設計

> 專為旗艦級產品發布、品牌故事與頂級數位體驗打造。借鏡 **Apple 產品官網的章節式敘事（Scrollytelling）**、**Dark Luxury 深色奢華氛圍** 與 **滿版沉浸式視覺**，將使用者從「閱讀資訊」帶入「身歷其境的感官旅程」。

---

## 🌌 電影級 UI 的 4 大核心美學原則

1. **章節式敘事節奏 (Chapter-based Storytelling)**：
   - 頁面不再是死板的區塊堆疊，而是分為「序幕 (Prologue) $\rightarrow$ 衝突/挑戰 (The Challenge) $\rightarrow$ 突破性創新 (The Innovation) $\rightarrow$ 極致細節 (The Craft) $\rightarrow$ 尾聲/行動 (The Finale)」。
2. **Dark Luxury 深邃氛圍 (Atmospheric Lighting)**：
   - 採用極深色背景（`#050508` ~ `#0D0E15`），搭配細膩的多層次放射狀微光（Radial Ambient Glow）與背光玻璃擬態（Frosted Glass）。
3. **視差滾動與固定鏡頭 (Scrollytelling Camera Movement)**：
   - 利用 GSAP ScrollTrigger 將主要視覺主體（如 3D 模型、產品特寫）固定在螢幕中央（Pin），隨滾動滑順切換特寫視角、爆炸圖解與標註文字。
4. **巨型字體與留白張力 (Dramatic Typography & Void)**：
   - 使用超大字級（`text-6xl` ~ `text-8xl`），緊湊字距（`tracking-tighter`），透過大面積純粹留白創造奢華平靜感。

---

## 🛠️ Apple 風格 Scrollytelling 實作模板結構

```html
<!-- 全螢幕固定敘事章節 -->
<section class="cinematic-chapter relative h-[300vh] bg-[#050508] text-white">
  <!-- 固定視窗 (Pinned Viewport) -->
  <div class="sticky top-0 h-screen w-full flex items-center justify-center overflow-hidden">
    
    <!-- 背景微光光暈 -->
    <div class="absolute w-[600px] h-[600px] bg-indigo-600/20 blur-[140px] rounded-full pointer-events-none"></div>

    <!-- 中央核心產品/視覺主體 (隨滾動放大/旋轉) -->
    <div class="product-hero relative z-10 scale-100 transition-transform">
      <img src="/mockup.png" alt="Product" class="max-w-xl drop-shadow-[0_20px_50px_rgba(0,0,0,0.8)]" />
    </div>

    <!-- 隨滾動切換的字幕敘事卡片 -->
    <div class="narrative-step absolute z-20 text-center max-w-lg opacity-0" data-step="1">
      <span class="text-indigo-400 font-mono text-sm tracking-widest uppercase">Chapter 01 : Precision</span>
      <h2 class="text-5xl font-bold tracking-tight mt-2">重新定義極致速度</h2>
      <p class="text-zinc-400 mt-4 leading-relaxed">每一個晶體排列，都為了毫秒之間的極限響應。</p>
    </div>

  </div>
</section>
```

---

## 🎨 配色與氛圍調色盤

| 元素 | 推薦色碼 | 說明 |
| :--- | :--- | :--- |
| **主背景** | `#050508` | 接近深空的微冷深黑 |
| **次背景/卡片** | `rgba(255, 255, 255, 0.03)` | 超微弱半透明白色底 |
| **邊框光澤** | `rgba(255, 255, 255, 0.08)` | 細緻髮絲線框 |
| **氛圍光源 (Accent Glow)** | `#6366F1` (Indigo) / `#38BDF8` (Sky) | 配合 `blur-[120px]` 漫反射 |
| **標題高光** | `linear-gradient(180deg, #FFFFFF 0%, #94A3B8 100%)` | 金屬質感文字漸層 |