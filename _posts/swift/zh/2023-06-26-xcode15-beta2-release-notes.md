---
layout: single
title: Xcode 15 beta 2 Release notes ChatGPT 繁中翻譯
date: 2023-06-26 16:30 +0800
category: swift
author: Marvin Lin
tags: [Swift, Xcode, release notes]
summary: This article talking about Xcode 15 beta 2 release notes. Marvin Lin use ChatGPT to translate the release notes to traditional Chinese.
permalink: /swift/:title:output_ext
---

以下是 Xcode 15 beta 2 的 Release notes，將將整個文字丟入 ChatGPT 後翻譯出來的繁體中文結果。

### 概觀
Xcode 15 beta 2 包括 iOS 17、iPadOS 17、tvOS 17、watchOS 10、macOS Sonoma 和 visionOS 的 SDK。Xcode 15 beta 2 版本支援在 iOS 12 及更高版本、tvOS 12 及更高版本、watchOS 4 及更高版本上進行設備上的調試。Xcode 15 beta 2 需要在運行 macOS Ventura 13.4 或更高版本的 Mac 上使用。

### 一般
Xcode 15 Beta 2 中已解決的問題
修復：Catalyst 應用程式連結 GameKit 框架的單元測試在啟動時會因 dyld 的「找不到符號」錯誤而崩潰。 (109730080)

### 已知問題
如果任何圖層小於 1024x1024 像素，visionOS 應用程式圖示在主畫面中不會顯示視覺效果（深度、動畫、邊緣紋理）。Xcode 對此行為不提供警告或錯誤訊息。 (107568059)

解決方法：使 visionOS 應用程式圖示的所有圖層都為 1024x1024 像素 (@2x)，並在每個圖層的 Asset Catalog 檢視器中啟用「置中於畫布」和「匹配內容圖像」選項。

使用 Xcode 15 無法進行針對 AMD 硬體和 macOS Ventura 的離線編譯。 (108372489)

解決方法：使用 Xcode 14 創建針對 AMD 硬體的 macOS Ventura 相容的離線編譯二進位檔。

運行 iOS 17 的裝置在使用 USB 纜線連接到 Mac 時，可能會連續快速提示用戶兩次信任該 Mac。第二個信任提示可能會遮擋第一個提示，使用戶無法輸入密碼。 (109539668)

解決方法：要設定 iOS 裝置信任該 Mac，請在任何未被遮擋的密碼螢幕上點擊「信任」並輸入裝置密碼。然後斷開並重新連接 iOS 裝置至 Mac。iOS 裝置可能會再次提示信任該 Mac。要接受，請點擊「信任」並再次輸入裝置密碼。

當 Apple Vision Pro 透過無線配對但目前未連接時，Xcode 的「Apple Vision（專為 iPad 設計）」選項中會缺少運行目標。此狀態下，Xcode 的「設備和模擬器」視窗將顯示「Apple Vision Pro 將按需連接」的訊息。 (109744525)

解決方法：在「設備和模擬器」視窗中，對 Apple Vision Pro 進行控制點擊或右鍵點擊，然後點擊「連接」。

Xcode 15 可能無法與運行 iOS 17+ 和 tvOS 17+ 的裝置以及與運行 iOS 17+ 的 iPhone 配對的手錶通訊，如果某些 VPN 啟用的話。 (110337781)

解決方法：停用 VPN 以與裝置互動，並聯絡 VPN 供應商解決問題。

在 macOS Sonoma 上，當嘗試自動安裝命令列工具（例如執行 xcode-select --install 後），您可能會收到一個錯誤訊息，指出這些工具目前無法使用。 (110346766)

解決方法：手動安裝命令列工具，或在終端中執行以下命令：

sudo mkdir -p /Library/Developer/CommandLineTools
sudo touch /Library/Developer/CommandLineTools/.beta
然後再試一次。

---

### 應用程式捷徑預覽
已知問題
如果一個應用程式新增了一個與相應的 AppShortcuts.strings 或 AppShortcuts.xcstrings 檔案中已存在的 App 捷徑觸發片語相同的字串，重新編譯後，應用程式捷徑預覽可能不會更新。 (109494636)

解決方法：在重新編譯應用程式之前進行清理操作，使應用程式捷徑預覽處於最新狀態。

資源目錄
已知問題
當嘗試查看 visionOS 資源目錄時，Xcode 可能會崩潰。 (110739616)

---

### Console
已知問題
在 macOS Ventura 13.3 上運行時，從 Xcode 啟動時禁用「除錯執行檔」的可執行文件會將 NSLog 調用的輸出在 Xcode 調試控制台中重複顯示兩次。 (106648026)

解決方法：升級到 macOS 13.4。

在調試控制台中顯示的 os_log 訊息的最大允許大小比之前的 Xcode 版本更小。這可能導致較長的訊息在調試控制台中更常被截斷。 (109381234)

解決方法：在項目中配置運行方案操作，將環境變數 IDELogRedirectionPolicy 的值設為 oslogToStdio，以通過標準輸入輸出流進行日誌流式傳輸，並增加大小限制。該策略禁用 os 日誌的結構化元數據。

### Debugging
已知問題
無法從 LLDB 表達式求值器中調用外部 Swift 宏。 (109854291)

---

### DeviceDiscoveryUI
已知問題
在構建 tvOS 模擬器時，DeviceDiscoveryUI 不可用。 (109224355)

### 設備
已知問題
運行 iOS 17 的設備不支援從 Xcode 15 啟動的應用程式指定「Routing App Coverage File」。(80105713)

Xcode 的「設備和模擬器」視窗無法準確顯示連接到 Mac 的設備的顏色。(98003308)

當使用者從「設定」應用程式重新命名設備時，Xcode 不會自動刷新運行 iOS 17、watchOS 10 或 tvOS 17 的設備名稱。(98406919)

解決方法：退出並重新啟動 Xcode。

Xcode 的「設備和模擬器」視窗不會顯示安裝在運行 iOS 17、watchOS 10 和 tvOS 17 的設備上的應用程式圖示。(108568165)

當 Xcode 透過無線連接到運行 iOS 17 的設備時，當設備使用 USB 纜線連接到 Mac 時，Xcode 不會自動切換到使用最快的連接方式。如果無線連接速度比 USB 連接慢，Xcode 可能會繼續使用無線連接與設備通訊。 (109466074)

解決方法：在 Mac 上禁用並重新啟用 Wi-Fi 以中斷無線連接。Xcode 將自動通過 USB 重新連接到設備。

---

### Instruments
Xcode 15 Beta 2 的新功能
Instruments 15 包含了一個新的 RealityKit Trace 模板。此模板包含了幾個新的工具，用於在 visionOS 上進行應用程式和遊戲的性能分析。RealityKit Frames 工具將視覺化渲染一個幀的不同階段。RealityKit Metrics 偵測渲染堆疊中的瓶頸，並提供建議和關鍵指標以診斷和消除渲染瓶頸。這些關鍵指標包括 CoreAnimation 統計數據、3D 渲染統計數據、RealityKit 系統 CPU 時間、系統功耗影響等等。(104091516)

---

### Metal
已知問題
Xcode 的 GPU 調試服務會自動嘗試連接到所有運行 iOS 17、watchOS 10 和 tvOS 17 的設備，這些設備已在本地區域網路中被發現。如果設備信任 Mac，它將接受連接，並可能比一般待機設備更快地耗盡電池電量。(108682066)

解決方法：如果你不打算從 Xcode 開發使用該設備，請在 Xcode 的「設備和模擬器」視窗中，右鍵點擊設備，然後選擇「取消配對」。如果你希望在該設備上進行開發，請將其連接到電源來減輕電池耗盡的問題。

---

### Organizer
已知問題
從 TestFlight 在 visionOS 上安裝的 iOS 應用程式崩潰可能不會出現在 Organizer 的崩潰部分中。(107965403)

解決方法：在 App Store Connect 中的你的應用程式的「定價和可用性」部分，啟用允許你的應用程式在 visionOS 上運行的核取方塊。

