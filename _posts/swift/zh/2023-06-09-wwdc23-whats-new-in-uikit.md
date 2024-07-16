---
layout: single
title: WWDC23 - What's new in UIKit - 重點整理
date: 2023-06-09 13:48 +0800
category: swift
author: Marvin Lin
tags: [Swift, WWDC]
summary: In WWDC 23, what's new in UIKit has some big improvement. UIViewController has preview feature. UIViewController has a new life cycle call back viewIsAppearing(_:). UICollectionView performance is improved in iOS 17, NSCollectionLayout has self sizing features.
permalink: /swift/:title:output_ext
---

## 重點1： UIViewController 可以用 Preview 了

在 WWDC23 中，我們可以看到 UIKit 中的 UIViewController 可以用 Preview 了，這個功能在 SwiftUI 中已經有了，但在 UIKit 中，我們可以看到在 storyboard 中的 UIViewController 可以用 Preview 了。使用上也和 SwiftUI 新的 Macro preview 方式一樣，在下面那一段加上 `#Preview`，就可以在右邊看到 UI 元件 Preview 的畫面了。

### Preview in UIViewController

![Preview in UIVC](/assets/swift/wwdc23/uikit_preview_uiviewcontroller.png)

### Preview in UIView

![Preview in UIVC](/assets/swift/wwdc23/uikit_preview_uiview.png)

## 重點2： UIViewController 加了一個 call back `viewIsAppearing(_:)`，且這個生命週期有 back-deploys 到 iOS 13.0

在 `viewWillAppear(_:)` 和 `viewDidAppear(_:)` 之間，多了一個 `viewIsAppearing(_:)` 的生命週期 call back。這個 call back 是為了解決 view 在過場時，尺寸正確性的問題。在 WWDC23 - What's new in UIKit 中，也附上了生命週期 call back 順序。在以前會使用 `viewWillLayoutSubviews()` `viewDidLayoutSubviews()` 進行 animation 的變化，但在未來，如果使用 `viewIsAppearing` 照 WWDC 的介紹，他只會被呼叫一次，而不是像 layoutSubviews 的 call back 會被呼叫多次。

![view is appearing](/assets/swift/wwdc23/view_is_appearing.png)

## 重點3：UICollectionView 效能優化

在效能比較上，以 10k item 為例，在新的 iOS 上，collection view 的效能快了將近1倍，bench mark 在下圖

![collection view performance](/assets/swift/wwdc23/collection_view_performance.png)

## 重點4: NSCollectionLayout 多了 uniformAcrossSiblings(estimate:) ，讓 UICollectionViewCell 可以自適應

### 新的 NSCollectionLayouDimension - Uniform layout

![layout in uniform layout](/assets/swift/wwdc23/uniform_layout.png)

請注意這個投影片的第二點，Use only with small numbers of sibling items。可以看出這並沒辦法保證在很複雜元件下，他也能良好的自適應。

簡報的原文如下

>  Keep in mind, when you use this feature, it requires all sibling items to be created and sized to determine the size of the largest item; so avoid using it when you have large numbers of items in a group.

### Uniform Across Siblings Demo

![layout in uniform demo](/assets/swift/wwdc23/uniform_layout_demo.png)

## 感想

- UIKit 可以做到 preview 讓我覺得驚豔，因為很多時候我們還是需要將整個專案建置起來，再開始進行 UI 的細節調整。有了 preview (如果 preview 不會影響效能)，這個時間應該會大輻縮減。
- 以前會在 SwiftUI 中使用 `UIViewControllerRepresentable` 包一個 VC 來看 UIKit 的 UI，但如果已經有很多 UI 元件，這個 SwiftUI 的 target 也需要 import 相關元件，最後也會很肥大。不過，現在只要 `#Preview` 即可。要猜的話，UIKit 的 `#Preview` 可能也是用 SwiftUI 的 preview 用 `UIViewControllerRepresentable` 來包 UIKit 的 VC 吧。
- `viewIsAppearing(_:)` 這個生命週期的 call back 的 `Is` 是以前不常見的，常常都是 `will` 表示這個動作開始之前，用 `did` 表示這個動作結束之後。這個 call back name 讓我想到 SwiftUI 中的 `onAppear` 。是不是後面還有其他招式會在 `viewIsAppearing` 呢？讓我拭目以待。

## 相關連結

[WWDC23 - State of the union](https://moonandeye.github.io/swift/wwdc23-state-union.html)

[What's new in UIKit](https://developer.apple.com/videos/play/wwdc2023/10055/)