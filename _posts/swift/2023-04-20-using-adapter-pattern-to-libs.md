---
layout: single
title: 將第三方 lib 包起來，減少升級 lib 的痛苦
date: 2023-04-22 00:01 +0800
category: swift
author: Marvin Lin
tags: [Swift, 設計模式]
summary: 
permalink: /swift/:title:output_ext
classes: wide
author_profile: false
---

現在的 iOS 開發，通常會用到第三方 libs。而隨著每年的 Swift 改版, Xcode 改版, 語法改變，libs 也會升版。下方是 Alamofire 和 Charts 進一年來的版號升級趨勢，libs 是會升級的。依照 [語意化版本的說明](https://semver.org/lang/zh-TW/) 如果動到大版號，是不太可能一行都不改，然後專案可以 build 成功的。有時候升級到中版號的 libs，也會出現意料之外的情形。

假設你使用的第三方 lib 會散落在專案裡面幾十個地方，那升級時要改動處就會在幾十處。隨著版號跳的愈大，或是散落的數量不斷的上升，會不斷的增加 lib 升級的風險。

![Alamofire tags list](/assets/swift/adapter-pattern/Alamofire-tags.jpeg){:width=50%}

![Charts tags list](/assets/swift/adapter-pattern/Charts-tags.jpeg){:width=50%}

## 減少依賴的 libs 因為升級而痛苦的方法 - 把 libs 包起來

在使用 libs 時，先思考界面會使用的參數，這邊先用最常見的紀錄事件的 lib 為例子。Google Firebase 服務的 FirebaseAnalytics 紀錄需要這兩個參數。

- 參數名: String
- 參數字典: [String: Any]?

那這兩個參數，通常會設定為 Adapter func 中的 arguments。

### 第一版，只使用了 FirebaseAnalytics

```swift
import Foundation
import FirebaseAnalytics

/// 將分析相關模組包住的物件，只有這個檔案會 import 分析相關模組
struct AnalyticsAdapter {
    
    /// 紀錄分析事件的 func，在要紀錄時，發動的是這個 func，接口參數會參考被包住的 lib 接口參數
    func logEvent(name: String, parameters: [String: Any]?) {
        
        Analytics.logEvent(name, parameters: parameters)
    }
}
```

### 第二版 除了 Google Analytics 以外，還要再加上 Flurry

```swift
/// 將分析相關模組包住的物件，只有這個檔案會 import 分析相關模組
struct AnalyticsAdapter {
    
    /// 紀錄分析事件的 func，在要紀錄時，發動的是這個 func，接口參數會參考被包住的 lib 接口參數
    func logEvent(name: String, parameters: [String: Any]?) {
        /// 第一版時就存在的 Google Analytics
        Analytics.logEvent(name, parameters: parameters)
        /// 在第二版加上去的追蹤 lib
        Flurry.log(eventName: name, parameters: parameters)
    }
}
```

### Adapter 在專案中用起來的圖，大概的樣子

在專案中，如果是 VCs 或是 Models 需要用到第三方 libs 的功能，就會透過 adapter 類別去呼叫，VCs 不會碰到第三方，會碰到第三方 lib 的，在這個架構下，只有 adapter 物件會碰到第三方 lib。用起來的樣子，就像下面這個圖

![Adapter 在專案中用起來的樣子](/assets/swift/adapter-pattern/AdaptersDiagram.jpeg)

## 範例 - 使用 Alamofire

```swift
import Foundation
import Alamofire

/// 轉接 Alamofire 的物件，專門處理 URLRequest
struct AlamofireAdapter {
    
    /// 將 request 送出，並先定義好可解開的 Decodable 物件，在完成後回傳 (Result<T: Decodable, Error>)
    func sendRequestDecodable<T: Decodable>(_ request: URLRequest, completion: @escaping ((Result<T, Error>) -> Void)) {
        
        /// 如果 Alamofire 升級到大版號 6 的時候，這邊的實作會修改
        AF.request(request)
            .validate(statusCode: 200..<300)
            .responseDecodable { (dataResponse: DataResponse<T, AFError>) in
                
                switch dataResponse.result {
                    case .success(let decodableObj):
                        completion(.success(decodableObj))
                    case .failure(let error):
                        completion(.failure(error))
                }
            }
    }
}
```

## 範例 - 使用圖片快取套件

```swift
//
//  ImageCacheAdapter.swift
//  ChatGPT
//
//  Created by cm0679 on 2023/4/22.
//

import UIKit
import Kingfisher

/// 專門處理 ImageView 與網路圖片資源交互作用的物件
struct ImageCacheAdapter {
    
    /// 接口為: UIImageView, URL, 與 placheHolder。placholder 預設為 nil
    /// 當 tableViewCell 中的 imageView 在 cellForRowAt 時將 imageView 傳入
    func downloadAndCache(imageView: UIImageView, with url: URL, placeHolder: UIImage?) {
        
        /// 如果想把 Kingfisher 改成 sd_webImage，將下列實作換掉即可
        imageView.kf.setImage(
            with: url,
            placeholder: placeHolder) { result in
                
            switch result {
            case .success(let value):
                print("Task done for: \(value.source.url?.absoluteString ?? "")")
            case .failure(let error):
                print("Job failed: \(error.localizedDescription)")
            }
        }
    }
}

```

## 使用 protocol 的方式進行 Adapter

如果去網路上找 Adapter pattern 的文章，會有一種先寫 protocol 的範例出來，如果是用前面的 URLRequest 為例的話，風格會是這樣。先寫一個 protocol，並將 func 定義好。然後在前述所用的轉接 Alamofire 的 Adapter 物件，讓該物件 conform URLRequest protocol，並在 func 中完成實作。

```swift
import Foundation
import Alamofire

protocol URLRequestAdapter {
    /// 將 request 送出，並先定義好可解開的 Decodable 物件，在完成後回傳 (Result<T: Decodable, Error>)
    func sendRequestDecodable<T: Decodable>(_ request: URLRequest, completion: @escaping ((Result<T, Error>) -> Void))
}

/// 轉接 Alamofire 的物件，專門處理 URLRequest
struct AlamofireAdapter: URLRequestAdapter {
    
    /// 將 request 送出，並先定義好可解開的 Decodable 物件，在完成後回傳 (Result<T: Decodable, Error>)
    func sendRequestDecodable<T: Decodable>(_ request: URLRequest, completion: @escaping ((Result<T, Error>) -> Void)) {
        
        /// 如果 Alamofire 升級到大版號 6 的時候，這邊的實作會修改
        AF.request(request)
            .validate(statusCode: 200..<300)
            .responseDecodable { (dataResponse: DataResponse<T, AFError>) in
                
                switch dataResponse.result {
                    case .success(let decodableObj):
                        completion(.success(decodableObj))
                    case .failure(let error):
                        completion(.failure(error))
                }
            }
    }
}
```

在應用的時候，這裡用 `FooModel` 為例，`FooModel` 只會看到 URLRequestAdapter protocol，但在 init 的時候，將這個物件用 `AlamofireAdapter` 進行 init()。實際上使用的狀況，可能會像下面的 `FooModel` 一樣。

```swift
class FooModel {
    
    let urlRequestAdapter: URLRequestAdapter
    
    init(urlRequestAdapter: URLRequestAdapter) {
        self.urlRequestAdapter = AlamofireAdapter()
    }
    
    func requestSomething() {
        
        guard let url = URL(string: "foo_url") else {
            return
        }
        
        let someRequest = URLRequest(url: url)
        urlRequestAdapter.sendRequestDecodable(someRequest) { (response: (Result<String, Error>)) in
            
            print("response: \(response)")
        }
    }
}
```

雖然這樣寫，會需要多宣告一個 protocol，好像不多宣告這個 protocol，你也可以達成一樣的事情，但這是有故事的。這種先寫一個稱之為「界面」的程式碼，然後再寫出一個物件去繼承這個界面，在其他語言中是非常常見的事情。當然和其他語言比起來，Swift 是相對較年輕的語言，直接套用前人的模式是很合理也很合邏輯的。此外，如果你的程式碼並不是包成 app release 出去，這種先寫界面，再寫物件繼承的手法，在進行整個 SDK 抽換的時候，是很有用的。舉例來說：支付 SDK 從 信用卡支付 改到 Apple Pay。或是第三方登入從 Facebook 登入改到 Github 登入，在這個模式上都是可以達到的。

### 不過在 mobile APP 開發中呢?

那如果很確定你手上的專案就是 iOS App，很確定套件就是用最大宗，星星數最多，folks 最多，還有沒有一定要先寫 protocol 再寫物件 conform protocol?

我．沒．有．答．案

但思考的方法可以從這幾個點出發

- 這個專案是個人 side project？ 還是公司重要專案？ 還是公司實驗專案？
- 這個 feature 的套件是不是只有少數幾個獨大？
- 這個專案怎麼決定專案使用第三方 libs 的方針？

最重要的當然是「專案團隊」的共識，如果專案人數只有 1，那共識當然是 1 個人決定，但當專案成員是複數的時候，優先思考的反而會是，這個專案怎麼決定第三方 libs。在怎麼「使用 libs 的共識」的更上一層，是有個「團隊開發溝通」這一層要先思考的。

## 參考資料

[語意化版本說明](https://semver.org/lang/zh-TW/)

[Refactoring Guru 的 Adapter pattern Swift Sample](https://refactoring.guru/design-patterns/adapter/swift/example#example-1)