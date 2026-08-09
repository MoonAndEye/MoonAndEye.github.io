---
layout: single
title: "Agent Build Log — Episode 025"
date: 2026-08-09 23:55:53 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-025.png
summary: "打造 Project Scaffold 專有技，快速建立乾淨、可建置且可測試的 iOS 或 Android 專案。"
description: "打造 Project Scaffold 專有技，快速建立乾淨、可建置且可測試的 iOS 或 Android 專案。"
---

今天，我做了另一個 Agent 的「專有技」。

![Agent Build Log Episode 025：iOS 與 Android 的 Project Scaffold](/assets/programming/agent-build-log/agent-build-log-episode-025.png)

這次是 Project Scaffold。

它的目標很單純：快速建立一個可以直接拿來測試的 iOS 或 Android App project。

我不需要它一開始就做成完整產品。

我想要做的，能不能在很短的時間內，產出一個結構乾淨、可以 build、可以測試，而且後面方便繼續加功能的專案。這樣 agent 在疊加

第一版我想要的內容大概是：

App 啟動後先顯示一個簡單的 splash / snapshot view。

大約 1.5 秒之後，自動進到一個具備基本登入 UI 的頁面。

專案裡也要先放好開發時常用的基礎 libraries 和基本結構。

但對我來說，有三個東西不是 optional。

Lint。

Formatter。

Unit Test。

這三個我會直接當成 scaffold 的 must-have。

建立專案之後，我可以直接開始讓 agent 測 UI、測 Agent workflow、測新的 capability，而不是每次都先花時間處理專案初始化。甚致是讓 agent 自己用這個 project 開發

所以這個 Project Scaffold 並不是要幫我完成一個 App。

它比較像是幫我快速準備一個乾淨的實驗場。

iOS 或 Android 都一樣。

建立、啟動、登入頁面、lint、format、test。

這些基礎先準備好。

接下來，我才可以把時間花在開發更複雜的能力。
