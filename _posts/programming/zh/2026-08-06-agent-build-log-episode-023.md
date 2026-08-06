---
layout: single
title: "Agent Build Log — Episode 023"
date: 2026-08-06 23:36:25 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-023.png
summary: "在 Agent GUI 中加入「專有技」，並以 spec-diff 將不同版本文件的變化整理成人類可讀的報告。"
description: "在 Agent GUI 中加入「專有技」，並以 spec-diff 將不同版本文件的變化整理成人類可讀的報告。"
---

今天，我在 Agent 的 GUI 裡做了一個新的區域。

![Agent Build Log Episode 023：Agent GUI 的專有技與 spec-diff](/assets/programming/agent-build-log/agent-build-log-episode-023.png)

我把它稱為「專有技」。

這個區域會收納只有這個客製化 Agent 才有的能力。

它的概念和 skills 很接近，但我希望這些能力不只是藏在 Agent 背後執行。

每一個專有技都會有自己的頁面，讓非程式開發職的人，有個 GUI 界面，他可以輸入資料、設定參數，並直接查看最後產出的結果。

我做的第一個專有技叫做 spec-diff。

它的使用方式很簡單。

輸入一份 previous spec，再輸入一份 new spec。

接著，Agent 會分析兩份文件的差異，並按照固定的報告格式，整理出哪些內容被修改、增加或刪除。

它不是只把兩份文件做文字上的逐行比較。

Agent 還需要理解內容的意思，找出規格本身發生了哪些變化，再把結果整理成人類容易閱讀的報告。

一開始，我只是想解決開發過程中的 spec 變更問題。

當規格更新時，開發者、PM 和 QA 可以更快知道這次到底改了什麼，以及哪些地方可能需要重新確認。

但把第一版做出來之後，我突然發現，這個功能的用途可能不只是在比較 spec。

只要輸入的是兩份不同版本的資料，它就可以分析其中的變化。

它可以比較契約，整理哪些條款被修改、增加或刪除。

它也可以比較兩份架構設計，找出元件、責任或資料流的變化。

甚至可以比較股票交易規則，整理新舊版本在進場、出場或風險控制上的差異。

這個方向讓我很驚喜。

因為我原本以為自己只是在做一個 spec-diff。

但在開發的過程中，我意外做出了一個可以比較不同版本文件，並把變化整理成人類可讀報告的工具。

有時候，真正有潛力的功能，不一定是最初規劃的那一個。

它也可能是完成第一版之後，才慢慢浮現出來的副產品。
