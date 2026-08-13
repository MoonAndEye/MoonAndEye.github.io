---
layout: single
title: "Agent Build Log — Episode 029"
date: 2026-08-13 23:43:32 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-029.png
summary: "先研究 Pi Agent extension 生態系，再決定哪些 MCP、權限與 Desktop GUI 能力值得自己打造。"
description: "先研究 Pi Agent extension 生態系，再決定哪些 MCP、權限與 Desktop GUI 能力值得自己打造。"
---

今天，我開始比較認真研究 Pi Agent 的 extension 生態系。

![Agent Build Log Episode 029：研究 Pi Agent 的 extension 生態系](/assets/programming/agent-build-log/agent-build-log-episode-029.png)

之前我一直把注意力放在 Agent core、本身的 tools，以及我自己的 capabilities。

但研究下去之後，我開始發現：

Pi Agent 很多我原本打算自己做的能力，其實已經有人透過 extensions 做出來了。

第一個是 MCP。

透過 MCP adapter，Pi Agent 可以接上現有的 MCP servers。

這對我來說很重要，因為我自己的 Agent 已經有不少能力是建立在 MCP 上。

像是 DKS、Jira、XcodeBuildMCP，未來也可能繼續加入更多外部工具。

如果這一層已經有成熟的 extension，我就不需要自己重新處理 MCP server 的連線、tool discovery 和呼叫方式。

第二個是 Approval / Permission System。

Agent 開始可以操作 shell、修改檔案、呼叫 MCP，甚至執行一些可能影響環境的操作之後，我一定需要一層權限控制。

哪些 tool 可以直接執行。

哪些操作要先問使用者。

哪些操作應該直接擋掉。

這些其實也已經有 Pi extensions 在處理。

我不需要重新發明一套 allow、deny、ask 的 permission system。

第三個是 Desktop GUI。

像 Pi GUI 這類專案，已經把 Pi Agent 包成 Desktop App，提供 session、workspace、tool execution timeline 和其他 GUI 操作方式。

這也讓我開始重新思考：

我自己的 Desktop App 裡，到底哪些東西是真的需要自己打造，哪些其實可以直接參考甚至使用現有的生態系。

研究這些 extensions 之後，我最大的感覺是：

我現在不只是「使用 Pi Agent」。

我其實是在使用一個已經開始形成的 Agent 生態系。

MCP 幫我接外部能力。

Permission System 幫我控制 Agent 可以做什麼。

Desktop GUI 幫我處理使用者和 Agent 之間的互動介面。

而我真正需要把時間花下去的地方，是那些只有我的 Agent 才需要的能力。

像 Acceptance、Bug Blame、Spec Diff，還有後面更多針對我工作流程打造的 capabilities。

以前我的想法比較像：

缺什麼，就自己寫什麼。

但今天開始，我的想法變成：

先看看 Pi Agent 的 ecosystem 裡，有沒有已經被做過、使用過、驗證過的 extension。

把時間留下來，做真正屬於這個 Agent 的東西。
