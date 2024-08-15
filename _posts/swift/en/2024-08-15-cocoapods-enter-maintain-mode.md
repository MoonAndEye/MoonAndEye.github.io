---
layout: single
title: Cocoapods Enters Maintain Mode
date: 2024-08-15 23:33 +0800
category: swift
author: Marvin Lin
tags: [Swift, Cocoapods, Xcode]
summary: Since Apple introduced the Swift Package Manager (SPM), CocoaPods has faced significant competitive pressures that have impacted its developmental momentum. As SPM is officially supported and seamlessly integrated into Apple's development environment, competing with Apple in the core domain of package management is often not advantageous. This integration gives Apple a distinct edge, as developers tend to prefer using SPM for dependency management due to its robust support and deep integration with their tools. Consequently, CocoaPods has seen a decline in market share and development investment, necessitating a strategic adjustment to adapt to the evolving development ecosystem.
---

## Cocoapods Enters Maintain Mode, But Will Still Release More Than Twice a Year to Keep Up with Xcode Updates

One evening, while scrolling through x (formerly Twitter), I stumbled upon a post retweeted by [Orta Therox](https://blog.cocoapods.org/CocoaPods-Support-Plans/) announcing that Cocoapods, after 13 years, has entered maintain mode.

![cocoapods announcement: enter maintain mode](/assets/swift/cocoapods-enter-maintain-mode/pods_enter_maintain_mode.png)

## Key Points
- Ensure security issues in the mainline are addressed.
- Release at least twice a year to keep up with Xcode updates.
- Review support requests every six months.
- Maintain website infrastructure operations.
- Support limitations: Will not actively follow up on GitHub issues as a support channel, nor commit to handling PRs for new features or application layer errors.
- Consider turning the Specs repository to read-only to simplify security management and maintain existing builds in the long run.
- For projects like React Native, which primarily acquire libraries via npm and not Trunk, such changes may be sufficient.

## Reasoning
Since Apple introduced the Swift Package Manager (SPM), Cocoapods has faced significant competitive pressure, impacting its development momentum. With SPM being officially supported by Apple and integrated directly into its development environment, competing with Apple in the core area of package management tools is disadvantageous. Apple's widespread influence and deep integration with its products have made developers lean towards choosing SPM as their dependency management tool, directly affecting Cocoapods' market share and related development investments. Therefore, facing competition from Apple, Cocoapods needs to adjust its strategy to adapt to the evolving development ecosystem.

## Impact on Pods
Since I have several older iOS projects underway and numerous interdependent modules using pods for management at work, it's inevitable to start supporting SPM. Considering the upcoming changes:
- Xcode 16 is expected to release in September 2024.
- iOS 18 is likely to release in September 2024.
- Swift 6, although optional, will appear with Xcode 16, with Swift 5.10 being the last of the version 5 series.

I anticipate that the development community will adapt to these changes by around early 2025. Therefore, I plan to initiate support for SPM starting in 2025.

## [Orta Therox's Article on Cocoapods Entering Maintain Mode](https://blog.cocoapods.org/CocoaPods-Support-Plans/)
