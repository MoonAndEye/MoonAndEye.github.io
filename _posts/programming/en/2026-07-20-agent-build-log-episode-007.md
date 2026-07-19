---
layout: single
title: "Agent Build Log — Episode 007"
date: 2026-07-20 00:25:37 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-007.png
summary: "I studied Google’s ADK and Agents CLI to understand how coding agents can use reusable commands and skills to build, evaluate, and deploy agents."
description: "I studied Google’s ADK and Agents CLI to understand how coding agents can use reusable commands and skills to build, evaluate, and deploy agents."
---

Today, I spent some time studying Google’s ADK and Agents CLI to see how Google turns the agent-building process into something repeatable.

![Agent Build Log Episode 007: studying Google ADK and Agents CLI](/assets/programming/agent-build-log/agent-build-log-episode-007.png)

Agents CLI is not another coding agent. It provides commands and skills that Codex, Claude Code, and other coding agents can use to build, evaluate, and deploy ADK agents.

![Google Agents CLI architecture](/assets/programming/agent-build-log/google-agents-cli-architecture.png)

What I really wanted to understand was how someone could describe an Agent in natural language, then take it all the way from creation to deployment.

I’m not planning to copy the entire approach into my own Agent. This was more about studying how others built it, finding the ideas worth learning from, and deciding which parts I might rebuild in my own way.

Building my own Agent does not mean everything has to start from zero.

Stand on the shoulders of giants.

GitHub:
[https://github.com/google/agents-cli](https://github.com/google/agents-cli)
