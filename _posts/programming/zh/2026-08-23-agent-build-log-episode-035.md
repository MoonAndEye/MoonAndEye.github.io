---
layout: single
title: "Agent Build Log — Episode 035"
date: 2026-08-23 00:31:28 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-035.png
summary: "把 mobile acceptance 功能拆成選配外掛，讓 App 從 1.1 GB 降到約 300 MB。"
description: "把 mobile acceptance 功能拆成選配外掛，讓 App 從 1.1 GB 降到約 300 MB。"
---

開始準備 ship 的版本了。

![Agent Build Log Episode 035：把驗收功能拆成選配外掛](/assets/programming/agent-build-log/agent-build-log-episode-035.png)

這次要認真決定，哪些功能應該一開始就包進 App，哪些功能應該拆成外掛，需要的時候再下載。

一開始開發的時候，我把 mobile acceptance 相關功能直接包進 build 出來的 App 裡。

其中包含 Xcode Build MCP 和 Appium。

結果整個 App 一度大到 **1.1 GB**。

但這些功能其實主要是拿來做驗收，不是每個人都會需要。

所以我開始把這些驗收相關的功能拆出去，改成選配的外掛。

拆完之後，App 大小已經降到大約 **300 MB**。

讓它變成外掛，需要的人再裝就好。
