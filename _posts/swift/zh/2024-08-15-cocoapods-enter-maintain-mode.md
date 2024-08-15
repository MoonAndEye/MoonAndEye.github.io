---
layout: single
title: Cocoapods 進入 maintain mode
date: 2024-08-15 22:10 +0800
category: swift
author: Marvin Lin
tags: [Swift, Cocoapods, Xcode]
summary: 自從 Apple 推出了 Swift Package Manager (SPM) 以後，CocoaPods 面臨了顯著的競爭壓力，這對其發展動力造成了影響。由於 SPM 是由 Apple 官方支持，直接整合在其開發環境中，這使得與 Apple 在包管理工具這一核心領域內進行競爭變得不太有利。Apple 的廣泛影響力和對其產品的深度整合，使得開發者傾向於選擇 SPM 作為依賴管理工具，這直接影響了 CocoaPods 的市場份額與相關的開發投入。因此，面對來自 Apple 的競爭，CocoaPods 在策略上需要做出調整，以適應不斷變化的開發生態。
---

## Cocoapods 進入 maintain mode，但一年還會發佈兩次以上，讓 pod 可以跟上 Xcode 的更新

有一天晚上，我滑了 x (前身為推特)，突然滑到了，有人轉推了 [Orta Therox](https://blog.cocoapods.org/CocoaPods-Support-Plans/) 的文章，有 13 年歷史的 Cocoapods 開始進入 maintain mode 了。

![cocoapods announcement: enter maintain mode](/assets/swift/cocoapods-enter-maintain-mode/pods_enter_maintain_mode.png)

## 重點整理
- 確保處理幹線的系統安全問題。
- 每年至少發布兩次版本以跟上 Xcode 更新。
- 每六個月檢查一次支持請求。
- 保持網站基礎設施運行。
- 支持限制: 不會積極跟進 GitHub 問題作為支持渠道，也不會承諾處理新增功能的 PR 或應用層錯誤。
- 考慮將 Specs 倉庫轉為只讀，以簡化安全管理，長遠保持現有構建運行。
- 對於如 React Native 等項目，這樣的變動可能足夠，因為它們的庫主要通過 npm 獲得而不是通過 Trunk。

## 原因
自從 Apple 推出了 Swift Package Manager (SPM) 以後，CocoaPods 面臨了顯著的競爭壓力，這對其發展動力造成了影響。由於 SPM 是由 Apple 官方支持，直接整合在其開發環境中，這使得與 Apple 在包管理工具這一核心領域內進行競爭變得不太有利。Apple 的廣泛影響力和對其產品的深度整合，使得開發者傾向於選擇 SPM 作為依賴管理工具，這直接影響了 CocoaPods 的市場份額與相關的開發投入。因此，面對來自 Apple 的競爭，CocoaPods 在策略上需要做出調整，以適應不斷變化的開發生態。

## 針對 pods 的這項變化
因為我手上還有很早就啟動的 iOS 專案，工作上也有一堆互相依賴的模組在使用 pod 來管理，這個狀況必然要開始進行支援 SPM 的動作。考量到接下來會有這些動作
- Xcode 16 應該會在 2024 9 月 release
- iOS 18 應該會在 2024 9 月 release
- Swift 6 雖然可選，但會在 Xcode 16 時一起出現，Swift 5.10 會是最後的版 5 開頭版本

預估開發社群對於環境的變化，應該會在 2025 年新年前後吧。所以我心中啟動 SPM 的支援，應該會在 2025 開始進行。


## [Orta Therox 聲明 Cocoapods 進入 maintain mode 的文章](https://blog.cocoapods.org/CocoaPods-Support-Plans/)

## 以下是機翻

TLDR: 我們依然在維護 CocoaPods，但我們會更明確地表達現在 CocoaPods 已進入維護模式。

CocoaPods 已有約 13 年的歷史，這段時間內 iOS 開發的格局發生了巨大變化。我還記得那些小型共享庫的碎片化島嶼（例如：ASIHTTPRequest、Three20、SBJson、SSToolkit、iCarousel），它們升級說明複雜且構建設置困難。CocoaPods 簡化了這一過程，讓它成為 iOS 和 Mac 社區分享代碼的事實標準方法。

2015 年，蘋果宣布 CocoaPods 項目已被 Sherlock，因為他們將創建自己的包管理器：Swift Package Manager。這一舉措有效地使 CocoaPods 失去了前進的動力，因為在自己的領域與蘋果競爭很少是值得志願者花時間的戰鬥。

自從 9 年前 Swift Package Manager 宣布以來，核心團隊的成員各自有持續維護的原因：一種責任感、被雇佣來維護使用 CocoaPods 的庫或應用、在大型項目的構建基礎設施工作中 CocoaPods 是關鍵部分，或只是對社區的熱愛。

然而，隨著時間的推移 - 這些聯繫也變得越來越脆弱，工作變動，人們轉移到新的生態系統，我們慢慢地將 CocoaPods 轉移到一個只有在外部因素促使時才會進行工作的地方。這可能是我在博客上過去幾年報告的安全問題，或者 Xcode 的重大更改，這需要我們調整一些設置並創建一個新版本。

如果 CocoaPods 的唯一受眾是原生 Cocoa 開發者，CocoaPods 的使用應該在下降，然而，情況並非如此。React Native 和 Flutter 的流行確保了大多數使用量/流量指標隨著時間穩步上升。

這使 CocoaPods 身處一個奇怪的位置，許多維護者不使用它，蘋果已經維護了一個替代品 9 年，而項目的新用戶幾乎不知道 CocoaPods 存在或它的作用。

所以，我們得出結論，我們需要弄清楚項目的狀況以及過去幾年我們作為維護者如何對待它。

### CocoaPods 是如何維護的
嚴格來說，我們不打算改變我們維護 CocoaPods 的方式。我們只是要開始清楚地表明 CocoaPods 是如何被維護的：

- 我們將確保處理幹線的系統安全問題
- 我們將目標是每年至少發布 2 次版本以跟上 Xcode 更新
- 我們將目標是每 6 個月查看一次幹線的支持請求
- 我們將保持網站基礎設施不完全崩潰
- 我們對讓 CocoaPods 更加未來友好的 PR 持開放態度

### 我們不會做的事：
- 我們不會積極跟蹤 GitHub 問題作為個人支持渠道
- 我們不打算在新功能方面進行積極的 CocoaPods 開發
- 我們不會保證處理添加新功能的人的 PR 或應用層面的錯誤

### 長期計劃
#### 只讀規格
我們正在討論在非常長的、多年的基礎上，我們可以通過將 Specs 倉庫轉換為只讀來大幅簡化 CocoaPods 幹線的安全性。像 Specs 倉庫和 CDN 這樣的基礎設施仍將運行，只要 GitHub 和 jsDelivr 繼續存在，這很可能是很長一段時間。這將保持所有現有構建的運行。