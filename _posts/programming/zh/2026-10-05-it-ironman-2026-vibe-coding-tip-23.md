---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜MCP 的概念：agent 接外面工具的標準插座 - Tip 23"
date: 2026-10-05 13:00 +0800
category: programming
author: Marvin Lin
tags: [IT鐵人賽, 2026鐵人賽, Vibe Coding, Vibe Coding 技巧, MCP, Claude Code]
summary: "整理 MCP 如何讓 coding agent 連接 Jira、資料庫、監控等外部服務，示範 Claude Code 的 HTTP／stdio 設定和接入前要確認的信任風險。"
description: "整理 MCP 如何讓 coding agent 連接 Jira、資料庫、監控等外部服務，示範 Claude Code 的 HTTP／stdio 設定和接入前要確認的信任風險。"
---

本篇 iT 鐵人賽文章：[前往 iT 閱讀](https://ithelp.ithome.com.tw/articles/10421246)。

MCP 是 Model Context Protocol，一個開放標準：外面的工具、資料庫、服務照這個標準做一個 server，agent 就能接上去用。Tip 10 的 XcodeBuildMCP、Tip 18 提到的 Jira MCP，都是這種 server。

## 為什麼

沒有 MCP 的時候，他要用外面的東西，靠的是你把資料貼進對話，或者他自己拼 CLI 指令。Claude Code 的文件講什麼時候該接一個 server：當你發現自己一直從別的工具，像 issue tracker、監控面板，複製東西進對話。接上之後，他直接讀、直接動那個系統。

文件列的例子：從 Jira 的 issue 做功能、開 PR；查 Sentry 和 Statsig 看某個功能的使用量；從 PostgreSQL 撈十個用過某功能的使用者；照 Figma 的設計更新 email 模板；開 Gmail 草稿邀人。

## 我怎麼做

Claude Code 用 `claude mcp add` 接 server，常見的兩種接法：

```bash
# 遠端 HTTP server（雲端服務最常見）
claude mcp add --transport http <name> <url>

# 本機 stdio server：跑一個本地程式當 server
claude mcp add --transport stdio airtable -- npx -y airtable-mcp-server

# 管理
claude mcp list
claude mcp get <name>
claude mcp remove <name>
```

`claude mcp list` 會在每個 server 旁邊標狀態：連上了、要先登入、連不上。雲端的 server 多半要授權，在 Claude Code 裡打 `/mcp`，挑那一台把登入流程走完；之後 token 被伺服器退掉，也是回到 `/mcp` 重新登入。

要找現成的 server，Anthropic Directory 上有審過的；自己做的話，MCP 的規格、schema 和文件都在 modelcontextprotocol.io。

## 坑

接進來的 server 等於讓他多一雙手。文件特別提醒：接之前確認你信任這個 server；會抓外部內容的 server 有 prompt injection 的風險。

## 小結

MCP 是 agent 接工具的標準插座。用得到就接，接之前看清楚是誰的。

明天講這一組的最後一個：Codex CLI，它是 CLI，所以別的 agent 也叫得動它。

參考：
- Claude Code 文件：MCP https://code.claude.com/docs/en/mcp
- Model Context Protocol https://modelcontextprotocol.io
