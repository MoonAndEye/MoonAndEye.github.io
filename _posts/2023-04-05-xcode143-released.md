---
layout: single
title: Xcode 14.3 release note，使用 ChatGPT 翻譯
date: 2023-04-05 11:22 +0800
category: swift
author: Marvin Lin
tags: [Xcode, Swift, release note]
summary: Xcode 14.3 release note summary. The important thing is Xcode no longer support Rosetta. Swift has backDeplooyed attribute
permalink: /swift/:title:output_ext
---

## 對 iOS 開發者可能影響較大的方面

### 停用功能 - Rosetta
Xcode 不支援 Rosetta。有關更多信息，請參閱開發人員技術通告「解決 Apple Silicon 上的架構構建錯誤」。 (92772361)

### Swift 的 backDeployed
現在可以使用 @backDeployed(before:) 屬性來將函數的可用性擴展到介紹該函數作為 ABI 之前的 OS 版本。

## Xcode 14.3 release note

Xcode 14.3 包括 Swift 5.8 和 iOS 16.4、iPadOS 16.4、tvOS 16.4、watchOS 9.4 和 macOS Ventura 13.3 的 SDK。Xcode 14.3 可支援 iOS 11 及以上、tvOS 11 及以上和 watchOS 4 及以上的設備調試。Xcode 14.3 需要在運行 macOS Ventura 13.0 或更高版本的 Mac 上運行。

## 一般

### 新功能

Xcode 14.3 包括一個新的模塊驗證器，為框架模塊中的問題生成診斷信息。 (97345247)

已解決問題
修復：從 App Extension 和基於擴展的 Watch App 中崩潰日誌未傳送到 Xcode 組織者的問題。此問題在 iOS 16.4、macOS 13.3、watchOS 9.4 和 tvOS 16.4 中已解決。 (90882288)

修復：現在可以使用 Xcode 的文檔查看器查看 Xcode 文檔，或在 https://developer.apple.com/documentation/Xcode 上查看。 (102522035)

停用功能
Xcode 不支援 Rosetta。有關更多信息，請參閱開發人員技術通告「解決 Apple Silicon 上的架構構建錯誤」。 (92772361)

Apple Clang 編譯器
新功能
Clang 和構建系統支援一種新的模式用於構建模塊依賴關係，稱為顯式模塊，可以改善構建性能、可靠性和正確性。新模式是可選的，可以通過在啟用模塊的 C 和 Objective-C 項目中設置 _EXPERIMENTAL_CLANG_EXPLICIT_MODULES 作為用戶定義的構建設置來啟用。 (104438594)

實現了以下 C++23 功能：

多維下標運算符的新支援。 (P2128R6)

放寬了在 constexpr 函數中存在非文字變量（和標籤和轉到）的限制 (P2242R3)。

引入自動(x)作為語言中的衰變複制。 (P0849R8)。 (104887755)

已解決問題
修復：編譯器不再對使用 <img/> 標記在 Objective-C 文檔註釋中包含的圖像發出錯誤警告。 (91464292)

修復：在 C++ 語言模式設置為 C++20 的情況下，ObjectiveC++ 中禁用

## 建構系統

新功能
現在 Xcode 會在執行清理操作之前提示使用者。使用者可以在執行清理時按住 option 鍵以繞過此提示，或者在提示中啟用「不要問我」設置以永久隱藏提示。(98914489)

問題解決
已修正：UI 測試目標不再在構建時強制使用 SWIFT_SERIALIZE_DEBUGGING_OPTIONS 為 YES，而是尊重項目中的覆蓋該設置。(94845934)

已修正：在構建部分的方案的前置操作和後置操作中運行腳本現在會在任何運行腳本退出時出現非零退出代碼，而不是報告錯誤的構建成功。(102896200)

已知問題
在預覽包內的預覽在應用程式使用該包的依賴和依賴的包內預覽時可能會失敗。(103716225)

解決方法：當在該包的檔案上使用 SwiftUI 預覽時，創建並選擇僅針對該包的方案。

當預先構建方案操作（例如編譯包插件）遇到錯誤時，Xcode 工作區窗口頂部的狀態消息有時不會更新。這會留下先前的狀態，如果先前的狀態為“構建成功”，可能會引起混亂。(104306342)

在預覽包內的預覽在應用程式使用該包的依賴和依賴的包內預覽時可能會失敗。(104683595)

解決方法：當在該包的檔案上使用 SwiftUI 預覽時，創建並選擇僅針對該包的方案。

