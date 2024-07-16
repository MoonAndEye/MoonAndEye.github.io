---
layout: single
title: Swift 5.10 Released
date: 2024-03-06 11:54 +0800
category: swift
author: Marvin Lin
tags: [Swift, iOS, Swift 5.10]
summary: 
permalink: /swift/:title:output_ext
---

## Swift 5.10 Released - 下一個版本就是 Swift 6

以下文章內容，來自 Swift.org 的 [Swift 5.10 Released](https://www.swift.org/blog/swift-5.10-released/)，由 Holly Borla 撰寫。

Holly BorlaHolly Borla
Holly Borla 是 Apple Swift 團隊的一名工程師，同時也是 Swift 核心團隊、語言指導小組和 Swift 多元化工作組的成員。
Swift 被設計為默認安全，能在編譯時防止整個類別的編程錯誤。在基於 C 的語言中未定義行為的來源，如在初始化之前使用變量或使用後釋放，都在 Swift 中被定義掉了。

一個越來越重要的未定義行為來源是並行代碼不經意地從一個線程訪問內存，而另一個線程同時寫入同一內存。這種不安全被稱為資料競爭，資料競爭使得編寫正確的並行程序變得異常困難。Swift 通過提供由演員和任務提供的數據隔離來解決這個問題，這保證了對共享可變狀態的互斥訪問。數據隔離執行自2020年Swift並行性路線圖發布以來一直在積極開發中。

Swift 5.10 在並發語言模型中實現了完全的數據隔離。這一重要的里程碑歷經多次發布的多年積極開發。並行模型於 Swift 5.5 引入，包括 async/await、演員和結構化並行。Swift 5.7 引入了 Sendable 作為基本概念，用於線程安全類型，其值可以在任意並行上下文中共享而不引入數據競爭的風險。現在，在 Swift 5.10 中，當啟用完整的並發檢查選項時，將在語言的所有領域強制實施完全數據隔離。

Swift 5.10 中的完全數據隔離為下一個主要發布版本，Swift 6，奠定了基礎。Swift 6.0 編譯器將提供一種新的，可選的 Swift 6 語言模式，默認強制完全數據隔離，我們將開始過渡以消除所有用 Swift 編寫的軟件中的數據競爭。

在某些情況下，Swift 5.10 將在代碼可以通過額外的編譯器分析證明為安全的情況下產生數據競爭警告。Swift 6 發布的語言開發的一個主要焦點是通過減輕在常見代碼模式中被證明為安全的虛假正面並發錯誤來改善嚴格並發檢查的可用性。

閱讀下去以了解 Swift 5.10 中的完全數據隔離，演員隔離檢查的新的不安全選擇，以及 Swift 6 之前剩餘的並發進化。

Swift 5.10 中的數據競爭安全
完全數據隔離
Swift 5.10 在語言的所有角落完善了數據競爭安全語義，並修復了 Sendable 和演員隔離檢查中的許多錯誤，以加強完整並發檢查的保證。當使用編譯器標誌 -strict-concurrency=complete 構建代碼時，Swift 5.10 將除非使用顯式不安全選擇，如 nonisolated(unsafe) 或 @unchecked Sendable，否則將在編譯時診斷出數據競爭的潛在性。

例如，在 Swift 5.9 中，以下代碼由於在演員之外評估了一個 @MainActor-隔離的初始化器而在運行時失敗了一個隔離斷言，但在 -strict-concurrency=complete 下沒有被診斷：

@MainActor
class MyModel {
private init() {
MainActor.assertIsolated()
}

static let shared = MyModel()
}

func useShared() async {
let model = MyModel.shared
}

await useShared()
上述代碼允許數據競爭。MyModel.shared 是一個 @MainActor-隔離的靜態變量，它在首次訪問時評估一個 @MainActor-隔離的初始值。MyModel.shared 從 useShared() 函數內的一個非隔離上下文同步訪問，因此初始值在主演員外計算。在 Swift 5.10 中，使用 -strict-concurrency=complete 編譯代碼會產生一個警告，即訪問必須異步進行：

警告：表達式是 'async' 的，但沒有標記為 'await'
let model = MyModel.shared
^~~~~~~~~~~~~~
await
解決數據競爭的可能修復是 1) 使用 await 異步訪問 MyModel.shared，2) 使 MyModel.init 和 MyModel.shared 都是 nonisolated 並將需要主演員的代碼移到一個單獨的隔離方法中，或 3) 將 useShared() 隔離到 @MainActor。

