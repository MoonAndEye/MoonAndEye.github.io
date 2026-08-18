---
layout: single
title: "Agent Build Log — Episode 033"
date: 2026-08-18 22:36:13 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-033.png
summary: "嘗試讓 Agent 啟動 Android Emulator，卻在第一個指令就被 Permission System 擋住。"
description: "嘗試讓 Agent 啟動 Android Emulator，卻在第一個指令就被 Permission System 擋住。"
---

今天做了一個「支線任務」。

![Agent Build Log Episode 033：Permission System 擋住 Android Emulator 任務](/assets/programming/agent-build-log/agent-build-log-episode-033.png)

主線沒有往前推，我先跑去處理另一個最近一直想測的東西。

我想試著直接使用自己做的 Agent，把 Android Emulator 啟動起來。

原本想得很簡單。

讓 Agent 找到 Android project。

確認 Emulator。

然後執行指令，把它啟動。

結果第一步就失敗了。

Agent 知道下一步要執行什麼指令，但當它真的準備執行時，被目前 Agent 裡的 Permission System 擋住了。

這反而讓我發現一個很實際的問題。

如果權限設計得太嚴格，Agent 明明知道該做什麼，最後卻什麼都做不了。
