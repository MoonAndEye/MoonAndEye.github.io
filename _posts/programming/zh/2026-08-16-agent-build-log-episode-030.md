---
layout: single
title: "Agent Build Log — Episode 030"
date: 2026-08-16 00:32:15 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-030.png
summary: "原本開始打造類似 OpenClaw 的 Agent Gateway，後來發現 Desktop GUI 已經讓它暫時沒有必要。"
description: "原本開始打造類似 OpenClaw 的 Agent Gateway，後來發現 Desktop GUI 已經讓它暫時沒有必要。"
---

今天的任務不多，一開始是想做一個 agent gateway。

![Agent Build Log Episode 030：移除 Agent Gateway](/assets/programming/agent-build-log/agent-build-log-episode-030.png)

就像 Openclaw 有一個 gateway，目的是讓 agent 只有一個 run time 實體，但使用者可以同時有數個界面可以和同一個 Agent 溝通。

但！做到一半，後來發現，以我要做的事情來說，我可能不需要 gateway ，因為我有一個 desktop 的 GUI，這一點可能和 openclaw browser 界面不同。

所以，最後我把 gateway 移除掉了，讓這個 agent 不會像 openclaw 那樣，有一個 gateway 或許，我哪一天還會把他加回來，

誰知道呢？
