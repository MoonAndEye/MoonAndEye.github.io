---
layout: single
title: "Agent Build Log — Episode 021"
date: 2026-08-04 22:55:30 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-021.png
summary: "開始實作規格驗收 capability，串接 branch、build、模擬器操作、截圖、報告與頻道交付流程。"
description: "開始實作規格驗收 capability，串接 branch、build、模擬器操作、截圖、報告與頻道交付流程。"
---

今天，我開始實作 Agent 的第一個 capability：規格驗收。

![Agent Build Log Episode 021：實作規格驗收的完整執行路徑](/assets/programming/agent-build-log/agent-build-log-episode-021.png)

我說的規格驗收，不是執行 unit test 或 UI test，再把測試結果整理成報告。

它的起點可以是一張 Jira ticket，也可以是一段用自然語言描述的規格或驗收條件。

但它的終點不是讓 Agent 只檢查程式碼，或判斷測試是否通過。

Agent 需要實際操作 repo，切換到指定的 target branch，準備對應的開發環境，再把 iOS Simulator 或 Android Emulator build 起來。

接著，Agent 會直接操作 App。

它會根據 Jira ticket 或驗收規格，進入指定頁面、執行操作，確認畫面與行為是否符合預期。

不論驗收的是 bug or feature，Agent 都要確認問題是否真的已經修正 or 實作正確。

驗收過程中的關鍵畫面會被截圖，作為驗收證據。

完成後，Agent 會把驗收步驟、執行結果和截圖整理成 HTML 與 PDF 報告，再透過 chat bot 發送到指定頻道。

有了這個想法之後，我就讓 Agent 開始動手完成第一版。

但第一次嘗試失敗了。

目前 Agent 還沒有成功連上 CoreSimulator。

iOS Simulator 沒有正常啟動，驗收流程沒有真的執行，最後產出的報告也是空的。

所以第一版的規格驗收還沒有成功。

但至少現在，我已經確認這個 capability 真正需要打通的完整路徑：

從 Jira ticket 或自然語言規格開始。

切換 branch、build App、啟動模擬器、操作 App、取得截圖、產出報告，最後把結果送到頻道。

今天，我讓 Agent 第一次嘗試自己完成規格驗收。

它失敗了，但， episode 會繼續
