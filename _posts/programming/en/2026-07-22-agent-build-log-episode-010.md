---
layout: single
title: "Agent Build Log — Episode 010"
date: 2026-07-22 23:55:34 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-010.png
summary: "I planned the Agent memory system and chose LanceDB with Qwen3 Embedding 0.6B for a lightweight first version that runs locally on my Mac mini."
description: "I planned the Agent memory system and chose LanceDB with Qwen3 Embedding 0.6B for a lightweight first version that runs locally on my Mac mini."
---

Today, I started planning the Agent’s memory system.

![Agent Build Log Episode 010: a memory system using LanceDB and Qwen3 Embedding 0.6B](/assets/programming/agent-build-log/agent-build-log-episode-010.png)

Before writing any code, I spent some time looking through a few well-known open-source projects with strong GitHub traction. I wanted to see how other teams handle storing memories, searching them, and bringing the right ones back when needed.

After going through several options, I had to come back to my actual setup.

This memory system needs to run directly on my Mac mini. I don’t want to start with a heavy model, and I don’t want to push everything to the cloud, so I decided to begin with LanceDB and Qwen3 Embedding 0.6B.

LanceDB will handle storing and searching the memories, while Qwen3 Embedding 0.6B will turn conversations and events into vectors that can be retrieved later.

Along the way, I also looked into the basic architectures of Mem0, Letta, MemOS, and Cognee. They all had useful ideas, but none of them matched the kind of Agent I’m trying to build right now.

I’ve saved my notes on them for later, but I’m not using them for the first version.

For now, the memory system starts with LanceDB and Qwen3 Embedding 0.6B.
