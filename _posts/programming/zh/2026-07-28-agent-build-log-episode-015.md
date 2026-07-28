---
layout: single
title: "Agent Build Log — Episode 015"
date: 2026-07-28 23:36:14 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-015.png
summary: "排查正式打包 Desktop App 的 OAuth 問題：從 bundle、重複 pi-ai module、舊 process 到 credential lifecycle。"
description: "排查正式打包 Desktop App 的 OAuth 問題：從 bundle、重複 pi-ai module、舊 process 到 credential lifecycle。"
---

今天，我把 OAuth 打開之後，Desktop App 直接壞掉了。

![Agent Build Log Episode 015：排查 Desktop App 的 OAuth 問題](/assets/programming/agent-build-log/agent-build-log-episode-015.png)

畫面上只顯示：

> Desktop agent did not produce an answer

一開始，我以為是登入失敗，也可能是 token、模型，或帳號出了問題。

但真正的錯誤其實發生得更早。

Pi 在準備模型 request 的 OAuth auth 時就失敗了，而且 token usage 是 0。也就是說，prompt 根本還沒有送到模型。

第一個問題出在正式打包後的 Desktop App。

開發環境裡可以載入的 OAuth flow，在 Electron production bundle 裡找不到對應的檔案。OAuth 還沒取得 request auth，整個流程就已經中斷。

我加上 OAuth loader，source-level test 也通過了。

但正式包還是壞的。

後來才發現，workspace 裡其實存在兩份 pi-ai module。

我把 loader 註冊到其中一份，但真正執行模型的 Pi ModelRuntime 使用的是另一份。

它們的 loader registry 並不共用。

所以看起來像是「我已經修好了」，實際上真正執行的 runtime 根本沒有拿到那個修正。

我又把 module identity 和 bundle 問題修掉，重新打包，再測一次。

結果畫面上還是同一個錯誤。

這次真正的原因更荒謬：Mac 上跑的還是修正前就已經啟動的舊 Desktop process。

磁碟上的 App 已經更新了，但記憶體裡的舊 process 不會自己變成新版本。

所以我看到的不是「新修正仍然失敗」，而是「舊程式仍然在執行」。

在處理這些問題的過程中，我又發現另一個風險。

CLI 和 Desktop 共用同一份 OAuth credential，但 Desktop worker 啟動後會把 auth 保存在記憶體裡。

如果 CLI 重新登入或 refresh token，已經開著的 Desktop 不一定會立刻讀到新的 credential。

所以我也補上了 credential lifecycle。

在真正送出 prompt 前，Desktop 會重新確認 auth。當 auth 檔案改變、Mac 從睡眠恢復，或 worker 已經過期時，它會在下一次操作前重建 worker，重新讀取 credential 和 DKS connection。

我也把 UI 的錯誤訊息改掉。

之後不會再把所有問題都吃成同一句 Desktop agent did not produce an answer，而是優先顯示 Pi 回傳的實際 OAuth error。

最後，正式打包的 Desktop App 成功收到了一次 pong。
