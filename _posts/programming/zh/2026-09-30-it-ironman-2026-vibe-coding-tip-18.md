---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜非開發職能也能用：PM 用 Codex App 或 Claude App 寫 Given-When-Then，直接進 Jira - Tip 18"
date: 2026-09-30 13:00 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - PM
  - Jira
  - Given-When-Then
  - Codex App
  - Claude App
summary: "我示範如何用 Codex App 或 Claude App 把 PM 的需求整理成 Given-When-Then 並寫進 Jira，也說明 prompt 要補哪些業務規則，避免開出只有通用錯誤訊息的需求單。"
description: "我示範如何用 Codex App 或 Claude App 把 PM 的需求整理成 Given-When-Then 並寫進 Jira，也說明 prompt 要補哪些業務規則，避免開出只有通用錯誤訊息的需求單。"
---

本文同步刊登於 [iT 鐵人賽第二系列](https://ithelp.ithome.com.tw/articles/10419204).

這一篇改寫自我部落格的《在非開發職能上，使用 Cursor 在 Jira 寫 GWT (Given - When - Then) 需求單》，照這個系列的格式重寫過。原始文章：https://www.marvinswift.com/zh/programming/using-cursor-in-jira/

coding agent 產出的「文字」本來就可以超過「程式」的範圍。團隊裡的 PM 也能用他開單：用 Codex App 或 Claude App 產 Given-When-Then 的需求單，直接寫進 Jira。開發者就能快速跨過自然語言和程式語言的隔閡，直接進開發。

## 為什麼

寫需求單這件事，他產的是文字，程式只是文字的一種。PM 用跟開發者同一類的工具寫需求單，寫出來的格式是開發者看得懂、測試也能直接對的 Given-When-Then，兩邊接起來就快。

原文（2025 年 3 月）是用 Cursor 做這件事，還要裝 Jira 外掛、開資料夾管文件。現在用 Codex App 或 Claude App，打開就能用，Cursor 那一套省掉了。

## 我怎麼做

打開 Codex App 或 Claude App，這樣下：

```markdown
請依 Given - When - Then (GWT) 的格式，將下列需求寫成 GWT 文件。
login
logout
reset password
```

產出來的其中一段長這樣：

```gherkin
Feature: 使用者登入

Scenario: 成功登入
Given 使用者在登入頁面
When 使用者輸入正確的帳號和密碼
And 點擊登入按鈕
Then 系統應該成功登入
And 導向到首頁
And 顯示登入成功訊息

Scenario: 登入失敗 - 錯誤的認證資訊
Given 使用者在登入頁面
When 使用者輸入錯誤的帳號或密碼
And 點擊登入按鈕
Then 系統應該顯示錯誤訊息
And 使用者停留在登入頁面
```

每個功能都有成功和失敗的情境：Given 是初始狀態，When 是使用者的操作，Then 是預期的系統回應。這段直接寫進 Jira 的票。接了 Jira 的 MCP，可以讓他直接把票開進 Jira；沒接，複製貼進票裡也只是一步。

## 坑

他只知道你寫在 prompt 裡的事。上面那段 prompt 只給了三個功能名，所以產出來的 Then 是「顯示錯誤訊息」這種通用句。業務規則要一起給，像密碼錯幾次要鎖、鎖多久，他才寫得進 Scenario；沒給的，他會用最常見的做法補上，開票前自己先看一遍。

## 小結

寫需求單這件事，PM 用 Codex App 或 Claude App 就能做，產出來是 Given-When-Then，進 Jira 之後開發者直接接。

明天開始講 skill 那一組：先講 skill 放在哪裡、從哪裡拿。

原文：https://www.marvinswift.com/zh/programming/using-cursor-in-jira/