---

### Particle Emitters
已知問題
在 Reality Composer Pro 中添加粒子發射器或載入粒子發射器可能會導致在基於 Intel 的 Mac 上崩潰。(110794948)

---

### Previews
Xcode 15 Beta 2 中已解決的問題
修正：在 Seed 2 上編譯並在 macOS 15.0 Seed 1 上運行，或反之亦然時，預覽將崩潰。(110649872)

已知問題
在由 watchOS 應用程式和 iOS 應用程式共用的小工具中預覽檔案時，預覽可能會失敗。(108017929)

使用固定位置並導航到不與固定預覽相同目標的檔案時，預覽將失敗。(108738163)

預覽畫布中的時間軸條目可能不會更新。(109223294)

解決方法：關閉並重新開啟預覽畫布。

返回 UIViewController 和 NSViewController 的預覽實例始終遵循安全區域。(109281049)

解決方法：將您的視圖控制器封裝在一個 UIViewControllerRepresentable 中並附加 ignoresSafeArea 修改器。

當採用 #Preview 宏語法時，部署目標 < iOS 17.0 的專案可能無法編譯。(109428179)

解決方法：可以在 #Preview 上添加 @available 注釋。

在預覽中連接新設備到 Mac 時，預覽畫布中的設備選擇器不會刷新。(109661791)

解決方法：打開方案編輯器並在不進行更改的情況下關閉它。

在 macOS 13 上創建的新小工具專案無法建構。(109897205)

解決方法：移除模板中的 containerBackground 修改器。

使用 Apple Vision Pro 預覽內容時，有時會出現陳舊的內容。(110509660)

解決方法：等待更新的內容出現。

當在相同模塊中定義的 Swift 類型擴展中的符號無法在 #Preview 中引用時，將使用 PreviewProvider，或直接將擴展的實現複製到 #Preview 本身或將其設為全局符號。(110671628)

---

### Reality Composer Pro
已知問題
底部面板顯示的統計數據在展開的動畫部分中不顯示具有動畫的物件。(103162531)

底部面板顯示的統計數據在計算紋理時忽略了 Shader Graph Materials。(109681637)

在從 Studio Display 切換音頻設備到其他設備（如 AirPods 或內建揚聲器）後，Reality Composer Pro 可能會意外退出。(109912081)

解決方法：保存項目並退出 Reality Composer Pro，切換音頻輸出設備，然後重新加載項目。

在選擇模式下，底部面板顯示的統計數據可能會將資源計數兩次（例如，同一紋理計數兩次）。(110007062)

當場景中未選中任何項目時，複製和粘貼菜單項目可能在編輯菜單中被禁用。(110181840)

解決方法：在視口中打開上下文菜單進行粘貼，或先選中任何項目。

某些庫資源無法通過點擊下載按鈕或使用下載菜單項目進行下載。(110209688)

解決方法：將項目從庫拖動到主視口以啟動下載。

在從 Reality Composer Pro 導出場景為 USDZ 文件時，某些圖像格式將按原樣導出，導致生成的 USDZ 文件無效。(110538624)

場景層級結構中的鎖定項目仍然允許執行編輯操作。(110545827)

音頻資源 "AtmosphereJungle" 不能加載，並將在後續版本中被移除。(110725118)

---

ShazamKit
已知問題
SHManagedSession.State 不可用。(109670750)

SHLibrary.default.items 不可用。(109670918)

SHManagedSession 在模擬器上不起作用。(109672477)

解決方法：使用實體設備。

---

### 簽名和分發
已知問題
Xcode Organizer 窗口中的 TestFlight 內部測試分發支持目前不可用。(106239462)

Xcode Organizer 窗口中的簡化分發方法不支持與使用自定義工作流時可用的所有錯誤恢復選項相同的功能。例如：使用簡化分發的方式上傳應用時，如果沒有應用記錄，Xcode 會顯示錯誤，而不允許您創建應用記錄。(109097705)

解決方法：使用自定義方法。

---

### Simulator
Known Issues
在使用 iOS 14 或更高版本的模擬器運行時，狀態欄覆蓋可能被設置錯誤。(101511614)

當使用 #Preview 宏定義的 iOS 應用目標 Apple Vision Pro (Designed for iPad) 時，可能會意外退出。(110801867)

解決方法：註釋掉 #Preview 宏定義，使用傳統的 PreviewProvider API。

---

### Source Control
已知問題
上游更改可能會在 Xcode 編輯器中顯示為暫存更改。(109285038)

---

### Source Editor
已知問題
在某些情況下，從其他宏擴展中展開的宏可能無法完全顯示。(107718413)

宏擴展中不顯示實時問題。(108375601)

如果當前工具鏈不匹配所選的 Xcode，打開文件時，源代碼編輯器可能會出現短暫的停頓。(109723219)

解決方法：運行 xcode-select -s /Applications/YourXcodePath.app。

---

### StoreKit Testing in Xcode
Known Issues
在事務管理器中通過“訂閱選項”對話框編輯自動續訂訂閱時，會創建一個新的事務，但續訂被禁用。這導致新選擇的訂閱到期並且不會續訂。(109403724)

---

### StoreKitTest
已知問題
新的 StoreKitTest API 在 SDK 中不可用。受影響的 API 包括：setSimulatedError(_:forAPI:)、simulatedError(forAPI:) 和 buyProduct(identifier:options:)。(110547289)

---

### Swift

已知問題
非可拷貝（Noncopyable）類型目前無法在元組中使用，也無法作為泛型類型使用。特別是，這意味著它們無法存儲在陣列（Arrays）、字典（Dictionaries）或集合（Sets）中，也無法形成非可拷貝類型的選擇性（Optionals）或打印它們。(104669935)

在啟用庫演進模式時，非可拷貝類型目前無法正常工作。(107371421)

借用（borrowing）和消耗（consuming）參數修飾符只能用於非可拷貝類型的參數。在可拷貝類型的參數上使用這兩個修飾符將導致編譯錯誤。(108383660)

非可拷貝類型無法在其 deinit 方法中進行變異（mutate）或消耗（consume）自身。(108682993)

無法在泛型非可拷貝類型的消耗方法中丟棄自身。（108975216）

如果一個~Copyable類型包含了泛型或協議類型的存儲屬性，那麼嘗試訪問該類型的計算屬性可能會導致編譯器崩潰。

例如：
```swift    
struct Foo<T> : ~Copyable {
var value: T

var property: Int { return 0 }
}
(109161396)
```
解決方法：嘗試將泛型或協議類型的字段封裝在一個類實例中。例如：

```swift
class Box<T> {
var value: T
init(value: T) { self.value = value }
}

struct Foo<T>: ~Copyable {
private let box: Box<T>
var value: T { return box.value }

var property: Int { return 0 }
}
```

在引入新變量的 if 或 switch 表達式中，當該 if 或 switch 用於賦值時，可能會產生虛假的“無法在作用域中找到'variableName'”錯誤。(109192116)

逃逸閉包目前會消耗非可拷貝的捕獲值，而不是按照 SE-390 中指定的借用（borrowing）方式。(109217216)

當消耗非可拷貝類型並重新賦值時，lldb 不再在當前框架中顯示該變量。(109218404)

對非可拷貝變量應用消耗運算符會導致不必要的拷貝。(109222496)

解決方法：使用 let _ = variableName 來消耗該值。

在嘗試對可選鏈進行賦值時，if 或 switch 表達式可能會產生虛假的“僅可在...中使用”錯誤。(109305454)

具有大量擴展的 Swift 模塊可能會遇到編譯時間過長的問題。(109543968)

具有在定義文件之外被引用的非可拷貝類型的 deinits 將導致編譯時崩潰。(109679168)

非可拷貝枚舉不能有 deinit 或包含 indirect 案例，與 SE-390 不同。(109686538)

解決方法：若要為枚舉添加 deinit，請在相關案例中添加帶有 deinit 的結構體。若要解決 indirect 案例，請將枚舉的 payload 包裝在一個類中。

