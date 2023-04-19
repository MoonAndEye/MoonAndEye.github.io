---
layout: single
title: SwiftUI 資料流
date: 2023-04-19 20:41 +0800
category: swift
author: Marvin Lin
tags: [Swift, SwiftUI]
summary: 
permalink: /swift/:title:output_ext
---

SwiftUI 以宣告式的方法進行 UI 設計。整個資料的傳遞是 Action →State → View 的方向，而這個方向是固定的，不會有逆向的可能。你也可以查 one way data flow 這個名詞，不只是 mobile 端，現在在其他端也有很多這樣的 data flow 設計。

## Action 是起點

Action 的啟動，可能來自於 User，也有可能來自於 external event。當 action 發動之後，會改變程式中的 State，接下來 SwiftUI 會自動去更新需要變化的 View。

比對以前的畫面渲染，這個職責在以前的 UIKit 是由 UIViewController 負責的

![SwiftUI Data flow](/assets/swift/state-change/one-way-data-flow.jpeg)

## View 的狀態管理 - Single source of truth

最好要記得單一資訊來源的原則，Apple 推薦的方式是，讓資料設計為 read-only 的 Swift Property，或是提供雙向的 State 綁定，SwiftUI 會觀察資料的變化，SwiftUI 會變化那些只需要變化的 View。

Apple 不建直接讓 persistent storage 成為 State properties，persistent storage 比較好的適用場景，是過場狀態的管理，比如說，highlight 狀態，filter settings。

![UI Stae 狀態管理](/assets/swift/state-change/ui-state.jpeg)

## 參考資料

[SwiftUI Model data - Apple 文件](https://developer.apple.com/documentation/swiftui/model-data)

[SwiftUI 管理 UI 狀態 - Apple 文件](https://developer.apple.com/documentation/swiftui/managing-user-interface-state)


