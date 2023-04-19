---
layout: single
title: Swift 中的 Value type 和 Reference type
date: 2023-04-19 11:42 +0800
category: swift
author: Marvin Lin
tags: [Swift]
summary: Swift designed array, dict is value types. When you using array and copied it, it might have different behavior than you think. This article also include the swift.org and swift blog.
permalink: /swift/:title:output_ext
---

在我以前的文章 [Prototype Pattern (原型模式) in Swift (Reference type vs. Value type 的不同)](https://moonandeye.github.io/swift/2018/06/09/prototype-patter.html) 中，已經有提到 Referce type 和 value type 在修改上的差別。但那一篇是來自於 Swift 的 Design Pattern 一書中，Prototype pattern 的延伸。這邊想再寫一篇 Value type 和 Reference type 的文章。

### Reference Type 

class 是 reference types。Swift 5.5 以後的 actor 也是 reference type。

### Value Type

struct 宣告的物件, enum, tuple, Dict, Array 都是 value types。

## 在 Swift 語言中，將 value type 設計為主要結構的原因

我目前查到最早的文章，是在 Swift 還在發展的時候寫的 blog。文章連結在下面，發文日期為 2014 年 8 月 15 日。

[Value and Reference Types - Swift 部落格](https://developer.apple.com/swift/blog/?id=10)

在後面幾段中有提到 **The Role of Mutation in Safety「變異在安全性中的作用」**

> 選擇值類型而不是引用類型的主要原因之一是能夠更輕鬆地理解程式碼。如果您始終獲得獨立的複製實例，您可以信任應用程序的其他部分不會在幕後更改數據。這在多線程環境中特別有用，其中不同的線程可能會在您之下更改數據。這可能會產生非常難以調試的嚴重錯誤。

> 由於差異是以修改數據時發生的情況來定義的，因此有一種情況是值型和引用型重疊的：當實例沒有可寫數據時。在沒有變異的情況下，值和引用的行為完全相同。你可能會想到一種情況，即完全不可變的類別可能是有價值的。

> 在 Swift 中，Array、String 和 Dictionary 都是值類型。它們的行為非常像 C 中的簡單 int 值，作為該數據的唯一實例。你不需要做任何特殊的事情——比如進行顯式複製——來防止其他代碼在背後修改該數據。重要的是，你可以安全地在線程之間傳遞值的副本而不需要同步。為了提高安全性，這種模型將幫助你在 Swift 中編寫更可預測的代碼。

## Swift 的 Array 是 value type，那這些操作，會更改什麼？

```swift
/// 忍者龜的宣告，注意! 這邊用 reference type class
class NinjaTurtle {
    
    var name: String = ""
}

// 先初始化一隻忍者龜，並命名為達文西
let turtle1 = NinjaTurtle()
turtle1.name = "達文西"

// 再初始化一隻忍者龜，並命名為米開朗基羅
let turtle2 = NinjaTurtle()
turtle1.name = "米開朗基羅"

/// 兩隻忍者龜裝進同一個 array 裡面
var turtles = [turtle1, turtle2]

/// 因為 array 是 value type，所以這個賦值是 copy
var copiedTurtles = turtles

/// 我們把原來 array 的烏龜拿出來，並命名為 拉斐爾
turtles[0].name = "拉斐爾"

/// 請問，複製的 array 裡面，第 0 隻烏龜的名字，是 拉斐爾 還是 達文西
print(copiedTurtles[0].name)

```

上面這段程式碼，建議自己跑過一遍，然後去驗證自己的想法。

如果會碰到其他語言的話，也可以把相同的邏輯，試著去跑在 Kotlin, Python, Java, C#, Rust 上，看看是一樣？還是不一樣？

## 在什麼場景下，要選擇哪個 type？

### 以下場景，適合用 value type

- 比較兩個物件時，用 `==` 比較合理
- 當你在複製時，複製後的物件和複製前的物件彼此狀態應該是獨立時
- data 會在多個執行緒下被操作時

### 以下場景，適合用 reference type (class)

- 比較兩個物件時，用 `===` 比較合理
- 需求使用會被共享且變更的狀態時

## 相關連結

[Prototype Pattern (原型模式) in Swift (Reference type vs. Value type 的不同)](https://moonandeye.github.io/swift/2018/06/09/prototype-patter.html)

[Value and Reference Types - Swift 部落格](https://developer.apple.com/swift/blog/?id=10)

[Structures and Clases - swif.org](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/classesandstructures/)
