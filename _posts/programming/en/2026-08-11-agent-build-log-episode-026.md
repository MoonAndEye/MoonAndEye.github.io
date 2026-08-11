---
layout: single
title: "Agent Build Log — Episode 026"
date: 2026-08-11 21:29:09 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-026.png
summary: "Building Bug Blame to trace a Jira bug through related code, commits, and the developers most relevant to the investigation."
description: "Building Bug Blame to trace a Jira bug through related code, commits, and the developers most relevant to the investigation."
---

Today, I built another “Signature Ability” for the Agent.

![Agent Build Log Episode 026: Bug Blame traces Jira bugs through code, commits, and developers](/assets/programming/agent-build-log/agent-build-log-episode-026.png)

This one is called Bug Blame.

The name comes from git blame.

It starts with a Jira ticket.

The Agent first understands the bug described in the ticket, along with the features and areas of code that may be affected.

Then, using the repo’s commit history and git blame, it traces backward to find the changes most relevant to the issue.

Finally, it maps those commits to the actual developers.

So the flow looks roughly like this:

Jira ticket → related code → git blame → commit → developer

I call it Bug Blame because git blame is one of the key signals behind the capability.

But the goal is not simply to answer, “Who wrote this bug?”

git blame can tell me who last modified a particular line of code, but that does not prove that person caused the bug.

So I want the final result to have clear levels of confidence.

If the connection between a commit and the bug is strong, the Agent can point to the most relevant developer.

If multiple developers have modified the feature over time, it should list the potentially related developers and the commits associated with each of them.

If there is not enough evidence, it should simply say, “Unable to determine.”

I do not want the Agent to force an answer just for the sake of having one. I want it to reflect the real situation.

What this Signature Ability is really trying to solve is this: when a Jira bug ticket appears, I want to quickly find out:

How this part of the feature was changed over time.

Which commits are most likely related to the issue.

And which developers should be involved in the next investigation.

So even though it is called Bug Blame,

what I really want is a fast way to find the development history and the people most relevant to a bug.
