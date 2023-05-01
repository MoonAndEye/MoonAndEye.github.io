---
layout: single
title: iOS 的 MVC 架構
date: 2023-05-01 08:48 +0800
category: swift
author: Marvin Lin
tags: [Swift, MVC, Cocoa framework]
summary: Analyze iOS MVC design pattern. MVC is model-view-controller pattern. The main point is model should isolate with view. Nomatter is macOS app or iOS app. This article using books example - Cocoa design patterns as example.
permalink: /swift/:title:output_ext
classes: wide
---

MVC 是 Apple 範例框架，在 UIKit 的時代，這是個很重要的 pattern。最近有空的時間，都會花一點時間去看一本很久以前的書**Cocoa 設計模式**。

![Cocoa design pattern](/assets/swift/mvc-pattern/books-cover.jpeg){: width: "50%"}

## 書本第二章：MVC 分析與應用

![第二章：MVC 分析與應用](/assets/swift/mvc-pattern/mvc-chapter.jpeg)

Apple cocoa design pattern 的 MVC 架構是一種軟體開發的方法，它將應用程式分成三個部分：模型（Model）、視圖（View）和控制器（Controller）。這樣可以讓程式碼更容易維護和重用，也可以提高應用程式的效能和可測試性。

Model 是負責管理應用程式的資料和邏輯的部分，它不直接與使用者介面互動，而是通過控制器來更新或取得資料。模型可以是任何類型的物件，例如陣列、字典、檔案或網路服務。

View 是負責顯示應用程式的使用者介面的部分，它接收使用者的輸入和事件，並將其傳遞給控制器。視圖可以是任何類型的使用者介面元件，例如按鈕、標籤、圖片或表格。

Controller 是負責協調模型和視圖的部分，它是應用程式的主要邏輯層。控制器可以接收來自視圖的輸入和事件，並根據其執行相應的動作，例如更新模型或改變視圖。控制器也可以與其他控制器溝通，以實現更複雜的功能。

### 書中以薪水計算器為例

在一個薪水計算器中，Model 是 Employee。calculator，在發動 `calculatePayAmount(:)` 後，要將員工的薪水算出來。如果一個程式沒有依 MVC 的功能切開，那呼叫關係就像下面這張圖。注意的是，即使一個程式沒有 MVC，仍然能夠運作正常，第一版也可以正常運作，但問題會是在之後的擴充。

![project not follow mvc design](/assets/swift/mvc-pattern/non-mvc.jpeg)

如果要讓 Model 和 View 切開，中間就會有個 Controller 的角色，讓 View 不會和 Model 耦合。在一個不斷增加 features 的專案上，常常會有這樣的情形。

### V1.1 (非真實情況，但有可能發生)
- UI 要加圓角、加漸層、加陰影
- UX 希望如果輸入框為空值時，自動
- 搜尋欄希望有自動完成提示

### V1.2 (非真實情況，但有可能發生)
- 每個分公司所在地的假日是不一樣的，希望擴增員工聘僱合約是依哪一地區的欄位
- 擴增 intern 這個職位，計薪方式和正職不同，且每個地區的 intern 計薪也可能不同
- 匯率換算，並希望設定一更改，欄位的 UI 也顯示對應的匯率符號 (當然貨幣的換算也要正確的數字，精確到小數點第3位)

上面兩個追加的 features 追加時，只要動到 view ，就會有可能動到 model，反向時，動到 model 也會動到 view。這樣的設計很容易會在開發時出現很難察覺的 bug。Apple 建議，在開發的時候，導入 mvc pattern，在 model 和 view 中間上一個 controller 的角色，就像下面這張圖一樣。

![project follow mvc pattern](/assets/swift/mvc-pattern/mvc.jpeg)

因為 cocoa design patterns 是很久以前就出版的書，書中並沒有 iOS 的範例，不過 iOS 的 UIKit 是 macOS 的子集，這一點在另一本書 **創意競澤** 中有提到。所以 iOS 開發當然也適用這個 pattern。以下使用 Stanford 193 p 中的圖案，來表示 iOS 的 MVC。

![mvc pattern in iOS](/assets/swift/mvc-pattern/mvc-ios.jpg)

## 在 iOS App 中，View 接觸到 Model 的狀況

```swift
/// 在 UI 上呈現 Employee 資料 UI 的 tableViewCell，是 MVC 的 View
class FooTableViewCell: UITableViewCell {
    /// Employee 是裝載資料的物件，是 MVC 的 Model
    /// 在 View 物件裡面處理 Model，程式的確會運作，也可能運作正常，但這並不符合 MVC pattern
    func setup(_ employee: Employee) {
        // 省略實作
    }
}
```

建議不要在專案中，讓 View 和 Model 耦合在一起，儘可能讓 View 單純呈現資料，讓 Model 描述資料，然後透過 Controller (或是其他不是 View 的物件)進行組裝。除了 MVC pattern 之外，MV(X) 家族已經開枝散葉，在 Githup 上可以找到很多的範例，來完成你的需求。

## 參考網站

[Nelson 對 iOS 架構的說明](https://chiahsien.github.io/post/common-ios-architecture-from-mvc-to-viper-with-redux/)

[Kodeco 對 MVC 的介紹](https://www.kodeco.com/1000705-model-view-controller-mvc-in-ios-a-modern-approach)

[唯一可行的 iOS 架構(MVC)](https://medium.com/@iamirzhan/the-only-viable-ios-architecture-c42f7b4c845d)

[iOS 的架構(MVC, MVP, MVVM, Viper)](https://medium.com/ios-os-x-development/ios-architecture-patterns-ecba4c38de52)
