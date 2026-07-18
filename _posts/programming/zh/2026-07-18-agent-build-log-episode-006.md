---
layout: single
title: "Agent Build Log — Episode 006"
date: 2026-07-18 20:42:09 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-006.png
summary: "開始整理 Agent 的 evals 題目庫，從既有 skills 與專案挑選真實的 iOS 與 mobile development 任務，建立可重複比較的基準線。"
description: "開始整理 Agent 的 evals 題目庫，從既有 skills 與專案挑選真實的 iOS 與 mobile development 任務，建立可重複比較的基準線。"
---

今天開始整理 Agent 的 evals 題目庫。

![Agent Build Log Episode 006：開始整理 Agent evals 題目庫](/assets/programming/agent-build-log/agent-build-log-episode-006.png)

我打算直接從自己過去累積的 skills，以及目前正在開發的專案中挑題目。第一階段會先以 iOS 和 mobile development 常見的工作為主，因為這些才是我真正希望 Agent 能處理好的事情。

沒有 evals，我其實很難判斷 Agent 是真的變好了，還是只是某一次剛好答對。

SWE 類型的 benchmark 也不只是測它會不會回答程式問題，而是看它能不能理解既有程式碼、找出需要修改的地方、完成實作、執行測試，最後把整個任務做完。

我做這套題庫不是為了追排行榜，而是想先留下一條可以重複比較的基準線。之後每次更換模型、工具或工作流程，我才知道 Agent 到底進步了，還是其實悄悄退步了。

不過今天連第一題都還沒建立。

目前只是先讓 Coding Agent 盤點和分類現有的 skills 與專案內容，看看哪些真實任務適合整理成之後可以反覆測試的 benchmark。

在讓 Agent 變得更好之前，我得先有辦法證明它真的變好了。
