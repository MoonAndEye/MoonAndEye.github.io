---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜Plugin 的概念：skill、subagent、hook、MCP server 打包成一個可以分享的東西 - Tip 21"
date: 2026-10-03 13:05 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - Plugins
  - Agent
  - MCP
summary: "整理 Claude Code 與 Codex 的 plugin 目錄，說明如何把 skill、subagent、hook 和 MCP server 打包分享，也列出安裝與從 standalone 遷移時要檢查的設定。"
description: "整理 Claude Code 與 Codex 的 plugin 目錄，說明如何把 skill、subagent、hook 和 MCP server 打包分享，也列出安裝與從 standalone 遷移時要檢查的設定。"
---
plugin 是一個資料夾，把 skill、subagent、hook、MCP server 這些東西打包在一起，一次裝、一次分享。

## 為什麼

skill 一個一個裝可以。但一套做法常常不只一個 skill：還有 agent 的定義、事件的 hook、要接的 MCP server。要給隊友或公開分享，散著給就會漏。plugin 把它們收在一個目錄裡，有版本，裝的人一個指令。

Claude Code 的文件把兩種放法分開：放在專案的 `.claude/` 目錄裡是 standalone，適合個人流程、專案裡的客製和快速試；要分享給隊友、公開發布、跨專案重用，就做成 plugin。它建議先用 `.claude/` 快速迭代，要分享時再轉成 plugin。

## 我怎麼做

**Claude Code 的 plugin 長這樣：**

```
my-plugin/
├── .claude-plugin/plugin.json   ← manifest
├── skills/<name>/SKILL.md
├── agents/                      ← subagent 的定義
├── hooks/hooks.json
├── .mcp.json                    ← MCP server 設定
└── settings.json                ← 啟用時套上的預設設定
```

安裝方式在 Tip 19 講過了。這裡看打包後的差別：plugin 裡的 skill 用 `/plugin-name:skill-name` 呼叫，名稱帶著所屬 plugin，方便分辨來源。

**Codex 那邊一樣的形狀：** openai/plugins 裡每個 plugin 一個 `.codex-plugin/plugin.json`，旁邊放 `skills/`、`.mcp.json`、`agents/`、`commands/`、`hooks.json`；預設的 marketplace 是 `.agents/plugins/marketplace.json`。

## 坑

一個 plugin 裝進來的東西比表面上多：hook 綁在事件上，背景 monitor 在 plugin 啟用的時候自己開始跑，`.mcp.json` 會把外面的 server 接進來，`settings.json` 會套上它的預設設定。裝之前把目錄看過一遍，來源要是自己信得過的。

自己把 `.claude/` 轉成 plugin 之後，原本那幾份記得刪掉。專案和個人 `.claude/agents/` 裡同名的 subagent 定義會蓋過 plugin 裡那一份，留著就一直用到舊的；skill 那邊則是兩份並存，各自有各自的叫法。

## 小結

plugin 是 skill 往上一層的包法：一個目錄、一個 manifest、一個指令裝。

明天講 plugin 裡常見的一件東西：subagent，把一段工作派出去。

參考：
- Claude Code 文件：plugins https://code.claude.com/docs/en/plugins
- Claude Code 文件：plugin marketplaces https://code.claude.com/docs/en/plugin-marketplaces
- openai/plugins https://github.com/openai/plugins
