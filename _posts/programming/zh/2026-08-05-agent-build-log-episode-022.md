---
layout: single
title: "Agent Build Log — Episode 022"
date: 2026-08-05 23:59:36 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-022.png
summary: "把開發者完成一件事情的過程拆成清楚的小步驟，逐步建立 Agent capabilities。"
description: "把開發者完成一件事情的過程拆成清楚的小步驟，逐步建立 Agent capabilities。"
---

這是我今天學到的事情。

![Agent Build Log Episode 022：把開發者工作拆成 Agent capabilities](/assets/programming/agent-build-log/agent-build-log-episode-022.png)

如果把一個軟體開發者的日常工作拆開來看，要完成「一件事」，其實需要很多不同的小能力。

首先，是語言的聽、說、讀、寫。

開發者需要聽懂別人在說什麼、讀懂需求，也要能把自己的理解、問題和結果表達清楚。

接著，收到需求之後，要先理解文字真正想解決的問題。

然後把需求轉換成實作時能使用的 prompt 或 notes，再把整件事拆成 Step 1 到 Step N。

完成實作之後，還要把 App build 起來。

不只確認自己修改的地方，也要實際走過相關功能，以及使用者最主要的 happy path，確定新的修改沒有破壞原本的流程。

最後，再回覆 stakeholder，告訴對方任務已經完成、實作了什麼，以及如何確認結果。

當我把這些步驟拆開之後，我突然領悟到：

這些一步一步的小能力，就是我現在要做的 Agent capabilities。

其中有些能力，現在的 LLM 已經具備了，我不需要重新實作。

例如理解自然語言、整理文字，以及把需求初步拆解成步驟。

我現在真正需要做的，是把剩下的小步驟規劃清楚。

只要把這些前述的小能力一個一個定義好，Pi Agent 就有能力理解目前完成到哪裡，並把結果轉換成下一步要做的事情。

我原本一直在想，Agent 還缺少哪一個強大的 capability。

但今天我發現，可能不需要先找到一個很大的能力。

我真正要做的，是把開發者完成一件事情的過程，拆成足夠清楚的小步驟。

然後，讓 Agent 一步一步走完。
