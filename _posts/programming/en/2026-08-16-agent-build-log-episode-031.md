---
layout: single
title: "Agent Build Log — Episode 031"
date: 2026-08-16 23:22:47 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-031.png
summary: "I started designing plug-in-based IM integrations that keep chat transport separate from the Agent itself."
description: "I started designing plug-in-based IM integrations that keep chat transport separate from the Agent itself."
---

Today, I started working on IM integrations like Google Chat, with some of the design inspired by OpenClaw.

![Agent Build Log Episode 031: plug-in-based IM integrations](/assets/programming/agent-build-log/agent-build-log-episode-031.png)

The basic idea is to use a plug-in architecture that keeps the Agent itself separate from the parts responsible for receiving and replying to chat messages.

When an inbound chat message mentions the Chat app I configured, the plug-in first identifies it using the space ID and message ID.

It also goes through a deduplication step before the message is passed into the Agent layer for processing.

Once the Agent finishes the task, the result goes back through the chat plug-in, which sends the response back to the conversation.
