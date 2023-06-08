---
layout: single
title: WWDC23 - Swift 加入了 Macros 特性 - State of the union
date: 2023-06-08 18:21 +0800
category: swift
author: Marvin Lin
tags: [Swift, WWDC]
summary: In WWDC23, Swift got a new feature - Macros. This article talks about how to use Macros in Swift.
permalink: /swift/:title:output_ext
---

在前面的文章，寫過了 [使用 swift async/await 串接 closure 的方法](https://moonandeye.github.io/swift/async-await-connect-closure.html)，但在 WWDC23 的 State of the union 影片上，我看到了 macros 可以只使用一個 anootation 達到，還可以泛用到以前每個寫的 escaping closure，這一篇的作法，會需要在每個 escaping closure 包上 async func 才能運用，這之間的程式碼數量差距真的是太多了，讓我對 Swift 5.9 有了更多的期待。

### 這是原來你寫的 fetch content，使用 completion handler

![completion handler](/assets/swift/wwdc23/origin.png)

### 這是使用了 @AddAsync Macros 後 (@AddAsync 應該不是 Swift 原生的 annotation，應該要自己寫)

![using macros](/assets/swift/wwdc23/using_macros.png)

## Macros 還用在哪？大量的用在 SwiftUI 上

從 [What's new in Swift 的影片中](https://developer.apple.com/videos/play/wwdc2023/10164/)，我們可以看到 SwiftUI 中的 `ObservableObject` 未來可以用 Macros 大量的簡化，讓你少寫很多 `@Published` 在 property 前面。

### 以前寫 `ObservableObject` 都要在要曝露出的 property 前面加上 `@Published`

![origin observable](/assets/swift/wwdc23/origin_observable.png)

### 現在只要使用 @Observable Macros 就可以了

![Macros observable](/assets/swift/wwdc23/macros_observable.png)

### 在 WWDC23 中對 Observable 的解釋

![behind observable](/assets/swift/wwdc23/behind_observable.png)

相信 SwiftUI 會愈來愈好寫

## 相關連結

[使用 swift async/await 串接 closure 的方法](https://moonandeye.github.io/swift/async-await-connect-closure.html)

[WWDC23 - Platforms State of the Union](https://developer.apple.com/videos/play/wwdc2023/102/)

[WWDC23 - What's new in Swift](https://developer.apple.com/videos/play/wwdc2023/10164/)

[Hacking with Swift 對 Macros 的介紹](https://www.hackingwithswift.com/articles/258/whats-new-in-swift-5-9)