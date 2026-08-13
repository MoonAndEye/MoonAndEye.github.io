---
layout: single
title: "Agent Build Log — Episode 029"
date: 2026-08-13 23:43:33 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-029.png
summary: "Exploring the Pi Agent extension ecosystem before rebuilding MCP integration, permissions, and Desktop GUI capabilities."
description: "Exploring the Pi Agent extension ecosystem before rebuilding MCP integration, permissions, and Desktop GUI capabilities."
---

Today, I started looking more seriously at the Pi Agent extension ecosystem.

![Agent Build Log Episode 029: exploring the Pi Agent extension ecosystem](/assets/programming/agent-build-log/agent-build-log-episode-029.png)

Until now, I had focused mostly on the Agent core, its tools, and the capabilities I was building myself.

But I realized that many things I planned to build already exist as extensions.

The first is MCP.

With an MCP adapter, Pi Agent can connect to existing MCP servers. Since my Agent already depends on tools like DKS, Jira, and XcodeBuildMCP, this means I do not need to rebuild connection handling, tool discovery, and invocation from scratch.

The second is the Approval / Permission System.

Once an Agent can run shell commands, modify files, or call MCP tools, I need rules for what can run automatically, what should ask first, and what should be blocked.

Pi extensions already provide solutions for this.

The third is Desktop GUI.

Projects like Pi GUI already provide sessions, workspaces, tool execution views, and other desktop interactions.

That made me rethink what I really need to build myself.

I am not just using Pi Agent anymore.

I am building on top of an ecosystem.

So instead of rewriting everything, I can reuse proven extensions and spend more time on what actually makes my Agent different:

Acceptance, Bug Blame, Spec Diff, and the capabilities built around my own workflows.

My mindset used to be:

If something is missing, build it.

Now it is:

Check the ecosystem first.

Then build only what truly belongs to this Agent.
