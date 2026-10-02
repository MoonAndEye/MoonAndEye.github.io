---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜Skill creator 的概念：把一件事的做法寫成 skill - Tip 20"
date: 2026-10-02 20:34 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - Skills
  - Skill Creator
  - Agent
  - Claude Code
summary: "我用 skill-creator 把重複做法整理成 skill，從釐清需求、寫 SKILL.md、測試到調整 description，並說明如何控制內文長度。"
description: "我用 skill-creator 把重複做法整理成 skill，從釐清需求、寫 SKILL.md、測試到調整 description，並說明如何控制內文長度。"
---
skill creator 是「寫 skill 的 skill」：告訴他你想把哪件事變成 skill，他帶著你問清楚、寫草稿、測、改。

## 為什麼

什麼時候該寫一個 skill？Claude Code 的文件講得直接：同一段指示、同一份 checklist、同一套步驟你一直貼進對話，或者 CLAUDE.md 裡某一節已經從一個事實長成一套流程，就該抽成 skill。skill 的內文平常不佔 context，用到了才整份載入。

寫 skill 最難的是 description 那一行。它是觸發的門：他平常只看 name 和 description，對上了才把整份讀進來。

## 我怎麼做

Anthropic 公開的 skill-creator（在 anthropics/skills 裡）走這個流程：

1. 先弄清楚這個 skill 要讓他做什麼、什麼時候觸發、輸出長什麼樣
2. 寫一版 SKILL.md
3. 寫幾個測試 prompt，讓有這個 skill 的他跑一遍
4. 一起看結果，改，再跑
5. 最後跑 description 的優化，把觸發修準

skill-creator 對 description 的建議很具體：現在的模型傾向「該用卻沒用」，所以 description 要寫得「推一點」，把會用到的情境都列進去。它舉的例子是，與其只寫「怎麼做一個顯示內部資料的 dashboard」，不如加上「只要使用者提到 dashboard、資料視覺化、內部指標、想顯示任何公司資料，就用這個 skill，即使沒說出 dashboard 這個字」。

叫他來的方式很簡單：

```
用 skill-creator 幫我把「新專案開起來就加 lint、formatter、unit test」這件事寫成一個 skill。
```

## 坑

SKILL.md 本身要短。Claude Code 的文件建議控制在 500 行以內，細的參考資料、規格、範例集拆成同一個資料夾裡的別的檔案，像 `reference.md`、`examples.md`，再在 SKILL.md 裡寫清楚哪一份放什麼、什麼時候該讀，他才會在需要的那一刻才去翻。

理由在載入之後：skill 的內文一旦進了對話就會留著，接下來每一輪都在花那些 token。所以本體只寫「要做什麼」，長的東西擺旁邊。

## 小結

skill creator 帶你走完寫 skill 的流程，重點在 description 那一行。

明天講比 skill 大一層的東西：plugin。

參考：
- anthropics/skills 的 skill-creator https://github.com/anthropics/skills/tree/main/skills/skill-creator
- Claude Code 文件：skills https://code.claude.com/docs/en/skills
