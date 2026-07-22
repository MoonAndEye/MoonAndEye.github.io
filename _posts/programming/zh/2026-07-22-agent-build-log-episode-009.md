---
layout: single
title: "Agent Build Log — Episode 009"
date: 2026-07-22 00:34:59 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-009.png
summary: "為 DKS MCP 加入 repository aliases，讓常用名稱、單複數與自然語言查詢都能解析到正確的 repo 與連結。"
description: "為 DKS MCP 加入 repository aliases，讓常用名稱、單複數與自然語言查詢都能解析到正確的 repo 與連結。"
---

今天我又回頭處理 DKS（Developer Knowledge Service）MCP，開始補 repository aliases。

![Agent Build Log Episode 009：為 DKS MCP 加入 repository aliases](/assets/programming/agent-build-log/agent-build-log-episode-009.png)

在真實對話裡，人通常不會直接講出完整而精確的 repo 名稱。他們會問：「登入模組在哪裡？」我希望 Agent 能理解這句話真正指的是什麼，然後回傳正確的 repository 名稱和連結。

接著我遇到了一個很常見的語言問題。

在我使用的語言裡，名詞通常沒有複數變化，動詞也不會像某些語言一樣隨著語境改變形式。所以我輸入的字，不一定會和 repository 的正式名稱完全一致。

例如 repo 可能叫 `trees`，但我搜尋的是 `tree`；或者正式名稱是 `node`，我卻輸入 `nodes`。對人來說意思很清楚，但對現在的 DKS 搜尋而言，這些是完全不同的字，所以它只會回傳找不到結果。

發現這件事之後，我讓 Agent 幫 repositories 建立 alias mappings。這些 aliases 現在會涵蓋常用名稱、單複數形式，以及人們自然提到同一個 repo 時可能使用的其他說法。我也補上測試，確保每一個 alias 都會解析到正確的 repository。

我不希望使用 DKS 的人必須記住每一個 repo 的完整正式名稱。

他們應該可以用自己的話提問。這些差異，應該交給 Agent 處理。
