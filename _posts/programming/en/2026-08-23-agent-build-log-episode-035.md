---
layout: single
title: "Agent Build Log — Episode 035"
date: 2026-08-23 00:31:29 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-035.png
summary: "I moved mobile acceptance features into optional plugins, reducing the App from 1.1 GB to around 300 MB."
description: "I moved mobile acceptance features into optional plugins, reducing the App from 1.1 GB to around 300 MB."
---

I’ve started preparing the version I actually want to ship.

![Agent Build Log Episode 035: moving mobile acceptance features into optional plugins](/assets/programming/agent-build-log/agent-build-log-episode-035.png)

This time, I need to seriously decide which features should be bundled with the App from the start, and which ones should be split out as plugins and downloaded only when needed.

When I first started building it, I bundled all the mobile acceptance features directly into the App.

That included Xcode Build MCP and Appium.

At one point, the whole App had grown to **1.1 GB**.

But those features are mainly for acceptance testing, and not everyone is going to need them.

So I started pulling the acceptance-related parts out and turning them into optional plugins.

After splitting them out, the App is now down to around **300 MB**.

If you need those features, you can just install the plugins when you need them.
