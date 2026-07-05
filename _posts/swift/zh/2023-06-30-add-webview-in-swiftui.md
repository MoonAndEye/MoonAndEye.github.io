---
layout: single
title: SwiftUI 專案加入 WebView
date: 2023-06-30 13:41 +0800
category: swift
author: Marvin Lin
tags: [Swift, SwiftUI, WebView]
summary: This article talks about how to add a WebView in SwiftUI project.
description: This article talks about how to add a WebView in SwiftUI project.
permalink: /swift/:title:output_ext
---

## 此文章曾發於 2022 年 IT 鐵人賽 - 使用 SwiftUI 讓有趣的點子變成 Apps

現代的 app，基本都會有和網路進行溝通的 feature。這一篇文章會讓 app 加上一頁 WebView，去連到葛麗絲．霍普的 wiki 頁面。這樣可以保證大家在讀取資料的時候，資訊是和 wiki 上的一樣，而不用在每次資訊有更新的時候，需要進行 client 端的更新。

> 葛麗絲．霍普的 wiki [https://en.wikipedia.org/wiki/Grace_Hopper](https://en.wikipedia.org/wiki/Grace_Hopper)
> 

### SwiftUI 使用 WebView 的方法

目前 SwiftUI 沒有 WebView 元件，所以需要使用 WebKit 的 WKWebView。橋接 SwiftUI 和 UIKit 的方法很簡單，讓元件 conform UIViewRepresentable 後，實作 makeUIView(:), updateUIView(:,:)。就能使用 UIKit 的元件了。

在這個 WKWebViewContainer 裡面，我們會放一個 url: URL，讓裡面的 WKWebView，去讀這個 URLRequest。

```swift
import WebKit

struct WKWebViewContainer: UIViewRepresentable {
    
    var url: URL
    
    func makeUIView(context: Context) -> WKWebView {
        return WKWebView()
    }
    
    func updateUIView(_ webView: WKWebView, context: Context) {
        let request = URLRequest(url: url)
        webView.load(request)
    }
}
```

再把 WKWebViewContainer 包起來，這樣可以在上下左右加上其他 SwiftUI 元件。

```swift
struct MyWebView: View {
  
  let urlString: String
  
  var body: some View {
    
    if let url = URL(string: urlString) {
      WKWebViewContainer(url: url)
    } else {
      Text("not a url")
    }
  }
}
```

嗯…🤔🤔🤔🤔🤔 如果解不開，目前的程式碼是會呈現一個  Text，這樣有點怪怪，這邊加上一個 Error View 好了。

在 Image 上，可以直接使用 SF Symbole 的 wifi.exclamationmark，不用特別去找素材。

SF Symbols 的網站，這邊可以下載 SF Symbols 的 app。

[https://developer.apple.com/sf-symbols/](https://developer.apple.com/sf-symbols/)

```swift
// 如果 URLString 給錯，就會跳 Error view
struct URLNotCorrectView: View {
  
  var body: some View {
    
    VStack {
      Image(systemName: "wifi.exclamationmark")
        .font(.system(size: 150))
        .padding()
      Text("Oops! Internet got error")
        .bold()
        .multilineTextAlignment(.center)
        .font(.system(size: 44))
    }
  }
}
```

![no internet view](/assets/swift/webview-in-swiftui/no_internet.png){: width="50%" }

最後， MyWebView 看起來就像這樣

```swift
struct MyWebView: View {
  
  let urlString: String
  
  var body: some View {
    
    if let url = URL(string: urlString) {
      WKWebViewContainer(url: url)
    } else {
      URLNotCorrectView()
    }
  }
}
```

不過， preview 是沒辦法看到網頁的，所以我們在進入點，把 View 換成 MyWebView，看一下結果。

```swift
import SwiftUI

@main
struct DemoApp: App {
    var body: some Scene {
        WindowGroup {
          MyWebView(urlString: "https://en.wikipedia.org/wiki/Grace_Hopper")
        }
    }
}
```

你也可以故意塞一個不是網址的 string，當無法轉換成 URL，就會出現前面寫好的網路故障 View。

### 展示 Grace Hopper 的 wiki

![Wiki of Grace Hopper](/assets/swift/webview-in-swiftui/grace_hopper_wiki.png){: width="50%" }
