---
layout: single
title: 單元測試從0到1 - 讓專案開始有測試
date: 2024-06-20 13:20 +0800
category: unitTesting
author: Marvin Lin
tags: [Unit Testing, Swift, Xcode]
summary: This article provides an introduction to integrating unit testing into iOS projects, emphasizing its role in validating individual components like functions and classes for correctness. Marvin Lin, the author, advocates starting tests with independent components and utilizes a dependency graph to illustrate where to begin in a project. The guide includes steps for setting up a unit testing environment in Xcode and discusses practical examples, such as handling JSON responses for authentication. It further explores how unit testing can help manage evolving project requirements, highlighting its benefits and limitations. The article ultimately stresses that while unit testing is crucial for functionality verification, it does not inherently solve all aspects of software quality or design.
permalink: /unit-testing/:title:output_ext
---

在這篇文章中，我們將介紹如何在 iOS 專案中加入單元測試。單元測試用於驗證程式碼的最小可測單元（如函數、方法或類別）是否正確。單元測試通常由開發人員自行編寫和執行，並使用各種工具和框架來自動化和簡化測試過程。單元測試的目的是確保程式的邏輯正確性和健壯性，提高程式質量和可維護性。

**這篇文章要感謝 Hanyu Chen, 陳涵宇請我喝咖啡**

![buy me a coffee from Hanyu](/assets/buyMeCoffee/buy_me_a_coffe_hanyu.png)

## 測試從哪裡開始加？建議從沒有依賴其他物件的物件開始

下面的圖是專案物件依賴的示意圖，如果要寫測試，建議從沒有依賴其他物件的物件開始。

![專案物件依賴示意圖](/assets/unitTesting/from-zero-to-one/dependency_graph.png)

而最常被其他物件傳來傳去的，通常是 json response 相關的 dto，我們先假設有一道登入的 api，這道 API 會回傳你兩個 token，一個是 refresh token，另一個是 access token。

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODg4ODU1OSwiaWF0IjoxNzE4ODAyMTU5LCJqdGkiOiIzMDQyZDhlMGIzOTc0MjQyYTI0MDFhZDU0ZjRhMjAxOCIsInVzZXJfaWQiOjh9.45URkd4iyBx7mjeyB9yzQp5x3gICLYxo3laqtCNjyLE",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4ODg4NTU5LCJpYXQiOjE3MTg4MDIxNTksImp0aSI6IjJjYzM2ZDFkZTMzYjQ3OTliNWE3MzQ1Njc5NzFkMWE1IiwidXNlcl9pZCI6OH0.j7CLMRL0EUknJ_HxRLeWS0vCD1QMfcrSL9kYDCTug1o"
}
```

## 在現有的專案加上 Unit Testing 的步驟

在 Project targets 的頁籤，按下 + 號，選擇 Unit Testing Bundle，就可以讓專案開始有測試。

![add test bundle](/assets/unitTesting/from-zero-to-one/add_test_bundle.png)

### 預設的測試模板

加上檔案後，這預設的模版，你會看到兩個測試，以及 setup 和 tear down。
![Unit testing template](/assets/unitTesting/from-zero-to-one/unit_testing_template.png)

### 第一步，加上 @testable import

import XCTest 的上方，記得要 import 自已的專案，這樣才能讓 Unit testing target 來操作專案中的物件。
```swift
@testable import YourProjectName
```

## 測試 token model

### model 的實作
```swift
/// 這是拿來接 json response 的 model
struct TokenResponse: Codable {
    let refresh: String
    let access: String
}
```

### Unit testing 實作
```swift
@testable import StartUnitTesting
import XCTest

final class CocoaTests: XCTestCase {

