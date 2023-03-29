---
layout: single
title: 使用zmud玩mud的第一步 定時器(timmer)和觸發(trigger)
date: 2015-08-27 16:41
category: life
author: Marvin Lin
tags: [life, game]
summary: 
---

使用zmud玩mud的第一步 定時器(timmer)和觸發(trigger)

  

如上一篇所說的。

玩mud就是要一直輸入指令，但如果你升一級要輸入100次指令，然後你想升到一百級呢？

這時候，就必需要用timer了，這邊先用zmud做例子。

  

[![](http://1.bp.blogspot.com/-bWTWihYErio/VdyIwgRtbTI/AAAAAAAAQKo/xIazTsXGo7k/s400/%25E5%25AE%259A%25E6%2599%2582%25E5%2599%25A8.png)](http://1.bp.blogspot.com/-bWTWihYErio/VdyIwgRtbTI/AAAAAAAAQKo/xIazTsXGo7k/s1600/%25E5%25AE%259A%25E6%2599%2582%25E5%2599%25A8.png)

  

當你打開計時器

Time interval : 這個計時器一個週期幾秒

Timeout margin: 當數到第幾秒時，送出指令

Timeout command: 你想輸入的指令

  

[![](http://2.bp.blogspot.com/-yHFQ9w-6SKk/VdyIwhXj-gI/AAAAAAAAQKk/vOy-ppKrhVk/s320/ScreenHunter_1063%2BAug.%2B25%2B23.00.jpg)](http://2.bp.blogspot.com/-yHFQ9w-6SKk/VdyIwhXj-gI/AAAAAAAAQKk/vOy-ppKrhVk/s1600/ScreenHunter_1063%2BAug.%2B25%2B23.00.jpg)

  
  

  

當然，你也可以使用複數的指令，舉例來說，我想要釣魚，但我身上可能有一條死魚，我想要先把之前釣到的魚丟掉，則command為

drop siyu; fish

zmud是用分號來進行複數指令

  

比較多的，是我想學莫聲谷的武功，但是在bot期間，有可能我會學到上限，那我希望在學到上限後直接學下一個。

  

learn mo force 180;learn mo yinyun-ziqi 180;learn mo dodge 180; learn mo parry 180; learn mo taoism 180; learn mo strike 180; learn mo taiji-quan 180;sleep

  

這就是先學「基本內功」，如果基本內功沒滿，則bot則會學180次，通常這時候就沒力了，所以後面的指令輸入也不會行動，直到最一個 sleep。

  

然後我又發現，可以在前面先放個內力。所以在前面先加上 exercise 10。不過在測試後發現，內力會有一個動作，所以必則把練內力的指令和後面學習的切開。

所以之間放了 #wa 1000，意思就是間隔1000ms (就是1秒)，才發送後面這一串的命令。

  

exercise 10; #wa 1000; learn mo force 180;learn mo yinyun-ziqi 180;learn mo dodge 180; learn mo parry 180; learn mo taoism 180; learn mo strike 180; learn mo taiji-quan;sleep

  

這樣，你就完成了自動練功，自動打工。

  

  

第二部分就是觸發 trigger

  

在武俠的世界，你需要喝水吃東西。

但你在bot的過程，可能人不會在電腦前面數個小時，那餓的時候，就要讓他自動進食，不然會進入昏迷狀態。因為這個遊戲餓不死人，所以餓就給他餓也行。

  

但為了提高效率，你也可以設trigger。

  

Trigger就是指，當你讀到「某些指令時」，程式就自動發送預設的訊息上去。以這個自動喝水進食為例，就是當程式讀到「你渴得喉嚨冒煙」、「你餓得頭昏眼花」時，自動發送進食喝水的需求。注意，並不需要整句一起設定，因為mud有時候會有吃字的問題，所以在這邊只要取「你渴得」「你餓得」這樣就可以了。

  

[![](http://4.bp.blogspot.com/-EActN1VZAqY/VdyIwcb6H2I/AAAAAAAAQKs/Qtvj2RYHzwo/s400/trigger.png)](http://4.bp.blogspot.com/-EActN1VZAqY/VdyIwcb6H2I/AAAAAAAAQKs/Qtvj2RYHzwo/s1600/trigger.png)

步驟1:按新增

步驟2:第一行就是觸發的訊息，值(value)就是你要發送的指令

所以如果讀到 渴和餓，就發送 drink shui; eat gan liang;

  

這樣，你就可以開始掛你的機器人了

  

下一篇是把這些組合起來，寫出一個自動釣魚機器人。