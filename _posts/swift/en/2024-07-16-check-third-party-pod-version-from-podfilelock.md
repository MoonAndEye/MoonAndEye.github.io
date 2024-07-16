---
layout: single
title: Checking Third-Party Package Versions from Podfile.lock
date: 2024-07-15 14:29 +0800
category: swift
author: Marvin Lin
tags: [Swift, Third-Party, CocoaPods]
summary: This article explains how to check the version of third-party pods used in a project from Podfile.lock.
---

In iOS app development, third-party libraries are commonly used. This article primarily focuses on how to verify the versions of third-party packages used in a project by examining Podfile.lock. In iOS projects, the file that records all third-party libraries and their dependencies is Podfile.lock. When collaborating developers work on the project, they simply need to run the `pod install` command in the terminal directory level where Podfile.lock is located, and CocoaPods will install the third-party packages as specified in Podfile.lock according to the versions listed in the Podfile. Next, we will explain the structure of Podfile.lock.

## Structure of Podfile.lock

The versions of the third-party libraries used and each library's dependencies are listed in the first section under the heading "PODS:".

![Podfile lock sample](/assets/swift/podfile-lock/podfile-lock-sample.png)

In Podfile.lock, a hyphen preceded by two spaces indicates the third-party library installed and its corresponding version number. In the sample image, you can see the areas marked in red; the following two lines both start with four spaces followed by a hyphen. This indicates that the installed third-party library depends on another third-party library. In this example, `Firebase/CoreOnly` and `FirebaseAnalytics (= 7.6.0)`. The dependent `FirebaseAnalytics` is pinned to a specific version `7.6.0`. Because of the dependency on `FirebaseAnalytics`, you will also see `Firebase/CoreOnly` and the version number of `FirebaseAnalytics` in the Podfile.lock.

## Reminder: Do Not Add Podfile.lock to .gitignore

This file precisely records the third-party libraries and their versions used in the project. When taking over a project, simply running `pod install` will install the corresponding code on the project. Therefore, please do not add Podfile.lock to .gitignore, as it can lead to complications for everyone involved.

## Related Links

[Documentation from Cocoapods.org](https://cocoapods.org/)