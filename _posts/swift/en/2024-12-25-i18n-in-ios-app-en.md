---
layout: single
title: If You Want to Implement i18n on iOS and Dynamically Switch Languages in the App, This is a Great Library
date: 2024-12-24 23:05 +0800
category: swift
author: Marvin Lin
tags: [i18n, Swift]
summary: 
---

If you’re working on i18n for iOS and need to dynamically switch languages within the app, you can use this package: [Localize-Swift](https://github.com/marmelroy/Localize-Swift). Recently, I worked on an i18n feature and compiled some related resources here.

## Installation

### Using CocoaPods
```
pod 'Localize-Swift'
```

### Using Swift Package Manager
```
dependencies: [
    .package(url: "https://github.com/marmelroy/Localize-Swift.git", .upToNextMajor(from: "3.2.0"))
]
```

## Usage

```swift
/// Import the library wherever you need multilingual support
import Localize_Swift
```

Add `.localized()` to any string object you want to translate:

```swift
textLabel.text = "Hello World".localized()
```

Get an array of available languages:

```swift
Localize.availableLanguages()
```

Change the current language:

```swift
Localize.setCurrentLanguage("fr")
```

If you need to update the UI in a view controller to handle language changes, observe `LCLLanguageChangeNotification`:

```swift
NotificationCenter.default.addObserver(self, selector: #selector(setText), name: NSNotification.Name(LCLLanguageChangeNotification), object: nil)
```

Reset the language back to the app’s default:

```swift
Localize.resetCurrentLanguageToDefault()
```

## Beyond Localizable.strings: Now You Can Use xcstrings

While working on development, I noticed that when adding a new strings file, there was a “deprecated” label, along with a new `xcstrings` option. After doing some research, I discovered this was introduced at WWDC 2023. The format looks quite similar to Android’s multilingual GUI interface. Below is the related video. Once I get to use this in a real project, I’ll write another blog post about it.

## WWDC 2023 - Discover String Catalogs | Apple

<iframe width="560" height="315" src="https://www.youtube.com/embed/7xxUopPqjyI?si=_ZDwqEMXWkIJD5_X" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## References

- [Localize-Swift](https://github.com/marmelroy/Localize-Swift)
- [Discover String Catalogs](https://developer.apple.com/videos/play/wwdc2023/10155/)