---
layout: single
title: Wrapping Third-Party Libraries to Ease the Pain of Upgrades
date: 2024-07-17 08:30 +0800
category: swift
author: Marvin Lin
tags: [Swift, Design Patterns]
lang: en
summary: Using the adapter pattern to wrap third-party libraries in Swift. It's common in iOS development to rely on third-party libraries. When libraries are upgraded, they sometimes break the build or cause runtime crashes. Using the adapter pattern can help develop a more stable environment and save time.
classes: wide
author_profile: false
---

In modern iOS development, third-party libraries are commonly used. With yearly updates to Swift and Xcode, as well as changes in syntax, libraries often undergo version upgrades. Below are the version upgrade trends for Alamofire and Charts over the past year, illustrating that libraries do get updated. According to [Semantic Versioning](https://semver.org/lang/zh-TW/), major version changes almost certainly require code modifications to build successfully. Sometimes, even minor version upgrades can introduce unexpected issues.

If the third-party library you're using is scattered across dozens of places in your project, then you'll need to make changes in as many places when upgrading. As the version jumps become larger or the number of scattered instances increases, the risk of library upgrade issues also rises.

![Alamofire tags list](/assets/swift/adapter-pattern/Alamofire-tags.jpeg){:width=50%}

![Charts tags list](/assets/swift/adapter-pattern/Charts-tags.jpeg){:width=50%}

## Reducing Dependency Pain Due to Upgrades - Wrapping Libraries

When using libraries, consider the parameters your interfaces will use. Take the most common event logging library as an example. Google Firebase's FirebaseAnalytics requires these two parameters:

- Parameter Name: String
- Parameter Dictionary: [String: Any]?

These parameters are typically set as arguments in the adapter function.

### First Version, Using Only FirebaseAnalytics

```swift
import Foundation
import FirebaseAnalytics

/// Object that wraps the analytics module; only this file imports the analytics module
struct AnalyticsAdapter {
    
    /// Function to log analytics events, triggers this function when recording, interface parameters reflect those of the wrapped lib
    func logEvent(name: String, parameters: [String: Any]?) {
        
        Analytics.logEvent(name, parameters: parameters)
    }
}
```

### Second Version, Including Google Analytics and Flurry

```swift
/// Object that wraps the analytics module; only this file imports the analytics module
struct AnalyticsAdapter {
    
    /// Function to log analytics events, triggers this function when recording, interface parameters reflect those of the wrapped lib
    func logEvent(name: String, parameters: [String: Any]?) {
        /// Google Analytics existing from the first version
        Analytics.logEvent(name, parameters: parameters)
        /// Tracking lib added in the second version
        Flurry.log(eventName: name, parameters: parameters)
    }
}
```

### Diagram of Adapter Usage in a Project

In the project, if VCs or Models need to utilize third-party lib functions, they would call through the adapter class. VCs won't touch the third-party lib directly; only the adapter objects interact with the third-party lib. The usage appears as in the diagram below.

![Diagram of Adapter Usage in a Project](/assets/swift/adapter-pattern/AdaptersDiagram.jpeg)

## Example - Using Alamofire

```swift
import Foundation
import Alamofire

/// Adapter object for Alamofire, handles URLRequest
struct AlamofireAdapter {
    
    /// Sends out requests and defines a decodable object to return upon completion (Result<T: Decodable, Error>)
    func sendRequestDecodable<T: Decodable>(_ request: URLRequest, completion: @escaping ((Result<T, Error>) -> Void)) {
        
        /// If Alamofire upgrades to major version 6, the implementation here would change
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

## Example - Using an Image Caching Package

```swift
//
// ImageCacheAdapter.swift
// ChatGPT
//
// Created by cm0679 on 2023/04/22.
//

import UIKit
import Kingfisher

/// Specialized object for interacting between ImageView and web image resources
struct ImageCacheAdapter {
    
    /// Interface: UIImageView, URL, and placeholder. The placeholder is optional by default
    /// When an imageView in a tableViewCell needs an image during cellForRowAt
    func downloadAndCache(imageView: UIImageView, with url: URL, placeHolder: UIImage?) {
        
        /// To switch from Kingfisher to sd_webImage, replace the following implementation
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

## Using Protocols for Adapters

If you search online for the Adapter pattern, you'll find examples that begin with defining a protocol, setting up functions within it. Then, the previously mentioned Alamofire Adapter object conforms to the URLRequest protocol and implements its functions.

```swift
import Foundation
import Alamofire

protocol URLRequestAdapter {
    /// Sends out requests and defines a decodable object to return upon completion (Result<T: Decodable, Error>)
    func sendRequestDecodable<T: Decodable>(_ request: URLRequest, completion: @escaping ((Result<T, Error>) -> Void))
}

/// Adapter object for Alamofire, handles URLRequest
struct AlamofireAdapter: URLRequestAdapter {
    
    /// Sends out requests and defines a decodable object to return upon completion (Result<T: Decodable, Error>)
    func sendRequestDecodable<T: Decodable>(_ request: URLRequest, completion: ```swift
        ((Result<T, Error>) -> Void)) {

        /// If Alamofire upgrades to major version 6, the implementation here would change
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

In application, for instance, `FooModel` would only interact with the `URLRequestAdapter` protocol, but during initialization, it uses the `AlamofireAdapter`:

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

While this approach requires declaring an extra protocol, which may seem like an unnecessary addition if the same functionality can be achieved without it, there is a story behind this method. Writing a "interface" in code first, and then creating an object to inherit this interface, is a common practice in many languages. Given Swift's relatively young age compared to other languages, adopting established patterns is both logical and practical. Furthermore, if your codebase isn't just for releasing apps but involves SDKs that might need switching, such as switching payment SDKs from credit card payments to Apple Pay or third-party logins from Facebook to GitHub, this pattern can be very useful.

### But what about mobile app development?

If you are certain that your project is an iOS app and that the libraries used are the most popular ones, with the highest number of stars and the most forks, is there a need to write a protocol before implementing objects that conform to it?

I don't have an answer.

But you can start your thinking from these points:

- Is this project a personal side project, a major company project, or a company experimental project?
- Is the feature's library one of a few dominant ones?
- How does the project decide the policy for using third-party libraries?

Of course, the most important thing is the consensus of the "project team." If the project team consists of just one person, then that person decides alone. But when the team consists of multiple members, what should be prioritized is how the project decides on third-party libraries. Above the consensus on "how to use libraries," there is another layer of "team development communication" that needs consideration.

## References

[Semantic Versioning](https://semver.org)

[Refactoring Guru's Adapter Pattern Swift Sample](https://refactoring.guru/design-patterns/adapter/swift/example#example-1)