---
layout: post
title: "Prototype Pattern (原型模式) in Swift (Reference type vs. Value type) 的不同"
date: 2018-06-09 15:36 +0800
category: Swift
author: Marvin Lin
tags: [Swift, design pattern, prototype pattern]
summary: "Prototype Pattern (原型模式) in Swift (Reference type vs. Value type) 的不同，這一篇文章是看了 "Pro Design Patterns in Swift " 後的心得，把原型模式整理後寫成中文的記錄。"
---

Prototype Pattern (原型模式) in Swift (Reference type vs. Value type) 的不同
=====================================================================

這一篇文章是看了 "Pro Design Patterns in Swift " 後的心得，把原型模式整理後寫成中文的記錄。

* * *

### Prototype Pattern (原型模式) in Swift (Reference type vs. Value type) 的不同

![](https://cdn-images-1.medium.com/max/800/1*oSH09tpBPZt9tTyivxUxhg.png)

> 這一篇文章是看了 "Pro Design Patterns in Swift " 後的心得，把原型模式整理後寫成中文的記錄。

情境:忍者頭目

![](https://cdn-images-1.medium.com/max/800/1*yGesVxbCpDZbw7gmPCClBQ.png)

先假設你要寫一個遊戲，某一關的頭目是忍者。 這一關裡，Boss 有各種 nerf 狀態，像是中毒、減傷、破甲、緩速、拌筋，等共30種 nerf 狀態，而 buff 有另外 10 種狀態。

打到 1/2 血的時候， boss 會使用絕招 -「影分身」。

影分身會複製出 4 個和 boss 狀態一模一樣的分身，血量和各種 buff, nerf 狀態會同時複製。

影分身受傷的時候，本體不會有影響，但本體 hp 歸 0 的時候，才進行寶物結算。

如果這樣類型的場合，用 Prototype 就是一個不錯的選擇，但請記得還有一句話，「這世上沒有銀色子彈」，在使用前，請依照場景及條件，去選擇一個最適合當下情況的模式，而不是讓「非用 XX 模式才是正道」這種想法去寫 app。

> _No Silver Bullet — Essence and Accidents of Software Engineering_

![](https://cdn-images-1.medium.com/max/800/1*VFfKvJ1VOTkkPaw2S3xGQw.png)

Prototype pattern 的操作方式

使用原型模式大概可以分成兩個步驟:

Step 1: 先生出模板，最簡單的方式可以用 let aStruct = SomeStruct(propertyA:a, propertyB:b) 這樣的方式

Step 2:把模板複製出一份，再開始修改裡面的 property，改成你要的物件。

在書上有例舉出來使用原型模式的各個要點，我這邊整理在下面

![](https://cdn-images-1.medium.com/max/800/1*U_RaBhdDQuXps5sEfMS7fg.png)

以這模式的好處來說，就是他使用的是 Copy ，雖然書上有寫說他可以避免 init 所花的成本，但 Swift 下的 Copy，其本上還是會跑一次 init()，所以我並無法理解他所提到的「成本」到底是指哪邊的成本，但還是照著書上所寫的列出來。

我們先用聚會的提醒來做例子。

如上所寫的，一個 Appointment 最重要的就是「和誰」、「什麼時間」、「哪個地點」。一開始的 beerMeeting 先設定為「和大學同學」在「星期五」的「酒吧」聚會，然後再複製出一份指定為 workMeeting，然後把設定調整成「和老闆」在「星期一」的「第二會議室」。這樣的模式就是「原型模式」。

![](https://cdn-images-1.medium.com/max/800/1*XTf04r3akc_X4MaTafg7Cw.png)

以上的方法在 struct 等value type 物件是沒有問題的，但如果用在 class 等 reference type 的物件的時候，會因為指向同一個物件，而產生奇怪的結果。

![](https://cdn-images-1.medium.com/max/800/1*dpVBVnLBol45bC0x6z-nXQ.png)

你可以發現，你在 21~ 23 的行為，雖然都是針對 workMeeting 的 property 做操作，但同時也影響了 beerMeeting 這個物件。因為他在 reference type 的創建中，你並沒有真正的「複製」，你只是讓 workMeeting 去指向 beerMeeting 同樣指向的地方。所以當你一更改，beerMeeting 的 property 也會變，用下面這張圖就可以清楚看到指向同樣的東西的示意圖。

![](https://cdn-images-1.medium.com/max/800/1*A1bDJrel1mkaseu_BtiXdw.png)

我在 Giphy 上找到這個神燈精靈的圖，算是可以解釋這種現象。下面這張圖的神燈精靈都只是原來的那一隻的分身。雖然看起來有很多隻，但如果他遭到神燈封印，那所有的分身照故事邏輯來說，都會同時被封印。這就是對一個物件改變，但所有指向的東西也一起改變。

看起來都是複製品，但其實都是那一個精靈

如果要對 class 做複製的行為，那你就要讓物件 confirm NSCopying 的 protocol。以下是範例，但因為是範例，所以直接使用了 force unwrap，在寫專案的時候，**記得用其他方法去避免 as! 的產生**，因為你每放了一個驚嘆號，就是放了一顆地雷，你只是不知道什麼時候會引爆。

這邊在 confirm NSCopying 後，要實作 copy()，return 的值就是自已的類別，並把當下的值塞入進行 init()。這樣你就得到一個內部的值完全一樣的拷貝版。之後再對裡面的 property 做變更就行了。

不過拷貝可以講的，到這邊還沒結束。這個 Appointment 類別裡面的三個值，都是 String。 String 是 value type 所以當你複製了一份 Appointment 時，這三個值毫無懸念的也以 value type 的型式 copy 了一份。所以後來複製出來的 workMeeting 裡面的值當然不會引響 beerMeeting。那如果裡面的值也是一個 reference type 的話，Appointment 的 NSCopying 會對那個 reference type 也會產生 copy 效果嗎?

我們現在定義一個 Location 的類別並取代原來的 place: String 試試看。

class Location {

     var name:String  
     var address:String

     init(name:String, address:String) {  
         self.name = name; self.address = address  
     }  
}

現在 beerMeeting 的 place 已經是一個 reference type，那在 copy 的時候， self.place 會不會也被 copy 一份呢?從下面這邊我們可以看到 place 的值。

![](https://cdn-images-1.medium.com/max/800/1*fmMQLtti93RjksF1EdVHOQ.png)

beerMeeting 的place 在更改workMeeting時一起被更改了。

> 這樣的 copy 行為，有一種稱呼，叫做 " shallow copy" (淺拷貝)。這是指拷貝的時候只拷貝了參照的行為，並沒有把實體真的拷貝一份。

> 相反的，在拷貝的時候，把實體再複製一遍的這個行為，叫做 "deep copy" (深拷貝)。

![](https://cdn-images-1.medium.com/max/800/1*gzdxGTOSNFlkERalOdTxZQ.png)

這張圖可以清楚的看到Location這個物件是怎麼被指向

如果你要讓 Location 也能被 copy ，那 Location 也要 confirm NSCopying 的 protocol ，並且在 Appointment 進行複製的時候使用 copy()。

下圖可以看到 clone 的 place 已經和 prototype 的 place 沒有關係了。這就是所謂的 "Deep copy" (深拷貝)

![](https://cdn-images-1.medium.com/max/800/1*2uWOyvT8x_VPu62t_U5cuQ.png)

書中也提到，深拷貝與淺拷貝並沒有優劣之別，你應該就當下的情況來決定你的物件是要走深拷貝或是淺拷貝。考量的點依照重要性如下表列。

1、該物件是怎麼被使用的?

2、Copy 所需要的記憶體和成本

3、寫 Copy 所需要的工

我們從第一個要點來思考前一個 Appointment 的範例。如果這個 Appointment 只會給單一 user 使用，這樣的 Appointment 預設應該會是深拷貝比較好，因為 user 複製了一個長得差不多的行程，下一步一定是去修改他，這才是 user 複製的目的。

但如果這個 Appointment 是集體的行事曆，那依照各種場合不同，也有可能是淺拷貝比較好。比如說遇到了會議室滿了、客戶臨時來訪等情況。當有權限的人更改了會議的地點或是時間，其他人參與者應該要知道一樣的情報。

> 所以在選擇使用深拷貝或是淺拷貝的時候，最重要的就是使用情境。

* * *

下一段，要說的是 prototype 模式中，可以讓某個物件在複製另一個物件的時候，不用知道對方的 init 條件，來降低耦合性。

先來假設一個情境，你的客戶在需求中要求紀錄 Message 這個物件，而且在開案的時候和你說:「這個 Message 要求很簡單，因為發送方一定是持有手機的人，所以你只要包含傳送方和內容就好了。另外這些 message 要 cache 起來。」

所以，依照需求，你的 Message 和 Message Logger 只要這樣就好了。

然後在結案前二周，客戶突然跟你說，他要追加一個「簡單的」需求(客戶和工程師的日常)，就是某些 Message 會是另一個人發過來的，讓對話中的兩個人看到。同樣的，這個 Message 也要進同一份 Message Logger。

如上所視，這個作法「暫時的」解決了問題。你只要在 logMessage 前先判斷他是哪一種 Message ，然後再用 init 的方式生出複製品然後加入 array 。

而客戶的日常-「增加需求」會不時的發動，如果又過了一個禮拜(結案前一周)，客戶又加了一個「簡單的」需求，要求兩種新的 message 種類，你該用什麼心情面對? 這邊有一個圖可以表示。

![](https://cdn-images-1.medium.com/max/800/1*_bgv9PCoER5Z1iAtKRiSEg.png)

假的~~~趕快把客戶的聯絡方式關起來 (誤)

* * *

或者，你可以在一開始的 Message 就讓這個類別可以自己拷貝一份出來，因為 MessageLogger 在使用拷貝的時候並不知道 Message init 的條件，所以不論你後面增加了幾十種 Message 的 sub class，Message Logger 這邊的程式碼都不需要改寫。

↓使用 Prototype Pattern 的程式碼

在看完這篇文章後，如果想測測看自己對 Deep copy, Shallow copy 的了解，你可以打開 Playground 寫段這樣的 code，然後先預測他的結果再按下執行。

1、創一個空 array

2、在這個 array 裡面塞一個 class，這個 class 要有可以變更的 store property，舉例 (忍者龜裡面的達文西)

3、複製這個 array (使用 var b = a 這種方式)

4、修改複製出來 array 裡面的class 裡面的 property ，舉例(修改成拉斐爾)

5、問題來了，請問原來 array 裡面的 class，會不會被改變呢?

這邊就不公佈答案了，你就自己試試看吧

> 如果你己經理解了，那這邊公佈與否，結果都一樣。但如果你還沒理解，你可能只是把答案背起來而已，換個場合換個條件可能就爆炸了。

By [Marvin Lin](https://medium.com/@atimis19) on [June 9, 2018](https://medium.com/p/bb47c13baecb).

[Canonical link](https://medium.com/@atimis19/prototype-pattern-%E5%8E%9F%E5%9E%8B%E6%A8%A1%E5%BC%8F-in-swift-bb47c13baecb)
