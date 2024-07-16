---
layout: single
title: Adding AppDelegate in a SwiftUI Project
date: 2023-04-18 22:50 +0800
category: swift
author: Marvin Lin
tags: [Swift, SwiftUI]
lang: en
summary: Using SwiftUI to initiate a project, but still needing AppDelegate lifecycle. This article helps you correctly initialize AppDelegate.
---

After SwiftUI was introduced, the way to start a project changed to include a SwiftUI setup. If you choose to start a project using SwiftUI, the original AppDelegate and SceneDelegate files will not appear. Instead, the entry point will be a SwiftUI file named after the project, containing a Scene that wraps a WindowGroup.

Even though AppDelegate is gone, some tasks that were originally done in AppDelegate still need to be performed. For example, a project still needs Crashlytics to log crashes and Analytics to record basic daily/weekly/monthly active user metrics. These initialization points still need to be placed in the lifecycle related to AppDelegate.

### Using SwiftUI to build a project, there is no AppDelegate at the start
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

### Add a new AppDelegate.swift file

First, add a new file named AppDelegate.swift and add the AppDelegate class

```swift
import UIKit

class AppDelegate: NSObject, UIApplicationDelegate {
    
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

        // Perform actions that are usually done at app startup
        // such as starting Crashlytics, Firebase, Analytics
        return true
    }
}

```
### Incorporating AppDelegate in SwiftUI

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

## If you are writing a Watch App or macOS App, the protocol your AppDelegate conforms to will be slightly different

### Watch App

```swift
import WatchKit

class AppDelegate: NSObject, WKApplicationDelegate {
    
    func applicationDidFinishLaunching() {
        // Perform actions that are usually done at app startup
        // such as starting Crashlytics, Firebase, Analytics
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
        // Perform actions that are usually done at app startup
        // such as starting Crashlytics, Firebase, Analytics
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

## Related Links

[Firebase iOS Project Tutorial](https://firebase.google.com/docs/ios/setup#swiftui)