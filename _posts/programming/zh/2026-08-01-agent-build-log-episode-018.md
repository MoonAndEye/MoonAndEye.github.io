---
layout: single
title: "Agent Build Log — Episode 018"
date: 2026-08-01 23:47:46 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-018.png
summary: "Alpha 階段的目標使用者從開發者改為負責需求驗收的 PM 與 QA。"
description: "Alpha 階段的目標使用者從開發者改為負責需求驗收的 PM 與 QA。"
---

今天，我調整了 Agent 的目標使用者。

![Agent Build Log Episode 018：將 Agent 的目標使用者調整為 PM 與 QA](/assets/programming/agent-build-log/agent-build-log-episode-018.png)

一開始，我想把它做給 iOS 和 Android 開發者使用。

除了基本的 coding agent 能力之外，我也打算加入各種客製化 tools，並針對我工作上常用的 skills 做特化。

但今天，我把 Agent 的 TA 從「開發者」改成了「驗收者」。

在我現在的工作環境裡，負責驗收的人通常是 PM 或 QA。

他們需要確認一個需求是不是真的完成、某個 bug 是不是真的修好，以及這一版 App 的行為是否符合預期。

但這個過程裡，他們常常會卡在兩件事上：

怎麼把最新的 code build 起來。

以及怎麼驗證這一版 App 真的有修好。

最近，PM 和 QA 也向我反映，他們希望可以縮短從拿到版本到完成驗收之間的時間。

這讓我重新思考，第一版 Agent 真正應該服務的人是誰。

如果我繼續把目標放在開發者身上，我的 Agent 就會直接和 Codex、Claude App 這些產品競爭。

它們本來就是為軟體開發特化的工具。

不論是理解 codebase、修改程式、執行指令，還是完成開發任務，我都很難在第一版就和這些成熟的產品正面競爭。

但「驗收需求」是一個不同的問題。

即使 PM 或 QA 拿到了 Codex 或 Claude App，他們通常還是需要開發者先協助設定 repository、build environment、credentials、tools，以及測試流程。

工具雖然存在，但使用門檻並沒有真的消失。

所以我開始意識到，我的 Agent 不一定要先成為另一個更好的 coding agent。

它可以先把開發者已經準備好的環境和流程包起來，讓驗收者可以直接使用。

驗收者不需要先理解整個專案怎麼建置，也不需要記住每一個 command。

他們只需要告訴 Agent：

> 「幫我 build 最新版本。」

> 「幫我確認這個 bug 是否修好。」

> 「幫我按照 ticket 的條件驗證這個功能。」

Agent 再負責執行背後的 build、安裝、測試和驗證流程。

所以從今天開始，Alpha 階段的目標正式更改。

第一版 Agent 不再以「幫助開發者寫 App」為主要方向。

它會先聚焦在「幫助 PM 和 QA 驗收需求」。

我找到了一個更明確，而且目前更需要被解決的問題。
