---
layout: post
title: Charts 的 4049 & 4132 issue
date: 2023-03-19 12:30 +0800
category: swift
author: Marvin Lin
tags: [Swift, Charts]
summary: 
---

# 這是草稿

## 要寫一篇 Charts 套件，遇到的 issue，主要是 iteration 遇到問題，最大和最小在 debug mode 下正常，但一切到 release mode ，就會發生閃退

Charts 是 iOS 專案開發中很常使用的圖表繪制套件，不過今年，我在專案上遇到了很奇怪的狀況，在 Firebase Crashlytics 的 Dashboard 上，一直有零星的閃退，這閃退是發生在使用 Charts 套件的 renderer 裡面。而且在 release 給 QA 時，也會在 iPhone 關電源的狀況下，經過長時間後再開啟，就會閃退的狀況。





