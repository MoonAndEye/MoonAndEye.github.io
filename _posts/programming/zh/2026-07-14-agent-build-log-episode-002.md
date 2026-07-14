---
layout: single
title: "Agent Build Log — Episode 002"
date: 2026-07-14 21:30:13 +0800
category: programming
author: Marvin Lin
tags: [agent]
summary: DKS MCP 第一版已能透過統一介面查找 MR、Commit、Repository 與 Jira，Pi Agent 也完成 OAuth 與 CLI 執行驗證。
description: DKS MCP 第一版已能透過統一介面查找 MR、Commit、Repository 與 Jira，Pi Agent 也完成 OAuth 與 CLI 執行驗證。
image: /assets/programming/agent-build-log/agent-build-log-episode-002.png
---

今天完成了兩個重要進展。

![Agent Build Log Episode 002：DKS MCP 與 Pi Agent 整合架構](/assets/programming/agent-build-log/agent-build-log-episode-002.png)

## DKS MCP

Developer Knowledge Service，也就是 DKS 的 MCP 已經完成第一版。

目前已驗證可以查找：

- Merge Request（MR）
- Commit
- Repository

另外也已經串接 Jira API，並整合進同一套 MCP 介面中。

這代表 Agent 未來可以透過統一入口，取得更多開發相關知識，而不是分別呼叫不同工具。

## Pi Agent 整合

已經先把 Pi Agent 包裝起來，並完成以下驗證：

- OAuth 可以正常通過
- CLI 指令可以正常執行

目前預設設定為：

- Model：**GPT-5.6 Terra**
- Effort：**xhigh**

DKS 負責開發知識，Pi Agent 負責執行。

整體架構開始慢慢成形了。
