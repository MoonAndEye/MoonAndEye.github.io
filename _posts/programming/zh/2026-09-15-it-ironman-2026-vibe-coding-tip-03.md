---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜基本必備：lint、formatter、unit test，新專案第一天就放進去 - Tip 03"
date: 2026-09-15 13:03:00 +0800
category: programming
author: Marvin Lin
tags: [IT鐵人賽, 2026鐵人賽, Vibe Coding, Vibe Coding 技巧, Lint, Formatter, Unit Test]
summary: "我開新專案第一天就放進 lint、formatter、unit test，讓 coding agent 建好可用一行指令執行的檢查，再開始加功能。"
description: "我開新專案第一天就放進 lint、formatter、unit test，讓 coding agent 建好可用一行指令執行的檢查，再開始加功能。"
---

這是 2026 iThome 鐵人賽《Vibe Coding：30 個開發實用技巧》系列的 Tip 03。

這一篇改寫自我部落格的《Agent Build Log — Episode 025》，照這個系列的格式重寫過。原始文章：https://www.marvinswift.com/zh/programming/agent-build-log-episode-025/

我開新專案，有三個東西第一天就放進去：lint、formatter、unit test。我覺得這是 Agent Coding 時代一定要有的。

## 為什麼

程式大多是他寫的。我自己不逐行看，看 code 的是 coding agent。這三道關替我看。

lint 抓寫法上的問題：沒用到的變數、少處理的錯誤、前後不一致的寫法，這些他寫得快、我又不會一個一個去看的地方。formatter 把格式統一，同一個專案裡的程式長得一樣，diff 裡不會混進純格式的改動。unit test 把行為釘住：他改了一個地方，別的地方有沒有壞，跑一次就知道。

這三個放在專案一開始，之後每一次讓他改東西，三道關就自動在。

## 我怎麼做

我把這三個當成 scaffold 的 must-have。新專案的第一版通常很簡單：一個啟動畫面、一個有基本登入 UI 的頁面、開發時常用的基礎 libraries 和基本結構。然後就是那三個：lint、formatter、unit test，缺一個都不算建好。iOS 或 Android 都一樣。

做 mobile 的話，Native、React Native、Flutter 都可以，你喜歡就好，選你熟悉、願意維護的那一套。框架換了，這三道關還是第一天放進去。

建專案這件事我讓他做。給他的指令大意像這樣：

```
幫我建一個新的 <iOS / Android / React Native / Flutter / Next.js> 專案，當成之後開發的乾淨起點。
一開始就要有：
1. lint
2. formatter
3. unit test，先放一個會過的測試，確認測試跑得起來
三個都要能用一行指令執行，指令寫進 README。
```

建好之後，我就能直接開始讓他做事：測 UI、加功能、試新的想法，甚至讓他自己在這個專案裡開發。每次都先花時間處理專案初始化的那一段，省掉了。

這個 scaffold 的目的是幫我快速準備一個乾淨的實驗場。建立、啟動、登入頁面、lint、format、test，這些基礎先準備好，接下來我才把時間花在更複雜的事上。

## 小結

lint、formatter、unit test，新專案第一天就放進去。程式是他寫的，這三道關替我看。

專案有了形狀，也有了三道關。明天講 git：別一直在 main 上做，開分支、開 release、打 tag。

原文：https://www.marvinswift.com/zh/programming/agent-build-log-episode-025/
