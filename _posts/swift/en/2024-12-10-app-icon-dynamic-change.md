---
layout: single
title: If You Need to Dynamically Change the App Icon, This Article Covers Everything You Need to Know
date: 2024-12-10 14:45 +0800
category: swift
author: Marvin Lin
tags: [Xcode, Swift]
summary: Change App icon feature
---

A couple of years ago, someone asked me whether it was possible to change an app icon dynamically based on certain conditions. A few days ago, I got asked the same question again. Unfortunately, I had forgotten the details I found previously. To avoid having to search for this information yet again, I’ve decided to document everything you need to know about implementing the dynamic app icon feature.

## Implementation
The implementation is simple and involves just one API:

```swift
/// The iconName must correspond to the app icon name in your project. The icon must already exist in the project. 
/// If the file name doesn't exist, the app won't crash, but the app icon will remain unchanged.
UIApplication.shared.setAlternateIconName(iconName) { (error) in
    if let error = error {
        print("Failed request to update the app’s icon: \(error)")
    }
}
```

[Apple Official Documentation on App Icon](https://developer.apple.com/documentation/xcode/configuring_your_app_to_use_alternate_app_icons)

[Apple App Icon Demo Project](https://docs-assets.developer.apple.com/published/ba6fbde5c8/ConfiguringYourAppToUseAlternateAppIcons.zip)

## Practical Considerations for Real Apps

Pre-packaged Icons: The app icons must be included in the app project beforehand. You cannot dynamically download an icon from the internet to replace it. Also, the icon format must be a 1024x1024 image; otherwise, it won’t work.
Triggering Logic: The icon change can be triggered either by user action or programmatically based on certain conditions. In Apple's demo project, the app icon is changed after the user taps on the app icon trigger.
Foreground Requirement: The app must be in the foreground to change the app icon. If you attempt to change the icon while the app is in the background, you’ll encounter a 3072 error.
System Alert After Change: After changing the app icon, the system will display an alert. This alert is system-level, similar to privacy prompts, and cannot be bypassed. The user will need to tap “OK” before any further UI interaction in the app can proceed.