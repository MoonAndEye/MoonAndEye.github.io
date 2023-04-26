---
layout: single
title: Google Bard AI 開放台灣申請了
date: 2023-04-26 16:03 +0800
category: programming
author: Marvin Lin
tags: [AI, Google]
summary: 
permalink: /programming/:title:output_ext
---

Google Bard AI 開放申請了，只要點選下面的連結按同意，就可以了。

[申請測試連結](https://bard.google.com/?hl=en)

## 申請過程

### Bard 的測試信

在申請完後，會有一封信寄到你的信箱，打開來會看到他附上了用 Bard 寫出來的一首詩給你。

![bard white list message with poem](/assets/programming/bard-beta/bard-white-list.png)

等待時間並不長，我只等了八分鐘，就可以用了。

![bard second email](/assets/programming/bard-beta/email-list.png)

## 開始使用 Bard

bard 現在只能接受英文，所以我這邊的問題都是用英文問的。

### 問新聞

![Ask bard news](/assets/programming/bard-beta/ask-news.png)

### 問股價

問了 Bard 能不能預測今晚 AAPL 的股價。回應是不行。

![Ask bard Apple's stock price in next day](/assets/programming/bard-beta/ask-predict-stock-price.png)

### 改問 AAPL 財報資料

改問已經發生的歷史資料，他可以回答出財報，包含數字。

![問財報](/assets/programming/bard-beta/ask-aaple-report.png)

### 問一下台積電工廠的地址

非常詳細啊，連廠房的名字都列上來了，看名字大概也知道哪個地址上的工廠是做哪一段半導體製程的。(不過，這應該是新聞都有報的)

![台積電地址](/assets/programming/bard-beta/ask-tsmc-address.png)

### 問 Android 和 iPhone 誰賣得比較好

這邊也給的出數字，而且數字也的確來自另一份報告。

![問 Android 和 iPhone 誰賣得比較好](/assets/programming/bard-beta/ask-iphone-android-selling.png)

### 問投資標的

給出很穩健的標的， AAPL, MSFT, AMZN, GOOGL, TSLA

Apple (AAPL): Apple is one of the most valuable companies in the world, and it is a leader in the technology industry. The company is known for its innovative products, such as the iPhone, iPad, and Mac. Apple is also a major player in the services industry, with its App Store, Apple Music, and Apple Pay.
Microsoft (MSFT): Microsoft is another tech giant that is a good investment target. The company is a leader in the software industry, and it also has a strong presence in the cloud computing market. Microsoft is a well-established company with a long history of innovation.
Amazon (AMZN): Amazon is a leading e-commerce company, and it is also a major player in the cloud computing market. The company is known for its low prices and its wide selection of products. Amazon is also a growing force in the advertising market.
Alphabet (GOOGL): Alphabet is the parent company of Google, which is one of the most popular search engines in the world. Google also has a strong presence in the advertising market, and it is a leader in the development of artificial intelligence.
Tesla (TSLA): Tesla is a leading electric vehicle manufacturer, and it is also a player in the solar energy market. The company is known for its innovative products and its ambitious goals. Tesla is a high-growth company, but it is also a risky investment.

![問投資標的](/assets/programming/bard-beta/ask-invest-target.png)

### 如何用 API 的方法串接 Bard

![如何用 API 的方法串接 Bard](/assets/programming/bard-beta/ask-connect-bard-api.png)

## 試用心得

Bard 在問像是餐廳等資訊時，我查起來是有這些餐廳的。然後在數字的表現上，不會有很大的誤差。

## 參考網址

[Bard AI](https://bard.google.com/u/1/faq?hl=en)

[Using Bard API](https://www.googlecloudcommunity.com/gc/AI-ML/Google-Bard-API/m-p/538517)