---
layout: single
title: 使用 DispatchWorkItem 設定特定時間的 API 任務
date: 2024-09-22 17:00 +0800
category: swift
author: Marvin Lin
tags: [Xcode, Swift]
summary: how to use DispatchWorkItem to implement a 5-second timeout for an API task in Swift. By using DispatchWorkItem alongside DispatchQueue.asyncAfter, it ensures a clean and efficient timeout mechanism, avoiding the need to modify other API calls. The article highlights the advantages of DispatchWorkItem over using simple flags, such as better code structure, built-in cancellation, precise time control, and efficient resource management. A Swift code example is provided to implement this feature for a real-time inventory check API in an e-commerce app.
---

情境假設: 你正在開發一個電子商務的 iOS 應用。這個應用有多個功能，包括瀏覽商品、添加到購物車、查看庫存、下單等。其中，實時庫存查詢功能特別關鍵，因為它直接影響用戶的購買決策和體驗。

## 特殊需求：
在這個應用中，大多數 API 請求都使用標準的網絡超時設置（比如 30 秒或 60 秒）。但是，庫存查詢 API 有一個特殊要求：
1. 嚴格的超時限制：如果庫存查詢 API 在 5 秒內沒有返回結果，應用就必須將其視為錯誤。
2. 用戶體驗考慮：這個嚴格的超時限制是為了確保用戶能夠快速獲得庫存信息。如果查詢時間過長，用戶可能會認為應用無響應或放棄購買。
3. 系統負載考慮：在高峰期，大量並發的長時間庫存查詢可能會對後端系統造成壓力。通過限制查詢時間，可以減輕服務器負擔。
4. 特殊錯誤處理：當發生 5 秒超時時，應用需要向用戶顯示一個特定的錯誤消息，例如「庫存信息暫時無法獲取，請稍後再試」，而不是通用的網絡錯誤消息。

其中，第 1 項和第 4 項的規格和 iOS 前端有關，但！也只有這一道 api 有這個需求，我們並不希望為了這個需求，而修改所有 api 的實作。

我們可以透過 `DispatchWorkItem` 來設定特定時間的 API 任務，並在任務完成後，透過 `DispatchQueue.main.async` 來執行我們的程式碼。

## 解法比較，使用 DispatchWorkItem vs. 單純使用 flag 的 true/false 來控制

使用 `DispatchWorkItem` 相比使用 flag 來實現超時控制確實有一些優勢。讓我們來比較一下這兩種方法：

### 使用 DispatchWorkItem 的優勢：

1. **清晰的代碼結構**：`DispatchWorkItem` 提供了一個封裝任務的清晰方式，使代碼更易讀和維護。

2. **內建的取消機制**：`DispatchWorkItem` 有內建的 `cancel()` 方法，可以輕鬆取消尚未執行的任務。

3. **更精確的時間控制**：使用 `DispatchQueue.asyncAfter` 配合 `DispatchWorkItem`，可以更精確地控制超時時間。

4. **更好的資源管理**：當 `DispatchWorkItem` 被取消或完成時，系統會自動處理相關資源的釋放。


## 使用 DispatchWorkItem 設定特定時間的 API 任務

以下是還沒有加上 5 秒超時限制的 api 任務實作：

```swift
    func postData<T: Encodable, U: Decodable>(to url: URL, body: T, completion: @escaping (Result<U, Error>) -> Void) {
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        do {
            request.httpBody = try JSONEncoder().encode(body)
        } catch {
            DispatchQueue.main.async {
                completion(.failure(error))
            }
            return
        }
        
        URLSession.shared.dataTask(with: request) { data, response, error in
            DispatchQueue.main.async {
                if let error = error {
                    completion(.failure(error))
                    return
                }
                
                guard let data = data else {
                    completion(.failure(NSError(domain: "APIManager", code: 0, userInfo: [NSLocalizedDescriptionKey: "No data received"])))
                    return
                }
                
                do {
                    let decodedData = try JSONDecoder().decode(U.self, from: data)
                    completion(.success(decodedData))
                } catch {
                    completion(.failure(error))
                }
            }
        }.resume()
    }
```

### 加上 5 秒超時限制

```swift
func postData<T: Encodable, U: Decodable>(to url: URL, body: T, completion: @escaping (Result<U, Error>) -> Void) {
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    
    do {
        request.httpBody = try JSONEncoder().encode(body)
    } catch {
        DispatchQueue.main.async {
            completion(.failure(error))
        }
        return
    }
    
    // 設定 5 秒超時限制 設定 workitem
    let timeoutWorkItem = DispatchWorkItem {
        DispatchQueue.main.async {
            completion(.failure(NSError(domain: "timeout", code: -1, userInfo: [NSLocalizedDescriptionKey: "timed out"])))
        }
    }
    
    // 設定 5 秒超時限制 設定
    DispatchQueue.main.asyncAfter(deadline: .now() + 5, execute: timeoutWorkItem)
    
    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        // 如果 request 在 5 秒內完成，取消 timeoutWorkItem
        timeoutWorkItem.cancel()
        
        DispatchQueue.main.async {
            if let error = error {
                completion(.failure(error))
                return
            }
            
            guard let data = data else {
                completion(.failure(NSError(domain: "APIManager", code: 0, userInfo: [NSLocalizedDescriptionKey: "No data received"])))
                return
            }
            
            do {
                let decodedData = try JSONDecoder().decode(U.self, from: data)
                completion(.success(decodedData))
            } catch {
                completion(.failure(error))
            }
        }
    }
    
    task.resume()
}
```

