---
layout: single
title: Value Types and Reference Types in Swift
date: 2024-07-16 23:11 +0800
category: swift
author: Marvin Lin
tags: [Swift]
lang: en
summary: Swift designed arrays and dictionaries as value types. When you use an array and copy it, it might behave differently than you expect. This article also includes references to swift.org and the Swift blog.
---

This discussion was an extension of the Prototype pattern from a book on Swift’s Design Patterns. Now, I aim to delve deeper into the nuances of value types and reference types.

### Reference Type 

`class` is a reference type. Since Swift 5.5, the `actor` is also a reference type.

### Value Type

Objects declared with `struct`, as well as `enum`, `tuple`, `Dict`, and `Array`, are value types.

## Reasons for Designing Value Type as the Main Structure in Swift

The earliest article I found was written when Swift was still in development. The article link is below, with the publication date of August 15, 2014.

[Value and Reference Types - Swift Blog](https://developer.apple.com/swift/blog/?id=10)

The following paragraphs discuss **The Role of Mutation in Safety**

> One of the main reasons for choosing value types over reference types is that they are easier to understand. If you always receive independent copy instances, you can trust that other parts of the application will not change the data behind the scenes. This is particularly useful in a multi-threaded environment where different threads might change the data beneath you. This can lead to serious errors that are very difficult to debug.

> Since the difference is defined by what happens when the data is modified, there is a situation where value and reference types overlap: when the instance has no writable data. Without mutation, the behavior of values and references is exactly the same. You might consider a situation where a completely immutable class could be valuable.

> In Swift, `Array`, `String`, and `Dictionary` are all value types. They behave much like simple `int` values in C, as the sole instances of that data. You do not need to do anything special—like making an explicit copy—to prevent other code from modifying the data in the background. Importantly, you can safely pass copies of values between threads without needing synchronization. This model will help you write more predictable code in Swift.

## What Changes When Arrays in Swift are Value Types?

```swift
/// Declaration of NinjaTurtle, note: this uses the reference type class
class NinjaTurtle {
    
    var name: String = ""
}

// Initialize a Ninja Turtle and name it Da Vinci
let turtle1 = NinjaTurtle()
turtle1.name = "Da Vinci"

// Initialize another Ninja Turtle and name it Michelangelo
let turtle2 = NinjaTurtle()
turtle1.name = "Michelangelo"

/// Both Ninja Turtles are placed in the same array
var turtles = [turtle1, turtle2]

/// Since the array is a value type, this assignment is a copy
var copiedTurtles = turtles

/// We take out the original turtle from the array and rename it Raphael
turtles[0].name = "Raphael"

/// What is the name of the turtle at index 0 in the copied array? Raphael or Da Vinci?
print(copiedTurtles[0].name)

```

It is recommended to run the above code yourself and verify your thoughts.

If you encounter other languages, try running the same logic in Kotlin, Python, Java, C#, or Rust to see if it behaves the same or differently.

## In What Scenarios Should You Choose Which Type?

### Scenarios Suitable for Value Type

- When comparing two objects, using `==` is more reasonable.
- When copying, the copied object and the original object should be independent in state.
- When data will be operated on across multiple threads.

### Scenarios Suitable for Reference Type (class)

- When comparing two objects, using `===` is more reasonable.
- When the need arises for a state that is shared and can be changed.

## Related Links

[Prototype Pattern in Swift (Differences Between Reference Type and Value Type)](https://moonandeye.github.io/swift/2018/06/09/prototype-patter.html)

[Value and Reference Types - Swift Blog](https://developer.apple.com/swift/blog/?id=10)

[Structures and Classes - swift.org](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/classesandstructures/)