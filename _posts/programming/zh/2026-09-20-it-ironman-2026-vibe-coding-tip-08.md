---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜iOS 的基本必備：SwiftLint 和 SwiftFormat 要用 - Tip 08"
date: 2026-09-20 13:02:07 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - iOS
  - Swift
  - SwiftLint
  - SwiftFormat
  - Xcode
summary: "iOS 專案把 SwiftLint 與 SwiftFormat 放進 repo 和 build，讓 lint、格式規則每次都能檢查程式碼。"
description: "iOS 專案把 SwiftLint 與 SwiftFormat 放進 repo 和 build，讓 lint、格式規則每次都能檢查程式碼。"
---
做 iOS，Tip 03 講的三道關落到工具上：lint 用 SwiftLint，formatter 用 SwiftFormat。基本的，要用。

## 為什麼

程式大多是他寫的，我自己不逐行看，Tip 03 那三道關替我看。iOS 專案一樣，差別只在用哪一套工具，而且要讓他也讀得到規則：設定檔進 repo，掛進 build，每一次 build 都過一遍。

## 我怎麼做

**Lint 用 SwiftLint。** 裝法很多種，Homebrew 一行：

```bash
brew install swiftlint
```

裝好之後掛進 Xcode：在主 target 的 Build Phases 加一個 Run Script，放在 Compile Sources 後面，每次 build 都跑一次。SwiftLint 的 README 給的腳本是這樣：

```bash
if command -v swiftlint >/dev/null 2>&1
then
    swiftlint
else
    echo "warning: `swiftlint` command not found - See https://github.com/realm/SwiftLint#installation for installation instructions."
fi
```

規則寫在專案根目錄的 `.swiftlint.yml`。這個檔案放在 repo 裡，他讀得到，改 code 的時候知道這個專案的規矩。

**Formatter 用 SwiftFormat。** nicklockwood 的 SwiftFormat，Homebrew 也是一行：

```bash
brew install swiftformat
```

規則寫在專案目錄的 `.swiftformat`，放在那裡它會自己讀到；在專案目錄跑 `swiftformat .`，整個專案格式化一遍。設定檔一樣放進 repo。

設定檔跟程式碼一起留在 repo，之後換環境也有同一份規則可以用。

## 坑

SwiftFormat 的 `swiftformat .` 會把當下目錄和底下所有子目錄的 Swift 檔全部改寫，README 特別警告：在家目錄跑，會把整顆硬碟上的 Swift 檔都重排一遍。在專案目錄裡跑，或者指定路徑。

## 小結

iOS 的 lint 用 SwiftLint，formatter 用 SwiftFormat，設定檔進 repo，掛進 build。

明天講 unit test 要寫什麼，拿購物車打折當例子。

參考：
- SwiftLint https://github.com/realm/SwiftLint
- SwiftFormat https://github.com/nicklockwood/SwiftFormat
