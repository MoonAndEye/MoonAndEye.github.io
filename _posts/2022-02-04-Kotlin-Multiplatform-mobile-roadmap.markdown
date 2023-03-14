---
layout: post
title: "Kotlin Multiplatform Mobile beta roadmap 重點節錄"
date: 2022-02-04 14:53
category: [Kotlin, Cross platform]
author: Marvin Lin
tags: [KMM, kotlin, cross platform]
summary: "Kotlin Multiplatform Mobile beta roadmap 重點節錄，在 2021 年 相關團隊發佈了 KMM beta 版本 roadmap 的影片。影片講者 Ekaterina Petrova 提到了數個 Alpha 到 Beta版本改進的內容"
---

### Kotlin Multiplatform Mobile beta roadmap 重點節錄

在 2021 年 相關團隊發佈了 KMM beta 版本 roadmap 的影片。影片講者 Ekaterina Petrova 提到了數個 Alpha 到 Beta版本改進的內容，主要為

*   新的記憶體管理機制
*   與 Apple 開法者想關的整合工具
*   Hierarchical Project 結構調整成預設

* * *

通常，你只需要針對不同平台的特性，去針對特定平台的 API 進行程式的撰寫。但當使用 KMM 進行共用程式碼開發時，有時候你仍然要對共用程式碼進行不同平台的特化。

其中一個例子，就是在併發情境下，Alpha 版的 KMM 在記憶體管理上，容易造成問題，且學習曲線陡峭。開發團隊在 2021 年中的時候，就表示未來的 Kotlin (Beta 版) 會在這個方面進行優化。

* * *

Apple Integration

KMM 在 Kotlin 專案的使用，「聽說」已經是相當友善了。而在 Apple 平台，用 embedAndSignAppleFrameworkForXcodeTest 取代以往手動的 packForXcodeTask，此外，還加強了 CocoaPods GradlePlugin DSL 的功能。但這邊有提到，這個 feature 應該會在 Beta release 後進行。

剩下的 Apple project 整合功能，因為還沒開始測試，所以這邊先不介紹剩下的部分

* * *

KMM stable for migration

會在 2022 春季進入 beta，講者說以後會兼顧兼容性，所以應該不用怕大的改動把你的 codebase 搞壞 （Swift 1.0 表示….）

* * *

Kotlin Beta roadmap 的影片

在 jetbrains 的文章

[**KMM Beta Roadmap Video Highlights | The Kotlin Blog**  
_The Kotlin 2021 Premier Online Event is in full swing, and The KMM Beta Roadmap video is already available for you to…_blog.jetbrains.com](https://blog.jetbrains.com/kotlin/2021/10/kmm-beta-roadmap-video-highlights/ "https://blog.jetbrains.com/kotlin/2021/10/kmm-beta-roadmap-video-highlights/")[](https://blog.jetbrains.com/kotlin/2021/10/kmm-beta-roadmap-video-highlights/)

By [Marvin Lin](https://medium.com/@atimis19) on [February 4, 2022](https://medium.com/p/60f673b3eda7).

[Canonical link](https://medium.com/@atimis19/kotllin-multiplatform-mobile-beta-roadmap-%E9%87%8D%E9%BB%9E%E7%AF%80%E9%8C%84-60f673b3eda7)