## C++ 標準庫

新功能
實現了以下新功能：

P0896R4 - 唯一範圍提案

P1004R2 - 使 std::vector constexpr

P0627R6 - 標記無法到達的程式碼的函數

P1165R1 - 使具有狀態的配置器傳播對於 operator+(basic_string) 更一致

P0674R1 - 在 make_shared 和 allocate_shared 中支持數組

P0980R1 - 使 std::string constexpr

LWG3659 - 考慮 ATOMIC_FLAG_INIT 的取消停用

P1423R3 - char8_t 的後向兼容性糾正

std::pop_heap

棄用項目
以下項目已被棄用：

已移除 <experimental/filesystem> 標頭。請改用 <filesystem> 標頭。相關的 _LIBCPP_DEPRECATED_EXPERIMENTAL_FILESYSTEM 宏也已被刪除。

在 C++03 或 C++11 模式下不再支援 C++14 函數 std::quoted(const char*)。

std::function 已在 C++03 中被移除。如果您正在使用它，請移除用途或升級到 C++11 或更高版本。

std::unary_function 和 std::binary_function 在 C++17 和 C++20 中不再可用。它們可以通過定義 _LIBCPP_ENABLE_CXX17_REMOVED_UNARY_BINARY_FUNCTION 重新啟用。它們也在 C++11 及更高版本中標記為[[deprecated]]。要禁用廢棄警告，您必須定義 _LIBCPP_DISABLE_DEPRECATION_WARNINGS。請注意，這會禁用所有廢棄警告。

std::wstring_convert 和 std::wbuffer_convert 的內容已被標記為棄用。要禁用廢棄警告，您必須定義 _LIBCPP_DISABLE_DEPRECATION_WARNINGS。請注意，這會禁用所有廢棄警告。

整數分配 std::binomial_distribution、std::discrete_distribution、std::geometric_distribution、std::negative_binomial_distribution、std::poisson_distribution 和 std::uniform_int_distribution 現在遵循標準，拒絕使用除 short、int、long、long long 和它們的 unsigned 版本之外的模板參數類型。作為擴展，int8_t、__int128_t 及其 unsigned 版本也受支持。特別是，使用 bool 和 char 等非整數類型實例化這些分配不再能夠編譯。（105097623）

調試
已解決問題
修復：當停在包含類方法中的 C++11 lambda 本體中時，LLDB 現在支持評估包含“this”指針成員的表達式。（50140179）

修復：LLDB 現在對於先前會結束調試會話的 Swift 模塊反序列化失敗更有韌性。（64511878）

文檔
新功能
Objective-C 的文檔工具鏈已遷移至開源 Clang 提取 API 工具。（101761719）



## DriverKit



新功能
Clang 現在會自動將未初始化的本地變數在堆疊上初始化為零，以供 DriverKit 擴展使用。(99166509)


## Instruments


新功能
當使用 Instruments 在鎖定的目標設備上嘗試啟動應用程式時，Instruments 現在會提示使用者等待解鎖，而非顯示錯誤訊息。(41464216)

xctrace export 現在支援在追蹤檔案中為進程請求二進位映像載入資訊。

每個映像包括路徑、UUID、名稱、載入地址和架構。(76676504)

Instruments 檢視器中的 Stores Inspector 現在允許在列出的儲存區上調用快捷選單後複製示例 xctrace export 命令。(89078433)

xctrace export 現在包括在 Instruments 追蹤中記錄的回溯可解析的描述。回溯中的每個框架都包括 VM 位址和符號名稱 (如果存在)。(95850764)

“檔案→符號”介面已更新，以使符號化工作流程更加流暢:

更好的顯示/篩選進程和映像清單

更多關於每個載入映像的資訊，包括 UUIS、版本、載入地址和載入時間。

通過“添加符號”按鈕更輕鬆地重新符號化，允許一次選擇多個 dSYM。(97920704)

擴展細節中的最重堆疊追蹤 UI 現在允許使用快捷選單複製符號的編碼名稱。(98017107)

在 Instruments Package 中指定的 Graph 和 Detail 元素現在可以根據追蹤參數的值禁用。(101357705)

最重堆疊追蹤 UI 現在有一個新的上下文選單，可以將框架顯示為載入地址和二進位偏移。(102116922)

os-signpost-interval-schema 現在公開了一種將 CLIPS 變量綁定到 signpost 區間的持續時間字段並將其用作其他列定義的方法。(102447071)