在某些情況下，使用 _ = x 來抑制關於借用參數的“未使用變量”警告可能會引發不正確的“無法被消耗”的錯誤。(109958008)

解決方法：使用 _ 作為綁定名稱標記參數為未使用：

```swift
func method(parameter _: borrowing Type) {
}
```

---

### Swift 和 C++ 互操作性
已知問題
從 Swift 中調用 std::string 值的 append 函數可能會導致編譯器崩潰。(107018724)

解決方法：在需要時，使用 += 運算符將內容添加到 C++ 字符串，而不是使用 append。

在啟用調試時，為 C++ 類型添加初始化器的 Swift 擴展可能會導致編譯器崩潰。(107561753)

在 Swift 中使用一個 C++ 類模板的多個特化可能會導致重複定義的鏈接錯誤。(107757051)

無法使用 Swift 中的 Set 值初始化 C++ 的 std::set 類型。(107909624)

Xcode 的程式碼補全結果在 Swift 代碼中有時會顯示具有不正確參數類型（Any）的 C++ 方法。(108855791)

Xcode 在 Swift 中不會為 C++ 命名空間成員提供程式碼補全結果。(109714059)

通過 SWIFT_COMPUTED_PROPERTY 注解將 C++ 成員作為屬性導入到 Swift 中，Swift 文件中的索引無法正確工作。(109714153)

包含 Objective-C 指針數據成員且沒有其他非平凡數據成員或特殊成員函數的 C++ 結構或類型，在 Intel 架構上從 Swift 中調用的 Objective-C 方法中傳遞不正確，導致運行時行為不正確或崩潰。(109714315)

---

### Swift Packages
已解決的問題（在 Xcode 15 Beta 2 中）
修復：在項目編輯器中查看套件依賴時，任何具有 Exact Version 規則的套件的版本號都會重置為 1.0.0。(110303613)

已知問題
當目標目的地是 macOS 以外的平台時，Swift 宏可能無法構建。(110541100)

解決方法：選擇 macOS 目的地進行構建，或從 package.swift 中刪除 .testTarget。

### SwiftData
已知問題
在刪除項目後，SwiftUI 在動畫期間可能嘗試引用已刪除的內容，導致崩潰。(109838173)

解決方法：在刪除後明確保存。

### Test Navigator
已知問題
測試套件偶爾顯示為“(Missing Suite)”。(109423329)

解決方法：打開其他導航器，然後重新打開測試導航器。

### TestFlight
已知問題
具有低於 6.0 的最小部署目標的 watchOS 應用可能無法正確安裝 TestFlight。(109797881)

解決方法：暫時將最小部署目標設置為 6.0 或更高。

測試
Xcode 15 Beta 2 中的新功能
watchOS 上的 UI 測試現在會在未處理的情況下自動關閉警報窗口。(59571331)

已解決的問題（在 Xcode 15 Beta 2 中）
現在為 Objective-C 測試啟用了完整的例外處理，這可能導致某些對象在以前泄漏時被釋放或解構。(47727351)

---

UI Automation
已知問題
當 UI 自動化運行時，visionOS 沒有任何視覺指示。仍需要輸入設備的密碼才能開始 UI 自動化。(85512012)

UI 測試
已知問題
選擇截圖而非屏幕錄製的 UI 測試可能無法看到附加的截圖。(109908952)

VideoToolbox
已知問題
canImport(VideoToolbox) 在 watchOS 上不返回 false。(109324910)

解決方法：使用條件 !os(watchOS)。


---

### visionOS 模擬器
已知問題
沒有用於模擬 Apple Vision Pro 的沉浸式皇冠的用戶界面。(109429267)

解決方法：使用 XCTest 的 XCUIDevice.rotateDigitalCrown(delta:) 方法。

模擬器不支持 Spatial Audio 的所有功能。您可以使用模擬器測試部分音頻功能，但最終測試應在實際設備上進行。(109912117)

僅在 Intel Mac 上運行時，visionOS 模擬器的紋理容量有限。渲染某些材質可能導致模擬器重新啟動。(110746210)

僅在 Intel Mac 上運行時，在 visionOS 模擬器上，Diorama 示例應用程序將崩潰。(110864503)

---

### Xcode
已知問題
在將任何設備從「一般 > 支援的目標」中添加或刪除後，「Apple Vision (Designed for iPad)」運行目標將從可用目標中消失。「顯示 Apple Vision (Designed for iPhone & iPad) 目標」建構設置將自動設置為 No，但 Apple Vision (Designed for iPhone & iPad) 仍然保留在支援的目標清單中。在添加或刪除其他設備類型時，可能會自動添加「Designed for iPad」目標。(110810619)

解決方法：在修改「支援的目標」清單後，將「顯示 Apple Vision (Designed for iPhone & iPad) 目標」建構設置設為 Yes。

---

### Xcode Cloud
已知問題
在為 Xcode Cloud 上的新產品進行設置後，可能會立即顯示「無法打開編輯器」對話框。(109781276)

解決方法：關閉對話框。

Xcode Cloud 目前不支援 visionOS 的測試操作。(110793833)

---

### Updates in Xcode 15 Beta

### General
已解決的問題 (Xcode 15 Beta)
修復：現在可以直接在 canvas 中與 macOS 預覽互動。您可以按住實時預覽模式按鈕，在 Xcode 和應用程序預覽之間切換。(49271058)

修復：對於在 iOS 17 或更高版本上進行鏈接的應用程序，URL 解析已從過時的 RFC 1738/1808 解析更新為與 URLComponents 相同的 RFC 3986 解析。這統一了 URL 和 URLComponents API 的解析行為。現在，URL 會自動對無效字符進行百分比編碼或 IDNA 編碼，以幫助創建有效的 URL。

要檢查 urlString 是否嚴格符合 RFC，請使用新的 URL(string: urlString, encodingInvalidCharacters: false) 初始化程序。該初始化程序將所有字符保持不變，如果 urlString 明確無效，則返回 nil。(93368104)

修復：Xcode 更可靠地固定了跨多行的 Swift 函數聲明，以便與 Xcode 的“滾動時顯示代碼結構”功能配合使用。(94476783)

修復：控制台、Safari 和 Accessibility Inspector 無法無線連接到運行 iOS 和 tvOS 16.4 和 16.5 的設備。(108032308)

修復：在系統內存壓力下，測試可能因“與 testmanagerd 的連接丟失”而失敗。(109163111)

修復：首次嘗試時可能無法下載平台。(110278080)

Apple Clang 編譯器
Xcode 15 Beta 的新功能
有一個關於 Apple 平台上 C++ 支持的新參考頁面：https://developer.apple.com/xcode/cpp/。(100245338)

Clang 和構建系統支持一種名為“explicit modules”的模塊依賴項構建模式，它提高了構建性能、可靠性和正確性。新模式是可選的，可以通過在使用模塊的 C 和 Objective-C 項目中設置 _EXPERIMENTAL_CLANG_EXPLICIT_MODULES 作為用戶定義的構建設置來啟用。(104438594)

在 C 和 C++ 中，現在禁止使用寬多字符字面量，例如 L'ab'，之前會將其解釋為 L'b'。這個變化的動機在字符字面量 P2362 中有說明。

已實現以下 C++20 語言功能：

完全實現了立即函數 [consteval]。(P1073R3)

已實現以下 C++23 語言功能：

取消對 volatile 複合操作的棄用。(P2327R1)

支援 #warning。(P2437R1)

界定的轉義序列。(P2290R3)

命名通用字符轉義。(P2071R2)

支援將 UTF-8 作為可移植源文件編碼。(P2295R6)

放寬對 wchar_t 的要求，以匹配現有實踐。(P2460R2) (108334479)

已解決的問題 (Xcode 15 Beta)
改進了 ARC 優化器，使 Objective-C 和 Swift 對象可以更早地被銷毀。這會導致依賴弱引用或無主引用而無需對目標對象進行強引用的代碼出現問題或崩潰。例如，這可能會在不必要地在一次性異步塊回調中使用“弱 self”捕獲的代碼中意外發生。(108386578)

