---
layout: single
title: "Agent Build Log — Episode 020"
date: 2026-08-03 22:59:14 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-020.png
summary: "I started building the Agent’s first acceptance capabilities: creating an acceptance brief, then executing it and producing a report."
description: "I started building the Agent’s first acceptance capabilities: creating an acceptance brief, then executing it and producing a report."
---

Today, I started implementing the Agent’s own capabilities.

![Agent Build Log Episode 020: building acceptance brief and reporting tools](/assets/programming/agent-build-log/agent-build-log-episode-020.png)

For the first version, I designed two tools.

The first tool creates an acceptance brief.

Based on a Jira ticket, it organizes how the item should be verified.

For example, it identifies which page the tester should open, which actions they should perform, and what results they need to see to prove that the requirement has been completed or the bug has been fixed.

This tool only defines the acceptance criteria and verification path. It does not perform the actual acceptance testing.

The second tool performs the acceptance testing and generates an acceptance report.

The Agent follows the path defined in the acceptance brief, captures screenshots at key steps, and organizes the results and images into the final report.

These two tools handle different stages of the process.

The first tool turns a Jira ticket into an actionable acceptance plan.

The second tool follows that plan, completes the verification, and preserves evidence that can be reviewed and delivered.

This is the first set of acceptance capabilities I have started building for the Agent.
