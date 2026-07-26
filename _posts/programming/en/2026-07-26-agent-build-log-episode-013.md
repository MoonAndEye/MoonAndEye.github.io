---
layout: single
title: "Agent Build Log — Episode 013"
date: 2026-07-26 23:35:40 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-013.png
summary: "I compared Sol, Terra, and Luna at medium and xhigh effort. For scoped DKS lookups, Terra xhigh was both fast and reliable; Sol remains the choice when strict protocol compliance matters most."
description: "I compared Sol, Terra, and Luna at medium and xhigh effort. For scoped DKS lookups, Terra xhigh was both fast and reliable; Sol remains the choice when strict protocol compliance matters most."
---

Today, I added GPT-5.6 Sol to the model comparison.

![Agent Build Log Episode 013: model routing across Sol, Terra, and Luna](/assets/programming/agent-build-log/agent-build-log-episode-013.png)

Previously, I had only tested Terra and Luna.

In Episode 012, Terra looked like a strong default because it was faster. But I still had one unanswered question:

Was it actually finding a better path, or was it simply skipping steps it should have completed?

So this time, I used the same DKS evals to compare Sol, Terra, and Luna at both medium and xhigh effort.

What changed my view was not just Terra’s speed. It was how much better Terra performed at xhigh effort.

At medium effort, Terra was fast, but it failed to call the required DKS tool six times and officially passed 20 out of 29 cases.

At xhigh effort, it missed only one required DKS call and passed 26 out of 29.

That result connects directly to the question I had in Episode 012.

Terra’s speed may not come only from skipping steps. With more effort, it fixed most of the protocol-compliance problem while keeping its speed advantage.

At xhigh effort, Terra and Sol both passed 26 out of 29 cases.

But Sol averaged about 29.1 seconds per task, while Terra averaged about 21.2 seconds.

For this kind of clearly scoped DKS lookup task, Terra xhigh no longer looks like “the faster option with a quality trade-off.” It was both fast enough and reliable enough.

Luna was not necessarily the faster model either.

In this test, Terra finished faster than Luna at both medium and xhigh effort. So speed alone is no longer a reason for me to choose Luna over Terra.

Sol’s advantage showed up somewhere else.

At both effort levels, Sol completed every required DKS protocol step.

So when process compliance matters more than speed, Sol is still the model I would trust first.

![Benchmark overview of Sol, Terra, and Luna at medium and xhigh effort](/assets/programming/agent-build-log/agent-build-log-episode-013-benchmark-report.png)

For tasks with a clear scope, a known tool, and a straightforward way to verify the result, I would currently start with Terra xhigh.

For tasks where strict process compliance matters more, or where I am willing to spend more time for stability, I would choose Sol.

Luna still has its own use cases, but in this round, speed was not its advantage over Terra.

One caveat: the six profiles were run in a fixed order, not in a fully balanced experiment.

So I am treating these results as a routing signal, not a final conclusion.

This comparison did not give me one model for everything.

It gave me a better model-routing rule.
