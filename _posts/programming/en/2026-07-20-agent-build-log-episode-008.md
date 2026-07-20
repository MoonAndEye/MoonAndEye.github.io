---
layout: single
title: "Agent Build Log — Episode 008"
date: 2026-07-20 20:55:30 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-008.png
summary: "I started restructuring the Agent core so the CLI, Browser, and Desktop App share the same capabilities while remaining thin clients."
description: "I started restructuring the Agent core so the CLI, Browser, and Desktop App share the same capabilities while remaining thin clients."
---

Today, I found a problem.

![Agent Build Log Episode 008: one Agent core shared by the CLI, Browser, and Desktop App](/assets/programming/agent-build-log/agent-build-log-episode-008.png)

The CLI, Browser, and Desktop App all appeared to be using the same Agent. In reality, they were not running through the same underlying logic. They only worked consistently because the three implementations happened to stay in sync.

In other words, I hadn’t actually built it the way I intended.

After discovering this, I had the Agent start restructuring this layer.

The goal is clear: whenever I add a new tool to the core, it should immediately become available to the CLI, Browser, and Desktop App. Each interface should not have to implement the same capability again.

I also want all three interfaces to remain thin. They should only handle input, display results, and manage their own interactions—not reimplement the Agent’s capabilities and logic.

I didn’t add any new features today. Instead, I started replacing something that was only “consistent by coincidence” with a system truly powered by the same shared capabilities.
