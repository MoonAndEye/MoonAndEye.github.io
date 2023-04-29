---
layout: single
title: 
date: 2023-04-31 11:48 +0800
category: swift
author: Marvin Lin
tags: [Swift, MVC, Cocoa framework]
summary: 
permalink: /swift/:title:output_ext
classes: wide
---

## 草稿 寫一篇關於 mvc 架構的文章，從 cocoa deesign patterns 開始

> It's looks ugly, but it's beautiful language - 已經找不到這是誰講的

MVC 是 Apple 範例框架，在 UIKit 的時代，這是個很重要的 pattern。最近有空的時間，都會花一點時間去看一本很久以前的書 **Cocoa 設計模式**。

![Cocoa design pattern](/assets/swift/mvc-pattern/books-cover.jpeg){: width: "50%"}

## 書本第二章：MVC 分析與應用

![第二章：MVC 分析與應用](/assets/swift/mvc-pattern/mvc-chapter.jpeg)

Apple cocoa design pattern 的 MVC 架構是一種軟體開發的方法，它將應用程式分成三個部分：模型（Model）、視圖（View）和控制器（Controller）。這樣可以讓程式碼更容易維護和重用，也可以提高應用程式的效能和可測試性。

Model 是負責管理應用程式的資料和邏輯的部分，它不直接與使用者介面互動，而是通過控制器來更新或取得資料。模型可以是任何類型的物件，例如陣列、字典、檔案或網路服務。

View 是負責顯示應用程式的使用者介面的部分，它接收使用者的輸入和事件，並將其傳遞給控制器。視圖可以是任何類型的使用者介面元件，例如按鈕、標籤、圖片或表格。

Controller 是負責協調模型和視圖的部分，它是應用程式的主要邏輯層。控制器可以接收來自視圖的輸入和事件，並根據其執行相應的動作，例如更新模型或改變視圖。控制器也可以與其他控制器溝通，以實現更複雜的功能。

### 書中以薪水計算器為例

## 在 iOS App 中，View 接觸到 Model 的狀況

```swift


```

## 參考網站

[Nelson 對 iOS 架構的說明](https://chiahsien.github.io/post/common-ios-architecture-from-mvc-to-viper-with-redux/)

