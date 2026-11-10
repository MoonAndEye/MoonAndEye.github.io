---
layout: single
title: 為什麼我做了 Lian Wu（蓮霧）
date: 2026-10-15 12:00 +0800
category: programming
author: Marvin Lin
tags: [Lian Wu, AI, AI Agent, Mac]
lang: zh
summary: 我常常換不同的 AI，但對話從來不會跟著我走。所以我做了一個會把對話一起帶走的 agent app。
description: 我常常換不同的 AI，但對話從來不會跟著我走。所以我做了一個會把對話一起帶走的 agent app。
---

*原文刊於 [Lian Wu 部落格](https://lianwu.app/blog/why-i-built-lian-wu)。英文版：[Why I built Lian Wu](/en/programming/why-i-built-lian-wu/)。*

我常常試不同的 AI：OpenAI 的 GPT、Gemini、Grok、Claude，還有很多透過 OpenRouter 接進來的模型。

可是每次一換，對話就留在舊的 app 裡。新的 AI 不知道我剛才在做什麼，我只好停下來、換地方重來，節奏斷了。

我也試過像 OpenCode 這種能接很多 provider 的工具。沒有一個感覺像我要的 agent。

所以我自己做了一個：給 Mac 用的桌面 agent app，照我喜歡的方式工作。在 Lian Wu 裡，我可以在同一段對話中途換成另一個 AI，整段對話會一起跟著過去。

比較大的工作，Lian Wu 還有 Guilds。一個 Guild 會把好幾個 skill 照順序串起來，完成一件事，有點像 Codex 或 Claude Code 的 plugins。例如 Code Review，會把一個 pull request 交給一組 AI reviewers，每個發現都投票決定。

名字從哪來？蓮霧是我長大的地方常見的水果，英文叫 wax apple。又脆又多汁又好吃，所以我用它幫 app 命名。

![掛在枝上的粉紅與紅色蓮霧](/assets/programming/why-i-built-lian-wu/wax-apples.jpg)

故事就是這樣。下面是 app 本身：這支 75 秒的 demo 裡，Claude 把四十則留言分組。接著我在同一段對話切到 GPT，由 GPT 檢查 Claude 的結果。

{% include youtube.html id="gVZYmYk5FtY" title="Claude hit its limit? Keep the same conversation in GPT (Mac app)" %}
