---
layout: single
title: 如果你遇到需要動態改變 App Icon 的需求，這篇文章大概涵蓋了你所需要的知識
date: 2024-12-10 13:30 +0800
category: swift
author: Marvin Lin
tags: [Xcode, Swift]
summary: Change App icon feature
---

這兩、三年前，曾經有需求方提問，如果想要依某個條件更改 app icon，是做得到的嗎？然後再前幾天，我又被問了一次。只是這一次，我已經忘記我之前找到的資料了。如果不把這個結果紀錄起來，大概過一陣子，我又要重新找一次。這邊紀錄一下動態 app icon 這個 feature，要考慮的東西。

## 實作方法
實作很簡單，只有一道 api

```
/// iconName 一定要能對應到 app icon name, 而且 app icon 的 iconName 一定要存在，如果 file name 不存在，不會閃退，app icon 會保持原樣
UIApplication.shared.setAlternateIconName(iconName) { (error) in
    if let error = error {
        print("Failed request to update the app’s icon: \(error)")
    }
}
```

[Apple 關於 App Icon 官方文件](https://developer.apple.com/documentation/xcode/configuring_your_app_to_use_alternate_app_icons)

[Apple 關於 App Icon Demo project](https://docs-assets.developer.apple.com/published/ba6fbde5c8/ConfiguringYourAppToUseAlternateAppIcons.zip)

## 但如果要用在實際的 app 上，還需要考慮以下幾點

- app icon 的 image 必需要先包在 app project 裡面，app icon 沒辦法即時從網路上下載後替換。且 icon 格式固定 1024 * 1024，尺寸不符合會包不起來。
- app icon 觸發的邏輯，可以是使用者點擊，也可以是程式滿足某個條件後，用程式觸發。Apple 的 Demo project 是這樣實作，點擊了 app icon 後，就會將 app icon 更換成這個圖案。
- app 一定要在前景，才能更換 app icon，試過 app 活著進入後景然後發動更換 app icon，會跳 3072 error
- app 在「更換完 app icon 後」，會強制跳一個系統 alert。這個 alert 是系統級的，和隱私權彈窗一樣，一定會觸發。使用者只有一個 OK 可以選，選完後你 app 其他的 UI 觸控才可以繼續。