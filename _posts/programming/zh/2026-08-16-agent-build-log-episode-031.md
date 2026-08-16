---
layout: single
title: "Agent Build Log — Episode 031"
date: 2026-08-16 23:22:46 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-031.png
summary: "開始設計 Google Chat 等 IM 整合，透過 Plug-In 將聊天訊息的收發與 Agent 主體分開。"
description: "開始設計 Google Chat 等 IM 整合，透過 Plug-In 將聊天訊息的收發與 Agent 主體分開。"
---

準備開始串接 Google Chat 等 IM 通知，設計有參考 OpenClaw。

![Agent Build Log Episode 031：以 Plug-In 串接 IM 通知](/assets/programming/agent-build-log/agent-build-log-episode-031.png)

有一個基本的 Plug-In 設計，讓 Agent 的主體和接受 Chat、回應 Chat 的部分切開。

當 Chat inbound message mention 我指定的 Chat 應用程式後，會依照 space ID + message ID 分類，還會經過一個去重的邏輯，然後才會送進 Agent 層進行處理。

處理完後，再回到這個 Chat Plug-In 裡面，把 message 送回去。
