---
layout: single
title: 你沒給 AI 正確方向，它就載不到你要去的地方
date: 2026-03-16 08:00 +0800
category: programming
author: Marvin Lin
tags: [AI, AI Agent, Product, Mobile, Workflow]
summary: 用 Figma Make 做 demo 時，我把「可見畫面」當成規格，結果 AI 也把 demo 當成 spec。真正要給的是行為規格：launch state machine。
---

## Writer

你沒給 AI 正確方向，它就載不到你要去的地方。

我今天踩了一個很典型、也很容易被忽略的坑：

我叫 AI agent：
> 請參考 Figma Make share link 中的內容，進行實作。

聽起來很合理對吧？

但問題是：**share link 裡的內容，其實是 demo，不是產品的行為規格（behavior spec）**。

### 我到底給錯了什麼？

為了 demo 快，我在 Figma Make 裡把 app 的起始畫面直接做成 main tab bar。

於是 AI 真的超級「聽話」：
- 它把 demo 當成真需求
- 直接實作成「一進 app 就進主頁」

這在 demo 上看起來沒問題。

但在 mobile app 上，這通常不是你想要的真實行為。

### 標準的 mobile app launch 其實是一個 state machine

在 mobile app 上，標準手法通常是：app launch 後先進入一個 Launch Screen 的 activity / view controller，然後在這個實例物件中做判斷。

例如一個常見流程會是：

1) 強迫更新 / 建議更新 / 可正常使用

2) 在「可正常使用」之後，才檢查是否可以 auto login
- if yes → go to main tab bar
- if not → go to login page

這些條件與分支，才是「方向」。

UI 長什麼樣，是結果。

### 我為什麼會一直以為 AI 在亂改？

我一開始一直以為：AI 沒有照我的指令做、一直改掉我的實作。

最後我去檢查 Figma Make build 起來的 React 網站，才發現網站的流程就是如此設計。

換句話說：
- **我給 AI 的「世界」就是那個 demo**
- AI 只能照我給的可見狀態去估

它沒錯。

錯的是我一開始給的方向：我給的是 demo，不是行為規格。

### 結論：要 AI 做對 UI，先把「行為規格」寫清楚

你要 AI 做對 UI，先定義「行為」：
- 入口狀態（entry states）
- 分支條件（branching conditions）
- 成功條件（success criteria）

**UI 是結果；流程才是方向。**

## Editor

這篇要傳達的核心很清楚，也符合 builder 角度：
- 不是模型問題，是 workflow/spec 的問題
- 有具體工具（Figma Make）與具體流程（update → auth → main/login）支撐可信度

我在 final 只做兩個「不改意思」的微調：
1) 讓「demo vs spec」對比更快出現（更像文章的主線）
2) 結尾再強化一次可複用的 checklist

## Final

你沒給 AI 正確方向，它就載不到你要去的地方。

我今天踩了一個很典型、也很容易被忽略的坑。

我叫 AI agent：
> 請參考 Figma Make share link 中的內容，進行實作。

聽起來很合理。

但我後來才發現：**share link 裡的內容，其實是 demo，不是產品的行為規格（behavior spec）**。

為了 demo 快，我在 Figma Make 裡把 app 的起始畫面直接做成 main tab bar。

於是 AI 真的超級「聽話」：
- 它把 demo 當成真需求
- 直接實作成「一進 app 就進主頁」

但在 mobile app 上，標準的啟動流程通常不是「看 UI 長什麼樣」，而是先跑一個 state machine。

一般做法是：app launch 後先進入 Launch Screen 的 activity / view controller，然後在這個實例物件中做判斷，例如：

1) 強迫更新 / 建議更新 / 可正常使用

2) 在「可正常使用」之後，才檢查是否可以 auto login
- if yes → go to main tab bar
- if not → go to login page

我一開始一直以為：AI 沒有照我的指令做、一直改掉我的實作。

最後我去檢查 Figma Make build 起來的 React 網站，才發現網站的流程就是如此設計。

換句話說：
- 我給 AI 的「世界」就是那個 demo
- AI 只能照我給的可見狀態去估

它沒錯。

錯的是我一開始給的方向：我給的是 demo，不是行為規格。

結論很簡單：**要 AI 做對 UI，先把行為規格寫清楚。**

一個最小 checklist：
- 入口狀態（entry states）
- 分支條件（branching conditions）
- 成功條件（success criteria）

UI 是結果；流程才是方向。
