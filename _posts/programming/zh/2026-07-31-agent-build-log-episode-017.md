---
layout: single
title: "Agent Build Log — Episode 017"
date: 2026-07-31 22:56:20 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-017.png
summary: "開始實作以 SQLite 建立索引、Markdown 保存內容，並按日期與 session 組織的 Agent 記憶系統。"
description: "開始實作以 SQLite 建立索引、Markdown 保存內容，並按日期與 session 組織的 Agent 記憶系統。"
---

今天，我正式開始實作 Agent 的記憶系統。

![Agent Build Log Episode 017：以 SQLite 和 Markdown 實作 Agent 記憶系統](/assets/programming/agent-build-log/agent-build-log-episode-017.png)

第一版不會先使用向量資料庫或複雜的 RAG 架構。

我打算先用 SQLite 和 Markdown，組成一套簡單、透明，而且可以直接檢查內容的記憶系統。

這個設計主要參考 OpenClaw 的記憶方式。

在歷史記憶的部分，系統會按照日期建立紀錄。

每一天都會有一個以 yyyy-mm-dd 命名的目錄，用來保存當天發生的事情。

但一天之內，Agent 可能會有很多次不同的對話和任務。

所以我不打算把所有內容都塞進同一個 Markdown 檔案。

同一天內的每一個 session，都可以有自己獨立的 Markdown 檔。

這樣可以保留每次 session 的上下文，也能避免不同任務的內容全部混在一起。

Markdown 負責保存人可以直接閱讀的記憶內容。

SQLite 則負責保存結構化資料，例如 session 的時間、標題、檔案位置、狀態，以及不同記憶之間的關聯。

Agent 需要尋找過去的記憶時，可以先透過 SQLite 找到可能相關的日期和 session，再讀取對應的 Markdown 檔案。

今天，我先從最簡單的結構開始：

SQLite 負責索引。

Markdown 負責記住發生過的事情。

而每一段記憶，都從一個日期和一次 session 開始。
