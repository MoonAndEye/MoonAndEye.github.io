---
layout: single
title: Charts 的 4049 & 4132 issue，造成閃退的原因
date: 2023-04-23 15:30 +0800
category: swift
author: Marvin Lin
tags: [Swift, Charts]
summary: When using Charts 3.4.1, I got crashed when dataSet updated then charts rendering. The issue 4049 and 4132 mentioned about this. This article summarized these issues and find the solution on charts crash.
permalink: /swift/:title:output_ext
---

Charts 是 iOS 專案開發中很常使用的圖表繪制套件，不過今年，我在專案上遇到了很奇怪的狀況，在 Firebase Crashlytics 的 Dashboard 上，一直有零星的閃退，這閃退是發生在使用 Charts 套件的 renderer 裡面。而且在 release 給 QA 時，也會在 iPhone 關電源的狀況下，經過長時間後再開啟，就會閃退的狀況。但是去年，在 Crashlytics 上並沒有相同的 crash 發生，而這之間的差異，就是將 Charts 套件升級到 `3.4.1` 以及發現這個閃退的情況之後，再繼續往 `3.5.0`, `3.6.0` 升級。

但如果把有問題的版本，裝在模擬器或是我手上的實機上，卻無法用相同步驟重現，驗證了軟體界的一句話「在我的機器上是好的」。在把 scheme 調到 release 後，這個閃退能重現。然後問題大概就鎖定在下列幾個點。

- 這個閃退和 Charts 有關，而且是在 Charts 渲染過程中發生的。閃退點會在 Charts 準備更新圖的時候
- Debug mode 中這個閃退不會發生，但改成 Release mode 後，就會發生，而且能夠一直重現 (最可怕就這點，Release 才出事)
- 在我的專案中，發動點是在資料重新拉取後，要求 charts 進行更新後發生
- 真正的閃退原因，是在上一點的資料更新後，Charts 進行重繪時，在跑 init() 時會有個 iterator，但輸入的參數 min 和 max 會倒過來，然後就會出現 crash，而這一點是 release mode 才會出現，但 debug 不會出現。

## 在 github 上的 issues 中找是否有類似的問題

### 其他開發者也反應有這個問題

caloon 也反應他的專案遇到類似的問題，但 crash 也不是 100% 會發生，具 caloon 的描述，大概佔 5% 左右

![](/assets/swift/charts-crash/developer-found-stable-321.jpeg)

在查詢後，發現 issue 4049 和 4132 這兩個 issue 有關。

[Charts Issue - 4049](https://github.com/danielgindi/Charts/issues/4049)

[Charts Issue - 4132](https://github.com/danielgindi/Charts/issues/4132)

### 關於 issue 4049

issue 4049 裡面描述的情景，和我專案遇到的情景比較像。而開發者 bweavgolfanatic 有將他閃退的情形說明，發生的閃退點和我一樣。

[開發者 bweavgolfanatic 對閃退的描述](https://github.com/danielgindi/Charts/issues/4049#issuecomment-550577869)

[Charts 閃退在 iterator](/assets/swift/charts-crash/charts-crash-in-iterator.jpeg)

從上面的 debug console 可以看到，max 是 1，min 是 98，這在 run time 呼叫 min...max 時閃退。而這個現像，我也能在專案中重現。然後繼續將 issue 的討論串看完，有看到 開發者 gordondove 提出一個解法。

```swift
    self.downloadDataSet.append(newThroughtputPoint)
    self.downloadDataSet.calcMinMax()
    chartView.data?.calcMinMax()
    self.chartView.notifyDataSetChanged()
```

[gordondove 解法](/assets/swift/charts-crash/crash-solution.jpeg)

### 關於 issue 4132

4132 則是關於這個 issue 的 PR，以及將多篇 issues 的文章整合起來，主要的資訊我還是從 issue 4049 找到的。

## 解決方案的選擇

1. 將 Charts 升級，因為後續的 4132 PR 有說他修正了，但合進去後的大版號在 4.0.0 以後
2. 找出 4132 issue 相關的 PR，並把這個改動合併到另外自己 folk 的 Charts repo 上，並打一個 tag。
3. 將 Charts 退回 3.2.0 (iterator 被改動之前)
4. 使用 bweavgolfanatic 的解法，重新呼叫 dataset 的 calMinMax()

最後選擇 `方案 4`，因為當時的版號一升到大版號4，整個專案就無法 build 起來。這時就體認到 Adapter 的重要性，有興趣的朋友可以參考 [將第三方 lib 包起來，減少升級的痛苦](https://moonandeye.github.io/swift/using-adapter-pattern-to-libs.html) 一文。沒有使用 方案2/方案3 的原因，就是這個專案使用的，是 folk 後再被修改的版本，如果要選擇回溯，是有呵能帶來其他風險的，所以最終選擇方案4。

## 參考文章

[使用 Adapter 將第三方 lib 包起來](https://moonandeye.github.io/swift/using-adapter-pattern-to-libs.html)

[Charts repo - iOS](https://github.com/danielgindi/Charts)

[MPCharts repo - Android](https://github.com/PhilJay/MPAndroidChart)

[語意化版本](https://semver.org/lang/zh-TW/)
