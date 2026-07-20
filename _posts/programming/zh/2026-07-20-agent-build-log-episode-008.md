---
layout: single
title: "Agent Build Log — Episode 008"
date: 2026-07-20 20:55:29 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-008.png
summary: "重整 Agent 核心，讓 CLI、Browser 與 Desktop App 共用同一套能力，並維持各介面為只負責輸入、顯示與互動的 thin clients。"
description: "重整 Agent 核心，讓 CLI、Browser 與 Desktop App 共用同一套能力，並維持各介面為只負責輸入、顯示與互動的 thin clients。"
---

今天發現一個問題。

![Agent Build Log Episode 008：讓 CLI、Browser 與 Desktop App 共用 Agent 核心](/assets/programming/agent-build-log/agent-build-log-episode-008.png)

CLI、Browser 和 Desktop App 雖然看起來都在使用同一個 Agent，但實際上，它們並沒有真的走同一套邏輯。之前之所以能正常運作，只是因為三邊的實作剛好維持一致。

也就是說，沒有實作成我想要的樣子。

發現這件事之後，我讓 Agent 自己開始重整這一層。

目標很明確：之後新增的 tool，只要接進核心，就要能同時被 CLI、Browser 和 Desktop App 使用，而不是每個介面各自再做一次。

我也希望這三個介面能一直維持 thin。它們只負責接收輸入、顯示結果和處理各自的互動，不應該把 Agent 的能力和邏輯重新實作一遍。

今天沒有增加新功能，但把一個原本只是「剛好一致」的狀態，開始改成真正由同一套能力支撐。
