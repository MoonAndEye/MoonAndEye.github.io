---
layout: single
title: "Agent Build Log — Episode 004"
date: 2026-07-16 22:04:12 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-004.png
summary: "Golem Desktop 開發第一天：以 Electron、React 與 Electron Vite 建立桌面介面，並將 Agent 執行隔離在 Electron Utility Process 中。"
description: "Golem Desktop 開發第一天：以 Electron、React 與 Electron Vite 建立桌面介面，並將 Agent 執行隔離在 Electron Utility Process 中。"
---

今天是 Golem Desktop 開發的第一天。

![Agent Build Log Episode 004：Golem Desktop 開發第一天](/assets/programming/agent-build-log/agent-build-log-episode-004.png)

前面幾個 Episode，一直都沒有碰 agent app，都是處理像是 DKS MCP、Pi Agent，以及模型和工具之間要怎麼串接。到了今天，終於開始把這些東西放進一個真正的桌面 App 裡。

Desktop App 使用 Electron，前端則是 React，並透過 Electron Vite 建置。UI 的部分，我暫時直接參考 Codex App，先把基本的操作方式和整體結構做出來，不急著在第一天就設計一套完全不同的介面。

不過我不想讓它只是 Electron 包住一個聊天頁面。

目前 UI 和真正執行 Agent 的地方是分開的。畫面負責顯示和操作，Agent 則跑在獨立的 Electron Utility Process 裡，模型呼叫、工具執行和權限判斷也都會放在那邊處理。

預設模型目前透過 OpenAI Codex OAuth 使用 gpt-5.6-terra，之前完成的 DKS MCP 也會慢慢接進 Desktop App，讓它可以查詢 MR、Commit、Repository 和 Jira 裡的資料。

工具執行前的確認機制和 sandbox 權限限制，也開始一起放進這個架構裡。

今天主要不是完成多少功能，而是正式決定 Golem Desktop 要怎麼開始。

這只是 Desktop App 的第一天，畫面和架構都還很早，但至少第一步已經走出去了。
