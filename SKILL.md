---
name: cola-skill-library
description: Cola 跨平台 AI Agent 技能庫全集入口 — 提供高階工作流技能（密涅瓦思考模式、UI/UX 設計、腦力激盪、影片規格等）與教學系列 MCP 懶人包。說「Cola 技能庫」「安裝 Cola 技能」時載入。
---

# 🚀 Cola Skill Library — AI Agent 自動安裝與導覽入口

當使用者給你這個 repo 網址並說要安裝或查詢技能時：

## 步驟一：列出技能分類

向使用者展示三大類技能：
1. **🧠 高階工作流技能 (Workflow Skills)**：
   * `minerva-thinking`：密涅瓦大學 100+ HCs 思考模塊與深層決策引導
   * `ui-ux-pro-max`：旗艦級 UI/UX 設計系統與元件庫
   * `brainstorming`：蘇格拉底式創意與需求深度探索引導
   * `skill-creator`：技能開發、評測與自動優化工作台
   * `video-spec-builder`：影音分鏡、TTS 與多模態影片規格生成器
   * `yourself-skill`：數位孿生 / 數位分身建構工具
   * `persona-coach`：多角色顧問諮詢教練 (Noah, Rose, Mark, Lucas...)
   * `meta-prompt`：YAML 結構化 Prompt 與系統指令架構師
   * `00_cola_ergo`：Noah 人因小管家圖卡與對比圖產生器
   * 學術系列：`academic-deep-research`、`academic-paper`、`academic-paper-reviewer`、`academic-pipeline`
    * 內容與生活：`article-noah`、`cola-uiux-game-design`、`draw`、`職場人因文案專家`、`presentation-coach`、`resume-builder`、`habit-tracker`、`yingyin-transcript`（影音轉運站：逐字稿＋精煉＋密涅瓦）
   * 專案流程：`project-init`、`startup`、`shutdown`

2. **⚙️ 工程與寫作技能集 (Engineering Skills)**：
   * 工程工作流：`code-review`、`tdd`、`diagnosing-bugs`、`implement`、`research`、`prototype`、`qa`、`triage`、`wayfinder`、`to-spec`、`to-tickets` 等
   * 密集面試：`grill-me`、`grilling`、`batch-grill-me`、`grill-with-docs`、`loop-me`
   * 交接協作：`handoff`、`claude-handoff`、`ask-matt`
   * 架構設計：`codebase-design`、`design-an-interface`、`domain-modeling`、`improve-codebase-architecture`
   * 寫作：`writing-beats`、`writing-fragments`、`writing-shape`、`writing-great-skills`、`edit-article`
   * 工具設定：`setup-pre-commit`、`setup-ts-deep-modules`、`wizard`、`setup-matt-pocock-skills` 等
   * 完整 41 個請見 `engineering-skills/` 目錄

3. **🛠️ 教學系列懶人包 (Lazy Packs)**：
   * `00-env-setup`、`01-notebooklm`、`03-github`、`05-obsidian`、`07-supabase`、`08-firebase`、`09-ollama`、`10-gemini`、`11-workspace`、`12-draw` 等。

## 步驟二：確認使用者需求並安裝

詢問使用者：「請問你想安裝哪一個或哪幾項技能？」
確定後，讀取對應目錄下的 `SKILL.md` 指令協助載入或安裝到全域技能目錄。
