---
layout: single
title: "Agent Build Log — Episode 007"
date: 2026-07-20 00:25:36 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-007.png
summary: "研究 Google ADK 與 Agents CLI，了解如何讓 Coding Agent 透過可重複使用的指令與 skills，建立、評估並部署 Agent。"
description: "研究 Google ADK 與 Agents CLI，了解如何讓 Coding Agent 透過可重複使用的指令與 skills，建立、評估並部署 Agent。"
---

今天花了一些時間研究 Google 的 ADK 和 Agents CLI，想看看 Google 是怎麼把 Agent 的建立流程整理成一套可以被重複使用的方法。

![Agent Build Log Episode 007：研究 Google ADK 與 Agents CLI](/assets/programming/agent-build-log/agent-build-log-episode-007.png)

Agents CLI 本身不是另一個 Coding Agent，而是一套給 Codex、Claude Code 或其他 Coding Agent 使用的指令與 skills，協助它們建立、評估和部署 ADK Agent。

![Google Agents CLI 架構圖](/assets/programming/agent-build-log/google-agents-cli-architecture.png)

我真正想研究的是：怎麼讓一個人只需要用自然語言描述需求，就能把一個 Agent 建立起來，最後一路部署上線。

目前我沒有打算把整套做法直接搬進自己的 Agent。這次比較像是在研究別人的實作，看看哪些設計值得參考，哪些地方可以用自己的方式重新做一次。

自己打造 Agent，不代表所有東西都必須從零開始。

站在巨人的肩膀上。

GitHub:
[https://github.com/google/agents-cli](https://github.com/google/agents-cli)
