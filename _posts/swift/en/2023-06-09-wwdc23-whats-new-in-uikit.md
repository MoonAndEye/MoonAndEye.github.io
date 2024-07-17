---
layout: single
title: "WWDC23 - What's New in UIKit - Key Highlights"
date: 2023-06-09 13:48 +0800
category: swift
author: Marvin Lin
tags: [Swift, WWDC]
lang: en
summary: At WWDC 23, significant improvements were announced for UIKit, including a preview feature for UIViewController, a new lifecycle callback `viewIsAppearing(_:)`, and enhanced UICollectionView performance in iOS 17 with self-sizing features in NSCollectionLayout.
---

## Highlight 1: UIViewController Now Supports Preview

At WWDC23, it was announced that UIViewController in UIKit can now utilize the Preview feature, similar to what has been available in SwiftUI. This functionality allows for the preview of UIViewControllers directly in the storyboard. Using the new Macro preview method in SwiftUI, simply add `#Preview` in the code snippet below to see the UI component preview on the right side.

### Preview in UIViewController

![Preview in UIVC](/assets/swift/wwdc23/uikit_preview_uiviewcontroller.png)

### Preview in UIView

![Preview in UIVC](/assets/swift/wwdc23/uikit_preview_uiview.png)

## Highlight 2: New Lifecycle Callback `viewIsAppearing(_:)` in UIViewController, Back-Deployed to iOS 13.0

A new lifecycle callback, `viewIsAppearing(_:)`, has been added between `viewWillAppear(_:)` and `viewDidAppear(_:)`. This callback addresses issues related to accurate view sizing during transitions. As outlined in WWDC23 - What's New in UIKit, this callback is detailed along with the sequence of lifecycle callbacks. Previously, `viewWillLayoutSubviews()` and `viewDidLayoutSubviews()` were used for animation changes, but going forward, `viewIsAppearing(_:)` will only be called once, unlike the multiple calls in layoutSubviews callbacks.

![view is appearing](/assets/swift/wwdc23/view_is_appearing.png)

## Highlight 3: Performance Optimization in UICollectionView

Regarding performance, with an example of 10k items, the performance of the collection view on the new iOS has nearly doubled, as shown in the benchmark below.

![collection view performance](/assets/swift/wwdc23/collection_view_performance.png)

## Highlight 4: NSCollectionLayout Now Includes `uniformAcrossSiblings(estimate:)` for Self-Sizing UICollectionViewCell

### New NSCollectionLayoutDimension - Uniform Layout

![layout in uniform layout](/assets/swift/wwdc23/uniform_layout.png)

Note the second point on the slide, "Use only with small numbers of sibling items." This indicates that it may not guarantee good adaptation in complex components.

The original text from the presentation states:

> Keep in mind, when you use this feature, it requires all sibling items to be created and sized to determine the size of the largest item; so avoid using it when you have large numbers of items in a group.

### Uniform Across Siblings Demo

![layout in uniform demo](/assets/swift/wwdc23/uniform_layout_demo.png)

## Reflections

- The ability for UIKit to support preview is impressive, as often we need to build the entire project to start fine-tuning the UI. With the introduction of preview (if it does not affect performance), this should significantly reduce the time required.
- Previously, we used `UIViewControllerRepresentable` in SwiftUI to wrap a VC to view UIKit's UI. If there were many UI components, this SwiftUI target also needed to import related components, ultimately becoming quite bulky. However, now simply using `#Preview` suffices. My guess is that UIKit’s `#Preview` might also use SwiftUI's preview functionality by wrapping the UIKit VC with `UIViewControllerRepresentable`.
- The use of `Is` in the new lifecycle callback `viewIsAppearing(_:)` is uncommon; typically, `will` indicates an action before it begins, and `did` after it ends. This callback name reminds me of SwiftUI's `onAppear`. Are there other tricks up the sleeve for `viewIsAppearing`? Let's wait and see.

## Related Links

[WWDC23 - State of the Union](https://moonandeye.github.io/swift/wwdc23-state-union.html)

[What's New in UIKit](https://developer.apple.com/videos/play/wwdc2023/10055/)