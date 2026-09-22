---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜iOS 開發用 XcodeBuildMCP：讓他自己 build、跑 simulator - Tip 10"
date: 2026-09-22 13:00 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - iOS
  - XcodeBuildMCP
  - Swift
  - MCP
summary: "用 XcodeBuildMCP 把 iOS 專案的 build、simulator 與 log 交給 agent，並整理安裝方式、CLI 與 code signing 的坑。"
description: "用 XcodeBuildMCP 把 iOS 專案的 build、simulator 與 log 交給 agent，並整理安裝方式、CLI 與 code signing 的坑。"
---

做 iOS，我給他裝 XcodeBuildMCP。這很好用。

## 為什麼

他改完 Swift 的 code，得有人 build、跑起來、看 log。沒有工具的時候，他只能在 terminal 裡拼 `xcodebuild` 和 `simctl` 的指令，參數長、出錯的地方多。XcodeBuildMCP 把這些包成他能直接呼叫的工具：build、跑 simulator、抓 log，他自己來。

## 我怎麼做

XcodeBuildMCP 是一個 MCP server 加 CLI，給 agent 在 iOS 和 macOS 專案上用的工具。Homebrew 或 npm 都能裝：

```bash
brew tap getsentry/xcodebuildmcp
brew install xcodebuildmcp

# 或
npm install -g xcodebuildmcp@latest
```

接到 Claude Code、Codex、Cursor 的設定片段在官方文件的 MCP Clients 那一頁；大部分 client 也可以不裝，直接用 `npx -y xcodebuildmcp@latest mcp` 按需啟動。

同一個套件也有 CLI，人自己在 terminal 也能用：

```bash
xcodebuildmcp tools
xcodebuildmcp simulator build --scheme MyApp --project-path ./MyApp.xcodeproj
```

抓 log、debug 這類要記狀態的操作，CLI 靠一個跟著工作目錄跑的 daemon，需要時自己起來，人不用管。

## 坑

照 README：要 macOS 14.5 以上、Xcode 16 以上，npm 裝法要 Node.js 18 以上。裝到實機的工具要先在 Xcode 把 code signing 設好。它會用 Sentry 收執行期錯誤的 telemetry，不要的話文件裡有關掉的方法。

## 小結

iOS 專案裝 XcodeBuildMCP，build、跑 simulator、抓 log 交給他。

明天講 mobile 的登入：Firebase Authentication。

參考：
- XcodeBuildMCP https://github.com/getsentry/XcodeBuildMCP
