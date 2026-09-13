---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜古騰堡之後人人能讀書，AI Agent 之後人人能做 app - Tip 01"
date: 2026-09-13 22:19:00 +0800
category: programming
author: Marvin Lin
tags: [IT鐵人賽, 2026鐵人賽, Vibe Coding, Vibe Coding 技巧, AI Agent, 軟體開發]
summary: "我用古騰堡印刷術的歷史，看 AI Agent 如何降低做出第一版 app 的成本。當更多人能把想法做成產品，需求、品質與工程判斷會更早進入開發流程。"
description: "我用古騰堡印刷術的歷史，看 AI Agent 如何降低做出第一版 app 的成本。當更多人能把想法做成產品，需求、品質與工程判斷會更早進入開發流程。"
---

這是 2026 iThome 鐵人賽《Vibe Coding：30 個開發實用技巧》系列的 Tip 01。

這一篇改寫自我部落格的《AI Agent Coding：第二次印刷術正在發生》，照這個系列的格式重寫過。原始文章：https://www.marvinswift.com/zh/programming/ai-agent-coding-gutenberg/

這個系列的第一篇先講一個觀點，技巧從明天開始。我覺得 AI agent coding 很像人類歷史上的古騰堡印刷術。它先改變的，是「把想法變成可複製產品」的成本。

## 以前，書離一般家庭很遠

以前要寫一篇 blog、做一個 web app、做一個 mobile app，通常要先準備一整套技能：會寫程式、懂 framework、會接 API、知道怎麼部署，最好還會一點 design。這些能力仍然重要，但起步的成本明顯不一樣了。

古騰堡印刷術普及之前，書主要靠手抄。Getty 對中世紀書本成本的整理講得很直覺：一本書背後有材料、羊皮紙、抄寫、插畫、裝訂這一整條手工流程。Jeremiah Dittmar 在 Book Prices in Early Modern Europe 裡整理到，1474 年一本印刷的 breviary 賣 4 個 gold ducats，大約是同類手抄本的五分之一；1481 年也有以前值 10 florins 的書，印刷後變成 2 florins 的紀錄。即使進入印刷時代，書還是貴：Swiss National Museum 提到 15 世紀末一個 manual trade 的 journeyman 一個月大概賺 1 個 guilder，而 1485 年的 Nuremberg Bible 要 6 個 guilders。

把這些數字排在一起看。先看收入。Maddison Project Database 估 1500 年前後的人均所得，單位是 2011 年的國際元：德意志地區一年約 1,800 元，英格蘭約 1,700 元，法國約 1,700 元，義大利約 2,700 元。換成一天，大約 5 到 7 美元。那是平均值，把貴族和商人都算進去了；一般人家過的日子在平均之下。

再看書。Swiss National Museum 那個例子可以直接換算：熟練工人一個月賺 1 個 guilder，一年 12 個；1485 年那本 Nuremberg Bible 要 6 個 guilders，等於半年的工資。這還是印刷過的價格。手抄的年代，照 Dittmar 記的那個五倍比例反推，同一本書大約要兩年半的工資。一個靠一份工資過日子的家庭，買一本書要花掉半年到兩年多的收入，所以書在大部分家庭裡就是沒有。

## 那書放在哪裡，誰讀得到

家裡沒有書，那書在哪裡？看兩份當時的文獻。

第一份是六世紀寫的《本篤會規》，本篤會的修道院照它過日子。第 33 章寫修士什麼都不能私有，「連一本抄本、一塊寫字板、一支筆都不行」（neque codicem, neque tabulas, neque grafium），書歸修道院。第 48 章把讀書排進每天的時間表：復活節到十月，早上先做工，第四時到第六時（大約上午十點到中午）「空下來讀書」；四旬期從早上讀到第三時；星期天全體讀書。還要派一兩位長老在讀書時間巡查，看有沒有修士偷懶聊天。第 38 章規定用餐時要有一位修士朗讀，其他人全部靜默，「只聽得到讀書人的聲音」。第 9 章寫夜間禮儀，弟兄們輪流從擱在讀經台上的抄本讀三段；第 53 章寫客人來了，先「在客人面前讀一段聖經」。修道院是書最多的地方，修士自己讀；外人在那裡碰到書，是坐著聽。

第二份是 1345 年的《Philobiblon》，作者 Richard de Bury 是杜倫主教，當過英王愛德華三世的大法官和財政大臣。第五章講修道院：從前修士在祈禱的空檔親手抄書，「今天大多數修道院裡那些裝滿書的聖庫，就是他們的勞動留下來的」；接著罵當時的修士只顧酒杯、羊群和田產，書丟在一邊。第八章講他自己的書從哪裡來：他當大臣，人人知道送書比送錢更容易討他歡心，「最有名的那幾座修道院打開了書櫃」，長年沒人動過、被老鼠和書蟲咬過的書被翻出來，有的送他、有的賣他、有的借他；他也翻遍在俗教士的藏書，去巴黎出差就進書店掃貨，「我們要的是抄本，愛抄本勝過金幣」。他的傳記作者 Chambre 說，他的書比全英格蘭其他主教加起來還多，每一處住所各有一間藏書室，臥房裡書堆到沒地方走路。第十八、十九章他打算把全部藏書捐給牛津一間學堂，寫下借書規則：五個管書人，三人同意才能借出；有複本的書才能借出牆外，還要押超過書價的抵押品；只有一本的，外人只能在牆內翻閱；借書人不能轉借，每年清點一次。

