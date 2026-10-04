---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜派出子代理：會塞爆 context 的工作交給 subagent，只拿摘要回來 - Tip 22"
date: 2026-10-04 13:00 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - Claude Code
  - subagent
  - context window
summary: "說明何時把大型輸出、平行研究和串接任務交給 subagent，並用可直接複製的 prompt 範例控制回傳內容。"
description: "說明何時把大型輸出、平行研究和串接任務交給 subagent，並用可直接複製的 prompt 範例控制回傳內容。"
---
本篇 iT 鐵人賽文章：[前往 iT 閱讀](https://ithelp.ithome.com.tw/articles/10420778)。

一段工作會吐出一大堆你之後用不到的東西，像跑測試、翻文件、讀 log，就派一個 subagent 去做。他在自己的 context 裡做完，只把摘要交回來。

## 為什麼

主對話的 context 有限（Tip 13 講 log 的時候就在省它）。subagent 有自己的 context window、自己的 system prompt、自己的工具權限；他去做那件事，中間的雜訊留在他那邊，主對話只收結果。Claude Code 的文件列的好處：保住主對話的 context、限制他能用哪些工具、同一套設定跨專案重用、把瑣事丟給便宜又快的模型。

## 我怎麼做

**用內建的就有。** Claude Code 內建幾個 subagent：Explore 是唯讀的，找檔案、搜 code、看 codebase，不能寫檔；Plan 在 plan mode 時負責研究。Claude 判斷任務對得上就自己派。

**要派得更準，自己講：**

```
用一個 subagent 跑整套測試，只回報失敗的測試和錯誤訊息。
```

```
用三個 subagent 分頭研究 auth、database、API 這三個模組，各自回報。
```

還有一種是串起來，前一個做完，Claude 把要用的部分交給下一個：

```
用 code-reviewer 這個 subagent 找出效能問題，再用 optimizer 把它們修掉。
```

第一種是把大量輸出隔離在外面；第二種是平行研究，路徑互不相關時最有效；串起來的那一種適合分階段的工作。

**要固定一種工人，寫成檔案。** 專案裡 `.claude/agents/<name>.md`，frontmatter 寫 name、description、能用的工具、模型，內文是他的 system prompt。description 決定 Claude 什麼時候派他，寫短、寫準。之後在對話裡用 `@` 點名，或者直接說「用 code-reviewer 這個 subagent 看我剛改的」。

## 坑

subagent 是全新開始的：看不到你們前面的對話、看不到你已經讀過的檔案。Claude 會寫一段委派說明給他，你要的東西沒在那段裡就要自己講。另外每個 subagent 的結果都會回到主對話，派很多個、每個回一大段，context 一樣會滿。工作需要來回討論、或者幾個階段共用很多 context 的，留在主對話做就好。

## 小結

會吐一堆東西、又能自己做完的工作，派 subagent；要來回討論的，留在主對話。

明天講他接外面工具的標準：MCP。

參考：
- Claude Code 文件：subagents https://code.claude.com/docs/en/sub-agents
