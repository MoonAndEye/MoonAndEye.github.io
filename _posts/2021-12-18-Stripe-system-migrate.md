---
layout: single
title: "Stripe 系統漸進式升級的過程"
date: 2021-12-18 15:11 +0800
category: programming
author: Marvin Lin
tags: [system design, migration]
summary: "Stripe 是很知名的支付服務，這篇文章是讀完 Stripe 系統漸進式升級的過程"
---

歷史上，如果火車的軌道寬度要升級，並不會在原來的鐵道上多鋪上兩條鐵軌，而是多蓋一條鐵軌，讓不同軌距的火車，都可以同時行駛在軌道上。等到其中一種軌距的火車全數被汰換掉，這時才會把不用的軌道拆掉。

### Stripe 系統漸進式升級的過程

![](https://cdn-images-1.medium.com/max/800/1*kVy_4E7Jw81-keZ1SwVu1g.png)

### Stripe 進行過的 online migrations

[**Online migrations at scale**  
_Jacqueline Xu on February 2, 2017 in Engineering Engineering teams face a common challenge when building software: they…_stripe.com](https://stripe.com/blog/online-migrations "https://stripe.com/blog/online-migrations")[](https://stripe.com/blog/online-migrations)

以下是在讀完 Stripe 文章後的整理

線上付款為主要業務，如果你想要有海外收款能力，直接找 Stripe 比去和當地銀行快很多。而且要拓展不同國家的業務，大部分都可以在 Stripe 上完成。

誠實蜜蜂的線上收款方案之一，就是 Stripe。

為什麼是「之一」? 因為當時營運的七個亞洲國家中，有幾個不在 Stripe 業務範圍內，所以又引入了另一個收款第三方平台。

### Stripe 的使用者數量級

文章中提到的是 Subscription object，有可能這些 object 為單一公司行號。數量為 hundred millions，所以在 2017 年的時候，在數億左右。

這些數億量級的資料，被放在 table 中，且在 code base 中數個地方大量使用。

且金流服務是不能斷的，所以 Stripe 使用的 migration 一定是 online 的。

### Online migration pattern — 四步驟

1: **Dual writing** to the existing and new tables to keep them in sync.

要對現有 table 和新的 table 都寫入一樣的資料

2: **Changing all read paths** in our codebase to read from the new table.

換掉所有的讀取路徑

3: **Changing all write paths** in our codebase to only write to the new table.

換掉所有的寫入路徑

4: **Removing old data** that relies on the outdated data model

移除掉舊的資料(應該是封存)

### Migration example

### 最初的商業邏輯

每個客戶都會有 Subscription，但最初只設計了一個

    class Customer  Subscription subscriptionend

但是，隨著業務愈做愈多，客戶需求愈來愈複雜。

折價券，折扣，invoice 等功能被加進來， subscription 就要變成 subscriptions

    class Customer  array: Subscription subscriptionsend

而當客戶成長到了一定程度，就要做資料庫的切分，可回頭看 CH6。

左邊是既有設計，右邊是要 migration 的架構

再回頭看一次，migration pattern 四步驟

1: **Dual writing** to the existing and new tables to keep them in sync.

2: **Changing all read paths** in our codebase to read from the new table.

3: **Changing all write paths** in our codebase to only write to the new table.

4: **Removing old data** that relies on the outdated data model

### part1: Dual writing 雙重寫入

只要有新的寫入，就會有一隻程式發動，把這個 subscription 的資料，移到新的 table

然後，再進行 backfilling，把以前的資料倒進新 table

Stripe 使用 Scalding 套件來進行 backfilling，看文章是建講在 Hadoop cluster 上，所以也有使用 MapReduce 進行。而且，只需要約十行程式碼。

Scalding is a useful library written in Scala that makes it easy to write MapReduce jobs (you can write a simple one in 10 lines of code).

Backfilling 的步驟如下

*   Write a Scalding job that provides a list of all subscription IDs that need to be copied over. (找出所有要被 Copy 的 IDs)
*   Run a large, multi-threaded migration to duplicate these subscriptions with a fleet of processes efficiently operating on our data in parallel. (使用多緒的程式開始處理 migration)
*   Once the migration is complete, run the Scalding job once again to make sure there are no existing subscriptions missing from the Subscriptions table. (結束後，使用 Scalding 進行檢查，看有無缺漏)

### part2: Changing all read paths — 改掉所有讀取路徑

前一個動作，已經讓新舊的 table 同步了，現在要改掉讀取路徑，原來舊的讀取路徑都要換成新的路徑。

為了確保新的 subscriptions table 讀到的東西都是正確的(和舊 table 一樣)，stripe 使用了 Scientist 的套件來驗證這一行為。

[https://github.com/github/scientist](https://github.com/github/scientist)

Scientist 是 Ruby library 中，拿來做實驗比對結果的，這個套件會讀新的表和舊的表，並把值交互比對，如果不同，他就發出 error alerting。

在確認新舊表完全相同之後，就會把讀取路徑切到新的 subscriptions table 中。

### part3: Changing all write paths — 改掉所有寫入路徑

下面是 part1 的寫入路徑，那時候設定為 dual write

現在狀況， dual write 會將資料先寫進舊的 customers 表，然後再寫入 subscriptions 表。在 Changing all write paths 這一步，我們要將寫入順序倒轉，先寫入 Subscriptions 再寫入 customers. 注意這一步並不是直接拿掉 customers 表的寫入，而是倒轉。這樣我們才能在改動過程中，進行觀察，並防止重大錯誤在不知情的狀況下持續。

更換寫入路徑，是 migration 最大的挑戰。在 Stripe 裡面，已經有上千行的程式碼和 subscription 有關，這些程式碼也四散在各個 service 中。

為了逐步確認每個步驟都是正確的，在重構的過程中，Stripe 將程式的路徑儘可能切到最小的單位，一步一步的抽換，確保新舊的表是同步。

在抽換的時候，一定要非常，非常小心的應對。Stripe 是不可以直接將新 records 蓋掉舊 records。只要有 miss，就會造成 data inconsistency。而抽換前後的資料確認， Stripe 也是用了 Scientist 套件中提供的功能，進行實驗(experiments 應該是這個 lib 的功能)

最後，抽換的結果如下。

最後，在 Customer 物件中，寫上 raise error，只要有人呼叫原來的 subscriptions，就會 raising an error

最後，在 Customer 物件中，寫上 raise error，只要有人呼叫原來的 subscriptions，就會 raising an error

    class Customer  def subscriptions    Opus::Error.hard("Accessing subscriptions array on customer")  endend

part4: **Removing old data — 將舊資料移除掉**

最後一步，移除掉把寫進舊 table 的程式碼移除掉，最後最後，就會真的刪掉這些程式碼 (你有在用版本控制，不用怕刪程式碼)

等到確認所有的程式碼，都只從 subscriptions 的表拿資料，那就可以把送資料進舊表的程式碼拿掉了。

最後，就完成轉移， subscriptions 的資料，就會從新表拿。

By [Marvin Lin](https://medium.com/@atimis19) on [December 18, 2021](https://medium.com/p/d2c7e73e298b).

[Canonical link](https://medium.com/@atimis19/stripe-%E7%B3%BB%E7%B5%B1%E6%BC%B8%E9%80%B2%E5%BC%8F%E5%8D%87%E7%B4%9A%E7%9A%84%E9%81%8E%E7%A8%8B-d2c7e73e298b)