這兩份放在一起看，那個年代的書在三種地方：修道院和主教座堂，抄書、藏書是他們的本行；大學和學堂，書鎖在牆內，借出去要押金；主教、大臣、貴族的住所，書跟著有權有錢的人走。《美女與野獸》把書放在城堡裡，方向對了：擺得出一面書牆的，就是住城堡的那種人。喬叟《坎特伯里故事》裡那個牛津窮學生，外套破了也寧可床頭擺二十本書，朋友給的錢全拿去買書；二十本書，在十四世紀值得寫進詩裡。

識字率也在同一個脈絡裡，Our World in Data 的 literacy dataset 提醒 1451 到 1800 年之間很多資料只能用書籍與手稿的產量間接估計，Robert Allen 的研究則估計 1500 年左右英格蘭成人識字率約 6%，荷蘭約 10%，法國約 7%。

所以古騰堡印刷術真正先改變的，是複製文字的成本。複製成本下降，更多人開始被拉進閱讀市場。這個轉折放到今天看，最像的就是 app 開發正在發生的事。

## AI agent coding 降低的是 app 的複製成本

以前做 app 很像手抄書。很多 code 不需要天才來寫，但就算只是一個簡單的 app，前端、後端、資料和部署加在一起，還是會變成門檻。

在 AI agent coding 之前，工程師已經一直在想辦法降低重複成本：模組、library、framework、template，都是把常見能力抽出來，讓下一個專案別從零開始。這些解決的是「程式碼怎麼重用」。AI agent coding 更進一步，它開始處理「需求怎麼變成一個可跑的 app」。一個 mobile app prototype、一個 web app 的第一版，現在都可以用 agent 很快做出來。原本要很高固定成本才會開始的事，現在可以用比較低的成本先試。這個差別很大。

## 更多人會開始接觸 coding

印刷術讓書變便宜之後，低收入家庭沒有隔天就多一整面書牆。真實的改變是，原本很難碰到書的人，開始有機會接觸單張印刷品、小冊子、便宜一點的書。閱讀的入口變多了。

AI agent coding 對 app 開發也會是這樣。更多設計師、PM、學生、創作者、小店老闆，會第一次真的做出自己的 web app，把腦中的流程變成一個可以打開的產品。以前他們只能畫 wireframe、寫需求文件、找工程師估價；現在可以先做出一個版本。這個版本可能很粗糙、code 很亂、安全性要重做、部署方式撐不了正式流量，但它已經可以被打開、被點、被修改，可以拿去問使用者：「這是你要的嗎？」

這就是 AI agent coding 最重要的地方。它讓更多人先進到工程世界裡面，也讓工程能力變成更多人需要理解的事情。

## 會 coding 的人，角色反而會變重要

印刷術讓書變便宜後，作者、編輯、出版商仍然重要。書變多之後，判斷哪一本值得讀、哪一個版本可信、哪一種論述有價值，這些能力變得更重要。

AI agent coding 也一樣。app 變得更容易生成，真正稀缺的能力會變成：你知不知道要做什麼，能不能拆出清楚的需求，能不能判斷 agent 寫出來的 code 能不能維護，最後能不能把 demo 變成真的產品。資料、安全、部署、成本、使用者回饋，這些事照樣留在開發流程裡，還會更早出現，逼你更早面對產品到底能不能用。

所以我覺得 coding 會更像閱讀。以前只有少數人需要讀書，因為書太少也太貴；後來書變多，讀書變成更多人的基本能力。未來 coding 可能也會這樣：專業軟體工程師還是專業工作，但更多人會需要看得懂 app 的結構，知道一個 repo 在做什麼，知道 agent 產出的結果哪裡危險，知道怎麼把一個 prototype 推到可以使用的狀態。

當更多人具備這種基本能力，下一個變化會很自然：app 會變成更多人的出版物。

## 小結

古騰堡印刷術讓書本不再只是少數人的手抄珍品；AI agent coding 可能會讓 app 不再只是公司和工程團隊才能生產的東西。以前是「我有一個 idea，但我不會寫程式」。接下來會變成「我有一個 idea，我先用 agent 做一版」。這就是 AI Agent 時代。

明天開始講技巧。第一個：前端、後端放在同一個資料夾。

參考：
- Getty, Why are books so expensive? https://www.getty.edu/news/why-are-books-so-expensive/
- Jeremiah Dittmar, Book Prices in Early Modern Europe https://eprints.lse.ac.uk/115588/1/Dittmar_book_prices_in_early_modern_europe_accepted.pdf
- Swiss National Museum, Book printing in Europe https://blog.nationalmuseum.ch/en/2017/05/series-book-printing-in-europe-4/
- Our World in Data, literacy rates https://ourworldindata.org/grapher/cross-country-literacy-rates
- Maddison Project Database 2020（Bolt and van Zanden） https://www.rug.nl/ggdc/historicaldevelopment/maddison/releases/maddison-project-database-2020
- 《本篤會規》拉丁全文（The Latin Library） https://www.thelatinlibrary.com/benedict.html
- Richard de Bury, Philobiblon，E. C. Thomas 英譯（Project Gutenberg #626） https://www.gutenberg.org/ebooks/626
- Richard de Bury, Philobiblon 拉丁原文（The Latin Library） https://www.thelatinlibrary.com/debury.html
- Chaucer, The Canterbury Tales（Project Gutenberg #2383） https://www.gutenberg.org/ebooks/2383

原文：https://www.marvinswift.com/zh/programming/ai-agent-coding-gutenberg/
