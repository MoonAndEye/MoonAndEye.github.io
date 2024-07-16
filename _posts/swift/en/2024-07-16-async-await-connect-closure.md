---
layout: single
title: Integrating Escaping Closure with async/await in SwiftUI Projects
date: 2024-07-16 21:42 +0800
category: swift
author: Marvin Lin
tags: [Swift, Combine, Asynchronous]
lang: en
summary: After Swift 5.5 introduced async/await, this article provides an example of connecting previous escaping closure functions.
---

## Method of Integrating Closure with swift async/await

If a project started before Swift had Combine, it would have a lot of @escaping closures for asynchronous data transfer. After Swift 5.5, Swift added the async/await syntax, making it unnecessary to have numerous curly braces when writing asynchronous tasks.

However, there's a new scenario where the previous libraries were already written with URLRequest methods using closures. Rewriting all existing escaping closures might not be significant and could also involve some risks. Therefore, writing an additional function to bridge async/await while retaining the original closures is a less risky option.

## Wrapping an async function

### Original class for sending requests

```swift
// Adapter that wraps Alamofire, each function simply uses Alamofire to send URL Request
class AlamofireAdapter {
    
    // The original closure function
    func getCoinMarketsInfo(coutPerPage: Int, page: Int, sparkLine: Bool = false, completion: @escaping (Result<[CoinMarketInfoElement], Error>) -> Void) {
        // Implementation code omitted
        
        // implemented code omitted
        completion(result)
    }
}
```

### Extending request to async/await

```swift
// Extending AlamofireAdapter
extension AlamofireAdapter {
    // Creating a function that can use await, but actually calls the original getCoinMarketsInfo
    func getCoinList(countPerPage: Int, page: Int) async -> Result<[CoinMarketInfoElement], Error> {
        
        // Performing the bridge
        return await withCheckedContinuation { continuation in
            
            alamofireAdapter.getCoinMarketsInfo(coutPerPage: countPerPage, page: page, sparkLine: true) { result in
                continuation.resume(returning: result)
            }
        }
    }
}
```

Using `withCheckedContinuation()` allows previous closure data to be returned asynchronously using `continuation`.

### Using getCoinList() in ContentView

```swift
func fetchList() {
        
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

### When used in a SwiftUI View

```swift
# When used in SwiftUI

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

## Conclusion

Please note that async/await still requires the project to support at least iOS 13. If your project can't support below iOS 13, then you won't be able to use async/await.

In my personal side projects, I've been trying to write small projects using SwiftUI, and after using async/await, the code for handling many asynchronous features is very readable to humans. Perhaps as Apple continues to push the minimum Xcode version, I will gradually increase the proportion of async/await code. Currently, I still have many closures performing data transfer in the project.

## Related Information

[Swift evolution on continuation](https://github.com/apple/swift-evolution/blob/main/proposals/0300-continuation.md)

[WWDC21: - Meet async/await in Swift](https://developer.apple.com/videos/play/wwdc2021/10132/)

[swift.org - Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)

[Article from Hacking With Swift](https://www.hackingwithswift.com/swift/5.5/continuations)

[Discussion on Apple Developer Forums](https://developer.apple.com/forums/thread/681980)

[Intense discussion on Swift Forums about backward support](https://forums.swift.org/t/will-swift-concurrency-deploy-back-to-older-oss/49370)

[Article on backward support for Swift Concurrency](https://www.swiftbysundell.com/special/swift-concurrency-backward-compatibility/)
