---
layout: single
title: "Agent Build Log — Episode 036"
date: 2026-09-07 08:56:04 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-036.png
summary: "準備採用開源 Pi GUI，沿用文字換行、模型選擇與 LLM Provider 串接的既有實作，把開發時間留給自己的專有技。"
description: "準備採用開源 Pi GUI，沿用文字換行、模型選擇與 LLM Provider 串接的既有實作，把開發時間留給自己的專有技。"
---

今天，我開始準備把開源的 [Pi GUI](https://github.com/minghinmatthewlam/pi-gui) 用在自己的 Desktop App 裡。

![Agent Build Log Episode 036：使用 Pi GUI 處理桌面互動，準備接入自己的專有技](/assets/programming/agent-build-log/agent-build-log-episode-036.png)

在 [Episode 029](/zh/programming/agent-build-log-episode-029/)，我就研究過 Pi Agent 的 extension 生態系，也提到了 Pi GUI。當時，我開始思考哪些功能可以直接使用現有的實作。

現在準備把 App 做到可以 ship，這件事變得更具體了。

之前自己做 Desktop App，除了 Agent 的能力，還有很多介面上的細節要處理。

像是文字的換行、模型的選擇，以及不同 LLM Provider 的串接。

這些看起來都很基本，但每一個都會影響實際使用。

文字換行不順，寫一段需求就會很卡。要換模型時，使用者需要能在介面裡直接選擇。換成另一個 LLM Provider，也需要有地方設定並完成串接。

如果這些都由自己實作，就得持續花時間處理和維護。

所以我打算直接使用 Pi GUI 的開源實作，讓這些桌面上的基本功能可以更快準備好。

Pi GUI 本身就是建立在 Pi Agent 上的桌面介面。既然我的 Agent 已經使用 Pi，接下來可以沿用這一層，再把自己的功能加進去。

我比較想繼續投入的，是前面做過的那些「專有技」。

像 Acceptance、Bug Blame 和 Spec Diff。

這些功能對應的是我工作上需要完成的事情，也關係到 PM 和 QA 能不能透過這個 Agent，把規格確認和驗收做完。

現在有了開源的桌面實作可以使用，我希望把更多開發時間留給這些能力。

接下來，我會先把 Pi GUI 和目前的 Agent 接起來，確認文字換行、模型選擇和 Provider 串接的操作，再逐步把自己的專有技接回桌面介面。
