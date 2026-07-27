---
layout: single
title: "Agent Build Log — Episode 014"
date: 2026-07-27 23:18:02 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-014.png
summary: "DKS 改用 GitLab API 與 Jira 查詢，不再為整個部門建立 Git repo mirror。"
description: "DKS 改用 GitLab API 與 Jira 查詢，不再為整個部門建立 Git repo mirror。"
---

今天，我改了 DKS（Developer Knowledge Service）MCP 的設計。

![Agent Build Log Episode 014：DKS 改用 GitLab API 與 Jira](/assets/programming/agent-build-log/agent-build-log-episode-014.png)

一開始，我想把部門的 Git repo 全部 mirror 到 Mac mini。這樣 DKS MCP 就可以查 MR、commit、開發意圖，以及一個 feature 最後是怎麼被實作的。

但我很快碰到一個很現實的限制：我現在能用的 Mac mini，硬碟空間不足以放下整個部門的 repo mirror。

所以我把 Git repo 相關的查詢改掉，讓 MCP 改用 GitLab API。

Jira 的查詢能力還是保留。只要 Jira 上有相關紀錄，也能和 commit 對得起來，Agent 還是可以把一個 feature 的背景和實際改動串起來。

我把資料來源改到 GitLab API 和 Jira，避免整個部門的 repo mirror 卡在 Mac mini 的硬碟空間上。之後我不會再為 DKS 建 repo mirror。
