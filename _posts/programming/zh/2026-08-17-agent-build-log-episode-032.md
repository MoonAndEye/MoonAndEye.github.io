---
layout: single
title: "Agent Build Log — Episode 032"
date: 2026-08-17 22:57:34 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-032.png
summary: "繼續打通 Chat 與 Agent 的完整流程，解決 inbound 與 outbound 過程中遇到的問題。"
description: "繼續打通 Chat 與 Agent 的完整流程，解決 inbound 與 outbound 過程中遇到的問題。"
---

今天，我繼續把 Chat 和 Agent 的流程真正打通。

![Agent Build Log Episode 032：打通 Chat 與 Agent](/assets/programming/agent-build-log/agent-build-log-episode-032.png)

原本以為，只要把昨天設計好的 Chat Plug-In 接起來，inbound message 送進 Agent，處理完再把結果回出去，應該就差不多了。

但真的開始串之後，才發現事情沒有那麼順。

一開始是各種 inbound error。

有時候 webhook 有收到訊息，但格式沒有正確進到 Chat Plug-In。

有時候 message 已經進來了，卻在 space、message 或 thread 的識別上出問題，導致 Agent 根本沒有收到真正要處理的內容。

好不容易把 inbound 打通之後，換 outbound 出錯。

Agent 已經成功收到訊息，也完成了處理，但最後的 response 卻送不回 Chat。

總之，這個 Agent 現在和 OpenClaw 或其他 Agent 一樣，可以從聊天界面中接受指令。
