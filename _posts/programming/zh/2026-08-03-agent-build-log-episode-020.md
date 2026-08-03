---
layout: single
title: "Agent Build Log — Episode 020"
date: 2026-08-03 22:59:13 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-020.png
summary: "開始建立 Agent 的第一組驗收 capabilities：產生 acceptance brief，以及執行驗收並整理報告。"
description: "開始建立 Agent 的第一組驗收 capabilities：產生 acceptance brief，以及執行驗收並整理報告。"
---

今天，我開始實作 Agent 自己的 capabilities。

![Agent Build Log Episode 020：建立 acceptance brief 與驗收報告工具](/assets/programming/agent-build-log/agent-build-log-episode-020.png)

第一版先設計了兩個 tools。

第一個 tool 是撰寫 acceptance brief。

它會根據 Jira ticket，整理出這個項目應該怎麼驗收。

例如，驗收時需要進入哪一個頁面、執行哪些操作，以及看到什麼結果，才能證明這個需求或 bug 已經完成修正。

這個 tool 只負責列出驗收項目和驗收路徑，不會實際執行驗收。

第二個 tool 則負責實際驗收，並產出驗收報告。

Agent 會按照 acceptance brief 裡定義的路徑進行操作，在關鍵步驟截圖，再把結果和圖片整理到驗收報告裡。

所以這兩個 tools 負責的是不同階段。

第一個 tool 把 Jira ticket 轉換成可以執行的驗收計畫。

第二個 tool 按照這份計畫完成驗收，並留下可以交付和確認的證據。

這是我今天開始為 Agent 建立的第一組 acceptance capabilities。
