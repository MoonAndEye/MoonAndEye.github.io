---
layout: single
title: For projects using Xcode 15.3 or higher, please upgrade Firebase to version 10.22.0 or higher, otherwise, the application may crash upon release
date: 2024-07-27 11:32
category: swift
author: Marvin
lang: en
tags: [swift, firebase, xcode]
summary: If you’re using Xcode version 15.3 or higher for your projects that incorporate Firebase, it is crucial to upgrade Firebase to version 10.22.0 or higher to avoid crashes upon release. After our team upgraded to Xcode 15.4, we experienced an increase in crash rates, primarily originating from the AppDelegate and compiler-generated code. Investigations into the crashes, supported by insights from Stack Overflow and Firebase GitHub issues, pinpointed the issue to nanopb. Always ensure that Firebase is updated to at least version 10.22.0 when working with newer versions of Xcode to prevent these issues.
---

If you are using Xcode version 15.3 or higher and your project utilizes Firebase, please ensure to upgrade Firebase to version 10.22.0 or higher; otherwise, your application may crash upon release.

![Crashlytics report on xcode15.4 vs. firebase 10.10.0](/assets/swift/crash-on-firebase10-10-0/crashlytics.png)

In early July, our team agreed to upgrade to Xcode 15.4. While other pods were kept stable, we noticed an increase in crash rates post-launch, as depicted in the image above.

Crashlytics analysis revealed that the crashes originated from the AppDelegate and were associated with compiler-generated code.

![Crash starts from AppDelegate](/assets/swift/crash-on-firebase10-10-0/crash_on_AppDelegate.png)

Further insights were gained from a Stack Overflow post, which recommended upgrading to Firebase version 10.22.0 or higher.

[Stack Overflow discussion on potential crash issues and the recommendation to upgrade Firebase to 10.22.0 or higher](https://stackoverflow.com/a/78122992/3764854)

[Firebase GitHub issues - 11403 discusses a series of related problems](https://github.com/firebase/firebase-ios-sdk/issues/11403)

The reasons are similar to those in my project, relating to nanopb.

## If Upgrading to Xcode 15.3 or Higher

**Make sure that the Firebase version is at least 10.22.0**

### Crash log

```
Crashed: com.apple.main-thread
EXC_BAD_ACCESS KERN_INVALID_ADDRESS 0x000000017338126c
0
nanopb
encode_field + 100
24
UIKitCore
keypath_get_selector_hoverStyle + 11024
25
ForumApp
<compiler-generated> - Line 4337149088
static AppDelegate.$main() + 4337149088
26
ForumApp
<compiler-generated> - Line 4337152352
type metadata accessor for AppDelegate + 4337152352
```