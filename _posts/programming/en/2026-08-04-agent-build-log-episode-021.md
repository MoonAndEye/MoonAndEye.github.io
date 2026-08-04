---
layout: single
title: "Agent Build Log — Episode 021"
date: 2026-08-04 22:55:31 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-021.png
summary: "I started implementing specification acceptance testing across branch switching, builds, simulator operation, screenshots, reporting, and delivery."
description: "I started implementing specification acceptance testing across branch switching, builds, simulator operation, screenshots, reporting, and delivery."
---

Today, I started implementing the Agent’s first capability: specification acceptance testing.

![Agent Build Log Episode 021: implementing the complete specification acceptance path](/assets/programming/agent-build-log/agent-build-log-episode-021.png)

By specification acceptance testing, I do not mean running unit tests or UI tests and then turning the results into a report.

The starting point can be a Jira ticket or a specification or set of acceptance criteria written in natural language.

But the endpoint is not for the Agent to simply inspect the code or determine whether the tests passed.

The Agent needs to operate the repo directly, switch to the target branch, prepare the required development environment, and build the App for an iOS Simulator or Android Emulator.

Then, the Agent will operate the App directly.

Based on the Jira ticket or acceptance specification, it will navigate to the specified page, perform the required actions, and confirm whether the screen and behavior match expectations.

Whether it is validating a bug or a feature, the Agent must confirm that the issue has actually been fixed or that the feature has been implemented correctly.

Key screens during the acceptance process will be captured as evidence.

Once complete, the Agent will organize the acceptance steps, execution results, and screenshots into HTML and PDF reports, then send them to the specified channel through a chat bot.

Once I had this idea, I asked the Agent to start building the first version by itself.

But the first attempt failed.

The Agent has not successfully connected to CoreSimulator yet.

The iOS Simulator did not start correctly, the acceptance workflow was never actually executed, and the final report was empty.

So the first version of specification acceptance testing has not succeeded yet.

But at least now, I have confirmed the complete path that this capability needs to connect:

Start with a Jira ticket or a natural-language specification.

Switch branches, build the App, launch the simulator, operate the App, capture screenshots, generate the report, and finally send the results to the channel.

Today, I let the Agent attempt specification acceptance testing on its own for the first time.

It failed, but the episode will continue.
