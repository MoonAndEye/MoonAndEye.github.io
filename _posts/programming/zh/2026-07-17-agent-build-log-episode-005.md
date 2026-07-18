---
layout: single
title: "Agent Build Log — Episode 005"
date: 2026-07-17 22:43:14 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-005.png
summary: "在 CLI、Browser 與 Desktop App 加入 Feedback 功能，透過共用 API 集中記錄測試時發現的問題與改進想法。"
description: "在 CLI、Browser 與 Desktop App 加入 Feedback 功能，透過共用 API 集中記錄測試時發現的問題與改進想法。"
---

今天做了一個看起來不大，但我覺得之後會很有用的功能：Feedback。

![Agent Build Log Episode 005：在三個介面加入 Feedback 功能](/assets/programming/agent-build-log/agent-build-log-episode-005.png)

我把它加進了 CLI、Browser 和 Desktop App。無論是給其他使用者，還是我自己在測試時，只要遇到問題、覺得哪裡怪怪的，或突然想到可以改進的地方，都可以直接在當下留下紀錄。

以前開發時常常會想著「這個晚點再修」，結果過幾天就忘了當時發生什麼，只剩下一個很模糊的印象。現在可以先把問題留下來，等到之後集中修 bug 或整理下一階段工作時，再從這些 Feedback 裡慢慢分類。

實作方式沒有弄得太複雜。我先找了一個資料庫，再開一個簡單的 API 接口，讓三個介面都可以把 Feedback 送到同一個地方。

既然我要開始 Eat my own dog food，就得把這份「狗食」哪裡難吃、哪裡需要改，也一起記下來。
