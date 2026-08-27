---
name: cola-uiux-game-design
description: "引導 AI 代理進行高品質的 UI/UX 與遊戲設計。當使用者提到「畫面不好看」、「介面想優化」、「設計 UI」、「開發遊戲」、「想要精緻感覺的 UIUX」或要求開發任何網頁/遊戲前端時，必須啟用此技能以確保產出具備現代感、精緻度、微動畫與優質人機互動體驗的成品。"
---

# 高階 UI/UX 與遊戲設計指南 (Premium UI/UX & Game Design)

本技能旨在引導 AI 代理在設計網頁、應用程式介面或遊戲時，擺脫「陽春、單調、工程師美感」的預設輸出，產出具有現代感、精緻視覺層次與流暢互動體驗（Micro-interactions）的專業級產品。

---

## 1. 視覺美學與設計系統規範 (Design System & Aesthetics)

### 🎨 拒絕平庸色彩 (Color Palette)
*   **禁用純色**：絕對不要使用 `#FF0000` (純紅)、`#00FF00` (純綠)、`#0000FF` (純藍)、`#FFFF00` (純黃)。
*   **精選色調 (Semantic Colors)**：
    *   **背景與文字**：使用深石板灰 (Deep Slate, e.g., `#0B0F19`, `#1E293B`) 或極致霧黑，搭配高對比但柔和的乳白 (`#F8FAFC`)。
    *   **主題色 (Primary)**：使用靛藍 (`#6366F1`)、極光綠 (`#10B981`)、紫羅蘭 (`#8B5CF6`)、漸層玫瑰紅。
    *   **狀態色**：錯誤用柔和珊瑚紅 (`#EF4444`)，成功用翡翠綠 (`#34D399`)。

### ✍️ 現代排版與字型階層 (Typography)
*   **字型載入**：一律從 Google Fonts 載入現代字型，例如：
    *   UI/內文：`Inter` 或 `Plus Jakarta Sans`。
    *   標題/數字：`Outfit` 或 `Cabinet Grotesk`。
*   **字重對比 (Font Weights)**：標題使用 `700` 或 `800`，副標題 `500`/`600`，內文 `400`。透過字體粗細而非單純字級大小來拉開視覺層次。

### 🔮 空間深度與磨砂玻璃效果 (Depth & Glassmorphism)
*   **圓角設計**：按鈕圓角至少 `8px` 到 `12px`；卡片圓角 `16px` 到 `24px`。
*   **磨砂玻璃 (Glassmorphism)**：
    ```css
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(12px) saturate(180%);
    -webkit-backdrop-filter: blur(12px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.1);
    ```
*   **柔和陰影 (Box Shadows)**：使用多層次微陰影創造浮空感，避免單層生硬的黑影：
    ```css
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.03), 
                0 1px 3px rgba(0, 0, 0, 0.02);
    ```

---

## 2. 流暢微互動與動態效果 (Micro-interactions & Motion)

UI 的精緻感來自於「回饋與動態」。沒有過渡動畫的介面會顯得生硬。

### ✨ 按鈕與互動組件的動態 (Button Interactions)
*   **平滑過渡**：所有 Hover/Focus/Active 狀態都必須加上平滑過渡：
    ```css
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    ```
*   **Hover 上浮與光暈**：滑鼠懸停時卡片微幅上浮、陰影加深，或者邊框點亮。
    ```css
    .card:hover {
      transform: translateY(-4px);
      box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
      border-color: rgba(99, 102, 241, 0.4);
    }
    ```
*   **點擊壓感 (Press Feedbacks)**：
    ```css
    .button:active {
      transform: scale(0.96);
    }
    ```

### 🌀 載入與過渡 (Transitions & Loaders)
*   **骨架屏 (Skeleton Screen)**：對於異步讀取的資料，一律設計平滑閃爍的骨架屏，而非生硬的 "Loading..." 文字。
*   **SVG 精緻動畫**：若需 Spinner，使用 CSS 旋轉的輕量化 SVG 圖示，配合漸變效果。

---

## 3. 遊戲 UI/UX 專用規範 (Game UI/UX Guidelines)

### ⏱️ 遊戲時鐘與流暢控制 (Game Loop & Controls)
*   **分離物理與渲染**：使用 `requestAnimationFrame` 進行渲染，並以固定時間步長處理。
*   **控制平滑化**：若使用感測器控制遊戲，對數據進行低通濾波或插值，避免元件抖動。

### 💥 回饋感果汁 (Game Juice & Tactile Feedback)
*   **得分/成功回饋**：
    *   字體放大並彈跳 (`transform: scale(1.2)` 配合 bounce 動畫)。
    *   噴灑粒子效果。
    *   數值向上飄浮淡出。
*   **受傷/失敗回饋**：
    *   **螢幕晃動 (Screen Shake)**。
    *   **紅色閃爍**。
    *   **卡片搖晃 (Shake animation)**。

### 📺 介面配置與 HUD (Heads-Up Display)
*   滿版無視差響應式佈局。
*   半透明暗化遮罩，彈出選單以 Scale-up 或 Slide-in 動畫喚出。

---

## 4. 開發工作流程與實作規範 (Implementation Workflow)

1.  **實作前先設計**：在撰寫代碼前，先以 ASCII/Markdown 繪製佈局草圖。
2.  **拒絕佔位符**：不使用 "Lorem Ipsum" 等測試資料；圖標一律用 SVG (如 Lucide icons)。
3.  **CSS Variables 集中管理主題色**。
