---
layout: single
title: 要升級 Xcode 15.3 以上的專案，請將 Firebase 升到 10.22.0 以上，否則發佈後會閃退
date: 2024-07-27 11:32
category: swift
author: Marvin
tags: [swift, firebase, xcode]
summary: If you’re using Xcode version 15.3 or higher for your projects that incorporate Firebase, it is crucial to upgrade Firebase to version 10.22.0 or higher to avoid crashes upon release. After our team upgraded to Xcode 15.4, we experienced an increase in crash rates, primarily originating from the AppDelegate and compiler-generated code. Investigations into the crashes, supported by insights from Stack Overflow and Firebase GitHub issues, pinpointed the issue to nanopb. Always ensure that Firebase is updated to at least version 10.22.0 when working with newer versions of Xcode to prevent these issues.
---

如果你使用了 Xcode 15.3 以上的版本，並且專案中使用了 Firebase，請注意 Firebase 版本要升到 10.22.0 以上，否則發佈後會閃退。

![Crashlytics report on xcode15.4 vs. firebase 10.10.0](/assets/swift/crash-on-firebase10-10-0/crashlytics.png)

7月初，團隊講好一起把 Xcode 升到 15.4 以上，其他的 pods 都是固定的，然後一線，閃退率就起來了，上面的圖就是上線後的結果。

看了 Crashlytics，發生閃退的地方是 AppDelegate 而且是 Compiler generated code。

![Crash starts from AppDelegate](/assets/swift/crash-on-firebase10-10-0/crash_on_AppDelegate.png)

看了一下 stack overflow 的資訊，有提到的是這篇。

[Stack overflow 查到可能閃退的點，並且建議升級到 Firebase 10.22.0 以上](https://stackoverflow.com/a/78122992/3764854)

[Firebase github issues - 11403 有提到一系列原因](https://github.com/firebase/firebase-ios-sdk/issues/11403)

原因和我專案上的類似，和 nanopb 有關。

## 如果升到 Xcode 15.3 以上的版本

**請一定要檢查 Firebase 的版本是不是在 10.22.0 以上**

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