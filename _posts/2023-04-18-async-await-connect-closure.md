---
layout: single
title: 使用 async/await 串接 escaping closure
date: 2023-04-18 13:22 +0800
category: swift
author: Marvin Lin
tags: [Swift, Combine, 非同步]
summary: After Swift 5.5, swift introduced async/await. This article have an example to connect previous escaping closure func.
permalink: /swift/:title:output_ext
---

## 使用 swift combine 串接 closure 的方法

如果一個專案是從 Swift 還沒有 combine 的時代就開始進行，那專案中會有大量的 @escaping closure 在做非同步的資料傳遞。在 Swift 5.5 之後，Swift 加進了 async/await 的語法，讓需要進行非同步的任務，不再需要在撰寫的時候有一堆的大括號。

所以

現在會有一個新的情境，以前的 lib 已經寫好 URLRequest 的方法，並使用 closure 進行傳值。把已經寫好的 escaping closure 全部改寫意義可能不大，而且也伴隨著一定程度的風險。因此，能另外寫一個 func 進行 async/await 轉接，並保留原來的 closure，是一個風險較低的選項。

## 包一層 async func 的方法

### 原來發送 request 的類別

```swift

// 將 Alamofire 包起來的 Adapter，每個 func 只是使用 Alamofire 發送 URL Request
class AlamofireAdapter {
    
    // 原來的 closure func
    func getCoinMarketsInfo(coutPerPage: Int, page: Int, sparkLine: Bool = false, completion: @escaping (Result<[CoinMarketInfoElement], Error>) -> Void) {
        // 省略實作 implement code omitted
        
        // implemented code omitted
        completion(result)
    }
}
```

### 擴充 request 到 async/await 

```swift
// 對 AlamofireAdapter 進行擴充
extension AlamofireAdapter {
    // 開出能使用 await 的 func，但實際上是呼叫原來的 getCoinMarketsInfo
    func getCoinList(countPerPage: Int, page: Int) async -> Result<[CoinMarketInfoElement], Error> {
        
        // 進行轉接
        return await withCheckedContinuation { continuation in
            
            alamofireAdapter.getCoinMarketsInfo(coutPerPage: countPerPage, page: page, sparkLine: true) { result in
                continuation.resume(returning: result)
            }
        }
    }
}
```

使用 `withCheckedContinuation()` 就可以將以前的 closure 資料，使用 `continuation` 進行 async return。

### ContentView 使用 getCoinList()

```swift

func fechList() {
        
        Task {
            let result = await manager.getCoinList()
            switch result {
                case .success(let list):
                    
                    DispatchQueue.main.async { [weak self] in
                        self?.updateLastFetchTime()
                        self?.cryptoList = list
                    }
                    Logger.log("you got list, count: \(list.count), first: \(String(describing: list.first))")
                case .failure(let failure):
                    Logger.log("fetch market got error: \(failure), description: \(failure.localizedDescription)")
            }
        }
    }
```

### 使用在 SwiftUI 的 View 時

```swift
# 在 SwiftUI 上使用時

import SwiftUI

struct ContentView: View {
    
    private let alamofireAdapter: AlamofireAdapter = .init()
    
    @State var cryptoList: [CoinMarketInfoElement] = []
    
    var body: some View {
        
        Text("this is test")
            .task {
                fetchList()
            }
    }
    
    private func fetchList() {
        let result = await alamofireAdapter.getCoinList()
        switch result {
            case .success(let list):
                
                DispatchQueue.main.async { [self] in
                    self.cryptoList = list
                }
            case .failure(let failure):
                print("fetch market got error: \(failure), description: \(failure.localizedDescription)")
    }
}

```

## 結尾

請注意 async/await 還是需要專案最低支援在 iOS 13 以上，如果你的專案沒辦法低於 iOS 13，那還是沒辦法使用 async/await。

在我個人的 side project 上，我已經試著使用 SwiftUI 寫一些小專案，在使用 async/await 後，很多非同步的 feature 處理的程式碼，在人類眼中非常好讀。或許在 Apple 不斷的推進 Xcdoe 最低上架版本後，我會不斷的增加 async/await 程式碼的比重。目前，在專案上我仍然有很多 closure 在進行傳值。

## 相關資料

[Swift evolution on continuation](https://github.com/apple/swift-evolution/blob/main/proposals/0300-continuation.md)

[WWDC21: - Meet async/await in Swift](https://developer.apple.com/videos/play/wwdc2021/10132/)

[swift.org - Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)

[Hacking With Swift 的文章](https://www.hackingwithswift.com/swift/5.5/continuations)

[Apple 開發者論壇的討論](https://developer.apple.com/forums/thread/681980)

[在 Swift 論壇上對向前支援非常激烈的討論](https://forums.swift.org/t/will-swift-concurrency-deploy-back-to-older-oss/49370)

[Swift Concurrency 向下支援的文章](https://www.swiftbysundell.com/special/swift-concurrency-backward-compatibility/)

