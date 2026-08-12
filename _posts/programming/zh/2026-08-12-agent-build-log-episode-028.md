---
layout: single
title: "Agent Build Log — Episode 028"
date: 2026-08-12 23:39:31 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-028.png
summary: "使用 Appium 補上 iOS Web Login 的操作缺口，讓 Agent 能繼續完成整個驗收流程。"
description: "使用 Appium 補上 iOS Web Login 的操作缺口，讓 Agent 能繼續完成整個驗收流程。"
---

今天，繼續解決上一篇留下來的問題。

![Agent Build Log Episode 028：Appium 補上 iOS 驗收流程的 Web Login 缺口](/assets/programming/agent-build-log/agent-build-log-episode-028.png)

iOS 的驗收目前有一個很麻煩的斷點。

如果 App 使用的是原生 UI，Agent 可以透過 XcodeBuildMCP 操作 Simulator、點擊按鈕、切換頁面，再按照 Jira ticket 上的 spec 進行驗收。

但只要登入流程是 Web 網頁，就會卡住。

XcodeBuildMCP 可以把 Agent 帶到登入畫面，卻沒有辦法直接操作網頁裡面的 DOM 元素。

也就是說：

Agent 可以打開登入頁。

但它沒辦法自己完成登入。

而如果連登入都過不了，後面的驗收流程也就全部無法開始。

所以今天，我開始找另一個方法。

最後我找到的是 Appium。

我發現 Appium 可以取得 iOS Web 登入頁面的 DOM 元素，也就代表 Agent 有機會操作原本 XcodeBuildMCP 無法處理的 Web 登入流程。

這剛好補上了目前驗收流程缺少的那一塊。

原生 App UI 的操作，可以繼續交給 XcodeBuildMCP。

遇到 Web Login 時，則切換到 Appium，找到對應的輸入框和按鈕，完成登入。

登入完成之後，再回到 App 裡。

這時候 Agent 才真正有能力進入我要驗收的 target tab 或 ViewController。

接下來，就可以繼續按照 Jira ticket 的 spec 操作 App 最後產出驗收報告。

所以這次解掉的，看起來只是一個「登入問題」。

但對 Acceptance 這個 capability 來說，它其實是一個很重要的缺口。

因為 Agent 要做到真正的 App 驗收，不能只會操作某一種 UI。

它必須有能力一路走過：

App → Web Login → App → Target Page → Acceptance

上一篇，Agent 走到登入頁就卡住了。

今天，我使用 appium 讓 agent 開發繼續往下
