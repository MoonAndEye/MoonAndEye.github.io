---
layout: single
title: "Agent Build Log — Episode 002"
date: 2026-07-14 21:30:14 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
summary: "The first DKS MCP now searches MRs, commits, repositories, and Jira through one interface, while Pi Agent runs behind my own OAuth-enabled CLI wrapper."
description: "The first DKS MCP now searches MRs, commits, repositories, and Jira through one interface, while Pi Agent runs behind my own OAuth-enabled CLI wrapper."
image: /assets/programming/agent-build-log/agent-build-log-episode-002.png
---

Another major milestone completed.

![Agent Build Log Episode 002: DKS MCP and Pi Agent integration architecture](/assets/programming/agent-build-log/agent-build-log-episode-002.png)

## DKS (Developer Knowledge Service) MCP

The Developer Knowledge Service (DKS) MCP is now working.

Current capabilities:

- Search Merge Requests (MRs)
- Search commits
- Search repositories
- Integrated Jira API into the same MCP interface

The goal is to give my agent a unified entry point for engineering knowledge instead of scattering requests across different tools.

## Pi Agent Integration

Wrapped Pi Agent behind my own interface.

Verified:

- OAuth authentication works
- CLI commands execute successfully

Default configuration:

- Model: **GPT-5.6 Terra**
- Effort: **xhigh**

One step closer to replacing individual components while keeping the overall workflow stable.

The architecture is starting to take shape.
