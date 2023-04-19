---
layout: single
title: 在 SwiftUI 專案中，加上 AppDelegate
date: 2023-04-18 22:43 +0800
category: swift
author: Marvin Lin
tags: [Swift, SwiftUI]
summary: Using SwiftUI init project, but you still need AppDelegate life cycle. This article helps you init AppDelegate in correct way.
permalink: /swift/:title:output_ext
---

在 SwiftUI 發表之後，開啟一個專案的方式，多了 SwiftUI 的設定。如果你選擇使用 SwiftUI 開啟專案，原來的 AppDelegate 還有 SceneDelegate 檔案不會出現。而檔案的進入點，會是一個和專案同樣名稱的 SwiftUI 檔，裡面有個 Scene 並把 WindowGroup 包住。

雖然 AppDelegate 不見了，但有些原來在 AppDelegate 裡面要做的事情，你仍然要做。舉例來說，一個專案基本上還是需要有 Crashlytics 來紀錄程式的崩潰和 Analytics來紀錄基本的使用者日活/週活/月活。而這些紀錄程式的發動點，仍要放在 AppDelegate 相關的生命週期中。

### 使用 SwiftUI 建置專案，啟動點沒有 AppDelegate
```swift
@main
struct FooApp: App {

  var body: some Scene {
    WindowGroup {
        ContentView()
    }
  }
}
```

### 新增 AppDelegate.swift 檔案

先新增一個 AppDelegate.swift 檔案，並加上 AppDelegate 的類別

```swift
import UIKit

class AppDelegate: NSObject, UIApplicationDelegate {
    
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

        // 去做原來在 App 啟動時就會進行的動作
        // 像是 Crashlytics 啟動，Firebase 啟動，Analytics 啟動
        return true
    }
}

```
### 在 SwiftUI 中加上 AppDelegate

```swift

import SwiftUI

@main
struct FooApp: App {
    
    @UIApplicationDelegateAdaptor(AppDelegate.self) var appDelegate
    
    var body: some Scene {
        WindowGroup {
            CryptoCoinListView()
        }
    }
}

```

## 如果你是寫 Watch App or macOS App 你的 AppDelegate conform 的 protocol 會有一點不一樣

### Watch App

```swift
import WatchKit

class AppDelegate: NSObject, WKApplicationDelegate {
    
    func applicationDidFinishLaunching() {
        // 去做原來在 App 啟動時就會進行的動作
        // 像是 Crashlytics 啟動，Firebase 啟動，Analytics 啟動
    }
}
```

```swift
import SwiftUI

@main
struct FooWatchApp: App {
    
    @WKApplicationDelegateAdaptor(AppDelegate.self) var appDelegate
    
    var body: some Scene {
        WindowGroup {
            WatchContentView()
        }
    }
}
```

### macOS App

```swift
import AppKit
import SwiftUI

class AppDelegate: NSObject, NSApplicationDelegate {

    func application(_ application: NSApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
        // 去做原來在 App 啟動時就會進行的動作
        // 像是 Crashlytics 啟動，Firebase 啟動，Analytics 啟動
    }
}
```

```swift
import SwiftUI

@main
struct FooMacAppApp: App {
  
    @NSApplicationDelegateAdaptor(AppDelegate.self) var delegate
    
    var body: some Scene {
        WindowGroup {
            MacContentView()
        }
    }
}
```

## 相關連結

[Firebase iOS 專案 Tutorial](https://firebase.google.com/docs/ios/setup#swiftui)