---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜實作 prompt 補上 SOLID、FIRST 與 design patterns - Tip 29"
date: 2026-10-11 01:00 +0800
category: programming
author: Marvin Lin
tags: [IT鐵人賽, 2026鐵人賽, Vibe Coding, Vibe Coding 技巧, SOLID, FIRST, Design Patterns]
summary: "用一段可直接貼用的 prompt，要求 coding agent 遵守 SOLID、FIRST，並只在適合任務時採用 design patterns。"
description: "用一段可直接貼用的 prompt，要求 coding agent 遵守 SOLID、FIRST，並只在適合任務時採用 design patterns。"
---

叫他開始實作的時候，我建議在 prompt 補上三件事：遵守 SOLID，單元測試符合 FIRST，有適合這個任務的 design pattern 就優先採用。

## 為什麼

Tip 03 把 lint、formatter、unit test 放進專案，Tip 09 講測試要涵蓋哪些規則。開始改功能時，我還會把程式設計與測試的要求一起講清楚。

SOLID 用來檢查責任怎麼分、模組怎麼依賴；FIRST 用來檢查測試能不能經常跑、結果能不能相信。Design patterns 則提供現成的設計方法，遇到適合的問題，可以先從這些做法開始。

## 我怎麼做

把下面這段接在任務描述後面：

```text
實作時請遵守：

1. SOLID 原則
   - S：單一職責，讓一個模組的修改理由集中。
   - O：開放封閉，新增行為時優先利用既有擴充點。
   - L：里氏替換，替代實作要遵守原本的行為契約。
   - I：介面隔離，使用端只依賴自己需要的介面。
   - D：依賴反轉，核心規則依賴抽象，具體服務放在邊界。

2. 單元測試符合 FIRST 原則
   - Fast：執行快，方便反覆跑。
   - Independent：各測試獨立，不依賴執行順序或其他測試留下的狀態。
   - Repeatable：相同條件下結果一致，控制時間、亂數與外部依賴。
   - Self-validating：用 assertion 自動判斷通過或失敗。
   - Timely：在設計與實作時及時寫測試，讓測試能回饋設計。

3. 優先採用適合的 design patterns
   - 先看專案既有的實作方式。
   - 如果這個任務有適合的現成設計模式，優先採用並說明理由。
   - 沒有合適的模式就保留簡單做法，不為了套模式增加多餘的層次。

完成後，指出實際調整的責任邊界、採用的模式與理由，
並列出實際跑過的測試和結果。沒有執行的測試要明說。
```

只想簡短提醒，也可以直接貼這三句：

```text
實作遵守 SOLID 原則。
單元測試符合 FIRST 原則。
如果任務有適合的現成 design pattern，優先採用，並說明選擇理由。
```

我會看他回報的具體位置。例如說符合單一職責，就指出哪個模組負責哪件事；說測試獨立，就看測試能不能單獨執行。只回一句「已遵守 SOLID／FIRST」，還看不出他做了什麼。

## 坑

把原則寫進 prompt，仍然要檢查產出。小功能拆出很多介面、每一層都包一個 factory，可能只是多了維護成本。模式要能解釋它處理了哪個問題。

FIRST 管的是測試的品質，測試案例本身是否符合需求，還是要像 Tip 09 那樣，用具體輸入和預期結果確認。

## 小結

實作前補上 SOLID、FIRST 與 design patterns 的要求，完成後請他對照實際程式碼和測試回報。

明天講設計原型：先用 Claude Design 或 HTML 把 mobile 畫面做出來看。

參考：
- Microsoft：Dangers of Violating SOLID Principles https://learn.microsoft.com/en-us/archive/msdn-magazine/2014/may/csharp-best-practices-dangers-of-violating-solid-principles-in-csharp
- ETH Zurich：Unit Testing https://siscourses.ethz.ch/sib_workshop_best_practices/UnitTesting/UnitTesting.html