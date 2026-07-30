---
layout: single
title: "Agent Build Log — Episode 016"
date: 2026-07-30 23:53:58 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-016.png
summary: "移除 DKS MCP 的 Jira 整合，讓每位使用者透過 Jira MCP 與自己的 OAuth 權限查詢資料。"
description: "移除 DKS MCP 的 Jira 整合，讓每位使用者透過 Jira MCP 與自己的 OAuth 權限查詢資料。"
---

今天，我把 DKS MCP 裡所有和 Jira 有關的功能都拔掉了。

![Agent Build Log Episode 016：重新劃分 DKS 與 Jira 的權限邊界](/assets/programming/agent-build-log/agent-build-log-episode-016.png)

原本的設計，是讓 DKS 可以在查 GitLab repo 相關時，附上 Jira ticket 來當輔助證明。

這樣 Agent 可以更加理解一個 feature 的來龍去脈。

但後來我發現，它有一個很嚴重的權限問題。

Jira 的 board、issue 和專案本身都有各自的存取權限。

如果 DKS MCP 使用自己的 Jira credential，替 user 查詢 Jira，那最後能看到哪些資料，取決於 DKS 使用的帳號，而不是正在使用 Agent 的那個人。

這代表，一個原本沒有權限查看某個 Jira board 的 stakeholder，可能透過 DKS 拿到超出自己權限範圍的 issue、需求背景，甚至其他相關資訊。

即使使用者只是問一個看起來很普通的問題：

> 「這個功能當初為什麼這樣做？」

DKS 也可能在背後查到使用者原本不應該看到的 Jira 內容，再把資訊整理進答案裡。

這是權限邊界設計錯了。

所以今天，我先把 DKS MCP 裡所有和 Jira 有關的 MCP 與查詢能力移除。

每個使用者都必須透過 Jira MCP 完成自己的 OAuth，使用自己的身分與權限查詢 Jira。

這樣 Jira 回傳的內容，才會和使用者原本在 Jira 裡能看到的範圍一致。

DKS 仍然負責 GitLab 相關的 repository、MR 和 commit 查詢。

當 Agent 需要 Jira 資訊時，則改由已完成使用者 OAuth 的 Jira MCP 處理。

兩邊仍然可以在 Agent 層整合，但不能再共用同一個 Jira 權限。

在有權限差異的系統裡，方便不能優先於存取控制。