x86 矢量化器使用飽和算術指令，可以獲得更短且更快的代碼。這可能會改變程序的行為，對於隱含依賴溢出行為的應用程序，例如將浮點值轉換為無法表示原始值的整數類型。(108386879)

---

Xcode 15 Beta 中已解決的問題：

修正：ARC 優化器的改進使得 Objective-C 和 Swift 對象可以更早地被銷毀。這導致依賴於弱引用或無主引用而保持有效的代碼在沒有對目標對象進行強引用的情況下出現問題或崩潰。例如，在一次性異步塊回調中不必要地使用了"weak self"捕獲的代碼可能會發生這種情況。 (108386578)

修正：x86 矢量化器使用飽和算術指令，可以產生更短更快的代碼。這可能會改變應用程序的行為，例如，將浮點值轉換為無法表示原始值的整數類型時，應用程序可能會隱式依賴溢出行為。 (108386879)

資源目錄：
Xcode 15 Beta 中的新功能：

Xcode 現在為資源目錄中的每個顏色和圖像生成 Swift 和 Objective-C 符號。這些符號提供了一種更安全、更易於使用的引用資源的方式，可以防止重命名和拼寫錯誤，利用編譯器的類型檢查功能，並與代碼完成集成。
Swift 資源符號生成為 ColorResource 和 ImageResource 類型的靜態屬性。可以使用 SwiftUI、UIKit 和 AppKit 的初始化器來實例化顏色和圖像。
Objective-C 資源符號提供為字符串常量，可以通過導入 "GeneratedAssetSymbols.h" 標頭文件來訪問。
資源符號生成默認情況下為啟用，但可以通過設置 "Generate Asset Symbols" 的構建設置來禁用。
默認情況下為 SwiftUI、UIKit 和 AppKit 生成符號支持，但可以使用 "Generate Swift Asset Symbol Framework Support" 的構建設置進行自定義。
Xcode 15 Beta 中已解決的問題：

修正：在"添加新資源"菜單中現在有一個"帶有命名空間的文件夾"項目，用於創建帶有命名空間的新文件夾。 (108468310)

---

### Build System：
Xcode 15 Beta 的新功能：

存檔構建現在支持與其他構建操作相同的一組積極編譯優化，提高構建性能。 (98526053)
Xcode 現在會自動為項目中的動態庫和框架生成中間的基於文本的動態庫 (TBD) 文件。這些存根允許更準確地跟踪鏈接器依賴關係，這意味著不會改變導出符號集的更改不再需要重新鏈接所有的傳遞依賴關係，從而加快增量構建的速度。 (99972271)
Xcode 現在支持構建和使用在 Swift Packages 中定義的宏。 (101818756)
Xcode 15 Beta 中已解決的問題：

修正：使用"複製文件"構建階段嵌入靜態框架時，現在會從框架中刪除靜態存檔，當它被嵌入到目標捆綁包中時。可以將 REMOVE_STATIC_EXECUTABLES_FROM_EMBEDDED_BUNDLES 構建設置設置為 NO，以選擇退出此行為。以前在傳統構建系統中使用的 COPY_RESOURCES_FROM_STATIC_FRAMEWORKS 構建設置，用於從靜態框架中提取和複製資源到目標捆綁包，對於新的構建系統已不再起作用，因為整個框架都被複製（如上所述，不包括靜態存檔）。 (47164939)
修正：在增量構建後，Swift 文件中的構建警告有時會消失的問題。 (105421512)
修正：如果未使用 Xcode 生成用於 App Store 提交的內容，則需要將 xcarchive 中的 Signatures 文件夾添加為附加內容。 (106438176)
修正：當在具有覆蓋文件類型的文件上使用預處理或組合等單文件構建操作時，現在可以正常工作了。以前，可能會出現"缺少輸入且沒有構建規則可用"的錯誤。 (107736241)
修正：在運行項目的常規構建後，依賴框架的本地化導出可能會失敗的問題。 (108867135)
Xcode 15 Beta 中的棄用功能：

刪除了對 Bitcode 的支持，ENABLE_BITCODE 構建設置不再起作用。 (105281961)

---

### C++標準庫：
Xcode 15 Beta 的新功能：

實現了以下新功能：

實現了 C++17 中的 <memory_resource> 库
P2499R0 - string_view 範圍構造函數應該是 explicit 的
P2417R2 - 更多 constexpr bitset
P2445R1 - std::forward_like
P2273R3 - 使 std::unique_ptr 成為 constexpr
P0591R4 - 用於實現使用分配器的構造的實用函數
P2291R3 - 在 <charconv> 標頭中為整數類型的函數 to_chars 和 from_chars 添加 constexpr 修飾符
P0220R1 - 採用 C++17 的 Library Fundamentals V1 TS 組件
P0482R6 - char8_t：用於 UTF-8 字符和字符串的類型
P2438R2 - std::string::substr() &&
P0600R1 - 在庫中使用 nodiscard
P0339R6 - polymorphic_allocator<> 作為一個詞彙類型
P1169R4 - 實現了 static operator() 的庫部分
P0415R1 - constexpr for std::complex
P1208R6 - std::source_location
P0323R12 - std::expected
P1035R7 - 輸入範圍適配器
P2325R3 - Views 不應該要求是可默認構造的
P2446R2 - views::as_rvalue
P1020R1 - 使用默認初始化進行智能指針創建
P2210R2 - 優越的字符串分割
copy、move、copy_backward 和 move_backward 的 ranges 版本現在也對 std::deque<>::iterator 進行了優化，這可以在某些算法上提供多達 20 倍的性能改進。

copy、move、copy_backward 和 move_backward 的 std 和 ranges 版本現在也對 join_view::iterator 進行了優化，這可以在某些迭代器和算法的組合上提供多達 20 倍的性能改進。 (108380402)

---

Xcode 15 Beta 中的棄用功能：

#### 以下項目已被棄用或移除：

在 C++17 和更新的標準模式中不再提供 unary_function 和 binary_function。可以通過 _LIBCPP_ENABLE_CXX17_REMOVED_UNARY_BINARY_FUNCTION 重新啟用它們。

從 libc++ 中刪除了幾個附帶的遞歸包含項。這些包含項基於使用的語言版本進行了刪除。如果在升級後的代碼中出現與缺少 std:: 實體相關的錯誤，請確保您包含了所有所需的頭文件。

整數類型的 to_chars 和 from_chars 函數僅在 C++17 起可用。libc++ 在 C++11 和 C++14 中提供了這些函數作為一個未記錄的擴展。該擴展使得實現這些函數的 C++23 規範變得困難，因此該擴展已被刪除。
已刪除了 _LIBCPP_ENABLE_CXX03_FUNCTION 宏，該宏允許重新啟用現已棄用的 C++03 std::function 實現。需要使用 std::function 的用戶應切換到 C++11 或更高版本。

<experimental/memory_resource> 的內容現在已被棄用，因為 libc++ 現在提供了 <memory_resource>。請改用 <memory_resource>。根據 libc++ 的 TS 棄用政策，<experimental/memory_resource> 將在下一個版本中被移除。

std::char_traits 的基本模板已被標記為棄用，將在下一個版本中被移除。如果您正在使用 std::char_traits 與除 char、wchar_t、char8_t、char16_t、char32_t 或自定義字符類型（已對 std::char_traits 進行特化）之外的其他類型，當我們刪除基本模板時，您的代碼將停止工作。標準並不要求提供基本模板，而這樣的基本模板對於某些類型來說是不正確的，這可能會導致當前未被檢測到的意外行為。

_LIBCPP_ENABLE_NODISCARD 和 _LIBCPP_DISABLE_NODISCARD_AFTER_CXX17 不再生效。C++20 中的標準所要求的 [[nodiscard]] 應用現在始終啟用。任何擴展的應用現在默認啟用，可以通過定義 _LIBCPP_DISABLE_NODISCARD_EXT 來禁用。

