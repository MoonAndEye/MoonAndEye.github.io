---
layout: single
title: "Excerpts from the Kotlin Multiplatform Mobile Beta Roadmap"
date: 2022-02-04 14:53:00 +0800
category: programming
author: Marvin Lin
tags: [KMM, kotlin, cross platform]
lang: en
summary: "Key excerpts from the Kotlin Multiplatform Mobile beta roadmap, where the relevant team released a video of the KMM beta version roadmap in 2021. The speaker, Ekaterina Petrova, mentioned several improvements from the Alpha to Beta versions."
---

### Excerpts from the Kotlin Multiplatform Mobile Beta Roadmap

In 2021, the relevant team released a video detailing the roadmap for the KMM beta version. The speaker, Ekaterina Petrova, discussed several upgrades from the Alpha to the Beta versions, primarily:

*   New memory management mechanism
*   Integration tools related to Apple developers
*   Adjusting the Hierarchical Project structure to be the default

***

Typically, you only need to write code for specific platform APIs tailored to the unique features of different platforms. However, when using KMM for shared code development, sometimes you still need to specialize the shared code for different platforms.

An example is in concurrent scenarios, where the Alpha version of KMM could cause problems with memory management and had a steep learning curve. The development team announced in mid-2021 that future Kotlin (Beta version) would optimize this aspect.

***

Apple Integration

Using KMM in Kotlin projects is "rumored" to be quite friendly already. On the Apple platform, the `embedAndSignAppleFrameworkForXcodeTest` replaces the manual `packForXcodeTask`, and the functionality of the CocoaPods GradlePlugin DSL has been enhanced. However, it is mentioned that this feature is expected to be implemented after the Beta release.

The remaining features for Apple project integration have not yet been tested, so they are not discussed here.

***

KMM Stability for Migration

The transition to beta is scheduled for Spring 2022, and the speaker mentioned that future versions would focus on compatibility, so significant changes that could disrupt your codebase are unlikely (a nod to Swift 1.0...).

***

Kotlin Beta Roadmap Video

Article at JetBrains:

[**KMM Beta Roadmap Video Highlights | The Kotlin Blog**  
_The Kotlin 2021 Premier Online Event is in full swing, and The KMM Beta Roadmap video is already available for you to…_blog.jetbrains.com](https://blog.jetbrains.com/kotlin/2021/10/kmm-beta-roadmap-video-highlights/ "https://blog.jetbrains.com/kotlin/2021/10/kmm-beta-roadmap-video-highlights/")

By [Marvin Lin](https://medium.com/@atimis19) on [February 4, 2022](https://medium.com/p/60f673b3eda7).

[Canonical link](https://medium.com/@atimis19/kotllin-multiplatform-mobile-beta-roadmap-%E9%87%8D%E9%BB%9E%E7%AF%80%E9%8C%84-60f673b3eda7)