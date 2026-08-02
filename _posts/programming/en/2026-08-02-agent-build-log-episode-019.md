---
layout: single
title: "Agent Build Log — Episode 019"
date: 2026-08-02 23:00:53 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-019.png
summary: "Pi Agent does not support ultra effort, so the Agent will display and validate effort values based on Pi’s declared capabilities."
description: "Pi Agent does not support ultra effort, so the Agent will display and validate effort values based on Pi’s declared capabilities."
---

Today, I discovered that Pi Agent does not support the ultra effort level.

![Agent Build Log Episode 019: limiting effort options to Pi Agent capabilities](/assets/programming/agent-build-log/agent-build-log-episode-019.png)

The currently available values are:

off, minimal, low, medium, high, xhigh, and max

If ultra is passed to the current Pi runtime, it will not be treated as a setting higher than max.

Instead, it will be converted to off.

This means users may think they have selected the highest reasoning effort, while they have actually turned reasoning off.

So effort support cannot be determined by the model name alone. A model belonging to the GPT-5.6 family does not automatically mean that it supports ultra.

From now on, the Agent will decide which effort levels to display based on the capabilities Pi actually declares for the selected model.

If a model does not support ultra, the UI will not display it.

The runtime will also validate the effort value to prevent the CLI, configuration files, or session restore from passing unsupported values.

For now, models such as Sol and Terra will use max, the highest effort level currently supported by Pi, as their upper limit.

The Agent will only enable ultra for a model when Pi explicitly reports that the model supports it.

Today, I learned that even though the agent I use, Codex, has an Ultra effort option, that does not mean ultra will work correctly through my Pi Agent integration. If that effort level does not exist in Pi Agent, it may even fall back to no reasoning.