    /// 將 json response 轉成 data, Unit testing 不會真的去 call api
    private func getAPIRespnose() -> Data {
        
        let string =
#"""
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODg4ODU1OSwiaWF0IjoxNzE4ODAyMTU5LCJqdGkiOiIzMDQyZDhlMGIzOTc0MjQyYTI0MDFhZDU0ZjRhMjAxOCIsInVzZXJfaWQiOjh9.45URkd4iyBx7mjeyB9yzQp5x3gICLYxo3laqtCNjyLE",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4ODg4NTU5LCJpYXQiOjE3MTg4MDIxNTksImp0aSI6IjJjYzM2ZDFkZTMzYjQ3OTliNWE3MzQ1Njc5NzFkMWE1IiwidXNlcl9pZCI6OH0.j7CLMRL0EUknJ_HxRLeWS0vCD1QMfcrSL9kYDCTug1o"
}
"""#
        
        return string.data(using: .utf8) ?? Data()
    }
}

```

第一步，先測試這段 unit testing 能不能在程式有錯的時候，提醒你，所以 XCTAssertEqual 的 equal 為空字串
```swift
    /// 測試 token response
    func testTokenResponse() throws {
        
        let data = getAPIRespnose()
        let model = try JSONDecoder().decode(TokenResponse.self, from: data)
        XCTAssertEqual(model.refresh, "")
        XCTAssertEqual(model.access, "")
    }
```

### 這時候，你會得到 failed test result，你會看到 Unit testing 告訴你哪個 model 的值是不對
![first test, you got error](/assets/unitTesting/from-zero-to-one/first_fail_test.png)

第二步，再將固定的 access token , refresh token 設為 equal 的值
```swift
func testTokenResponse() throws {
        
        let data = getAPIRespnose()
        
        let model = try JSONDecoder().decode(TokenResponse.self, from: data)
        XCTAssertEqual(model.refresh, "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODg4ODU1OSwiaWF0IjoxNzE4ODAyMTU5LCJqdGkiOiIzMDQyZDhlMGIzOTc0MjQyYTI0MDFhZDU0ZjRhMjAxOCIsInVzZXJfaWQiOjh9.45URkd4iyBx7mjeyB9yzQp5x3gICLYxo3laqtCNjyLE")
        XCTAssertEqual(model.access, "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4ODg4NTU5LCJpYXQiOjE3MTg4MDIxNTksImp0aSI6IjJjYzM2ZDFkZTMzYjQ3OTliNWE3MzQ1Njc5NzFkMWE1IiwidXNlcl9pZCI6OH0.j7CLMRL0EUknJ_HxRLeWS0vCD1QMfcrSL9kYDCTug1o")
    }
```

### 再跑一次 testing，讓 test 通過

![pass test](/assets/unitTesting/from-zero-to-one/second_test_pass.png)

## 另一個場景：需求變更 or 需求疊加

以下是某種情境假設，在「app 迭代的過程中，Unit testing 可以怎麼幫你」

- 你寫一個 app，裡面有個類別-使用者。
- 需要在某一個頁面，呈現後端儲存的資料，其中有 first name & last name
- 但前端顯示的時候，要組合起來，變成 firstName lastName

### Customer model
```swift
struct Customer {

    let firstName: String

    let lastName: String
    /// UI 顯示用的
    var displayName: String {

        return firstName + lastName
    }
}
```
## 需求開始疊加

App 推出後大賣，不過！歐美 sales 反應，他們的客戶有些有 middle name，而且被強烈要求在 UI 上呈現出 middle name。所以需要在 user 顯示名稱那邊，顯示 middle name。因為有一個成員剛進來

```swift
struct Customer {

    let firstName: String

    let lastName: String

    var middleName: String?

    var displayName: String {
        /// 因為這任務交給一個剛來的人寫，所以那個人就這樣寫了
        return firstName + middleName! + lastName
    }
}
```
## 沒有意外的話，就要發生意外了

新的使用者，可能都沒問題，但如果是舊版本的使用者升級到新版，原來的程式並沒有存下 middleName，因為那個時期這個 property 不存在，所以每個升級的使用者都遇到了 app 閃退的問題。
修復後，這個物件宣告長這樣。

```swift
struct Customer {

    let firstName: String

    let lastName: String

    var middleName: String?

    var displayName: String {

        /// 如果是有中間名的 user，就呈現中間名
        if let middleName = middleName {

            return firstName + middleName + lastName
        }

        /// 如果是沒有中間名的，就不處理 middle name
        return firstName + lastName
    }
}
```

## 你可以讓 Unit testing 來幫你
```swift

    func testCustomerDisplayName() {
        
        let customer = Customer(firstName: "Foo", lastName: "Bar")
        
        let answer = "FooBar"
        /// 第一次跑 unit testing，會讓 testing failed，來確保 unit testing 是正確運作的
        XCTAssertEqual(customer.displayName, answer)
    }
    
    func testCustomerDisplayNameHasMiddleName() {
        
        let customer = Customer(firstName: "Foo", lastName: "Bar", middleName: "MMM")
        
        let answer = "FooMMMBar"
        
        XCTAssertEqual(customer.displayName, answer)
    }
```

## 如果 App 成長的話，需求就會不斷疊加，但如果不成長的話....

然後再經過幾次行銷活動，這個 app 更紅了。某天你被叫進需求會議，接到了亞洲區 Sales 的需求。
- App 修改完後更大賣，但亞洲區 sales 反應，姓要在名字前面。且中間不要空格
這邊就省略程式碼，不斷的進行時間快轉。
下一個需求
- 日本 sales 反應。日本 UI 如果呈現姓加名字黏在一起，會讓特殊姓氏不知道怎麼念，而且日本人習慣姓和名中間空一格
下一個需求
- 馬來西亞 sales 反應，他們的中間名可能有五個起跳，但習慣上可能用不同於其他國家的方式進行呈現。所以需要先判斷 x 條件，然後符合 y 條件時，呈現 z UI。

上面所述的這個狀況，是會不斷的發生的。改需求，改文案，增加銷售地區，因為增加銷售地區所以增加了新的需求。當你手上的程式碼註定會碰到這樣的變化，Unit testing 真的可以幫你。

## Unit testing 是銀色子彈嗎？

- Q: Unit Test 可以幫助你設計嗎?
    - 不會, 因為你的程式碼並不會因為有 Test Case 就自己變得符合設計模式
- Q: Unit Tes 可以幫助提高程式碼品質嗎?
    - 不能，因為測試和品質也沒絕對關係，你在 test case 中沒有寫的東西，如果有可能導致 crash，他就會 crash
- Q: Unit Tes 可以改善使用者體驗嗎?
    - 不能，因為使用者體驗無法用程式測試
- Q: Unit Tes 可以做出酷炫的 App 嗎?
    - 不能，因為是否酷炫沒辦法用程式測試

## Cocoaheads Taipei Youtube 影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/KeQ0OkJnktk?si=hEhkbHM7hi60FaCT&amp;start=1283" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>