---
layout: single
title: Adding a WebView to a SwiftUI Project
date: 2024-07-16 18:20 +0800
category: swift
author: Marvin Lin
tags: [Swift, SwiftUI, WebView]
lang: en
summary: This article discusses how to add a WebView to a SwiftUI project.
---

## This article was previously published in the 2022 IT Ironman Competition - Using SwiftUI to Turn Interesting Ideas into Apps

In today's apps, features that communicate with the web are fundamental. This article will add a WebView page to the app that links to Grace Hopper’s Wikipedia page. This ensures that the information accessed is consistent with what's on Wikipedia, without needing to update the client side every time there’s new information.

> Grace Hopper's wiki [https://en.wikipedia.org/wiki/Grace_Hopper](https://en.wikipedia.org/wiki/Grace_Hopper)

### How to Use WebView in SwiftUI

Currently, SwiftUI does not have a WebView component, so we need to use WebKit’s WKWebView. Bridging SwiftUI with UIKit is straightforward: make the component conform to `UIViewRepresentable`, then implement `makeUIView(:)` and `updateUIView(:,:)`. This allows the use of UIKit components.

Inside this `WKWebViewContainer`, we will place a URL that the WKWebView will use to load the URLRequest.

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

Wrap the `WKWebViewContainer` so that other SwiftUI components can be added around it.

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

Hmm…🤔🤔🤔🤔🤔 If the URL can't be parsed, the current code will display a Text, which seems odd. Let's add an Error View then.

For the image, you can directly use the SF Symbol `wifi.exclamationmark`, no need to search for additional assets.

SF Symbols website, where you can download the SF Symbols app.

[https://developer.apple.com/sf-symbols/](https://developer.apple.com/sf-symbols/)

```swift
// If the URLString is incorrect, an Error view will appear
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

Finally, `MyWebView` looks like this:

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

However, you can't see the webpage in the preview, so at the entry point, we change the View to `MyWebView` to see the result.

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

You can also intentionally insert a string that is not a URL; if it cannot be converted into a URL, the previously written network error View will appear.

### Displaying Grace Hopper's Wiki

![Wiki of Grace Hopper](/assets/swift/webview-in-swiftui/grace_hopper_wiki.png){: width="50%" }