---
layout: post
title:  "SwiftUI & Compose"
date:   2022-06-03 22:33:38 +0800
categories: jekyll update
---

Google 的現在正在推 Android study jam 活動，心裡因為好奇，所以也在線上參與了 Study jam 的說明活動。

詳細的文章我寫在另一篇，可以直接從下方連結過去

[**Android Study Jam — 介紹**  
_Google 官方是很重視 Android 開發環境的，常常會推出不同區域的 Study Jam。這些練習會分成數個階段，當你完成每個階段，都可以拿到徽章，在 2022/06/23 內完成指定的題目後，還會有 Google…_medium.com](https://medium.com/@atimis19/android-study-jam-%E4%BB%8B%E7%B4%B9-fc2c44dd2f64 "https://medium.com/@atimis19/android-study-jam-%E4%BB%8B%E7%B4%B9-fc2c44dd2f64")[](https://medium.com/@atimis19/android-study-jam-%E4%BB%8B%E7%B4%B9-fc2c44dd2f64)

* * *

在說明會中，我看到 Android 也有一個以宣告式方法，來進行 UI rendering 的框架 — Compose。這個框架可以和 iOS 開發環境中的 SwiftUI 可以進行類比。

在 Study Jam 說明會中，Tim Lin 示範了用 Compose 畫出一個 Text Label。

![](https://cdn-images-1.medium.com/max/800/1*2CZhpAOPfHN_baUdGtkIIA.png)

Tim Lin 在 Study jam 中的案例

於是，我好奇的想，如果我在 SwiftUI 中，使用和 Compose 的排列方式一樣的時候，兩個平台畫出來的東西，會不會一樣呢? (如果會的話….事情就簡單多了)。所以下方就是一個和上面 Compose 一樣順序的 SwiftUI 程式碼。

![](https://cdn-images-1.medium.com/max/800/1*EZMuPTxtjvOyFYtkJMgXrg.png)

和上方 Compose 一樣順序的 SwiftUI 程式碼

![](https://cdn-images-1.medium.com/max/800/1*rfx2jRCOGrcDpGyuxpaceA.png)

看渲染的 preview，就會知道，雙方的渲染邏輯不一樣。在 Compose 第一行的 background，會是整個元件的底色(紅色區域)，然後在下一個區域，加上圓角，保留 8 dp 的 padding 後，再畫出黃色區域。

而 SwiftUI 元件下方第一行的 background，是這個 Text 的 background，然後加上 8 pt 的 padding，再畫上黃色 background。而最後的 4 pt padding，就會產生了 SwiftUI 的白色區域。因為我現在並沒有多的硬碟空間裝 Android Studio 了，所以我目前無法確定 Compose 最外層，或是 Compose 元件套疊的狀況。但 SwiftUI 最後一行的 4pt padding，是有他的意義的，而在沒有多餘顏色下，他會是 default background。

* * *

目前對於 SwiftUI / Compose 都沒有很明確的結論，仍然在研究中。

也歡迎大家回覆對於這兩個框架的想法。

Exported from [Medium](https://medium.com) on March 14, 2023.