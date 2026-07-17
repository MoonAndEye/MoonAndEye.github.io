---
layout: single
title: "Agent Build Log — Episode 004"
date: 2026-07-16 22:04:13 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-004.png
summary: "Day one of Golem Desktop uses Electron, React, and Electron Vite, with Agent execution isolated in an Electron Utility Process."
description: "Day one of Golem Desktop uses Electron, React, and Electron Vite, with Agent execution isolated in an Electron Utility Process."
---

Today was the first day of building Golem Desktop.

![Agent Build Log Episode 004: day one of Golem Desktop](/assets/programming/agent-build-log/agent-build-log-episode-004.png)

In the previous episodes, I hadn’t touched the agent app itself. Most of the work was focused on DKS MCP, Pi Agent, and figuring out how the models and tools should connect. Today, I finally started bringing those pieces into an actual desktop app.

The desktop app uses Electron with a React frontend and is built with Electron Vite. For now, I’m using the Codex App as a UI reference. The goal on day one was to get the basic interactions and overall structure in place, rather than trying to design a completely different interface from the start.

But I don’t want it to be just a chat page wrapped in Electron.

The UI and the part that actually runs the Agent are separated. The interface handles display and interaction, while the Agent runs in its own Electron Utility Process. Model calls, tool execution, and permission checks will all be handled there.

The default model currently runs through OpenAI Codex OAuth using gpt-5.6-terra. I’ll also gradually bring the DKS MCP into the desktop app, so it can search MRs, commits, repositories, and Jira data.

I’ve also started adding confirmation before tool execution, along with sandbox permission controls.

Today wasn’t really about how many features I finished. It was about deciding how Golem Desktop should begin.

This is only day one of the desktop app. Both the UI and the architecture are still at a very early stage, but at least the first step is now in place.
