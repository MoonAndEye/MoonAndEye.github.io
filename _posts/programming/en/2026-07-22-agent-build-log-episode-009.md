---
layout: single
title: "Agent Build Log — Episode 009"
date: 2026-07-22 00:35:00 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-009.png
summary: "I added repository aliases to DKS MCP so natural names, singular and plural forms, and everyday queries resolve to the correct repo and link."
description: "I added repository aliases to DKS MCP so natural names, singular and plural forms, and everyday queries resolve to the correct repo and link."
---

Today, I went back to the DKS (Developer Knowledge Service) MCP and started working on repository aliases.

![Agent Build Log Episode 009: repository aliases in DKS MCP](/assets/programming/agent-build-log/agent-build-log-episode-009.png)

In real conversations, people usually don’t ask for an exact repo name. They ask things like, “Where’s the login module?” I want the Agent to understand what they mean and return the right repository name and link.

That’s when I ran into a very normal language problem.

In the language I use, nouns generally don’t have plural forms, and verbs don’t change the way they do in some other languages. So the words I type don’t always match the official repository name exactly.

For example, the repo might be called trees, but I search for tree. Or it might be node instead of nodes. To a person, the meaning is obvious. To the current DKS search, they are completely different words, so it simply returns no results.

Once I noticed this, I had the Agent build alias mappings for the repositories. The aliases now cover common names, singular and plural forms, and other ways people might naturally refer to the same repo. I also added tests to make sure each alias resolves to the right repository.

I don’t want anyone using DKS to memorize the exact name of every repo.

They should be able to ask in their own words. The Agent should handle the difference.
