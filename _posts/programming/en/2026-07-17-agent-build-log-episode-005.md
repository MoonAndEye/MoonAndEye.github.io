---
layout: single
title: "Agent Build Log — Episode 005"
date: 2026-07-17 22:43:15 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-005.png
summary: "I added Feedback to the CLI, Browser, and Desktop App so problems and improvement ideas can be captured immediately through one shared API."
description: "I added Feedback to the CLI, Browser, and Desktop App so problems and improvement ideas can be captured immediately through one shared API."
---

Today, I added a feature that looks small but will probably become very useful later: Feedback.

![Agent Build Log Episode 005: Feedback across the CLI, Browser, and Desktop App](/assets/programming/agent-build-log/agent-build-log-episode-005.png)

I added it to the CLI, Browser, and Desktop App. Whether it’s for other users or just for me while testing, I can now record a problem the moment I notice it—something feels wrong, a bug appears, or I suddenly think of something that could be improved.

During development, I often tell myself, “I’ll fix this later.” A few days pass, and I can barely remember what happened or why it felt wrong. Now I can capture the issue first, then go back and sort through the feedback when I’m ready to fix bugs or plan the next round of work.

I kept the implementation simple. I picked a database and created a basic API endpoint, so all three interfaces can send feedback to the same place.

If I’m going to eat my own dog food, I also need to keep a record of where that dog food tastes bad and what needs to be improved.
