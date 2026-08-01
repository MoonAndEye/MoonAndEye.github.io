---
layout: single
title: "Agent Build Log — Episode 018"
date: 2026-08-01 23:47:47 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-018.png
summary: "I changed the Alpha target audience from developers to PM and QA teams responsible for acceptance testing."
description: "I changed the Alpha target audience from developers to PM and QA teams responsible for acceptance testing."
---

Today, I changed the target users for the Agent.

![Agent Build Log Episode 018: shifting the Agent toward PM and QA acceptance testing](/assets/programming/agent-build-log/agent-build-log-episode-018.png)

At first, I wanted to build it for iOS and Android developers.

In addition to basic coding agent capabilities, I also planned to add various custom tools and specialize it around the skills I use at work.

But today, I changed the Agent’s target audience from “developers” to “people responsible for acceptance testing.”

In my current work environment, the people responsible for acceptance testing are usually PMs or QA team members.

They need to confirm whether a requirement has actually been completed, whether a bug has truly been fixed, and whether the behavior of the current App build matches expectations.

But during this process, they often get stuck on two things:

How to build the latest code.

And how to verify that the issue has actually been fixed in this version of the App.

Recently, PM and QA colleagues also told me that they wanted to shorten the time between receiving a build and completing acceptance testing.

That made me rethink who the first version of the Agent should really serve.

If I continued targeting developers, my Agent would compete directly with products like Codex and the Claude App.

Those tools are already specialized for software development.

Whether it is understanding a codebase, modifying code, running commands, or completing development tasks, it would be difficult for my first version to compete directly with such mature products.

But acceptance testing is a different problem.

Even if PMs or QA team members have access to Codex or the Claude App, they usually still need a developer to help set up the repository, build environment, credentials, tools, and testing workflow.

The tools already exist, but the barrier to using them has not really disappeared.

That made me realize that my Agent does not need to become another, better coding agent first.

Instead, it can wrap the environment and workflows already prepared by developers, so that people responsible for acceptance testing can use them directly.

They do not need to understand how the entire project is built, and they do not need to remember every command.

They only need to tell the Agent:

> “Build the latest version for me.”

> “Help me confirm whether this bug has been fixed.”

> “Verify this feature according to the conditions in the ticket.”

The Agent can then handle the build, installation, testing, and verification steps behind the scenes.

So starting today, the goal of the Alpha stage has officially changed.

The first version of the Agent will no longer focus mainly on helping developers build Apps.

It will first focus on helping PM and QA teams perform acceptance testing.

I found a clearer problem, and one that needs to be solved more urgently right now.