您可以在 Swift 5.10 發布說明中找到更多關於完全數據隔離編程模型的變化和添加的詳細信息。

不安全選擇
像 @unchecked Sendable 一樣的不安全選擇對於當編譯器無法自動證明代碼免於數據競爭時表明代碼安全非常重要。在編譯器無法理解的同步方式實現的情況下，例如通過操作系統特定的原語或與 C/C++/Objective-C 中實現的線程安全類型工作時，這些工具是必需的。然而，@unchecked Sendable 一致性難以正確使用，因為它們使整個類型選擇退出數據競爭安全檢查。在許多情況下，只有類型中的一個特定屬性需要選擇退出，而其餘的實現遵循靜態並發安全。

Swift 5.10 引入了一個新的 nonisolated(unsafe) 關鍵字，用於退出存儲屬性和變量的演員隔離檢查。nonisolated(unsafe) 可以用於任何形式的存儲，包括存儲屬性、局部變量和全局/靜態變量。

例如，全局和靜態變量可以從代碼的任何地方訪問，因此它們要麼是不可變且 Sendable 的，要麼是隔離到一個全局演員的：

import Dispatch

struct MyData {
static let cacheQueue = DispatchQueue(...)
// 所有對 'globalCache' 的訪問都由 'cacheQueue' 保護
static var globalCache: [MyData] = []
}
當使用 -strict-concurrency=complete 構建上述代碼時，編譯器發出警告：

警告：靜態屬性 'globalCache' 不是並發安全的，因為它是非隔離的全局共享可變狀態
static var globalCache: [MyData] = []
^
注意：將 'globalCache' 隔離到一個全球演員，或將其轉換為 'let' 常量並使其符合 'Sendable'
所有對 globalCache 的使用都由 cacheQueue.async { ... } 保護，因此這段代碼在實踐中免於數據競爭。在這種情況下，可以將 nonisolated(unsafe) 應用於靜態變量以消除並發警告：

import Dispatch

struct MyData {
static let cacheQueue = DispatchQueue(...)
// 所有對 'globalCache' 的訪問都由 'cacheQueue' 保護
nonisolated(unsafe) static var globalCache: [MyData] = []
}
nonisolated(unsafe) 還消除了使用 @unchecked Sendable 包裝類型的需求，這些包裝類型僅用於在沒有並發訪問可能性時將特定非 Sendable 值的實例跨隔離邊界傳遞：

// 'MutableData' 不是 'Sendable'
class MutableData { ... }

func processData(_: MutableData) async { ... }

@MainActor func send() async {
nonisolated(unsafe) let data = MutableData()
await processData(data)
}
請注意，如果沒有正確實現同步機制以實現數據隔離，從獨占性強制或如 Thread Sanitizer 這樣的工具的動態分析可能仍然識別出失敗。

Swift 6 之前的語言進化
下一次 Swift 發布將是 Swift 6。Swift 5.10 中的完整並行模型過於嚴格，幾個 Swift Evolution 提案正在積極開發中，以通過移除虛假的數據競爭錯誤來改善完全數據隔離的可用性。這項工作包括當編譯器確定沒有並發訪問的潛在性時，解除在隔離邊界之間傳遞 non-Sendable 值的限制，為函數和關鍵路徑更有效地推斷 Sendable，等等。您可以在 Swift.org/swift-evolution 上找到將完善 Swift 6 的一套提案。

下一步
嘗試完整的並發檢查
您可以通過在您的項目中嘗試完整的並發檢查並提供您的體驗反饋來幫助塑造過渡到 Swift 6 語言模式。

如果您發現任何剩餘的編譯器錯誤，其中完整的並發檢查未在編譯時診斷出數據競爭，請報告一個問題。

您還可以提供反饋以幫助改進並發文檔、編譯器錯誤消息和即將到來的 Swift 6 遷移指南。如果您遇到編譯器診斷出您不理解的數據競爭警告，或者您不確定如何解決給定的數據競爭警告，請在 Swift 論壇上使用並發標籤開始討論帖。

下載
官方的 Swift 5.10 二進制文件可從 Swift.org 為 macOS、Windows 和 Linux 下載。

Swift Evolution 附錄
以下語言提案通過 Swift Evolution 過程被接受並在 Swift 5.10 中實現：

SE-0327：關於演員和初始化
SE-0383：廢除 @UIApplicationMain 和 @NSApplicationMain
SE-0404：允許在非泛型上下文中嵌套協議
SE-0411：隔離的默認值表達式
SE-0412：全局變量的嚴格並發
