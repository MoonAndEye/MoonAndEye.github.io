---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜Codex CLI 的概念：它是 CLI，所以 Claude 叫得動它 - Tip 24"
date: 2026-10-06 13:00 +0800
category: programming
author: Marvin Lin
tags: [IT鐵人賽, 2026鐵人賽, Vibe Coding, Vibe Coding 技巧, Codex CLI, Claude Code]
summary: "整理 Codex CLI 如何讓 Claude Code 呼叫 Codex、用 codex exec 交辦非互動任務，並保留我目前無法以 -p 呼叫 Claude Code 的限制。"
description: "整理 Codex CLI 如何讓 Claude Code 呼叫 Codex、用 codex exec 交辦非互動任務，並保留我目前無法以 -p 呼叫 Claude Code 的限制。"
---

本篇 iT 鐵人賽文章：[前往 iT 閱讀](https://ithelp.ithome.com.tw/articles/10421615)。

Codex CLI 是 OpenAI 的 coding agent，在你自己的電腦上跑的 terminal 版。因為它是 CLI，別的 agent 也叫得動它：Claude Code 可以在 terminal 裡呼叫 Codex，把一件事交給他做。反過來，用 -p 叫 Claude Code 這條路，現在對我來說行不通了。

## 為什麼

一個 agent 做成 CLI，就多了一種被使用的方式：人在 terminal 裡一句一句問是一種，別的程式、別的 agent 丟一句話進來、拿結果走是另一種。Claude Code 本來就能跑 shell 指令，所以 Codex 只要是 CLI，Claude 就能把它當工具用：讓 Codex 去做一段、看結果、再接著做。兩個 agent 各有擅長的事，接起來互相補。

## 我怎麼做

**裝 Codex CLI**（照它的 README）：

```bash
npm install -g @openai/codex
# 或
brew install --cask codex
```

跑 `codex`，選 Sign in with ChatGPT，用 ChatGPT 的方案登入。

**互動用**：`codex` 進去一句一句下。**被程式叫**：`codex exec` 是非互動模式，prompt 當參數丟進去，做完印結果就走。所以在 Claude Code 裡可以這樣講：

```
用 codex exec 叫 Codex 把 src/cart 底下的測試補齊，做完把它的輸出貼給我看。
```

Claude 會在 terminal 裡跑 Codex，等它做完，讀輸出。

## 坑

反過來，Claude Code 也有 `-p`（print，非互動模式）。以前我可以用它讓別的程式叫 Claude；現在這條路對我行不通了，所以「誰叫誰」我只留 Claude 叫 Codex 這一個方向。

## 小結

Codex CLI 是 CLI，所以 Claude 叫得動它，`codex exec` 一句話交辦。兩個 agent 接起來用。

明天講紀錄放哪裡：GitHub Issues，一件事一張票。

參考：
- openai/codex https://github.com/openai/codex
- Claude Code 文件：非互動模式 https://code.claude.com/docs/en/headless
