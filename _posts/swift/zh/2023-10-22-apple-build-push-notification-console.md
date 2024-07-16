---
layout: single
title: Apple 推出了 push notification console 推播通知控制台
date: 2023-10-22 11:03 +0800
category: swift
author: Marvin Lin
tags: [Apple, Swift, push notification, console]
summary: 使用 Apple 推播通知控制台，可以更方便的管理推播通知
permalink: /swift/:title:output_ext
---

最近在 X (前身為 Twitter) 上看到推文，說 Apple 推出了一個新的推播通知控制台，可以讓開發者們更方便的管理推播通知。我馬上就去看了一下，發現這個功能真的很方便，可以讓開發者們更方便的管理推播通知。現在的推播通知，通常都是透過 Firebase 來發動，在我個人的 app 上，Firebase 是很夠用的。但如果在公司的產品，就會想知道各種推播推發出去後，在客戶端的狀況。目前我還沒使用 Apple push notification console ，但之後會去試試看。

## Apple Push Notification Console 截圖

![Apple Push Notification Console](/assets/swift/apple-push-notification-console/apple-console1.png)

### 除了使用後台以外，也有提供 cURL 的方式，除了 token，也可以用 certificate 的方式
![Apple Push Notification Console](/assets/swift/apple-push-notification-console/apple-console2.png)

### payload 的客製化在這邊調整
![Apple Push Notification Console](/assets/swift/apple-push-notification-console/apple-console3.png)

### 也可以直接使用 json format
![Apple Push Notification Console](/assets/swift/apple-push-notification-console/apple-console4.png)