在自由站立模式下，如果平台可以為該大小實現無鎖原子，則 atomic<small enum class> 不再包含鎖定字節。此 ABI 破壞僅影響使用 -ffreestanding 編譯的用戶，僅針對 atomic<T>，其中 T 是可能在平台上具有無鎖特性的非內建類型。 (108380359)

---

Console
Xcode 15 Beta 中的新功能：
默认情况下，Xcode 通过统一的日志记录和活动跟踪基础设施来流式传输 os_logs。与之前版本的 Xcode 相比，输出可能以不同的格式进行，并且相对于标准 IO 的顺序也可能发生变化。要自定义日志记录的行为，请编辑运行方案操作以设置环境变量 IDELogRedirectionPolicy。值“oslogToStdio”将 os_log 消息重定向到标准 IO，并以与之前版本的 Xcode 相同的样式进行格式化。值 stdioToOSLog 将标准 IO 重定向到 os_log 消息，并在调试控制台中以附加元数据的方式呈现它们。 (109380695)

Xcode 15 Beta 中已解决的问题：
修复：调试控制台中从 os_log 消息跳转到发出该消息的源代码行的操作仅在本地 Mac 或模拟器上调试可执行文件时受支持。在调试连接设备上的可执行文件时，菜单项将被禁用。 (109171925)

---

### Create ML
Xcode 15 Beta 中已解决的问题：
修复：在新的 macOS Seed 1 构建中，使用 Xcode 内的开发人员工具中的 CreateML 应用程序无法使用手势动作分类器和手势姿势分类器训练机器学习模型。特定的错误消息是在单击“训练”按钮时出现的“意外错误”。 (108227967)

调试
Xcode 15 Beta 中的新功能：
LLDB 现在在类型摘要中省略了默认的模板参数。

例如：

(lldb) frame variable
(std::vector<std::vector<std::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::basic_string<char, std::char_traits<char>, std::allocator<char> > > >, std::allocator<std::vector<std::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::basic_string<char, std::char_traits<char>, std::allocator <char> > > > > >) nested = size=0 {}
现在显示为：

(lldb) frame variable
(std::vector<std::vectorstd::string >) nested = size=0 {}
通过使用 frame variable --raw-output 选项，仍然可以查看默认参数。 (101329922)

LLDB 现在支持在表达式求值中引用泛型类型参数。例如，给定以下代码：

func use<T>(_ t: T) {
print(t) // 在此处设置断点
}

