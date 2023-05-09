---
layout: single
title: Delegate Pattern (委派模式)in Swift
date: 2023-05-03 08:47 +0800
category: swift
author: Marvin Lin
tags: [Swift, 設計模式, design pattern]
summary: The Delegate Pattern is widely used in iOS development to delegate responsibilities or behaviors to other objects, increasing flexibility. Swift uses protocols to define the delegate's interface, and the delegate object conforms to that protocol. An example is a job dispatcher that delegates box-moving tasks to a delegate, who can use different tools like a porter or a forklift to move boxes. Regardless of the method used, the box will be moved.
permalink: /swift/:title:output_ext
classes: wide
---

Delegate Pattern 是 iOS 開發常用的設計模式，它可以讓一個物件將某些職責或行為委託給另一個物件，從而實現解耦和靈活性。在 Swift 中，我們通常使用 protocol 來定義 delegate 的介面，並讓 delegate 物件遵循該 protocol。在這篇文章中，我們將介紹如何在 Swift 中使用 delegate pattern，並給出一個實際的範例。

下面是一個會將搬箱子任務派發的範例，`JobDispatcher`會收到 Box 箱子，`JobDispatcher`並不會實際去搬箱子，他會將搬箱子的任務委派給他的 delegate。這個 delegate 並不限定用什麼工具來搬，可以是徒手來搬，像是搬運工(Porter)，也可能是用機器來搬，像是叉車(Forklift)。雖然 `Porter` 和 `Forklift` 都可以搬箱子，但因為使用的工具不一樣，所以搬的方法會不一樣，這會反應到程式的實作上。但不論哪種方法去搬，箱子都會被搬走

```swift
/// 能成為工作派發者的 delegate 都要 conform 這個 delegate
/// 在 Swift 中，delegate protocol 要被 AnyObject conform 才能下 weak
protocol JobDispatcherDelegate: AnyObject {
    func move(box: Box, to location: (Int, Int))
}

/// 工作派發者，在接收到工作後，將工作派發給 delegate
class JobDispatcher {
    /// delegate 為了防止 retain cycle 發生，要設定成 delegate，如果你觀察 iOS 元件，大部分的元件 delegate 都會設定成 optional
    /// 在 JobDispatcher init() 後，再將 delegate 指派給某個物件(這個物件也可能是 self)
    /// 因為是 optional 在操作的時候，可以用 optional chain 處理
    weak var delegate: JobDispatcherDelegate?
    
    /// 接收到搬箱子的任務，但這個類別不搬，會把搬箱子的任務委派給 delegate (但有可能是搬運工，也可能是叉車)
    func move(box: Box, to location: (Int, Int)) {
        delegate?.move(box: box, to: location)
    }
}

/// 搬運工，可以移動 box，用手搬 Box
class Porter: JobDispatcherDelegate {
    
    func move(box: Box, to location: (Int, Int)) {
        // 用手搬運 box 到 location(Int, Int)
    }
}

/// 叉車，可以移動 box，用叉車搬 Box
class Forklift: JobDispatcherDelegate {
    
    func move(box: Box, to location: (Int, Int)) {
        // 用叉車搬運 box 到 location(Int, Int)
    }
}
```

接下來，我們用 iPhone 上的兩個實例，來進行 delegate pattern 的範例

## MontionManager - 偵測 xyz 軸跳動方向，當滿足移動程度時，就發訊號給當下的 VC，這個類不一定只用在一個 VC 上

先實作 MotionManager，MotionManager 的單一職責為 CoreMotion 滿足移動量時的觸發，但這個類不處理 UI 和使用者的互動。

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

接下來，就可以在 VC 中，將 CoreMotion 的功能，讓 MotionManager 處理，這個 VC 不處理 Motion 相關邏輯，只在滿足特定條件時，經過 delegate func 觸發對應的 UI 行為。

