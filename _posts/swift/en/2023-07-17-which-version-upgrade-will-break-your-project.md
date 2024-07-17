---
layout: single
title: When Upgrading Third-Party Versions, What Kind of Version Number Causes a Project Build to Fail?
date: 2024-07-17 08:50 +0800
category: swift
author: Marvin Lin
tags: [Swift, third party, cocoapods]
lang: en
summary: Explaining semantic versioning in development. In semantic version control, we have major, minor, and patch versions, each signifying different types of changes. Patches are for bug fixes, minor updates are compatible, and major updates can break your code. This article also provides examples.
---

In iOS development, we often use third-party packages to add functionality or reduce workload. However, if we download the source code of the packages directly or use git submodules, we might encounter issues such as version inconsistencies, unclear dependencies, and inconvenient updates. To solve these problems, we can use cocoapods, a tool that helps manage third-party packages.

Cocoapods is an open-source project written in Ruby that automates the installation and updating of third-party packages while handling dependencies effectively. The benefits of using cocoapods include:

- Specifying the packages and their versions in one file (Podfile) allows cocoapods to automatically download and install the required packages.
- It is easy to view and manage which packages and their dependencies and versions are used in our projects.
- Packages can be easily updated by modifying the version number in the Podfile and running the pod update command, and cocoapods will automatically update the packages and dependencies.
- The search function of cocoapods helps find suitable packages, or you can browse the official cocoapods website (https://cocoapods.org/) to see what new or popular packages are available.

## When upgrading libraries, to what extent will the code likely fail to build directly?

When you run `pod install` or `pod update`, the terminal will display the pods being installed and their version upgrades.

For example, if you see:

```ruby
Installing Alamofire 5.6.4 (was 5.6.2)
```

This means your project has been upgraded from Alamofire 5.6.2 to 5.6.4.

Whether this upgrade from `5.6.2` to `5.6.4` will cause your project to fail to build depends on whether the library follows "semantic versioning".

## Semantic Versioning

[Semantic Versioning](https://semver.org/) uses the format MAJOR.MINOR.PATCH, where:

- MAJOR: Major version number, indicating backward-incompatible changes. When there are major revisions or significant breaking changes, the major version number should be increased. For example, from 1.0.0 to 2.0.0.
- MINOR: Minor version number, indicating backward-compatible new features. When new features are added that do not affect existing functionality, the minor version number should be increased. For example, from 1.0.0 to 1.1.0.
- PATCH: Patch version number, indicating backward-compatible bug fixes. When bugs are fixed that do not affect existing functionality, the patch version number should be increased. For example, from 1.0.0 to 1.0.1.

The purpose of semantic versioning is to help developers and users better understand the significance of software version numbers, facilitating version control and upgrade management. It emphasizes the importance of version numbers, informing users how changes might affect their applications. Additionally, semantic versioning highlights compatibility between versions, making it easier for developers and users to manage upgrades and updates.

### PATCH Example

Consider a function that divides numbers:

```swift
/// 1.0.0 Simply divides numbers
func getDividedNumber(number: Int, divisor: Int) -> Int {
    return number / divisor
}
```

However, if the divisor is 0, it will crash. So, blocking divisor 0 and following semantic versioning rules, this is a PATCH increment.

```swift
/// 1.0.1 Handling the case when divisor is 0
func getDividedNumber(number: Int, divisor: Int) -> Int? {
    if divisor == 0 {
        return nil
    }
    return number / divisor
}
```

### MINOR Version Example

Suppose we have an object that moves in a specified direction—only "east, west, south, north" as shown below:

```swift
/// Version 1.0.1
enum Direction {
    case east
    case west
    case south
    case north
}

func move(toward direction: Direction, path: Int) {
    /// Implementation omitted
}
```

But a new requirement is added: after moving, the object should return to its original position after three seconds.

```swift
/// Version 1.1.0, added functionality
func move(toward direction: Direction, path: Int) {
    /// Implementation from 1.0.1
    /// Implementation omitted
}

/// 1.1.0 New requirement - object returns to original position after three seconds
func backToStartPointAfter3Sec(toward direction: Direction, path: Int) {
    /// Implementation from 1.1.0
    /// Implementation omitted
}
```

### Major Version Example with Alamofire, as there is a significant difference between major versions 4 and 5

In Alamofire major version 4:

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

But in Alamofire major version 5:

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

From the above code, it is clear that moving from Alamofire 4 to 5 would require code changes. To lessen the pain of upgrading versions, you can refer to [Wrapping Third-Party Libraries to Ease Upgrade Pains](https://moonandeye.github.io/swift/using-adapter-pattern-to-libs.html).

## Differences in versioning in Podfile

If no specific version is mentioned, the latest version will be used:
```
pod 'Alamofire'
```

To specify version 5.0.0:
```
pod 'Alamofire', '5.0.0'
```

To use versions greater than 5.0.0, operators such as <=, <, > are also available:
```
pod 'Alamofire', '>= 5.0.0'
```

To specify versions above 5.0.0 but below 5.1.0. If changed to `~> 5.0`, then it means versions above 5.0 but below 6.0:
```
pod 'Alamofire', '~> 5.0.0`
```

## Reference Articles

[Wrapping Third-Party Libraries to Ease Upgrade Pains](/en/swift/using-adapter-pattern-to-libs/)

[Semantic Versioning](https://semver.org/)

[Alamofire 5 Migration Guide](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Alamofire%205.0%20Migration%20Guide.md)