---
layout: single
title: "SwiftUI & Compose"
date: 2022-06-03 22:34:38 +0800
categories: swift
lang: en
tags: [Swift]
---

Google is currently promoting the Android Study Jam event, and out of curiosity, I participated in the Study Jam online briefing.

I have detailed the event in another article, which you can access directly through the link below:

[**Android Study Jam — Introduction**  
_Google places great emphasis on the Android development environment and frequently launches Study Jams in different regions. These sessions are divided into several phases, and completing each phase earns you a badge. By completing certain tasks by June 23, 2022, you can also receive a Google…_](https://medium.com/@atimis19/android-study-jam-%E4%BB%8B%E7%B4%B9-fc2c44dd2f64)

---

During the briefing, I discovered that Android has a framework for UI rendering called Compose, which uses a declarative approach similar to SwiftUI in the iOS development environment.

At the Study Jam, Tim Lin demonstrated how to create a Text Label using Compose.

![](https://cdn-images-1.medium.com/max/800/1*2CZhpAOPfHN_baUdGtkIIA.png)

Example from Tim Lin in the Study Jam

This piqued my curiosity about whether the same layout in SwiftUI would produce a similar result on both platforms (which would simplify things considerably). Below is the SwiftUI code arranged in the same order as the Compose example shown above.

![](https://cdn-images-1.medium.com/max/800/1*EZMuPTxtjvOyFYtkJMgXrg.png)

SwiftUI code in the same order as the above Compose example

![](https://cdn-images-1.medium.com/max/800/1*rfx2jRCOGrcDpGyuxpaceA.png)

Looking at the rendering preview, it’s clear that the rendering logic differs between the two. In Compose, the first line’s background applies to the entire component (red area), then the next block adds rounded corners and retains an 8 dp padding before drawing the yellow area.

In SwiftUI, the first line's background is only for the Text, followed by an 8 pt padding, and then the yellow background is drawn. The final 4 pt padding creates a white area in SwiftUI. Currently, I do not have enough disk space to install Android Studio, so I cannot verify the outermost layer or the stacking conditions in Compose. However, the last 4 pt padding in SwiftUI has its purpose, and in the absence of additional color, it defaults to the background.

---

Currently, there are no clear conclusions about SwiftUI/Compose; research is ongoing.

Feel free to share your thoughts on these two frameworks.