---
layout: single
title: Unit Testing from Zero to One - Getting Started with Tests in Your Project
date: 2024-07-16 15:00 +0800
category: unitTesting
author: Marvin Lin
tags: [Unit Testing, Swift, Xcode]
lang: en
summary: This article introduces how to integrate unit testing into iOS projects. It highlights the role of unit tests in verifying the correctness of the smallest testable units of code, such as functions, methods, or classes. The author suggests starting with components that do not depend on others and uses a dependency graph to illustrate this point. The article includes practical steps for setting up a unit testing environment in Xcode and discusses examples such as handling JSON responses for authentication. It also explores how unit testing can help manage changing project requirements, noting both its benefits and limitations.
---

In this article, we will introduce how to integrate unit testing into iOS projects. Unit tests are used to verify that the smallest testable units of code (such as functions, methods, or classes) are correct. They are typically written and executed by developers using various tools and frameworks to automate and simplify the testing process. The purpose of unit testing is to ensure the correctness and robustness of the program's logic, enhancing the quality and maintainability of the code.

**Special thanks to Hanyu Chen for the coffee!**

![buy me a coffee from Hanyu](/assets/buyMeCoffee/buy_me_a_coffe_hanyu.png)

## Where to Start Testing? It's Best to Start with Objects That Do Not Depend on Others

The following diagram shows the dependency graph of project objects. It is recommended to start testing with objects that do not depend on others.

![Project Object Dependency Diagram](/assets/unitTesting/from-zero-to-one/dependency_graph.png)

Commonly passed around objects are usually DTOs related to JSON responses. Let's assume there is a login API that returns two tokens, a refresh token, and an access token.

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODg4ODU1OSwiaWF0IjoxNzE4ODAyMTU5LCJqdGkiOiIzMDQyZDhlMGIzOTc0MjQyYTI0MDFhZDU0ZjRhMjAxOCIsInVzZXJfaWQiOjh9.45URkd4iyBx7mjeyB9yzQp5x3gICLYxo3laqtCNjyLE",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4ODg4NTU5LCJpYXQiOjE3MTg4MDIxNTksImp0aSI6IjJjYzM2ZDFkZTMzYjQ3OTliNWE3MzQ1Njc5NzFkMWE1IiwidXNlcl9pZCI6OH0.j7CLMRL0EUknJ_HxRLeWS0vCD1QMfcrSL9kYDCTug1o"
}
```

## Steps to Add Unit Testing to an Existing Project

In the Project targets tab, click the + sign, select Unit Testing Bundle, and you can start having tests in your project.

![add test bundle](/assets/unitTesting/from-zero-to-one/add_test_bundle.png)

### Default Test Template

After adding the file, you will see two tests, along with setup and teardown.
![Unit testing template](/assets/unitTesting/from-zero-to-one/unit_testing_template.png)

### First Step, Add @testable Import

Above `import XCTest`, remember to import your own project, so the Unit Testing target can interact with objects within your project.
```swift
@testable import YourProjectName
```

## Testing the Token Model

### Model Implementation
```swift
/// This model is for receiving JSON responses
struct TokenResponse: Codable {
    let refresh: String
    let access: String
}
```

### Unit Testing Implementation
```swift
@testable import StartUnitTesting
import XCTest

final class CocoaTests: XCTestCase {

    /// Convert JSON response into data, unit testing won't actually call the API
    private func getAPIResponse() -> Data {
        
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

The first step is to test if this unit testing can alert you when there is an error in the program, so the `XCTAssertEqual` equals an empty string.
```swift
    /// Test the token response
    func testTokenResponse() throws {
        
        let data = getAPIRespnose()
        let model = try JSONDecoder().decode(TokenResponse.self, from: data)
        XCTAssertEqual(model.refresh, "")
        XCTAssertEqual(model.access, "")
    }
```

### At this point, you will receive a failed test result, which will tell you which model's value is incorrect.
![first test, you got error](/assets/unitTesting/from-zero-to-one/first_fail_test.png)

The second step is to set the fixed access token and refresh token as the equal values.
```swift
func testTokenResponse() throws {
        
        let data = getAPIRespnose()
        
        let model = try JSONDecoder().decode(TokenResponse.self, from: data)
        XCTAssertEqual(model.refresh, "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODg4ODU1OSwiaWF0IjoxNzE4ODAyMTU5LCJqdGkiOiIzMDQyZDhlMGIzOTc0MjQyYTI0MDFhZDU0ZjRhMjAxOCIsInVzZXJfaWQiOjh9.45URkd4iyBx7mjeyB9yzQp5x3gICLYxo3laqtCNjyLE")
        XCTAssertEqual(model.access, "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4ODg4NTU5LCJpYXQiOjE3MTg4MDIxNTksImp0aSI6IjJjYzM2ZDFkZTMzYjQ3OTliNWE3MzQ1Njc5NzFkMWE1IiwidXNl
