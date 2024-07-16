---
layout: single
title: 從 Podfile.lock 確認專案使用的第三方套件的版本
date: 2023-05-30 14:29 +0800
category: swift
author: Marvin Lin
tags: [Swift, 第三方, CocoaPods]
summary: This article talks about how to check the third-party pod version from Podfile.lock.
permalink: /swift/:title:output_ext
---

iOS App 開發中，通常會用到第三方 libs，本篇文章主要是要介紹如何從 Podfile.lock 確認專案使用的第三方套件的版本。在 iOS 專案中，紀錄所有第三方 libs 和相依關係的檔案，是 Pofile.lock，當協同的開發者進行開發時，我們只要在 terminal 的同層目錄下，下指令 `pod install` ，pod 就會依照 Podfile.lock 的內容，安裝 Podfile 上符合版本修件的第三方套件。接下來會說明 Podfile.lock 的結構。

## Podfile.lock 的結構

使用的第三方 lib 版本，和每個第三方依賴的 lib 會在第一段，就是下方圖片 Pods: 的下方。

![Podfile lock sample](/assets/swift/podfile-lock/podfile-lock-sample.png)

在 Podfile.lock 裡面，空兩格接一個短線，表示專案安裝的第三方 lib 與對應的版本號。在範例圖片中，你可以看到紅色框起來的地方，下兩行都是空四個空格再接一個短線。這表示你安裝的這個第三方有另外依賴第三方。以這個例子為，`Firebase/CoreOnly` 與  `FirebaseAnalytics (= 7.6.0)`。而其中依賴的 `FirebaseAnalytics` 的第三方是固定版本 `7.6.0`。因為有 `FirebaseAnalytics` 的依賴，所以你會在 Podfile.lock 裡面也看到 `Firebase/CoreOnly`，`FirebaseAnalytics` 的版本號。

## 提醒：不要將 Podfile.lock 加入 gitignore

這個檔案明確的紀錄這個專案所使用的第三方與版本號，在接手專案時，只要下 `pod install`，就可以在專案上安裝對應的程式碼，所以請不要將 Podfile.lock 加入 gitignore，這會造成大家的困擾。

## 相關連結

[Cocoapods.org 的文件](https://cocoapods.org/)