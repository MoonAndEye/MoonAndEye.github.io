---
layout: single
title: "Agent Build Log — Episode 023"
date: 2026-08-06 23:36:26 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-023.png
summary: "Adding Signature Abilities to the Agent GUI, starting with spec-diff for human-readable document change reports."
description: "Adding Signature Abilities to the Agent GUI, starting with spec-diff for human-readable document change reports."
---

Today, I added a new section to the Agent’s GUI.

![Agent Build Log Episode 023: Signature Abilities and spec-diff in the Agent GUI](/assets/programming/agent-build-log/agent-build-log-episode-023.png)

I call it “Signature Abilities.”

This section will contain capabilities that are unique to this custom Agent.

The concept is similar to skills, but I do not want these capabilities to remain hidden behind the Agent.

Each Signature Ability will have its own page, giving non-developers a GUI where they can enter data, configure parameters, and directly view the final result.

The first Signature Ability I built is called spec-diff.

The workflow is simple.

Enter a previous spec, then enter a new spec.

The Agent analyzes the differences between the two documents and produces a report in a fixed format, showing which content was changed, added, or removed.

It does more than compare the two documents line by line.

The Agent also needs to understand what the content means, identify how the specification itself has changed, and organize the results into a report that is easy for people to read.

At first, I only wanted to solve the problem of spec changes during development.

When a specification is updated, developers, PMs, and QA teams can quickly understand what changed and which areas may need to be reviewed again.

But after building the first version, I realized that this capability could be useful for more than comparing specs.

As long as the input contains two different versions of the same kind of information, it can analyze the changes between them.

It can compare contracts and summarize which clauses were changed, added, or removed.

It can compare two architecture designs and identify changes in components, responsibilities, or data flow.

It can even compare stock trading rules and summarize differences in entries, exits, or risk controls between the old and new versions.

This direction surprised me.

I originally thought I was only building a spec-diff tool.

But during development, I accidentally created a tool that can compare different versions of documents and turn the changes into a human-readable report.

Sometimes, the feature with the most potential is not the one that was originally planned.

It may be a byproduct that only begins to emerge after the first version is complete.
