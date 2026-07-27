---
layout: single
title: "Agent Build Log — Episode 014"
date: 2026-07-27 23:18:03 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-014.png
summary: "DKS now uses the GitLab API and Jira for lookup, so it no longer needs a mirror of every department repository."
description: "DKS now uses the GitLab API and Jira for lookup, so it no longer needs a mirror of every department repository."
---

Today, I changed the design of the DKS (Developer Knowledge Service) MCP.

![Agent Build Log Episode 014: DKS now uses the GitLab API and Jira](/assets/programming/agent-build-log/agent-build-log-episode-014.png)

At first, I planned to mirror every Git repo in my department to a Mac mini. That would let the DKS MCP look up MRs and commits, trace why a feature was built, and see how it was implemented.

But I ran into a practical limit pretty quickly: the Mac mini I have available does not have enough disk space for a mirror of every repo in the department.

So I changed how DKS handles Git data. It now uses the GitLab API.

I am keeping Jira search. When a Jira record matches a commit, the Agent can still connect the reason a feature was built to the actual code change.

I moved DKS's data sources to the GitLab API and Jira. That removes the need to fit a mirror of every repo in the department on the Mac mini. I will not build repo mirrors for DKS anymore.
