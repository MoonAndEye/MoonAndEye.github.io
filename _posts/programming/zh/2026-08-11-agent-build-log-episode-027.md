---
layout: single
title: "Agent Build Log — Episode 027"
date: 2026-08-11 22:40:07 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-027.png
summary: "打造 Acceptance，將 Jira ticket 轉換成 iOS 或 Android 的完整驗收流程與證據報告。"
description: "打造 Acceptance，將 Jira ticket 轉換成 iOS 或 Android 的完整驗收流程與證據報告。"
---

今天，我做了另一個 Agent 的「專有技」。

![Agent Build Log Episode 027：Acceptance 將 Jira ticket 轉換成完整驗收報告](/assets/programming/agent-build-log/agent-build-log-episode-027.png)

這次是 Acceptance。

它的起點是一張 Jira ticket。

終點則是一份完整的驗收報告。

我希望最後的驗收結果，不只是單純的 Pass 或 Fail。

而是分成四種狀態：

通過驗收。

未通過驗收。

待人類判定。

無法判定。

當 Agent 收到一張 Jira ticket 之後，第一步不是直接開始操作 App。

它要先找到這張 ticket 對應的 branch 或 commit。

接著 checkout 到正確的版本，開始 build code。

build 完成後，再依照 Jira ticket 上的 spec 進行真正的驗收。

如果是 iOS，Agent 會透過 XcodeBuildMCP 啟動 Simulator、操作 App，移動到指定頁面，再按照 ticket 裡的描述一步一步確認。

如果是 Android，Agent 本身已經可以直接操作 Emulator，所以同樣可以依照 spec 實際走完整個驗收流程。

過程中需要留下關鍵畫面的截圖。

最後再把操作步驟、驗收結果和證據整理成報告。

我刻意把結果設計成四種狀態，是因為有些事情 Agent 可以很明確地判斷，有些事情卻不應該硬給答案。

如果畫面和規格完全一致，就是通過驗收。

如果明確不符合，就是未通過驗收。

如果 Agent 已經完成操作，也取得證據，但最後還是需要產品、設計或 QA 幫忙確認，就標成待人類判定。

如果連驗收條件本身都無法完成，或證據不足，就標成無法判定。

我不希望 Agent 為了產出結果，硬把所有事情都塞進 Pass 或 Fail。

在目前一個很簡單的新手導覽頁驗收裡，我也順便比較了三個模型完成整個任務的時間。

Sol 大約 5 分鐘。

Terra 大約 8 分鐘。

Luna 大約 15 分鐘。

所以這又回到之前發現的事情：

Agent 任務真正重要的，不只是單次 response 有多快，而是整個驗收流程要花多久才能走完。

不過 iOS 的驗收目前還有一個很麻煩的問題。

如果 App 使用的是 Web 網頁型登入，XcodeBuildMCP 可以操作原生 App UI，但沒有辦法直接操作登入網頁裡面的 DOM 元素。

也就是說，Agent 可以一路走到登入畫面。

然後卡住。

這個問題要怎麼解決？

下一個 Episode 繼續。