已解決的問題
修復: Instruments的啟動時間性能現在得到了改進。啟動應用程序應該快上3倍。(12219587)

修復: 從Instruments源代碼查看器中選擇“在Xcode中打開”，現在會在現有工作區中打開所選文件。(76846286)

修復: 在Instruments和Xcode之間轉換時，“在Xcode中打開”操作的源代碼查看器現在會保留行和文本範圍的選擇。(91005085)

修復: 在詳細視圖中調用查找字段時，與之互動的可靠性得到了改善。(94526531)

修復了在呼叫樹視圖中輸入多個篩選令牌並選擇“全部”匹配仍然會導致匹配任何指定令牌的問題。(97454950)

修復了使用觸控板在呼叫樹視圖中水平滾動無法實現的問題。(97752177)

修復: 當所選符號沒有可用的源代碼時，源代碼視圖現在會自動打開反汇編視圖。(99206757)

修復: 將新Instruments從庫添加到現有跟踪文檔的性能已經得到顯著改進。(100873173)

修復了在CPU計數器Instruments中，在蘋果硅機器上不會計算RETIRE_UOP事件的問題。(101330117)

## Interface Builder

新功能
「Based On Introduced Variations」屬性面板現在會記住上次選擇的尺寸類別和變化設定。(98647372)

通過屬性面板，可在UISearchBar上配置啟用屬性。(101423711)

問題已解決
修復：可以在NS/UITextView的段落樣式和UILabel的屬性面板上配置斷行策略。(70369164)

修復：SF Symbol庫的搜索結果已改進，包括除符號名稱以外的搜索詞。例如，搜索“寫作”還會顯示相關的“鉛筆”SF符號。(94857888)

修復了在自定義類別屬性面板中，防止“在編輯器中顯示”按鈕顯示源代碼編輯器中的類別的問題。(100136260)

修復了XIB只包含“User Defined Runtime Attributes”的文件無法在運行時加載的問題。(100357502)

修復：Xcodebuild支持使用“-downloadPlatform <watchOS|tvOS>”參數來請求下載單個平台。(100869261)

修復：在橫向模式下，安全區域的尺寸現在在畫布中的位置正確。(101164646)

修復了當打開Storyboard時有時框架會移位的問題。(102221237)

修復了調整NSViewController大小時無法顯示調整光標的問題。(102609072)

## 本地化

新功能
現在您可以指定Xcode專案的預設本地化。從專案編輯器的“資訊”選項卡中的語言列表中進行配置。(4886288)

已解決問題
修復了一個在導出專案進行本地化時的問題，其中可能不會導出引用的專案。(91126400)

## Playgrounds

已知問題
Xcode Playgrounds的手動執行模式可能失敗。(104976410)

## 簽名和分發

已解決問題
修復：Xcode自動簽名現在可以為開發人員ID創建受管理的配置文件。這解決了在應用程式分發工作流程期間使用開發人員ID證書進行雲簽名時Xcode引發錯誤的問題。(90026719)

已解決問題：解決了分發使用Game Center的應用程式時的問題。如有必要，Xcode自動簽名現在可以在分發期間啟用您的應用程式ID上的Game Center功能。(103426363)

模擬器
已解決問題
修復：在iOS模擬器中模擬用戶手勢時，加載WebView可能會導致整個屏幕出現黑色方塊。(107143140)

已知問題
重複構建和運行目標為iOS 16.1及更高版本模擬器運行時，有時可能導致啟動失敗。(101990080)

解決方法：重新啟動模擬器設備，然後重新嘗試啟動。

## Source Control


已解決問題
修復了：Xcode 的 Git 整合現在支援 mailmap。更改名稱或電子郵件地址的使用者可以在他們的存儲庫中設置 .mailmap 檔案，Xcode 現在在提交和分支歷史中顯示正確的規範名稱。 (62682973)

修復了：重新添加對 perl 兼容正則表達式的 git grep 支援。 (101318680)

修復了：解決了安全漏洞 CVE-2022-23521 和 CVE-2022-41903。 (102376850)

已知問題
分支歷史檢視器在少數情況下可能顯示不完整的分支歷史。 (96024292)

解決方法：選擇其他分支，然後再次選擇所需的分支。


## 原始碼編輯器


新功能
Swift 的程式碼完成排名得到了改進。 (98687334)



## StoreKit

新功能
StoreKit 測試框架現在支援測試 SKAdNetwork 4.0。 (91782868)


