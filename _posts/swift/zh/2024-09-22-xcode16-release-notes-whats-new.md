---
layout: single
title: Xcode 16 Release Notes 新功能 機翻
date: 2024-09-22 16:03 +0800
category: swift
author: Marvin Lin
tags: [Xcode, Swift]
summary: Xcode 16 的 Release Notes 中有以下新增功能（New Features)
---

這份 Xcode 16 的 Release Notes 中有以下新增功能（New Features）：

### General
1. **預測代碼完成**（Predictive Code Completion）：Xcode 16 現在支援在所有 Apple silicon Mac 上進行預測代碼完成。這功能透過專為 Swift 和 Apple SDK 訓練的機器學習模型驅動，需在 macOS 15 或更新的系統上運行。（116310768）

### Build Settings
2. **從構建設置編輯器複製和貼上**：現在使用 `.xcconfig` 檔案語法。（14333348）

3. **項目導航的“以...方式開啟”上下文菜單**：現在支援為每個檔案類型選擇預設編輯器。（24666459）

### xcodebuild
4. **匯入和匯出下載的平台**：`xcodebuild` 現在支援匯入和匯出下載的平臺到磁碟。這可用於將模擬器磁碟映像匯出到其他需要該模擬器運行時的機器上，無需重新下載。（129189162）

### Reality Composer Pro
5. **時間軸**：可以序列化執行動作，並根據觸發條件啟動時間軸。（75589529）

6. **虛擬環境探測元件**：可以控制虛擬環境的照明效果。（117770245）

7. **碼位支持**：支持控制音頻屬性及擴展至8個紋理座標。（123364636）

### Previews
8. **共享構建產物**：新的預覽引擎支持在 Build and Run 與 Previews 之間共享構建產物。（37353090）

9. **`@Previewable` 宏**：允許在預覽中直接使用 SwiftUI 的 property wrapper，無需定義中介包裝視圖。（110570957）

### StoreKit
10. **隱私協議**：可以在 StoreKit 配置中設置測試用的隱私政策及訂閱協議。（114228169）

### Swift
11. **Swift 支持非複製的 C++ 類型**：允許在 Swift 中使用不需要複製的 C++ 類型。（83358475）

12. **`~Copyable` 修飾符**：可用於 protocols 和泛型參數來禁止複製。（101653009）

13. **函數型別中的錯誤類型**：可以在函數簽名中指定錯誤類型，支援更精確的錯誤傳播。（125992062）

### Test Plans
14. **測試報告中支持 Swift Testing 框架**：測試報告現在顯示 Swift Testing 框架的元數據標籤，以及按測試執行狀態進行篩選的功能。（127015832）
