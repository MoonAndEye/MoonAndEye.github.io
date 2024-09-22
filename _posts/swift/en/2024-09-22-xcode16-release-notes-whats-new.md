---
layout: single
title: Xcode 16 Release Notes, new features
date: 2024-09-22 16:03 +0800
category: swift
author: Marvin Lin
tags: [Xcode, Swift]
summary: Xcode 16 的 Release Notes 中有以下新增功能（New Features)
---

Here are the **New Features** from the Xcode 16 release notes:

### General
1. **Predictive Code Completion** is now supported on all Apple silicon Macs. It uses a machine learning model specifically trained for Swift and Apple SDKs. (116310768)

### Build Settings
2. **Copy and paste from the build settings editor** now uses xcconfig file syntax. (14333348)
3. **The Project Navigator’s “Open As” context menu** now supports choosing default editors per file type. (24666459)

### xcodebuild
4. **xcodebuild supports importing and exporting a downloaded platform** to disk. This allows simulator disk images to be exported and applied to other Xcode installations without redownloading. (129189162)

### Reality Composer Pro
5. **Timelines** allow you to sequence actions to be executed in a particular order or time. (75589529)
6. **VirtualEnvironmentProbeComponent** enables control of the lighting of virtual environments. (117770245)
7. **Extended texcoords** from 2 to 8 buffers, allowing for more complex data types. (123364636)

### Previews
8. **New Preview Execution Engine** supports shared build products between Build and Run and Previews for faster switching. (37353090)
9. **@Previewable macro** allows direct use of property wrappers like @State in Previews without needing an intermediate wrapper view. (110570957)

### StoreKit
10. **Privacy manifests** can now be included as copied resources in StoreKit configurations for testing privacy policies and terms of service in SubscriptionStoreView. (114228169)

### Swift
11. **Swift now supports non-copyable C++ types** when interacting with C++ code from Swift. (83358475)
12. **~Copyable modifier** can now be used to suppress copyability on protocols and generic parameters. (101653009)
13. **Typed throws** allows functions to specify the exact type of error they throw. (125992062)

### Test Plans
14. **Test reports now support Swift Testing framework** metadata and the ability to filter by test run status. (127015832)

