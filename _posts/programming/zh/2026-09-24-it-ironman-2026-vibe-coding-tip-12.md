---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜Remote Config 控參數：Day 1 就把強制更新、建議更新、維修中、正常使用做進去 - Tip 12"
date: 2026-09-24 13:01:57 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - Remote Config
  - Mobile
  - App Release
  - Feature Flags
summary: "把強制更新、建議更新、維修中、正常使用四種狀態放進 Remote Config，讓 app Day 1 就能處理上線後的版本與維修情境。"
description: "把強制更新、建議更新、維修中、正常使用四種狀態放進 Remote Config，讓 app Day 1 就能處理上線後的版本與維修情境。"
---

本文同步刊登於 [iT 邦幫忙](https://ithelp.ithome.com.tw/articles/10416457)。

這篇是 Vibe Coding 系列 Tip 12：先把 app 的四種狀態交給 Remote Config 控制，讓後續更新與維修不用重新發版。

Remote Config 控參數很好用。app 的 Day 1 就把四個狀態做進 Remote Config：強制更新、建議更新、維修中、正常使用。

## 為什麼

app 發出去之後，裝在使用者手機上的那一版就改不了了。出了嚴重的問題要大家更新、後端要停機維修、某一版有 bug 想請大家升級，這些都得在 app 開起來的第一個畫面就處理。這個開關放在 Remote Config 裡，改一個參數，全部的使用者下一次開 app 就吃到。

## 我怎麼做

四個狀態，一個參數決定：

| 狀態 | app 開起來做什麼 |
| --- | --- |
| 正常使用 | 直接進 app |
| 建議更新 | 提示有新版，可以關掉繼續用 |
| 強制更新 | 只能去商店更新，進不了 app |
| 維修中 | 顯示維修訊息，進不了 app |

Remote Config 裡大概放這幾個參數：

```json
{
  "app_status": "normal",
  "min_supported_version": "1.2.0",
  "latest_version": "1.4.0",
  "maintenance_message": "系統維護中，預計 02:00 恢復"
}
```

`app_status` 四個值：`normal`、`suggest_update`、`force_update`、`maintenance`。app 啟動先抓 Remote Config，照 `app_status` 決定走哪一條；`min_supported_version` 是保險，版本比它低的直接當強制更新。這一段邏輯讓他寫，四個狀態各給一個測試（接 Tip 09）。

## 坑

- 抓不到 Remote Config 的時候（沒網路、第一次開），app 裡的預設值要是「正常使用」。預設值設成別的，斷網的人會被擋在外面。
- 版本號要拆成三段數字比，別當字串比。字串比的話 1.10 會被當成比 1.9 小，裝了最新版的人反而被要求更新。

## 小結

四個狀態 Day 1 就做進 Remote Config，之後出什麼事，改一個參數就能先擋住。

明天講 mobile 開發我建議的最後一件事：埋 debug console log，AI 很好 debug。