## Swift

新功能
現在可以使用 @backDeployed(before:) 屬性來將函數的可用性擴展到介紹該函數作為 ABI 之前的 OS 版本。

例如，假設在 macOS 12 的 SDK 框架中引入了結構體 Temperature，稍後在 macOS 13 中，框架作者決定添加一個 degreesFahrenheit 屬性以方便使用：

```
@available(macOS 12, *)
public struct Temperature {
public var degreesCelsius: Double

// ...
}

```

```
extension Temperature {
@available(macOS 12, *)
@backDeployed(before: macOS 13)
public var degreesFahrenheit: Double {
return (degreesCelsius * 9 / 5) + 32
}
}

```
將 @backDeployed 屬性添加到 degreesFahrenheit 使得框架作者可以將此新聲明提供給最低部署目標為 macOS 12 的應用程式，即使 degreesFahrenheit 的 ABI 入口點僅存在於 macOS 13 及更高版本中。

當呼叫具有 @backDeployed 的函數時，編譯器會將函數的調用包裝在 thunk 中。thunk 檢查是否在運行時可用該聲明的庫入口點，如果可用，則調用它。否則，將調用客戶端發出的函數的副本。SE-0376 (105198323)

現在支援轉換模式中的Сollection downcasts。例如：

```
func collectionDowncast(_ arr: [Any]) {
switch arr {
case let ints as [Int]:
// ...
case is [Bool]:
// ...
}
}
```
(105198506)

改進了 UnsafeMutableRawPointer、UnsafeMutableBufferPointer 和 UnsafeMutableRawBufferPointer 的 API，添加了先前缺失的初始化（和析構）方法，包括從 Collection 類型進行更高效的初始化。

對於 UnsafeMutablePointer<T> 和 UnsafeMutableBufferPointer<T>，包含單詞“assign”的方法名已更名為使用單詞“update”，並添加了更多方法。現在，每個 UnsafeMutablePointer 和 UnsafeMutableBufferPointer 的多元素初始化方法都有相應的“update”方法。

UnsafeBufferPointer、UnsafeRawBufferPointer、UnsafeMutableBufferPointer 和 UnsafeMutableRawBufferPointer 的切片現在共享其基類型的類似集合的 API。

例如，給定已初始化的 b: UnsafeMutableBufferPointer<Int>，以下行是同義的：

b.update(repeating: 0)
b[b.startIndex..<b.endIndex].update(repeating: 0)
SE-0370 (105198642)

隱式 self 現在允許在解開 self 之後弱引用捕獲，例如以下隱式 self 用法是被允許的：

```
class ViewController {
let button: Button

func setup() {
button.tapHandler = { [weak self] in
guard let self else { return }
dismiss() // 引用到 self.dismiss()
}
}

func dismiss() { ... }
}

```

在 Swift 5 語言模式中，即使 self 還未解開，隱式 self 也允許在非逃逸閉包中弱引用捕獲。例如，在 Swift 5 語言模式下，以下程式碼可以成功編譯：

```
class ExampleClass {
func makeArray() -> [String] {
// Array.map 採用非逃逸閉包：
["foo", "bar", "baaz"].map { [weak self] string in
double(string) // 隱含地參照到 self!.double(string)
}
}
```

```
func double(_ string: String) -> String {
string + string
}
}
```

在 Swift 6 中，上述程式碼將不再編譯。非逃逸閉包中的弱引用捕獲現在具有與逃逸閉包中捕獲相同的行為（如 SE-0365 中所述）。依賴於以前行為的程式碼需要更新，以解開 self（例如通過添加 guard let self else return 語句）或使用不同的捕獲方法（例如使用 [self] 或 [unowned self] 而不是 [weak self]）。SE-0365 (105198849)

現在可以使用編譯器標誌 -enable-upcoming-feature X 來啟用已被進化過程接受但其引入到語言中正在等待下一個主要版本（例如版本 6）的特定功能 X。X 是由任何屬於此類別的提案指定的：

ConciseMagicFile 在 SE-0274 中啟用了新的 #file 語意。

ForwardTrailingClosures 關閉了 SE-0286 的「後向」掃描行為。

BareSlashRegexLiterals 啟用了 SE-0354 的正規表達式字面量語法。

可以使用 #if hasFeature(X) 在原始碼中檢測特徵。SE-0362 (105198978)

