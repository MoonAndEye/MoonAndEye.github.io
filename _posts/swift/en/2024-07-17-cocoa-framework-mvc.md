---
layout: single
title: iOS MVC Architecture
date: 2023-05-01 08:48 +0800
category: swift
author: Marvin Lin
tags: [Swift, MVC, Cocoa framework]
summary: Analyzing the iOS MVC design pattern. MVC stands for Model-View-Controller. The main point is that the model should be isolated from the view, applicable to both macOS and iOS apps. This article uses the book "Cocoa Design Patterns" as an example.
permalink: /swift/:title:output_ext
classes: wide
---

MVC is Apple's exemplary framework; in the era of UIKit, it was an important pattern. Recently, whenever I find some free time, I spend it reading an old book, **Cocoa Design Patterns**.

![Cocoa design pattern](/assets/swift/mvc-pattern/books-cover.jpeg){: width="50%"}

## Chapter Two: Analysis and Application of MVC

![Chapter Two: Analysis and Application of MVC](/assets/swift/mvc-pattern/mvc-chapter.jpeg)

Apple's Cocoa design pattern of MVC is a software development approach that divides an application into three parts: Model, View, and Controller. This separation makes the code easier to maintain and reuse, enhancing the application's performance and testability.

The **Model** is responsible for managing the application's data and logic. It does not interact directly with the user interface but updates or retrieves data through the controller. The model can be any type of object, such as arrays, dictionaries, files, or web services.

The **View** is responsible for displaying the user interface of the application. It receives user input and events and passes them to the controller. Views can be any type of user interface component, such as buttons, labels, images, or tables.

The **Controller** coordinates the model and view. It is the main logic layer of the application. The controller can receive input and events from the view and act accordingly, such as updating the model or changing the view. Controllers can also communicate with other controllers to implement more complex functionalities.

### Book Example: Payroll Calculator

In a payroll calculator, the Model is the Employee class. After triggering `calculatePayAmount(:)`, the employee's salary is calculated. If a program is not divided according to the MVC functionality, the call relationships would look like the diagram below. Note that even without MVC, a program can still function correctly; the first version may work well, but problems arise during subsequent expansions.

![Project not following MVC design](/assets/swift/mvc-pattern/non-mvc.jpeg)

If we were to separate the Model and View, a Controller would act as a mediator to prevent tight coupling between the View and Model. In a project that continuously adds features, it's common to encounter such situations.

### V1.1 (Hypothetical but possible scenarios)
- UI needs rounded corners, gradients, and shadows
- UX requires placeholder text if input fields are empty
- Search bars should have autocomplete suggestions

### V1.2 (Hypothetical but possible scenarios)
- Each branch's holidays differ based on location, requiring an expansion of the fields in the employment contracts to include regional specifics
- Introducing an intern position with different payroll calculations than regular employees, varying by region
- Currency conversion with UI fields displaying corresponding currency symbols (accurate to three decimal places)

With these feature additions, any modifications to the view could potentially affect the model, and vice versa. This design is prone to subtle bugs during development. Apple recommends adopting the MVC pattern in development, inserting a controller between the model and view, as shown in the diagram below.

![Project following MVC pattern](/assets/swift/mvc-pattern/mvc.jpeg)

Since the Cocoa design patterns book was published a long time ago and does not include iOS examples, it's worth noting that iOS's UIKit is a subset of macOS's (as of UIKit's release). This is mentioned in another book, **Creative Competition**. Therefore, iOS development certainly applies this pattern. Below is a diagram from Stanford 193 p, representing MVC in iOS.

![MVC pattern in iOS](/assets/swift/mvc-pattern/mvc-ios.jpg)

## In iOS Apps, When Views Touch Models

```swift
/// FooTableViewCell, representing MVC's View in the UI displaying Employee data
class FooTableViewCell: UITableViewCell {
    /// Employee is the data-carrying object, MVC's Model
    /// Handling Model inside a View object; the program might function but it doesn't adhere to the MVC pattern
    func setup(_ employee: Employee) {
        // Implementation omitted
    }
}
```

It is recommended not to couple the View and Model together in projects. Keep Views purely for presenting data, let Models describe data, and use Controllers (or other non-View objects) for assembly. Besides the MVC pattern, the MV(X) family has branched out extensively, and many examples on GitHub can meet your needs.

## Reference Websites

[Kodeco's Introduction to MVC](https://www.kodeco.com/1000705-model-view-controller-mvc-in-ios-a-modern-approach)

[The Only Viable iOS Architecture (MVC)](https://medium.com/@iamirzhan/the-only-viable-ios-architecture-c42f7b4c845d)

[iOS Architectures (MVC, MVP, MVVM, Viper)](https://medium.com/ios-os-x-development/ios-architecture-patterns-ecba4c38de52)