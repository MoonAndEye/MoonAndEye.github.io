---
layout: single
title: "Agent Build Log — Episode 003"
date: 2026-07-15 20:42:40 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-003.png
summary: "完成第一版 Browser UI，支援建立新對話、搜尋歷史與釘選；介面專注回答、搜尋與整理，Agent 執行將由其他介面負責。"
description: "完成第一版 Browser UI，支援建立新對話、搜尋歷史與釘選；介面專注回答、搜尋與整理，Agent 執行將由其他介面負責。"
---

今天完成了第一版 Browser UI。

![Agent Build Log Episode 003：Browser UI 第一版](/assets/programming/agent-build-log/agent-build-log-episode-003.png)

整體操作方式接近 ChatGPT，目前已具備：

- 建立新對話
- 搜尋歷史對話
- 釘選重要對話

![Golem Browser UI 第一版實際畫面](/assets/programming/agent-build-log/agent-build-log-episode-003-browser-ui.png)

「專案」功能暫時不做，先把最核心的對話與搜尋體驗完成。

下一步會把 DKS MCP 串接進來，讓使用者可以直接透過介面查找開發相關資料。

不過目前不打算把 Agent 的實際執行流程放進 Browser UI。

這個介面的定位很明確：

**專注回答問題、搜尋資料，以及整理對話。**

Agent 的執行與控制，之後會由其他介面負責。

功能開始增加，但每一層的責任也必須保持清楚。
