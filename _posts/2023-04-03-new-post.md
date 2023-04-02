---
layout: single
title: Twitter 開源了推薦演算法
date: 2023-04-03 00:11 +0800
category: programming
author: Marvin Lin
tags: [Twitter, open source, algorithm]
summary: Twitter opened algorithm of recommend
permalink: /programming/:title:output_ext
---

## Twitter 開源了使用在 Twitter 上的推薦演算法

馬斯克實現了他在併購 Twitter 時講過的話，「要開源演算法」

現在，這個 repo 已經在 github 上公開了，任何人都可以 fork 了

[Twitter algorithm link](https://github.com/twitter/the-algorithm)

## 怎樣做你的 tweet 才會被演算法提高權重呢？

[這篇文章有對演算法整理](https://vocus.cc/article/6427f71ffd897800010fa4e6)

### 以下有利觸及

- 點擊推文愛心表示 favorite 喜歡 30X boost
- 轉推 retweet 20X boost
- 每個推文回覆只有 1X
- 推文有圖 2X boost
- 推文有影片 2X boost
- 在信任圈 Trusted Circle 3X
- 點擊進入推文，並在那停留至少2分鐘
- 用戶打開推文作者個人資料頁面並互動喜歡或回覆推文
- 回覆推文並被推文作者互動
- 付費藍勾，如果是你關注又有藍勾的 4X boost，沒關注的藍勾 2X boost

### 以下不利觸及

- 非新聞媒體的外連連結 URL 對觸及不佳，除非有高互動，如果沒有高互動會被視為spam降觸及權重
- 有外連 URL 沒有文字，失敗中的失敗
- 如果出現大量unfollowed，你會自然被算法隱形
- 沒收功就罵髒話，講冒犯的話 0.1X
- 負面回饋：顯示較少、屏蔽、靜音、濫用和Spam舉報
- 用太多hashtag 0.6X
- 寫錯字或是創造字電腦認不出來 0.01X
- 推文是英文，但是UI語言不是英文 0.7X
- UI語言是英文，但推文不是 0.3X
- 用戶語言和推文語言不同，兩者都不是英文 0.1X

## 參考連結

- [Twitter 開源推薦演算法，從中了解社群媒體推送邏輯](https://vocus.cc/article/6427f71ffd897800010fa4e6)

- [Intl Econ Observe Twitter](https://mobile.twitter.com/IEObserve)

- [Intl Econ 的推](https://mobile.twitter.com/IEObserve/status/1642148470944575488)