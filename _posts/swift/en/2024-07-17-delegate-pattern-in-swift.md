---
layout: single
title: Delegate Pattern in Swift
date: 2024-07-17 13:10 +0800
category: swift
author: Marvin Lin
tags: [Swift, Design Pattern]
lang: en
summary: The Delegate Pattern is extensively used in iOS development to delegate responsibilities or behaviors to other objects, thereby achieving decoupling and flexibility. In Swift, we usually use protocols to define the interface for the delegate, and the delegate object conforms to this protocol. This article will explain how to use the delegate pattern in Swift and provide a practical example.
classes: wide
---

The Delegate Pattern is a commonly used design pattern in iOS development that allows one object to delegate certain responsibilities or behaviors to another object, thereby achieving decoupling and flexibility. In Swift, we typically use protocols to define the delegate's interface, and the delegate object adheres to this protocol. In this article, we will introduce how to use the delegate pattern in Swift and provide an actual example.

Below is a task involving moving boxes, where the tool to be used is not specified. It could be manual, like a porter, or mechanical, like a forklift. Although both a `Porter` and a `Forklift` can move boxes, they do so in different ways due to the tools they use, which reflects in the implementation of the program. Regardless of the method used, the box will be moved. After moving the box, the porter needs to inform the supervisor/foreman so that the foreman knows that a task has been completed to facilitate the dispatch of the next task.

```swift
/// Any class that can be a supervisor must conform to this protocol
/// In Swift, delegate protocols must conform to AnyObject to allow 'weak' references
protocol SupervisorDelegate: AnyObject {
    func didMoveBox(box: Box, to location: (Int, Int))
}

/// Job dispatcher, upon receiving a job, dispatches it to a delegate
class Supervisor: SupervisorDelegate {

    func didMoveBox(box: Box, to location: (Int, Int)) {
        /// record that the box has been moved and dispatch the next task or idle
    }
}

/// Porter, can move boxes manually
class Porter {

    /// The delegate is set to 'weak' to prevent retain cycles, you will notice that most iOS component delegates are set as optional
    weak var delegate: SupervisorDelegate?
    
    /// Receives the task to move a box, but does not move it itself, delegates the moving task to the delegate (which could be another porter or a forklift)
    func move(box: Box, to location: (Int, Int)) {
        /// Manually moves the box to location (Int, Int)
        /// After moving the box, informs the supervisor that the box has been moved
        delegate?.didMoveBox(box: box, to: location)
    }
}

/// Forklift, can move boxes mechanically
class Forklift {

    weak var delegate: SupervisorDelegate?
    
    func move(box: Box, to location: (Int, Int)) {
        /// Moves the box using a forklift to location (Int, Int)
        /// After moving the box, informs the supervisor that the box has been moved
        delegate?.didMoveBox(box: box, to: location)
    }
}
```

Next, we will use two examples from an iPhone app to demonstrate the delegate pattern.

## MotionManager - Detects movement in the xyz axes, signals the current VC when a movement threshold is met, this class isn't used exclusively in one VC

First, implement MotionManager. The sole responsibility of MotionManager is to trigger when CoreMotion meets a movement threshold, but this class does not handle UI or user interaction.

```swift
import Foundation
import CoreMotion

protocol MotionManagerDelegate: AnyObject {
    func deviceIsNotAvailable()
    func deviceIsMoving(accerlationX: Double, accerlationY: Double, accerlationZ: Double)
    func deviceUpdateGotError(_ error: Error?)
}

class MotionManager {
    
    private lazy var motionManager: CMMotionManager = .init()
    
    weak var delegate: MotionManagerDelegate?
    
    func startDetection() {
        
        guard motionManager.isDeviceMotionActive else {
            delegate?.deviceIsNotAvailable()
            return
        }
        
        
        motionManager.deviceMotionUpdateInterval = 0.1
        motionManager.startDeviceMotionUpdates(to: .main) { [weak self] motion, error in
            guard let self = self else {
                return
            }
            
            if let motion = motion {
                let acceleration = motion.userAcceleration
                let accelerationMagnitude = sqrt(acceleration.x * acceleration.x + acceleration.y * acceleration.y + acceleration.z * acceleration.z)
                if accelerationMagnitude > 1.5 {
                    print("Device is moving!")
                    self.delegate?.deviceIsMoving(accerlationX: acceleration.x, accerlationY: acceleration.y, accerlationZ: acceleration.z)
                }
            } else {
                print("Error: \(error?.localizedDescription ?? "Unknown error")")
                self.delegate?.deviceUpdateGotError(error)
            }
        }
    }
    
    func stopDetection() {
        motionManager.stopDeviceMotionUpdates()
    }
}
```

The VC can now delegate the responsibility of detecting motion to the MotionManager. This VC does not handle the motion-related logic but is responsible for handling UI interactions when motion conditions are met.

```swift

import UIKit

/// VC that appears on screen during motion detection
class MotionDetectViewController: UIViewController {
    
    /// This VC is the delegate for the MotionManager, handling UI and user interactions within delegate functions
    private lazy var motionManager: MotionManager = {
        let manager = MotionManager()
        manager.delegate = this
        return manager
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        /// Implementation omitted
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        manager.startDetection()
    }

    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        manager.stopDetection()
    }
}

extension MotionDetectViewController: MotionManagerDelegate {
    func deviceIsNotAvailable() {
        /// Handle the device not being able to start motion detection
    }
    
    func deviceIsMoving(accerlationX: Double, accerlationY: Double, accerlationZ: Double) {
        /// Handle the device reaching the movement threshold
    }
    
    func deviceUpdateGotError(_ error: Error?) {
        /// Handle device error conditions
    }
}
```

## Benefits of Using the Delegate Pattern

The delegate pattern allows your objects to adhere to the "Single Responsibility Principle." For example, the `MotionManager` handles motion detection but does not deal with the UI. It is responsible only for signaling the VC when the motion threshold is met. The VC does not handle motion detection; it only handles displaying corresponding UI interactions when motion conditions are met.

The second example is the detection of whether the device is facing north. The `NorthDetector` handles the detection of northward direction but does not handle the UI. It is responsible only for signaling the VC when the device is facing north. The VC does not handle the north detection; it only handles displaying corresponding UI interactions when facing north.

**Note that the second example's sample code omits permission checks.**

As shown in the examples, other pages in a project might also trigger "motion detection" and "device north-facing." Since these logics have already been implemented in the managers, simply instantiate the manager in the VC implementation, set up the delegate, and you can develop different UI responses based on different situations.

### CLLocationManager Permission Check

Note that the above examples use the CoreLocation framework, which requires user permission before use. The response to this permission varies with different iOS versions. It is recommended to refer to the [official Apple documentation](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/1423640-authorized) for implementing permissions.

## Naming Conventions for Delegate Functions

In the Cocoa framework, you can see many delegate functions prefixed with 'did' and 'will'. Consider these prefixes as indicating:
- When a delegate function is about to start something, use `will`. For example, in tableView delegates, `cell willDisplay` indicates the cell is about to appear.
- After something has completed, use `did`, such as `cell didEndDisplaying`, indicating the cell display has ended after the event.

## When Not to Use Delegates

Delegates are suitable for 1-to-1 communication. If your scenario requires 1-to-many or many-to-many communication, do not use the delegate pattern. In Swift, you can use closures or NotificationCenter for non-1-to-1 communication.

### Reference Websites

[iOS Location Permission Documentation](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/1423640-authorized)