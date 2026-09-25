---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜Mobile 開發建議埋 debug console log，AI 很好 debug - Tip 13"
date: 2026-09-25 18:00:19 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - Mobile
  - Debug Log
  - AI Debugging
summary: "在 mobile 的重要流程埋好 debug console log，讓 AI 除錯有線索，同時避免雜訊與敏感資料外洩。"
description: "在 mobile 的重要流程埋好 debug console log，讓 AI 除錯有線索，同時避免雜訊與敏感資料外洩。"
---

本文同步刊登於 [iT 邦幫忙](https://ithelp.ithome.com.tw/articles/10417000)。

這篇是 Vibe Coding 系列 Tip 13：在 mobile 的重要路徑埋 debug console log，讓 AI 除錯時有執行線索。

做 mobile，我建議埋 debug console log。這樣 AI 很好 debug。

## 為什麼

他看不到手機的畫面，看得到 log。畫面上發生的事，log 裡有一行，他就能對出來是哪一步出了問題；沒有那一行，他只能猜。

## 我怎麼做

埋在會出事的地方：

- 畫面切換：從哪一頁到哪一頁
- API：送出什麼、回來什麼、花了多久
- 登入狀態變化：登入、登出、token 過期
- Remote Config 抓到的值（接 Tip 12）

格式固定，每一行帶一個 tag，好 grep：

```
[Auth] signIn ok uid=abc123
[API] GET /cart 200 132ms
[RemoteConfig] app_status=normal min_supported_version=1.2.0
[Nav] Cart -> Checkout
```

只在 debug build 開，release 不印：uid、token 這種東西別留在使用者裝置的 console 裡。出問題的時候，把 console 的 log 整段抓下來貼給他，或者讓他自己跑起來抓（Tip 10 的 XcodeBuildMCP 就能抓 log），指出哪一段不對，他從那幾行開始查。

## 小結

debug console log 埋好，他 debug 的時候有東西可以看。

明天講怎麼下指令：先讓他把設計攤出來、不動手。
