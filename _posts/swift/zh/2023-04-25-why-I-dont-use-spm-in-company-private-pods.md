---
layout: single
title: 為什麼我開發的 Swift 模組，沒有做 spm 支援 (2023年)
date: 2023-04-25 23:29 +0800
category: swift
author: Marvin Lin
tags: [Swift, cocoapods, spm]
summary: Compare iOS development third party system. One is cocoapods, another is spm. Currently, I only used cocoapods and using pod to manage my libs. This mainly because dependency relation between libs. For future, if spm let developers more convinient on iOS development, we will change on that time. 
permalink: /swift/:title:output_ext
---

Apple 新的套件管理 spm (swift package manager) 是一個用來建立、測試和分發 Swift 程式碼的工具。spm 可以讓開發者輕鬆地管理 Swift 專案的依賴關係，並且支援多平台的開發環境。spm 的優點有以下幾點：

- spm 使用 Swift 語言本身來定義套件的配置，這樣可以減少學習成本和錯誤的可能性。
- spm 採用模組化的設計，可以讓開發者自由地組合不同的套件，並且避免重複的程式碼。
- spm 與 Xcode 緊密整合，可以讓開發者在 Xcode 中直接使用 spm 建立和管理套件，並且享受 Xcode 的各種功能和優化。
- spm 支援跨平台的開發，可以讓開發者使用相同的程式碼在不同的平台上執行，例如 iOS、macOS、Linux 等。

## 那…我的模組，已經導入 spm 了嗎？

在 spm 出現了之後，我有沒有導入呢?

答案是：**沒有**

原因是，cocoapods 的依賴關係，和 spm 的依賴關係不同。而我所需要管理和開發的模組，有兩層關係以上。是會出現 `a 模組` 依賴 `x 模組`，然後還有 `bcd 模組` 都依賴 `a 模組的狀況`。整個依賴關係如下所示。

![模組間的依賴關係](/assets/swift/cocoapods/pods-dependency.jpeg)

因為我負責的模組有依賴關係，如果也要能支援 spm 的話，我就必須讓所有模組都支援 spm。然後也可能導致最下面那一層的 app 層，讓 app 專案有可能使用 spm 也有可能用 pod，導致開發環境管理的複雜度提升。所以「目前的方針」，是模組們並不支援 spm。

## 未來呢?

以上所述，只是我模組開發到 **2023年** 的現況，因為每年的 Xcode, spm, Swift, iOS 開發工具 都會變化，我並不認為我「只」會讓模組一直支援 pod，如果未來 spm 在 Xcode 的整合上，比 pod 更方便，能讓開發者省下更多時間，到時候就會增加模組支援 spm 的功能。這篇並不表示未來的我只會讓模組使用 pod，這只是目前現狀而已。

## 參考文件

[Apple SPM 文件](https://github.com/apple/swift-package-manager)

[Stackoverflow 上對於 SPM 和 pod 依賴的問題](https://stackoverflow.com/questions/70855053/swift-package-manager-spm-and-cocoapod-dependency-conflict)

[將第三方 lib 包起來，減少升級 lib 的痛苦](https://moonandeye.github.io/swift/using-adapter-pattern-to-libs.html)

[當升級第三方版本時，什麼樣的版號會讓專案 build 失敗?](https://moonandeye.github.io/swift/which-version-upgrade-will-break-your-project.html)