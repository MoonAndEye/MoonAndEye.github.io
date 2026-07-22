---
layout: single
title: "Agent Build Log — Episode 010"
date: 2026-07-22 23:55:33 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-010.png
summary: "規劃 Agent 記憶系統，在比較 Mem0、Letta、MemOS 與 Cognee 後，第一版選擇可在 Mac mini 本機運行的 LanceDB 與 Qwen3 Embedding 0.6B。"
description: "規劃 Agent 記憶系統，在比較 Mem0、Letta、MemOS 與 Cognee 後，第一版選擇可在 Mac mini 本機運行的 LanceDB 與 Qwen3 Embedding 0.6B。"
---

今天開始規劃 Agent 的記憶系統。

![Agent Build Log Episode 010：使用 LanceDB 與 Qwen3 Embedding 0.6B 建立記憶系統](/assets/programming/agent-build-log/agent-build-log-episode-010.png)

在真的動手之前，我先找了一輪目前比較知名、GitHub 星星數也比較高的開源方案，想看看別人是怎麼處理記憶的保存、搜尋和召回。

看了一圈之後，最後還是得回到我自己的使用環境。

這套記憶系統必須能直接跑在手上的 Mac mini。我不想一開始就依賴太重的模型，也不想把所有東西都丟到雲端，所以最後選擇用 LanceDB 搭配 Qwen3 Embedding 0.6B。

LanceDB 負責保存和搜尋記憶，Qwen3 Embedding 0.6B 則負責把對話和事件轉成可以被檢索的向量。

這個過程中，我也看了 Mem0、Letta、MemOS 和 Cognee 的基本架構。但研究之後，發現它們都不太是我現在想做的 Agent 方向。

這些方案我先整理進筆記裡，暫時不採用。

第一版的記憶系統，就先從 LanceDB 加上 Qwen3 Embedding 0.6B 開始。