已解決的問題
修復了使用 Swift Concurrency 的應用程式在運行於 macOS 12.3 及更早版本、iOS 15.4 及更早版本、watchOS 8.5 及更早版本和 tvOS 15.4 及更早版本時，在 await 中暫停時偶爾會發生崩潰的問題。（101299662）

修復了 Swift 編譯器可能無法為使用 BUILD_LIBRARY_FOR_DISTRIBUTION 啟用的 XCFramework 依賴項構建模組的問題。當 XCFramework 包含具有隱含添加 @MainActor 約束的公共 Swift 声明時，例如 UIView 或 NSView 的子類，將會發生這些失敗。Swift 編譯器期望這些聲明標有 @available，在支持 Swift Concurrency 的作業系統版本上可用。（105610970）


## Swift Packages

新功能
當插件所需的工具在目標平台上不受支援時，現在會顯示正確的診斷信息而不是不明確的錯誤。 (91000836)

現在允許有重複的產品名稱的套件。請注意，這只適用於命令行構建。 (94744134)

實現了 SE-0378，為套件註冊請求添加了令牌驗證支持。 (99716571)

二進制目標現在可以直接作為產品出售，而無需聲明額外的源目標。 (101096803)

SwiftPM 現在支持根據 SE-0362 分步實現即將推出的 Swift 語言改進。 (104718540)

已解決問題
修正：套件中的條件目標依賴（SE-0273）現在正確應用於二進制目標，並導致頂級目標從根套件構建中過濾掉。 (85762201)

修正：刪除了在使用 tools-version 5.8 或更高版本的工具清單中隱含的 Foundation 可用性。如果在清單中使用 Foundation 的 API，現在需要顯式導入 Foundation。 (92879696)

修正：當預建命令依賴於不是預建二進制文件的工具時，它顯示了一個不明確的錯誤信息。修復程序已添加以顯示正確的診斷信息。 (94712361)

修正：當插件對不受支援的產品或目標有依賴時，現在會顯示正確的診斷信息而不是不明確的錯誤。 (95117424)

修正：解決了一個錯誤，該錯誤有時會導致套件解析失敗，並出現類似以下消息：An unknown error occurred. reference 'refs/remotes/origin/main' not found (-1)。 (100387832)

修正：當套件圖解析失敗時，Xcode 現在會顯示構建失敗，而不是讓構建開始，然後出現有關缺少構建產品的錯誤。 (101835157)

修正：與套件相關的警告和錯誤現在在套件解析日誌中顯示，以適用於它們所適用的套件。 (102879707)

已修正多個在使用套件時可能導致“無法解析建置檔案：XCBCore.BuildFile”建置錯誤的問題。(102912126)

已知問題
當套件建置工具插件為特定的輸入檔案產生建置命令時，該檔案被視為已由插件處理，並不會傳遞到建置系統。如果該輸入檔案是源代碼文件（例如Swift或Objective-C源代碼文件），它將不會被編譯到正在建置的產品中。(102789077)

## SwiftUI Preview

### 新功能

在 SwiftUI 預覽中選擇“預覽”選項卡後，現在可以在控制台中看到 print 輸出。目前僅支持 Swift 的 print 函數。 (96569171)

### 已解決的問題

修復：在預覽一個 Swift 套件目標內的檔案時，該 Swift 套件目標作為可執行目標的相依目標時，預覽可能會失敗。 (97630721)

修復：當預覽兩個檔案並排顯示時，其中一個檔案位於 Swift 套件內時，Xcode 畫布中的預覽可能會失敗。 (99296071)

修復：在預覽不支援預覽的目標（例如 XPC 服務或靜態庫）的相依目標中進行預覽時，預覽可能會失敗。 (99707713)

修復：在 Swift 套件中使用二進制相依性時，預覽可能會失敗。 (99936678)

修復：在最低部署目標為 <= iOS 14.0 的應用程式中使用 Swift Concurrency 時，預覽可能會失敗。 (99969698)

修復：某些預覽崩潰的情況在畫布中不會顯示。 (100586176)

修復：預覽在存在於 widget 目標和應用程式目標中的檔案時可能會失敗。 (101221314)

修復：在另一個類型的返回類型中使用不透明類型作為泛型參數時，預覽可能會失敗。 (101832285)

修復：在具有與捆綁識別符不同的應用程式識別符的應用程式中進行預覽可能會失敗。 (102753115)

## 測試

### 新功能