use(5)
use("Hello!”)
当在 use 处停止时，运行 po T.self 将在第一次调用中打印 Int，并在第二次中打印 String。这在与条件断点组合使用时特别有用，可以仅在泛型函数实例化为特定具体类型时停止。例如，将以下表达式作为断点的条件添加到 use 内部时，只有当变量 t 为 String 时才会停止：T.self == String.self。 (101976441)

Xcode 现在显示 AppKit 运行时问题，例如通过代码构建的自动布局约束问题。 (105229806)

创建监视点时，可以看到其祖先路径层次结构。这可以为您提供更好的上下文，尤其是在发生冲突时。 (106777931)

Xcode 15 Beta 中已解决的问题：
修复：当您尝试从菜单中附加时，Xcode 不再显示僵尸进程。以前在筛选要调试的实际进程时，需要费力浏览这些无法调试的进程，这很令人困惑。此功能适用于所有平台。 (11113209)

修复：重新定义了 p 和 po 命令别名，将其重新定义为新的 dwim-print 命令。dwim-print 命令使用最友好的实现来打印值。“DWIM” 是“Do What I Mean”的缩写。具体来说，当打印变量时，dwim-print 将使用与 frame variable 或 v 相同的实现。

p 的输出不再包括持久的结果变量，例如 $0、$R0 等。偶尔需要持久结果的用户可以直接使用 expression（或唯一的前缀，如 expr），而不是使用 p。要每次启用持久结果，可以在 ~/.lldbinit 文件中重新定义 p 别名：

command unalias p
command alias p dwim-print --persistent-result on --
dwim-print 还为 po 提供了新功能。po 命令现在可以通过地址打印 Swift 对象。当运行 po <object-address> 时，内嵌的 Swift 编译器将使用表达式 unsafeBitCast(<object-address>, to: AnyObject.self) 进行评估。 (104348863)

---

Devices
Xcode 15 Beta 中已解决的问题：
修复：Apple Watch 模拟器现在在“设备和模拟器”窗口中作为独立的模拟器显示。 (106664675)

修复：Xcode 需要连接到互联网才能准备运行 iOS 17、watchOS 10 或 tvOS 17 的设备进行开发。当由于缺乏互联网连接而导致开发准备失败时，Xcode 不会自动重新尝试准备设备进行开发。 (109511717)

文档
Xcode 15 Beta 中的新功能：
Xcode 15 现在包括一个助理编辑器，可在您输入时实时预览 Swift-DocC 文档。

您可以通过首先激活助理编辑器（通过编辑器 > 助理）然后在助理编辑器的跳转栏中选择“文档预览”来访问文档预览。

助理编辑器支持 Swift 文件、Objective-C 头文件和文档标记文件。 (56250383)

使用 Xcode 15 构建的文档现在包括外部模块的 Swift 扩展页面。

例如，您可以扩展 SwiftUI 的 Image 结构以包含额外的初始化器：

public extension Image {
/// 从给定的树懒创建图像。
///
/// 此初始化器对于显示静态树懒图像很有用。
/// 要创建包含树懒的交互式视图，请使用SlothView。
///
/// 一个冰树懒的屏幕截图，下方显示文本“冰树懒”。
init(_ sloth: Sloth) {
self.init("(sloth.power)-sloth")
}
}
该初始化器的文档现在将与您的项目的其他文档一起包含在内。

如果您希望排除这些页面，请将 DOCC_EXTRACT_EXTENSION_SYMBOLS 构建设置设置为 NO。有关详细信息，请参阅构建设置参考。 (63987302)

为了支持从其他文档工具更轻松迁移，Swift-DocC 现在支持一些基本的 Doxygen 样式命令，如 @param 和 @returns。 (69835334)

文档链接的诊断现在包括关于链接失败的详细信息，并提供建议如何更新链接以引用已知符号。 (73903936)

Swift-DocC 现在通过使用 @Row、@TabNavigator、@Links 和 @Metadata 等新指令来支持使用完全自定义布局设计页面。了解更多信息，请参阅 API 文档。 (97705029)

使用 Xcode 15 构建的 Swift-DocC 网站现在包括快速导航功能，可以通过激活键盘快捷键并输入页面名称直接导航到页面。在浏览 Swift-DocC 网站时，按下 Shift+Cmd+O 或 Shift+/ 来激活新的快速导航弹出窗口。 (100346089)

Xcode 15 Beta 中已解决的问题：
修复：Swift-DocC 现在正确地允许您使用 Markdown 的链接语法自定义 API 链接的标题。

SlothCreator 包含一些您可以喂给虚拟树懒的不同树懒食物。
(79992417)

修复：带有 Unicode 字符的符号名称的文档链接无法解析。 (85531439)

修复：来自协议要求的符号的文档链接需要进行消歧义，以区分它们与可能的默认实现。 (98781530)

---

### Instruments
Xcode 15 Beta中的新功能
儀器現在可以在分配、洩漏和VM Tracker儀器中打開.memgraph文件，如果為進程啟用了Malloc Stack Logging，則可以可視化活動分配的時間軸。 Xcode Memory Graph調試器功能中增加了一個新的共享按鈕，可以在儀器中查看捕獲的.memgraph文件。（53014738）

Instruments 15增加了一個新的dyld Activity儀器，可以可視化與應用程序啟動性能分析相關的dlopen、dlclose、靜態初始化器和其他dyld統計信息。 dyld Activity包含在App Launch模板中，並取代了Static Initializer儀器。（106383871）

Instruments 15新增了一個新的音頻系統跟踪模板，提供了音頻和操作系統的全面視圖。它可視化應用程序如何與音頻服務器交互，使您瞭解音頻線程I/O循環和其他一般性能指標。（106843172）

Xcode 15 Beta中解決的問題
修復：大大提高了使用複雜模板（如遊戲性能、系統跟踪和金屬系統跟踪）打開新文檔的性能。（72983621）

修復了在HTTP Traffic儀器中選擇包含大型請求或響應主體的HTTP事務時應用程序卡死的問題。（87893253）

### Interface Builder
Xcode 15 Beta中的新功能
Cocoa故事板Popover演示跳躍支持全尺寸內容檢查器屬性，允許呈現的內容超出安全區域插入並超過氣泡窗的箭頭區域。（102107829）

NSView支持Clips Bounds屬性檢查器，更精細地控制視圖的內容是否應該被裁剪。（104581720）

---

### 鏈接
Xcode 15 Beta中的新功能
為了顯著提高靜態鏈接的速度，編寫了一個新的鏈接器。它是所有iOS二進制文件的默認鏈接器，以及使用“可合併庫”功能的任何人。可以通過使用-ld64明確要求使用經典鏈接器，但該經典鏈接器將在未來版本中被刪除。（108915312）

### 本地化
Xcode 15 Beta中的新功能
String Catalogs（.xcstrings）是Xcode中的一種新文件類型，可通過管理字符串並跟踪翻譯進度，輕鬆實現應用程序的本地化。Xcode會自動從源代碼中提取可本地化字符串，以使任何String Catalogs保持同步。可以在本地編輯器中查看和編輯String Catalogs，以預覽和管理項目中的本地化字符串。要開始使用，可以通過文件選擇器添加新的String Catalog，或者在菜單欄中選擇編輯>轉換>為String Catalog...，從而遷移現有的.strings和.stringsdict文件。（67254382）

本地化目錄編輯器現在在查看和編輯導出的字符串時（對於具有此信息的文件）顯示字符串的翻譯狀態。（79101944）

Xcode現在在本地化App Intents短語時給您更多靈活性。您現在可以在每個地區獨立地使用String Catalog編輯器在AppShortcuts.xcstrings中添加或刪除短語，以管理本地化字符串。（97283450）

Xcode 15 Beta中解決的問題
修復：Xcode現在在文件檢查器中從可本地化文件中刪除所有本地化時，給您提供了取消本地化資源的選項。（11795220）

修復了在導出Swift包的本地化時無法添加新的本地化的問題。現在可以使用String Catalog編輯器添加新的本地化。（92296781）

修復：Xcode現在在導出本地化時在所有平台上構建多平台目標。（99457038）

---

### Metal調試器
Xcode 15 Beta中的新功能
幾何查看器和Shader調試器現在支持Mesh和Object渲染階段。綁定資源現在支持按照Mesh管線的Shader訪問進行過濾。（81698727）

Metal調試器已更新，增強了對MetalFX的支持。您可以輕鬆導航到MetalFX調用，查看綁定資源，比較輸入和輸出結果。依賴關係查看器也已更新，您可以查看輸入依賴關係的來源，甚至查看完成升頻作業所需的時間。（101047483）

緩衝區查看器已更新，具有新功能、改進的用戶界面和性能改進。新功能包括數據搜索、列固定、列過濾和類型轉換。（101241716）

組織器
Xcode 15 Beta中的新功能
組織器中顯示了由於Foundation異常而導致的一些崩潰的異常原因。如果存在異常原因，它會顯示在Inspector中，在回溯視圖的右側顯示。（103453197）

Playgrounds
Xcode 15 Beta中的新功能
Playgrounds控制台使用了Xcode 15的新控制台，並增加了內嵌查找等功能。（42891656）

Xcode Playgrounds中的結果側邊欄顯示了該行中所有表達式的摘要，並提供了一個新的控件，可以查看有關每個表達式的詳細信息的彈出窗口。（105740414）

Playgrounds地圖模板已更新，使用了現代的MapKit API。（107284909）

Xcode 15 Beta中解決的問題
修復：Xcode Playgrounds中的結果側邊欄始終顯示最近結果的摘要，而不是結果的數量。（105108520）

修復：在Xcode Playgrounds中選擇內聯結果會突出顯示生成結果的源代碼。（105426026）

修復：SwiftUI彈簧動畫現在有專用的可視化結果。（106978230）

---

### 預覽
Xcode 15 Beta中的新功能
預覽畫布新增了一個控制項，用於選擇預覽時使用的設備。默認情況下，它跟踪所選運行目的地的設備系列，但可以選擇特定的設備。這應優先使用previewDevice修飾符。（100562366）

現在可以使用＃Preview宏創建預覽。這包括支援預覽SwiftUI、UIView＆UIViewController、NSView＆NSViewController和小部件時間軸提供程序、時間軸項目和實時活動。（101566716）

macOS預覽現在在畫布中顯示窗口外框和工具欄。（105705642）

選擇連接到Mac的設備進行預覽現在僅為該設備進行預覽。選擇模式和變體模式現在還使用連接的設備來渲染在Xcode中顯示的內容。（106208191）

Xcode 15 Beta中解決的問題
修復：在某些類型上使用@objc註釋時，預覽失敗。（96018813）

修復：在導航文件時保留畫布設置，例如畫布模式、設備設置和所選的預覽設備。（100999447）

### 簽署和分發
Xcode 15 Beta中的新功能
選擇模擬器運行目的地時，現在可用於存檔操作。使用模擬器進行存檔操作將生成適用於所選平台上所有設備的CPU架構的應用程式。（13094592）

項目編輯器中的Xcode簽署和功能選項卡現在支持添加與您的開發團隊和App ID關聯的Apple批准的受管功能。關聯的受管功能可在庫中看到，並與自動簽署一起使用。（27253063）

xcodebuild -exportArchive支持使用App Store Connect身份驗證金鑰上傳應用程式到App Store Connect和Apple驗證服務。（76036452）

Xcode現在向上傳到App Store Connect的人員發送應用程式上傳狀態推送通知。（100033585）

Xcode組織器窗口現在支持簡化的存檔分發。現在可以通過點擊一次來上傳或導出存檔。簡化的分發方法使用建議的設置。自定義方法允許選擇其他選項。（103967573）

Xcode 15 Beta中解決的問題
修復：如果您的應用程式與Game Center集成，請確保Entitlements.plist文件中存在com.apple.developer.game-center權限。之前的Xcode版本會自動將該權限注入到您的應用程式簽名中，如果它在您的設置文件中存在。這種行為與大多數其他權限不一致，已在Xcode 15中刪除。（106596235）

修復：解決了在Xcode和Xcode Cloud中“管理版本和構建號”分發選項覆蓋應用程式中框架依賴項的版本和構建號的問題。分發應用程式時，框架依賴項將保留其原始版本和構建號。（106869375）

修復：自動簽署可能無法為DriverKit驅動程序目標創建設置文件。（109588156）

---

模擬器
Xcode 15 Beta中解決的問題
修復：在運行於macOS 14 beta 1上的模擬器應用程式可能在連接遊戲控制器時崩潰。（110038857）

原始碼控制
Xcode 15 Beta中的新功能
原始碼控制操作和Xcode Cloud操作已移至新的結合的“整合”菜單，取代了“原始碼控制”菜單。（105752873）

Xcode現在完全與git的分段功能整合，提交代碼現在以非模態方式執行。（107490188）

Xcode 15 Beta中解決的問題
修復了在審查拉取請求時可能錯誤插入額外撇號的問題。（107586336）

Xcode 15 Beta中的廢棄項目
Xcode 15不再包括Xcode Server。Xcode Cloud是獲取代碼更改的自動構建/測試/部署工作流程的最佳方法。xcodebuild工具也可用於自定義自動化需求。（99606507）

---

### Source Editor
Xcode 15 Beta中的新功能
#if...#endif區塊中的非活動代碼現在會變暗。可以在「文本編輯」>「顯示」偏好設定中關閉此功能。（2450148）

Quick Help現在支援在文件註解中包含的圖像呈現。支援通過URL引用的外部圖像以及項目的文件目錄中的本地圖像。（45258339）

Xcode現在支援通過在模塊名稱的引用上調用Quick Help來訪問SDK框架文件。例如，通過在import SwiftUI語句上進行Option點擊來激活Quick Help，現在會顯示SwiftUI的文件。（46583395）

現在支援“gd” Vim命令跳轉到定義。（81116920）

“顯示程式碼動作”命令已被替換為“顯示快速動作”，以快速訪問任何菜單命令。預設情況下，編輯器中Command點擊一個標記現在執行“跳轉到定義”。這可以在「導航」偏好設定中進行更改。Control點擊一個標記會彈出標準上下文菜單，該菜單現在包含了所有在“程式碼動作”中可用的命令。（86179596）

添加了一個“格式化為多行”重構動作，將代碼拆分到獨立的行中。（93150897）

改進了VoiceOver支援的編輯功能。源代碼的地標和行號信息現在顯示在VoiceOver的“更多內容”菜單中。配件，包括斷點、源控制更改和代碼折疊標籤出現為VoiceOver鏈接項目。源編輯器縮排偏好設定也與VoiceOver的語音和聲音縮排偏好設定同步。此外，使用VoiceOver導航源編輯器已經改進，編輯器的重要部分現在作為VoiceOver視窗標誌包含在內。（100877198）

在使用QuickHelp時，當類型不明確時，會顯示多個符號的信息。（101256759）

在代碼完成中，只包含一個默認參數的函數現在在代碼完成中自動展開顯示。在一個包含多個默認參數的函數上按右箭頭，會展開顯示其參數的所有可能排列。（103815908）

現在支援選擇內部區塊的“i<”和“i>”Vim命令。（104433144）

代碼完成現在在聲明Swift類型時建議名稱。（106005529）

Xcode 15 Beta中解決的問題
修復：快速說明彈出窗口中使用的字體大小現在會自動調整以匹配編輯器當前主題的大小。（6955736）

修復：在右括號之前按回車鍵時，源編輯器不應該添加額外的一行。（64872737）

修復：修復了多行字符串文字和字符串插值的語法突出顯示的一些問題。（75009350）

修復：“%”Vim命令在視覺模式下現在可以正常工作。（79076961）

修復：在選擇整行內容時，當輸入開括號時錯誤地在所選代碼之前和之後插入換行符。（98690994）

修復：打開“刪除行末多餘空白”時，在放棄對一段代碼或整個文件的更改時不要去除空白。（102984729）

修復：上滾“^u”/下滾“^d”Vim命令現在在視覺模式下擴展選擇。（103835213）

修復：插入光標後的文本“p”Vim命令現在插入文本而不會插入額外的新行。（104037351）

修復：上滾“^u”/下滾“^d”Vim命令現在處理計數前綴。（104635013）

修復：向前選擇段落“{”/向後選擇段落“}”Vim命令現在在視覺模式下擴展選擇。（104782625）

修復：“更改大小寫“gu{motion}”和“gU{motion}”Vim命令現在更改字符而不是整個單詞。（104870847）

---

### StoreKit Testing in Xcode
Xcode 15 Beta中的新功能
您現在可以在Xcode的StoreKit事務管理器中創建新的應用內購買事務。只需在事務管理器中點擊“+”按鈕，然後使用菜單配置您的新事務。只有在macOS 14.0、iOS 17.0、watchOS 10.0或tvOS 17.0上測試應用時才能使用部分功能。

您可以在SKTestSession上使用新的buyProduct(identifier:options:) API，根據產品識別符在自動化測試中編程地創建應用內購買事務。當您在自動化測試中使用StoreKitTest框架時，可以使用額外的新的Product.PurchaseOption值來配置測試事務的屬性，例如購買日期。（101591947）

StoreKit配置編輯器有一個新的“應用配置”菜單，允許您配置本地StoreKit測試環境的全局屬性。在應用配置菜單中，您可以選擇模擬任何可能出現的StoreKit 2 API錯誤。這會導致該API始終以您配置的錯誤失敗，以便您可以驗證您的應用正確處理每個StoreKit錯誤。您還可以在SKTestSession上使用新的setSimulatedError(_:forAPI:)方法，在自動化測試中編程地模擬失敗。（101592113）

您現在可以在Xcode的StoreKit事務管理器中管理無活動調試會話的事務。一旦使用StoreKit配置從Xcode安裝應用，只要設備或模擬器已連接並運行，該應用就會顯示在事務管理器的導航器中。要在Mac應用程序中在沒有調試會話的情況下管理事務，您需要運行macOS 14.0或更高版本。要在其他設備和模擬器上管理事務，您需要測試系統運行iOS 17.0、watchOS 10.0或tvOS 17.0。只要有活動的調試會話，您仍然可以在舊操作系統上管理事務。（101592166）

---

## Swift
Xcode 15 Beta中的新功能
Swift 5.9引入了參數包(parameter packs)的概念，允許您編寫接受任意數量的類型參數的通用代碼。使用each關鍵字聲明參數包，使用repeat關鍵字遍歷參數包中的類型：

```swift
struct Pair<First, Second> {
  init(_ first: First, _ second: Second)
}

func makePairs<each First, each Second>(
  firsts first: repeat each First,
  seconds second: repeat each Second
) -> (repeat Pair<each First, each Second>) {
  return (repeat Pair(each first, each second))
}

let pairs = makePairs(firsts: 1, "hello", seconds: true, 1.0)
// 'pairs' is '(Pair(1, true), Pair("hello", 2.0))'
```

參數包的概念由SE-0393和SE-0398引入。（17414398）

引入了withDiscardingTaskGroup和withThrowingDiscardingTaskGroup。這是一種新的結構化並發(task group)類型，可以在父任務不需要顯式等待其結果時，盡早並高效地丟棄已完成的子任務。這由SE-0381引入。（101965913）

支持非可拷貝類型，遵循SE-0390。（104489948）

支持consume運算符，遵循SE-0366。（104490005）

遵循SE-0377，支持對函數參數使用借用(borrowing)和消耗(consuming)修飾符。這提供了對對象拷貝行為的更詳細控制，在將非可拷貝類型傳遞給函數時需要使用這些修飾符。（108511703）

禁止使用@available將存儲的屬性標記為不可用(unavailable)，以防止意外的安全漏洞，避免運行任意不可用代碼和在運行時使用不可用的類型元數據：

```swift
@available(*, unavailable)
struct Unavailable {
  init() {
    print("Unavailable.init()")
  }
}

struct S {
  @available(*, unavailable)
  var x = Unavailable()
}

_ = S() // 打印 "Unavailable.init()"

```

出於相同原因，禁止將deinit標記為不可用(unavailable)。（108800140）

使用consume運算符可以明確結束局部變量值的生命周期，將所有權傳遞給周圍的調用、賦值或初始化，而不進行拷貝：

```swift

var x: [String] = []
x.append("apples")
x.append("bananas")
x.append("oranges")

process(consume x) // 將當前值傳遞，而不進行拷貝

x = [] // 開始構建新值
x.append("broccoli")
x.append("cauliflower")
x.append("asparagus")
...

```

這是SE-0366的特性。（108800422）

現在，函數可以聲明它們通過借用(borrowing)訪問調用方提供的值，還是通過消耗(consuming)允許調用方擁有該值：

```swift

struct HealthyFoods {
  var values: [String] = []

  // 聲明以 `consuming` 參數，因為我們想將它加入到我們自己的 `values` 數組中
  mutating func add(_ value: consuming String) {
      values.append(value)
  }
}

```

這是SE-0377的特性。（108800628）

現在，if和switch語句可以作為表達式使用，可以用於：

從函數、屬性和閉包中返回值（使用隱式或顯式的return）
使用throw拋出錯誤
為變量賦值
声明变量
if或switch的每個分支必須是一個表達式，當選擇該分支時，該表達式的值將成為整個表達式的值。

```swift
let bullet =
  if isRoot && (count == 0 || !willExpand) { "" }
  else if count == 0 { "- " }
  else if maxDepth <= 0 { "▹ " }
  else { "▿ " }

public static func width(_ x: Unicode.Scalar) -> Int {
  switch x.value {
    case 0..<0x80: 1
    case 0x80..<0x0800: 2
    case 0x0800..<0x1_0000: 3
    default: 4
  }
}
```
這是SE-0380的特性。（109305622）

Swift 5.9包括了一個新的宏系統，可以用於消除樣板代碼並提供新的表達式API。宏使用新的宏介紹符號聲明：

```swift

@freestanding(expression)
macro assert(_ condition: Bool) = #externalMacro(module: "PowerAssertMacros", type: "AssertMacro")
宏具有參數和返回值類型，類似於函數，但它們作為獨立程序進行定義，操作語法樹（使用swift-syntax），並產生新的語法樹，將其合併到程序中。使用@freestanding屬性標記的宏會在源代碼中展開，使用領先的#符號：


#assert(x + y == z) // 展開為檢查 x + y == z 的結果，如果為false則報錯
宏也可以標記為@attached，這意味著它們將使用自定義屬性語法進行展開。例如：


@attached(peer, names: overloaded)
macro AddCompletionHandler() = #externalMacro(
  module: "ConcurrencyHelperMacros",
  type: "AddCompletionHandlerMacro"
)

@AddCompletionHandler
func fetchAvatar(from url: URL) throws -> Image { ... }

// 展開為...

func fetchAvatar(from url: URL, completionHandler: @escaping (Result<Image, Error>) -> Void) {
  Task.detached {
    do {
      let result = try await fetchAvatar(from: url)
      completionHandler(.success(result))
    } catch {
      completionHandler(.failure(error))
    }
  }
}

```

宏是在Swift編譯器中由獨立程序實現的。Swift Package Manager的清單提供了一個新的宏目標類型來描述宏：

```swift

import PackageDescription
import CompilerPluginSupport

let package = Package(
    name: "ConcurrencyHelpers",
    dependencies: [
          .package(url: "https://github.com/apple/swift-syntax", from: "509.0.0"),
    ],
    targets: [
          .macro(name: "ConcurrencyHelperMacros",
                 dependencies: [
                     .product(name: "SwiftSyntaxMacros", package: "swift-syntax"),
                     .product(name: "SwiftCompilerPlugin", package: "swift-syntax")
                 ]),
          .target(name: "ConcurrencyHelpers", dependencies: ["ConcurrencyHelperMacros"]),
          .testTarget(name: "ConcurrencyHelperMacroTests", dependencies: ["ConcurrencyHelperMacros"]),
    ]
)
```
這些特性涉及到SE-0382、SE-0389、SE-0394和SE-0397。（109903303）

Xcode 15 Beta中的已解決問題
修復：＃64927

Swift 5.9引入了一個警告，當將調用方的inout參數轉換為被調用方的UnsafeRawPointer時，如果原始類型包含對象引用，則會引發警告。

```swift

func inspectString(string: inout String) {
  readBytes(&string)
  // 警告：將一個inout類型的變量'UnsafeRawPointer'形成到字符串的內部表示，而不是字符串的內容。
}
func inspectData(data: inout Data) {
  readBytes(&data)
  // 警告：將一個變量'T'形成到'UnsafeRawPointer'中；這可能是不正確的，因為'T'可能包含對象引用。
}
```
（97963116）

修復：當忘記寫.element時，可能會出現“無法生成診斷信息”的消息。（107160966）

---

## Swift和C++互操作性
Xcode 15 Beta中的新功能
Swift支持與C++ / Objective-C++的雙向互操作性。現在您可以在Swift中使用C++ API的子集，並從C++中使用Swift API。通過在“C++和Objective-C互操作性”構建設置中選擇“C++ / Objective-C++”來啟用C++互操作性。

有關C++互操作性的更多信息，請參閱https://swift.org/documentation/cxx-interop。（100830806）

Xcode 15 Beta中已解決的問題
修正：啟用C++互操作性後，無法調用C類型的默認初始化程序。（109727620）

Swift Packages
Xcode 15 Beta中的新功能
您現在可以使用“文件”>“新增”>“包…”菜單命令創建各種類型的Swift包。模板包括宏、包插件，以及配置為使用swift-argument-parser的命令行工具。（60274812）

Swift標準庫
Xcode 15 Beta中的新功能
Zip2Sequence的實例（即調用zip()的結果）現在如果它們zip的序列也符合Sendable，則符合Sendable。（103840319）

測試導航器
Xcode 15 Beta中的新功能
測試導航器已重新設計和重寫，以實現更快的開發-測試-調試循環。它報告和執行測試的速度更快，並且具有新的過濾系統，支持額外的測試結果和記錄先前的過濾器。（94313839）

測試導航器中的過濾器欄現在使用標記而不是切換開關。可以通過在過濾器欄中單擊過濾器圖標或在欄中輸入“failed”、“skipped”或“expected failure”並進行自動完成來添加標記。通過單擊插入的標記並選擇當前使用的相反斷言的相反斷言來反轉過濾器。（101487428）

---

## 測試
Xcode 15 Beta中的新功能
xcodebuild現在支持列舉測試套件，該測試套件本來會由測試或測試無需構建的調用執行。測試列舉將以人類可讀或JSON格式列出套件中包含的每個目標、類和方法。此外，列舉的測試可以按層次分組或作為標識符的扁平列表（適用於將來的xcodebuild調用）。示例：

構建並列舉項目和方案中的測試：

xcodebuild test -enumerate-tests -project MyProject.xcodeproj -scheme MyScheme -destination 'platform=iOS Simulator,name=iPhone 14 Pro'
構建並列舉在xctestproducts捆綁包中已編譯的測試：

xcodebuild test-without-building -enumerate-tests -testProductsPath MyBuiltTests.xctestproducts -destination 'platform=iOS Simulator,name=iPhone 14 Pro'
構建並列舉由xctestrun文件指定的已編譯測試：

xcodebuild test-without-building -enumerate-tests -xctestrun MyBuiltTests.xctestrun -destination 'platform=iOS Simulator,name=iPhone 14 Pro'
有關詳細信息，請參閱xcodebuild的手冊頁面。（27230120）

XCTest現在支持自動屏幕錄製，除了截圖之外。屏幕錄製可以細緻地查看測試運行期間發生的情況，這對於調查UI測試失敗非常有意義。屏幕錄製默認啟用（優先於截圖）。可以在測試計劃或方案的測試操作選項中禁用它們。（35129014）

Xcode的測試報告已重新設計，以提供對許多不同設備和測試配置的測試結果的簡化理解。（100825750）

XCTWaiter的實例現在可以重用。（101293832）

Xcode 15 Beta中已解決的問題
修正：在iOS和iPadOS上，XCTest提供了一個公共API，用於支持硬件鍵盤的修改器鍵。要訪問此API，請使用XCUIElement.typeKey(_:modifierFlags:)。（20185910）

修正：已添加對使用其他束的符號對XCTest捕獲的回溯進行符號化的支持。（103923199）

修正：對於不並行執行的測試，現在設置了一個看門狗計時器，該計時器涵蓋XCTestCase實例構造的期間（即調用指定的初始化程序-initWithInvocation:）。在此期間發生的停頓和長時間延遲導致測試工具提前中止測試並將spindump附加到結果捆綁包以進行進一步調查。如果在測試用例初始化程序中有昂貴的工作，應將該工作移至-setUp或以其他方式重構，使其在測試方法本身中發生。（104390801）

---

## UI Testing
Xcode 15 Beta中的新功能
無障礙審核支持：無障礙審核是對給定視圖進行的自動檢查，用於檢測多種無障礙問題。這些問題包括缺少標籤、文字不隨動態類型縮放以及低對比度等。參見XCUIApplication().performAccessibilityAudit()（100732814）

## Xcode Cloud
Xcode 15 Beta中的新功能
Xcode現在在Xcode Cloud工作流程中支持macOS產品的新的Notarize後置操作。（64009778）