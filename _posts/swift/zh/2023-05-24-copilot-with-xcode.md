---
layout: single
title: Xcode 上使用 GitHub Copilot 的體驗 (結論：不是很理想，現在在使用 Xcode 時候都是關掉 copilot 的)
date: 2023-05-24 11:03 +0800
category: swift
author: Marvin Lin
tags: [Swift, Xcode, copilot]
summary: This is a post about my experience using GitHub Copilot on Xcode. Conclusion - not very good, I turn it off when I use Xcode.
permalink: /swift/:title:output_ext
---

在 [前一篇文章中](https://moonandeye.github.io/programming/start-using-copilot.html) 提到，我已經購買了 github copilot 服務，並嘗試在 side project 中使用。我主要工作是 iOS app 開發，而且使用 Native 開發，也嘗試了在 Xcode 中使用 copilot。在 [相關文章](#relative-article) 中，有放 Xcode 整合 copilot 的教學，如果想要在 Xcode 中使用，可以參考。

## 但，我現在不在 Xcode 中使用 copilot 了

copilot 在 Xcode 的開發體驗上，並沒有 VScode 那麼流暢。在我打字的過程中，Xcode 的 copilot 插件在運作過程中，會干擾 Xcode 本身的自動完成反應時間，在我的「體感」上，我會「感覺到」我在等 Xcode 的自動完成跳出來，我才能選那些自動完成的建議。

另一方面，現在 Xcode copilot 建議的程式碼，可能因為和我的機器/帳號磨合還不夠，建議的程式碼常常有上下文對不起來的問題。在一個 VC 或 class 或 struct 中，我們一定會有 property 宣告在 func 外面，但 copilot 的程式碼一遇到要和這些變數交互作用的場景，給的建議程式碼就沒什麼作用(但這種全域變數，即使是人類開發者，也不一定好理解，所以才有 design patterns 各種流派的出現)。

在我把他關掉後，我開發的心情有比較好，不過速度上的差異沒辦法很客觀的比較，就我的理解，Copilot 會愈用愈好，但目前在 Xcode 上的體驗，還不夠好。

## 在 Xcode 中，你可以使用 Code Snippet 來做到類似的程式建議功能

Snippet 是大多數 IDE 具備的功能，你可以把常用的程式碼先建個模版，並在中間挖出要填空的區域和字，在呼叫 snippet 時，只需要填入剩下的地方就好了，下面是一個我常用的讓其他 Queue 回到 main Quque 的 snippet。在 iOS 13 以後，如果在非 main queue 中使用 UI 的元件，會閃退。

```swift
        // 這是一個我常用的 snippet
        DispatchQueue.main.async {
            
        }
```

## <a name="relative-article">相關文章

[開始使用 Github Copilot 服務，來讓 side project 加速](https://moonandeye.github.io/programming/start-using-copilot.html)

[Xcode copilot - 作者 Intini](https://github.com/intitni/CopilotForXcode)

[在 Xcode 使用 Copilot 幫忙寫程式 - 作者 彼得潘](https://medium.com/%E5%BD%BC%E5%BE%97%E6%BD%98%E7%9A%84-swift-ios-app-%E9%96%8B%E7%99%BC%E5%95%8F%E9%A1%8C%E8%A7%A3%E7%AD%94%E9%9B%86/%E5%9C%A8-xcode-%E4%BD%BF%E7%94%A8-copilot-%E5%B9%AB%E5%BF%99%E5%AF%AB%E7%A8%8B%E5%BC%8F-7e8761a206f4)