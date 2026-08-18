---
layout: single
title: "Agent Build Log — Episode 033"
date: 2026-08-18 22:36:14 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-033.png
summary: "I tried to launch an Android Emulator with my Agent, but its Permission System blocked the first command."
description: "I tried to launch an Android Emulator with my Agent, but its Permission System blocked the first command."
---

Today, I went on a bit of a side quest.

![Agent Build Log Episode 033: Permission System blocking the Android Emulator task](/assets/programming/agent-build-log/agent-build-log-episode-033.png)

I didn’t make any progress on the main track. Instead, I decided to test something else I’d been wanting to try for a while.

I wanted to see if I could use the Agent I built to launch an Android Emulator.

The plan sounded pretty simple.

Have the Agent find the Android project.

Check the Emulator.

Then run the command to launch it.

It failed at the very first step.

The Agent knew exactly which command it needed to run next. But when it actually tried to execute it, the Permission System in my Agent blocked it.

That ended up revealing a very practical problem.

If the permission system is too restrictive, the Agent can know exactly what it needs to do and still end up unable to do anything.
