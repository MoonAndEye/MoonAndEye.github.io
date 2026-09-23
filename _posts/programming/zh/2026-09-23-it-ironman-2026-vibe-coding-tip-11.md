---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜Mobile 用 Firebase Authentication：Email、Google、Apple 與匿名登入 - Tip 11"
date: 2026-09-23 13:01 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - Mobile
  - Firebase
  - Authentication
  - iOS
  - Android
summary: "用 Firebase Authentication 快速接上 Email／密碼、Google、Apple 與匿名登入，並把登入、登出與重開 app 的驗收條件交代清楚。"
description: "用 Firebase Authentication 快速接上 Email／密碼、Google、Apple 與匿名登入，並把登入、登出與重開 app 的驗收條件交代清楚。"
---

本文同步刊登於 [iT 邦幫忙](https://ithelp.ithome.com.tw/articles/10415931)。

做 mobile，要快速有一套登入，我會用 Firebase Authentication。Email／密碼、Google、Apple，再加匿名登入，看 app 需要哪幾種。

## 為什麼

用 Firebase 可以很快有一套 Authentication 加 Remote Config。一個 app 第一天就要這兩件事：使用者要能登入，上線之後要能從外面改設定。自己做都要一個後端；Firebase 一個專案裡兩個都有，SDK 裝一次，設定在同一個 console 裡。這一篇先講登入，Remote Config 明天講。

## 我怎麼做

先把 app 接上 Firebase：

1. 在 Firebase console 建專案，把 iOS 和 Android 的 app 加進去，各自下載設定檔（iOS 是 `GoogleService-Info.plist`，Android 是 `google-services.json`）放進專案
2. 開 Authentication，勾要用的登入方式：Email／密碼、Google、Apple，再加匿名登入（Anonymous），看 app 要哪幾種；Google 和 Apple 各自有 provider 那一端的設定要做
3. 讓他實作登入、登出和登入狀態變化，匿名登入也列進需求，別漏掉
4. 這些步驟都可以交給他做，設定檔的路徑跟他說清楚

我會把想要的行為寫成一段 prompt，避免他只做出登入畫面：

```text
幫這個 app 接 Firebase Authentication。
登入方式依需求選 Email／密碼、Google、Apple、匿名登入。

先列出本專案需要的 Firebase 與 provider 設定，缺的資料列給我。
設定齊全後，實作並驗收：
1. 登入成功後顯示目前的登入狀態。
2. 登入失敗時顯示錯誤，讓使用者重試。
3. 登出後回到未登入狀態。
4. 重開 app 後，依實際登入狀態決定進主頁或登入頁。
5. 有啟用匿名登入時，也走完匿名登入流程。
回報實際測過的情境，以及還沒測的部分。
```

這些是我要交代給他的驗收條件。測試時每種啟用的登入方式分開走一遍，成功、失敗和登出都要看。

## 小結

登入用 Firebase Authentication。先選需要的登入方式，再把登入、登出與重開 app 的行為一起交代清楚。

明天講 Remote Config：強制更新、建議更新、維修中、正常使用，Day 1 就做進去。

參考：
- Firebase Authentication https://firebase.google.com/docs/auth
