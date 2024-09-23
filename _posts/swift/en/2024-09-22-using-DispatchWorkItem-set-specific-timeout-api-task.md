---
layout: single
title: Using DispatchWorkItem to Set Specific Time Limits for API Tasks
date: 2024-09-22 17:00 +0800
category: swift
author: Marvin Lin
tags: [Xcode, Swift]
summary: This article demonstrates how to use DispatchWorkItem to implement a 5-second timeout for an API task in Swift. By using DispatchWorkItem alongside DispatchQueue.asyncAfter, it ensures a clean and efficient timeout mechanism, avoiding the need to modify other API calls. The article highlights the advantages of DispatchWorkItem over using simple flags, such as better code structure, built-in cancellation, precise time control, and efficient resource management. A Swift code example is provided to implement this feature for a real-time inventory check API in an e-commerce app.
---

Scenario - You are developing an e-commerce iOS app. This app has multiple functionalities, including browsing products, adding items to the cart, checking inventory, and placing orders. Among these, the real-time inventory checking feature is particularly crucial as it directly impacts user purchasing decisions and experience.

## Special Requirements:
In this app, most API requests use standard network timeout settings (e.g., 30 seconds or 60 seconds). However, the inventory checking API has a unique requirement:

1. **Strict Timeout Limit**: If the inventory check API does not return results within 5 seconds, the app must treat it as an error.
2. **User Experience Consideration**: This strict timeout limit ensures that users receive inventory information quickly. If the query takes too long, users may perceive the app as unresponsive or abandon their purchase.
3. **System Load Consideration**: During peak periods, a large number of concurrent, long-running inventory checks could put a strain on the backend system. Limiting the query time can reduce the load on the servers.
4. **Special Error Handling**: When a 5-second timeout occurs, the app needs to display a specific error message to the user, such as "Inventory information is temporarily unavailable, please try again later," rather than a generic network error message.

The first and fourth points are related to the iOS front-end, but this requirement only applies to this one API. We do not want to modify the implementation of all APIs just for this requirement.

We can use `DispatchWorkItem` to set a specific time limit for API tasks and execute our code using `DispatchQueue.main.async` after the task is completed.

## Comparison of Solutions: Using DispatchWorkItem vs. Using a Simple True/False Flag

Using `DispatchWorkItem` has some advantages over using a flag to control timeout behavior. Let's compare these two methods:

### Advantages of Using DispatchWorkItem:

1. **Clear Code Structure**: `DispatchWorkItem` provides a clear way to encapsulate tasks, making the code easier to read and maintain.
2. **Built-in Cancellation Mechanism**: `DispatchWorkItem` comes with a `cancel()` method, making it easy to cancel tasks that have not yet been executed.
3. **More Precise Time Control**: By using `DispatchQueue.asyncAfter` with `DispatchWorkItem`, you can more accurately control the timeout duration.
4. **Better Resource Management**: When `DispatchWorkItem` is canceled or completed, the system automatically handles the release of related resources.

## Using DispatchWorkItem to Set Specific Time Limits for API Tasks

Here is the implementation of an API task without the 5-second timeout limit:

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

### Adding the 5-Second Timeout Limit

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
    
    // Set the 5-second timeout limit using DispatchWorkItem
    let timeoutWorkItem = DispatchWorkItem {
        DispatchQueue.main.async {
            completion(.failure(NSError(domain: "timeout", code: -1, userInfo: [NSLocalizedDescriptionKey: "timed out"])))
        }
    }
    
    // Set the timeout after 5 seconds
    DispatchQueue.main.asyncAfter(deadline: .now() + 5, execute: timeoutWorkItem)
    
    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        // If the request completes within 5 seconds, cancel the timeoutWorkItem
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

With this implementation, if the API request does not complete within 5 seconds, the timeout mechanism will trigger and return a timeout error to the user. This approach is both efficient and maintains a clean code structure.