```swift

import UIKit

/// 偵測 Motion 時在畫面上的 VC
class MotionDetectViewController: UIViewController {
    
    /// 這個 vc 是 MotionManager 的 delegate，會在 delegate func 中處理 UI 和 user 互動
    private lazy var motionManager: MotionManager = {
        let manager = MotionManager()
        manager.delegate = self
        return manager
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        /// 實作省略
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
        /// VC 處理裝置沒辦法啟動 motion detect
    }
    
    func deviceIsMoving(accerlationX: Double, accerlationY: Double, accerlationZ: Double) {
        /// VC 處理裝置達到移動值的狀態
    }
    
    func deviceUpdateGotError(_ error: Error?) {
        /// VC 處理裝置出現 error 的狀況
    }
}
```

## 陀螺儀 Manager - 偵測東南西北的指針，看是否達到某個角度

```swift
import Foundation
import CoreLocation

protocol NorthDetectorDelegate: AnyObject {
    func isHeadingNorth()
}

/// CLLocationManager 的權限確認省略，請記得自行加上權限確認
class NorthDetector: NSObject, CLLocationManagerDelegate {
    
    private lazy var locationManager: CLLocationManager = .init()
    
    weak var delegate: NorthDetectorDelegate?
    
    override init() {
        super.init()
        /// CLLocationManager 的權限確認省略，請記得自行加上權限確認
        locationManager.delegate = self
    }
    
    func startDetection() {
        locationManager.startUpdatingHeading()
    }
    
    func stopDetection() {
        locationManager.stopUpdatingHeading()
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateHeading newHeading: CLHeading) {
        let heading = newHeading.magneticHeading
        if (heading >= 0 && heading < 22.5) || (heading >= 337.5 && heading <= 360) {
            print("Is heading north")
            delegate?.isHeadingNorth()
        }
    }
}
```

```swift

import UIKit

/// 偵測裝置是否朝北時的 VC
class NorthDetectViewController: UIViewController {
    
    private lazy var northDetector: NorthDetector = {
        let detector = NorthDetector()
        detector.delegate = self
        return detector
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        /// 實作省略
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        northDetector.startDetection()
    }
    
    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        northDetector.stopDetection()
    }
}

extension NorthDetectViewController: NorthDetectorDelegate {
    func isHeadingNorth() {
        /// 處理朝北時的 UI 事件
    }
}

```

## 使用 delegate pattern 的好處

能讓你的物件具備「單一職責原則」，以上面的例子來說，`MotionManager` 只處理運動量的偵測，但不處理 UI。只負責在滿足運動量時，將訊號傳給 VC。VC 不處理運動量的偵測，只負責在運動量滿足條件時，負責呈現對應的 UI。

第二個例子是朝向北方的偵測，`NorthDetector` 只處理是否朝向北方，不處理 UI。只負責在朝向北方時，將訊號傳給 VC。VC 不處理北方的偵測，只負責在朝向北方時，負責呈現對應的 UI。

**注意，第二個例子的範例 code 省略了權限的確認。**

從上面的例子可以看到，一個專案裡面也可能有其他頁面會發動**運動量的偵測**和**裝置是否朝北**。因這兩個邏輯已實作在 manager 裡面了，只要 VC 在實作的時候將 manager init 起來，並設定好 delegate，就可以針對不同 UI response，進行開發。

### CLLocationManager 權限確認

注意上面的範例使用了 CoreLocation 框架，但這個框架在使用前需要取得使用者權限，而這個權限在不同的 iOS 時代有不一樣的 response。建議參考 [Apple 官方文件](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/1423640-authorized) 進行權限的實作。

## delegate func 命名習慣

在 Cocoa framework 裡面，你可以看到很多 delegate func 前面有 did, will。可以這樣思考
- 在 delegate 發動的時候，是指「某件事」準備要開始 -> 用 `will`。例：tableView delegate 中有 cell willDisplay，表示 cell 在出現「之前」會發動此 func
- 在某件事做完後 -> 用 `did`， cell didEndDisplaying ，就表示 cell 在 display 「結束」了後，才會發動此 func

## 不該使用的場合

delegate 適用於 1 對 1 傳值，如果你的情境要 1 對多傳值，或是多對多傳值，請不要使用 delegate pattern。在 Swift 裡面，你可以用 closure 或 NotificationCenter 進行不是 1 對 1 的傳值。

### 參考網站

[iOS 位置權限文件](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/1423640-authorized)