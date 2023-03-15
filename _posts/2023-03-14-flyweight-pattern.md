---
layout: post
title: "Flyweight Pattern — 蠅量級模式(享元模式)"
date: 2022-08-10 21:16 +0800
category: swift
author: Marvin Lin
tags: [Design pattern, Swift]
summary: "Flyweight Pattern — 蠅量級模式(享元模式)，本文在介紹 Flyweight Pattern 時採用 refactoring.guru 上的範例和情境。"
---

本文在介紹 Flyweight Pattern 時採用 refactoring.guru 上的範例和情境。

* * *

### Flyweight Pattern — 蠅量級模式(享元模式)

本文在介紹 Flyweight Pattern 時採用 [refactoring.guru](https://medium.com/r?url=http%3A%2F%2Frefactoring.guru) 上的範例和情境。

出處: [https://refactoring.guru/design-patterns/flyweight](https://refactoring.guru/design-patterns/flyweight)

* * *

#### 情境:

你寫了一個遊戲，是 FPS 型的，裡面有飛彈、子彈等飛行道具。還有各種酷炫的特效，這些特效和爆炸的聲光效果，都卓越超群。你把這個遊戲 push 上去，讓你和你的朋友玩。

### 但是、Shi ka shi、but 「在你的電腦上是好的」

在你朋友的電腦上，每玩幾分鐘，這個遊戲就閃退了! 遊戲體驗在你朋友的電腦上非常的差。你開始 debug，然後 de 了幾個小時，從 log 中翻找各種數據。你找到原因，是出在 RAM 上，error message 最後 trace 到 RAM 不足。因為你電腦的配置很強，但你的朋友電腦設備沒那麼好，所以 RAM 吃光了。

而 RAM 被吃光的原因，是在那個你寫出來的 particle system (專門處理粒子效果)。每個粒子，例如子彈、飛彈，還有各種會飛的物件，只要出現在玩家的螢幕，就會生出一個 particle 物件，最後，當 RAM 不足的時候，程式就崩潰了。

從下圖可見，每個粒子會佔掉 21 KB。當有 1,000,000 個粒子的時候，這時會需要 21 GB 的 RAM。

![](https://cdn-images-1.medium.com/max/800/1*G4GebBvS7ZChon7wEhSvZg.png)

from refactoring.guru

我們來看個 Overwatch 畫面。

![](https://cdn-images-1.medium.com/max/800/1*bZSGkmXGYofMadtii2wyGQ.png)

![](https://cdn-images-1.medium.com/max/800/1*UzKC0uTVHQXLaqTyZhmNNA.png)

如何使用 Flyweight 模式，改善你的遊戲體驗?

* * *

### Flyweight 如何減輕系統上的負擔

再回頭看一下 ”Particle” 這個類別，然後思考一下。

![](https://cdn-images-1.medium.com/max/800/1*4dPir95Ideb9wzMRjK9hbg.png)

你應該會發現，有兩個 property 可以設計成不變的 (也就是剛剛講的內部資料)

*   color
*   sprite

而其他屬性，是會變化的 (也就是剛剛講的外部資料)

*   particle (粒子)
*   coords (座標)
*   vector (移動向量)
*   speed (移動速度)

![](https://cdn-images-1.medium.com/max/800/1*5r80IzFWvGH9MCL0Kgm8nA.png)

再回來看這個系統

![](https://cdn-images-1.medium.com/max/800/1*5yXJEnkUFcrlOgFIqbz86g.png)

最吃資源的，仍然是 sprite，以上面同樣數量的粒子來看。1,000,000 個粒子，在不 init 新的內部資料狀況下，他需要的是 32MB RAM，對比沒有使用 design pattern 的狀況 — 21 GB，這樣的設計，讓你朋友的電腦上，也可以運作順利。

* * *

結束了嗎?這樣已經發揮了 design pattern 最佳的結果了嗎?

### **設計模式是可以進行疊加的!**

* * *

### 再加上一個外部物件儲存池，可以更優化

在實務上，通常會再加上一個「池」(pool)，把生出來的「內部資訊」放在池子 裡面。

在這個案例裡面，因為有一個最大的類別 Game，會在 Game 裡面用一個 property 去存 Particle，當螢幕需要 particle 的時候，系統 會先從池子裡面找有沒有沒用過的 particle，有的話，就拿出來塞「外部資訊」(也就是向量、速度、座標)。如果池子裡面沒有所需要的 partile，就會 init 一個，然後塞外部資訊。

![](https://cdn-images-1.medium.com/max/800/1*9oTHsQUlMpuXtZcj47OviA.png)

當 particle 用完後，就會放入池子裡面，等待下一次被使用。

這可以想成是結合了 Object Pool 模式的蠅量級模式，當然，在 UIKit 中，有某個很重要的元件，使用了這兩個模式的綜合體。

當然還有人再優化，連外部資訊也再加上一套蠅量級模式。

蠅量級的蠅量級模式。沒有最細，只有更細。

* * *

### 再深入一點，當你剛入行，在台灣，你不一定進的去「真正的」遊戲公司，你可能是個 iOS 前端。不論你是哪一領域的前端，在 2022 年，大家起手都是框架。假如你是個 iOS 前端，我們來想想看，在 iOS 系統裡面，哪個東西在應用「蠅量級模式(享元模式)」

By [Marvin Lin](https://medium.com/@atimis19) on [August 10, 2022](https://medium.com/p/a5ab3b6054f).

[Canonical link](https://medium.com/@atimis19/flyweight-pattern-%E8%A0%85%E9%87%8F%E7%B4%9A%E6%A8%A1%E5%BC%8F-%E4%BA%AB%E5%85%83%E6%A8%A1%E5%BC%8F-a5ab3b6054f)
