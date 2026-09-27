---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜給行為規格、不給畫面：demo 當 spec 給他，他就照 demo 做 - Tip 15"
date: 2026-09-27 13:01 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - Figma Make
  - 行為規格
summary: "我曾把 Figma Make share link 當成產品規格，結果 Agent 依 demo 把啟動畫面做成主頁。這篇示範如何用入口狀態、分支條件與成功條件，寫出可執行的行為規格。"
description: "我曾把 Figma Make share link 當成產品規格，結果 Agent 依 demo 把啟動畫面做成主頁。這篇示範如何用入口狀態、分支條件與成功條件，寫出可執行的行為規格。"
---

這一篇改寫自我部落格的《你沒給 AI 正確方向，它就載不到你要去的地方》，照這個系列的格式重寫過。原始文章：https://www.marvinswift.com/zh/programming/ai-direction-demo-spec-state-machine/

你沒給他正確方向，他就載不到你要去的地方。要他做對 UI，先把行為規格寫清楚，別只給他畫面。

## 為什麼

我踩過一個很典型、也很容易被忽略的坑。我叫他：「請參考 Figma Make share link 中的內容，進行實作。」聽起來很合理。後來才發現，share link 裡的內容是 demo，產品的行為規格（behavior spec）它沒有。

為了 demo 快，我在 Figma Make 裡把 app 的起始畫面直接做成 main tab bar。於是他真的超級「聽話」：把 demo 當成真需求，直接做成「一進 app 就進主頁」。

我一開始以為他沒照我的指令做，一直改掉我的實作。最後我去檢查 Figma Make build 起來的 React 網站，才發現網站的流程就是這樣設計的。換句話說，我給他的「世界」就是那個 demo，他只能照我給的可見狀態去估。他沒錯。錯的是我一開始給的方向：我給的是 demo，該給的是行為規格。

## 我怎麼做

mobile app 標準的啟動流程，先跑的是一個 state machine，畫面長什麼樣是後面的事。一般做法是：app launch 後先進一個 Launch Screen 的 activity 或 view controller，在這個實例物件裡做判斷：

1. 強迫更新／建議更新／可正常使用（Tip 12 講的那幾個狀態）
2. 「可正常使用」之後，才檢查能不能 auto login：可以就進 main tab bar，不行就進登入頁

這些條件與分支，才是「方向」。UI 長什麼樣，是結果。

要他做對 UI，給他一個最小的行為規格，三件事：

- 入口狀態（entry states）
- 分支條件（branching conditions）
- 成功條件（success criteria）

拿上面的啟動流程填一次：

- 入口狀態：app 剛啟動，還沒登入
- 分支條件：版本檢查的結果（強迫更新、建議更新、可正常使用）；有沒有還有效的登入
- 成功條件：可正常使用而且 auto login 成功，進 main tab bar；其他情況各進對應的畫面

## 小結

UI 是結果，流程才是方向。給他行為規格，別只給 demo。

明天講一個小技巧：畫面上的問題，截圖直接貼進 Claude Code。

原文：https://www.marvinswift.com/zh/programming/ai-direction-demo-spec-state-machine/

