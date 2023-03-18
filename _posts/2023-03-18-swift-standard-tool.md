---
layout: post
title: Swift 程式碼標準化工具 - swiftlint & swiftformat
date: 2023-03-18 14:26 +0800
category: swift
author: Marvin Lin
tags: [swift, programming]
summary: 
---

# Swift 程式碼的標準化

在多人共同協作的專案中，Swift 程式碼的標準化是一個重要的主題，如果你的專案只有一個人，那標準化只需要那一位開發者，但我在實務上是會有三、四個人同時在一個專案的，想憑著過去的經驗讓這群人有程式碼風格的共識，是不可能的。。使用 Swiftlint 和 Swiftformat 可以幫助所有成員檢視和自動修正程式碼風格。

## Swiftlint

[Swiftlint github link](https://github.com/realm/SwiftLint)

Swiftlint 是一種靜態程式碼分析工具，可以檢查我們的程式碼是否符合 Swift 的標準風格和最佳實踐。它可以檢測和警告我們的程式碼中的一些常見錯誤和風格問題，例如缺少註釋、空格、括號和命名不一致等。使用 Swiftlint 可以使我們的程式碼更加一致和易於閱讀，從而提高程式碼品質和可維護性。

你可以使用 --fix 指令，讓 swiftformat 一次處理掉簡單的 format，像是空行等。但這個指令沒辦法處理太複雜的 lint，像是我實測後，他不會移動 trailing closure 中，參數不在 `{` 同一行的狀況。

```
# swiftlint 自動更正指令
swiftlint --fix
```

## Swiftformat

[Swiftformat github link](https://github.com/nicklockwood/SwiftFormat)

和 swiftformat 是類似的工具，我平常會同時用這兩個工具，因為 lint 的能力不太一樣，這個工具可以調整到 indent 的規範，opaque 型別是不是該處理，甚致細緻到 import 的順序是不是依照英文字母排序。

## 好處

程式碼標準化的好處在於提高程式碼質量和可讀性，從而使得我們的程式碼更加易於維護和擴展。通過使用 Swiftlint 和 Swiftformat，我們可以自動檢測和修正我們的程式碼風格問題，從而使得我們的程式碼更加一致和易於閱讀。此外，這些工具還可以提高我們的開發效率，從而使我們更加專注於開發高品質的應用程式。

總的來說，Swift 程式碼的標準化是一個重要的主題，它可以幫助我們提高程式碼品質和可讀性，從而使得我們的程式碼更加易於維護和擴展。通過使用 Swiftlint 和 Swiftformat，我們可以自動檢測和修正我們的程式碼風格問題，從而提高我們的開發效率和應用程式的品質。

繼續來看一下 Swift 程式碼的標準化所帶來的好處。
- 透過使用 Swiftlint 和 Swiftformat 我們可以自動化檢測和修正我們的程式碼風格問題，這樣可以節省我們大量的時間和精力，提高我們的開發效率。
- 程式碼標準化可以使得我們的程式碼更加一致和易於閱讀，這樣可以提高程式碼的質量和可維護性。
- 透過程式碼標準化，我們可以使得我們的程式碼更加易於擴展和維護，這樣可以使得我們開發的應用程式更加穩定和可靠。

總體來說，程式碼標準化是一個非常重要的主題，特別是在大型項目中，它可以使得我們的程式碼更加易於維護和擴展。透過使用 Swiftlint 和 Swiftformat，我們可以自動化檢測和修正我們的程式碼風格問題，提高我們的開發效率和應用程式的品質。如果你還沒有開始使用這些工具，我強烈建議你開始使用它們，這樣可以使得你專案的程式碼更加易於閱讀、維護和擴展。