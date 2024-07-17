---
layout: single
title: SwiftUI Data Flow
date: 2024-07-17 06:00 +0800
category: swift
author: Marvin Lin
tags: [Swift, SwiftUI]
lang: en
summary: Apple recommends a specific data flow for SwiftUI. It adheres to a unidirectional data flow.
---

SwiftUI employs a declarative approach for UI design. The data transmission follows the sequence of Action → State → View, which is a fixed direction with no possibility of reversal. You can also research the term "one-way data flow," which is prevalent not only on mobile platforms but also on other platforms due to its data flow design.

## Action as the Starting Point

An action may be triggered by a user or an external event. Once an action is initiated, it changes the state within the program, and subsequently, SwiftUI automatically updates the necessary views.

Compared to previous screen rendering responsibilities, which were handled by UIViewController in the older UIKit.

![SwiftUI Data flow](/assets/swift/state-change/one-way-data-flow.jpeg)

## View State Management - Single Source of Truth

It's important to remember the principle of a single source of truth. Apple's recommended approach is to design data as read-only Swift properties or provide bidirectional state bindings. SwiftUI observes data changes and updates only the views that need to change.

Apple advises against using persistent storage directly as state properties. Instead, persistent storage is more suitably used for managing transitional states, such as highlight statuses or filter settings.

![UI State Management](/assets/swift/state-change/ui-state.jpeg)

## References

[SwiftUI Model Data - Apple Documentation](https://developer.apple.com/documentation/swiftui/model-data)

[Managing UI State in SwiftUI - Apple Documentation](https://developer.apple.com/documentation/swiftui/managing-user-interface-state)