Xcode 現在預設為新專案使用測試計畫。測試計畫標記為「自動建立」，可在「測試計畫編輯器」中查看和修改。若要更改自動建立的測試計畫，使用者必須先將其存檔到磁碟上。可以在「測試計畫編輯器」中進行變更，然後透過畫面提示將檔案遷移至磁碟上的表示形式，或從「測試計畫編輯器」中明確存檔自動建立的測試計畫。(97048381)

XCTestCase.wait(for:timeout:enforceOrder:) 和相關方法的 timeout 參數現在是可選的。如果未指定，該函式會無限等待（直到整個測試超時）。為確保合理的執行時間，請為正在運行的 XCTestCase 實例（self）設定適當的 executionTimeAllowance 屬性。(100811826)

已解決問題
修正：若有符號資訊，async Swift 測試方法以及 async setUp 或 tearDown 方法拋出的錯誤現在會顯示它們被拋出的來源位置，並包含更高保真度的描述。(72813349)

修正：如果測試計畫中啟用了測試超時，並且已向共用的 XCTestObservationCenter 註冊了測試觀察器，則觀察器的 -testCaseWillStart: 和 -testCaseDidFinish: 方法現在會計算每個測試的時間津貼。這允許控制系統防止觀察器實現這些方法時可能出現的掛起。(78408785)

修正：XCTestCase.wait(for:timeout:enforceOrder:) 和相關方法現在在並行 Swift 函式中被標記為不可用，因為它們可能導致測試死鎖。代之以使用新的並行安全方法 XCTestCase.fulfillment(of:timeout:enforceOrder:)。(91453026)

修正：當使用 xcodebuild build-for-testing 構建測試並使用 xcodebuild test-without-building 執行時，測試計畫的「失敗時收集診斷資訊」設置現在會生效。(93053592)

修正：在較早的 setUp 或 tearDown 中使用 XCTSkip 後，記錄在稍後 setUp 或 tearDown 中出現的問題不再會將測試

修正了:當在 async Swift 測試方法或 async setUp 或 tearDown 方法執行期間拋出錯誤，但在從該方法返回之前被捕獲時，XCTest 避免構建錯誤描述，因為這樣做可能是不安全的。(98847718)

修正了:在 macOS 目的地上，如果目標的“在並行執行”核取方塊已選中，測試計劃中包含的具有不同調試器啟用的配置的測試目標(例如，一個配置啟用地址調試器，另一個配置啟用線

已知問題
在 Xcode Cloud 中嘗試啟動 watchOS UI 測試應用程式時，測試可能會因為應用程式未載入輔助功能而失敗，並顯示錯誤訊息。(90334748)

在執行、檢視效能、分析或封存動作中加入自動建立的測試計畫會導致專案檔案重新開啟時崩潰。(90378346)

解決方法：刪除在 xcshareddata 目錄內被修改的方案。

在執行測試並顯示覆蓋率報告後，Swift 檔案沒有顯示程式碼覆蓋率資料。(104935416)

手動新增、移除測試計畫到已有自動建立的測試計畫的專案會導致測試導覽器顯示 "無測試計畫"，即使自動建立的測試計畫實際上支援該專案。(105433014)

解決方法：關閉並重新開啟專案。

有時候在方案中加入測試計畫會導致該測試計畫在後續專案開啟時無法顯示在方案或測試導覽器中。(105455341)

解決方法：打開並關閉方案編輯器以讓 Xcode 將方案內容的更改持續到支援其的 .xcscheme 檔案。

## UI測試

新功能
現在您可以設置模擬位置供您的設備即時使用，或檢索先前設置的模擬位置。（18825683）

您現在可以使用指定的應用程式打開URL，或告訴設備使用其默認應用程式打開URL。（21387710）

您現在可以獲取或設置設備的淺色或深色外觀模式。（81016755）

已解決問題
已修復：確保在UI測試期間如果使用者要求方向更改，則禁用方向鎖定。（98693525）

已修復：單按鈕警告自動解除改進。（102036701）

## Xcode Cloud

已解決的問題
修正：使用 Xcode 14.3 的 Xcode Cloud 工作流程現在可以正確地報告構建 Xcode 專案時遇到的構建警告和靜態分析問題。(99978366)

已知問題
使用 Xcode 的 UI 連接 Slack 可能無法成功。(106153362)

解決方法：從 Xcode Cloud 的 web UI 連接 Slack。

## Xcode 預覽

新功能
使用 Xcode 預覽時，任何 print() 輸出都會記錄到調試控制台中。(71080261)