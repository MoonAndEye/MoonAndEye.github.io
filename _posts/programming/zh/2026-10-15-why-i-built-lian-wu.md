---
layout: single
title: 為什麼我做了 Lian Wu（蓮霧）
date: 2026-10-15 12:00 +0800
category: programming
author: Marvin Lin
tags: [Lian Wu, AI, AI Agent, Mac]
lang: zh
summary: 換 AI 的時候，對話留在舊的 app。所以我做了一個 Mac agent app，換 AI，對話會跟著走。
description: 換 AI 的時候，對話留在舊的 app。所以我做了一個 Mac agent app，換 AI，對話會跟著走。
---

*原文刊於 [Lian Wu 部落格](https://lianwu.app/blog/why-i-built-lian-wu)。英文版：[Why I built Lian Wu](/en/programming/why-i-built-lian-wu/)。*

我平常會輪流用好幾家的 AI：OpenAI 的 GPT、Gemini、Grok、Claude，還有透過 OpenRouter 接的各種模型。

麻煩在換的那一刻。對話留在原本的 app，新的 AI 不知道我剛剛在做什麼。我只能停下來，到另一個地方從頭交代一次，原本的節奏就斷了。

OpenCode 這類可以接很多 provider 的工具，我也用過。但用起來，都不是我想要的 agent。

所以我自己做了一個。Lian Wu 是 Mac 上的桌面 agent app，照我習慣的方式工作。對話做到一半，我可以直接換成另一個 AI，前面的整段對話會一起帶過去。

## Guild：把好幾個 skill 串成一件事

比較大的工作，我會交給 Guild。一個 Guild 會把幾個 skill 照順序串起來，完成一件事，概念有點像 Codex 或 Claude Code 的 plugin。

例如 Code Review。它會把一個 pull request 交給一組 AI reviewer，每一個發現都由大家投票決定要不要留下。

## 為什麼叫蓮霧

蓮霧是我長大的地方很常見的水果，英文叫 wax apple。咬下去很脆、水分很多，很好吃，所以我用它來命名。

![掛在枝上的粉紅與紅色蓮霧](/assets/programming/why-i-built-lian-wu/wax-apples.jpg)

## 實際用起來

下面這支 75 秒的 demo，先讓 Claude 把四十則留言分組。接著我在同一段對話裡換成 GPT，請 GPT 檢查 Claude 分得對不對。

{% include youtube.html id="gVZYmYk5FtY" title="Claude hit its limit? Keep the same conversation in GPT (Mac app)" %}
