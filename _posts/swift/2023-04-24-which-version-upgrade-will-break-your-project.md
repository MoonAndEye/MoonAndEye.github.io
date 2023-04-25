---
layout: single
title: 當升級第三方版本時，什麼樣的版號會讓專案 build 失數?
date: 2023-04-24 20:58 +0800
category: swift
author: Marvin Lin
tags: [Swift, third party, cocoapods]
summary: Explain semantic version in development. In semantic version control, we have major, minor, patch version. Each change has their own meaning. Patch is for bug fix, minor is compatibal update. Major weill break your code. This article also give your example.
permalink: /swift/:title:output_ext
---

在 iOS 開發中，我們常常會使用第三方套件來增加功能或減少工作量。但是，如果我們直接下載套件的原始碼，或者使用 git submodule 的方式，我們可能會遇到一些問題，例如版本不一致、相依性不清楚、更新不方便等等。為了解決這些問題，我們可以使用 cocoapods 這個工具來協助管理第三方套件。

cocoapods 是一個用 Ruby 寫的開源專案，它可以幫助我們自動化安裝和更新第三方套件，並且處理好相依性的問題。使用 cocoapods 的好處有以下幾點：

- 我們只需要在一個檔案中（Podfile）指定我們要使用的套件和版本，cocoapods 就會自動下載和安裝所需的套件。
- 我們可以方便地查看和管理我們的專案中使用了哪些套件，以及它們的相依性和版本。
- 我們可以輕鬆地更新套件，只需要在 Podfile 中修改版本號，然後執行 pod update 命令，cocoapods 就會自動更新套件和相依性。
- 我們可以使用 cocoapods 的搜尋功能，找到適合我們需求的套件，或者瀏覽 cocoapods 的官方網站（https://cocoapods.org/），看看有哪些熱門或新出的套件。

## 升級 lib 時，升到什麼程度，程式碼高機率是無法直接 build 起來的?

當你在下 `pod install` 或是 `pod update` 時, terminal 會跳出現在正在安裝的 pod，以及升級前的版號。

如果看到下面的文字

```ruby
Installing Alamofire 5.6.4 (was 5.6.2)
```

表示你的專案從 Alamofire 5.6.2 升級到 5.6.4

而這個 `5.6.2` 升級到 `5.6.4` 會不會直接讓你的專案 build 不過，是看 lib 有沒有照「語意化版本」

## 語意化版本

[語意化版本](https://semver.org/lang/zh-TW/) 連結，語意化版本採用以下格式：MAJOR.MINOR.PATCH，其中：

- MAJOR：主版本號，表示非向下相容的改變。當進行重大改版或有重大的破壞性改變時，應該增加主版本號。例如，從 1.0.0 到 2.0.0。
- MINOR：次版本號，表示向下相容的新功能。當新增了一些功能，但是不會影響現有功能的使用，應該增加次版本號。例如，從 1.0.0 到 1.1.0。
- PATCH：修補版本號，表示向下相容的錯誤修復。當修復了一些錯誤，但是不影響現有功能的使用，應該增加修補版本號。例如，從 1.0.0 到 1.0.1。

語意化版本的目的是為了讓開發者和使用者更好地理解軟體版本號的意義，方便版本控制和升級管理。它強調了版本號的主次要區分，讓使用者知道版本號的變化對他們的應用是否有影響。此外，語意化版本也強調了版本號的相容性，讓開發者和使用者更容易判斷版本間的相容性，以便更好地進行升級和更新管理。

### PATCH 案例

以一個取商數的功能為例
```swift
/// 1.0.0 單純取商數
func getDividedNumber(number: Int, divisor: Int) -> Int {
    return number / divisor
}
```

但如果 divisor 為 0，會 crash，所以在擋掉 0 以後，依照語意化版本的規則，這是讓 PATCH version 加 1。

```swift
/// 1.0.1 的時候，排除 divsor 為 0 的狀況
func getDividedNumber(number: Int, divisor: Int) -> Int? {
    if divisor == 0 {
        return nil
    }
    return number / divisor
} 
```

### MINOR version 案例

假設我們寫了一個會朝某個方向前進的物件，方向只有「東南西北」，範例程式碼如下

```swift
/// 1.0.1 版，
enum Direction {
    case east
    case west
    case south
    case north
}

func move(toward direction: Direction, path: Int) {
    /// 實作省略
}
```

但增加了需求，如果增加了物件在移動完後，過三秒要回到原位的需求。

```swift
/// 1.1.0 版，加上
func move(toward direction: Direction, path: Int) {
    /// 1.0.1 的實作
    /// 實作省略
}

/// 1.1.0 新需求 - 物件在移動完後，過三秒要回到原位的需求。
func backToStartPointAfter3Sec(toward direction: Direction, path: Int) {
    /// 1.1.0 的實作
    /// 實作省略
}
```

### Major version 案例，以 Alamofire 為例，因為大版號 4 和 5 有很大的差異

在 Alamofire 大版號 4 的時候，

```swift
let urlString = "https://httpbin.org/get"

Alamofire.request(urlString, method: .post, parameters: ["foo": "bar"],encoding: JSONEncoding.default, headers: nil).responseJSON {  
response in
  switch response.result {
                case .success:
                    print(response)

                    break
                case .failure(let error):

                    print(error)
                }
}

```

但 Alamofire 大版號 5

```swift
let url = "https://httpbin.org/get"

AF.request(URL(string: url)!, method: .post, parameters: parameters, encoding: JSONEncoding.default, headers: headers).responseJSON { (response) in
        print(response.result)

        switch response.result {

        case .success(_):
            if let json = response.value
            {
                successHandler((json as! [String:AnyObject]))
            }
            break
        case .failure(let error):
            failureHandler([error as Error])
            break
        }
    }
```

從上面這兩段程式碼來看，Alamofire 在 4 和 5 的版本，是不可能一行程式碼都不改，就能運作的。而對於減少升版本的痛苦，這邊有一篇 [將第三方 lib 包起來，減少升級 lib 的痛苦](https://moonandeye.github.io/swift/using-adapter-pattern-to-libs.html) 可以參考。

## podfile 中，在 pod 後面版本的差別

如果不寫後面的版號，那就會使用最新的版本
```
pod 'Alamofire'
```
<hr>

指定 5.0.0 的版本
```
pod 'Alamofire', '5.0.0'
```
<hr>

指定比 5.0.0 大的版本，可以使用的運算符號還有 <=, <, > 可以使用。 
```
pod 'Alamofire', '>= 5.0.0'
```
<hr>

指定 5.0.0 以上，但低於 5.1.0。如果把後面改成 `~> 5.0`，那版本就是 5.0 以上，但低於 6.0
```
pod 'Alamofire', '~> 5.0.0`
```

## 參考文章

[將第三方 lib 包起來，減少升級 lib 的痛苦](https://moonandeye.github.io/swift/using-adapter-pattern-to-libs.html)

[語意化版本](https://semver.org/lang/zh-TW/)

[Alamofire 5 migration 守則](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Alamofire%205.0%20Migration%20Guide.md)