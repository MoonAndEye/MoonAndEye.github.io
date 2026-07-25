---
layout: single
title: "Agent Build Log — Episode 012"
date: 2026-07-26 00:18:19 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-012.png
summary: "I compared Terra and Luna with counterbalanced evals: they reached the same accuracy, while Terra ran slightly faster with fewer tool calls but missed the required DKS protocol more often."
description: "I compared Terra and Luna with counterbalanced evals: they reached the same accuracy, while Terra ran slightly faster with fewer tool calls but missed the required DKS protocol more often."
---

Today, I thought I had found a more efficient default model.

![Agent Build Log Episode 012: comparing Terra and Luna](/assets/programming/agent-build-log/agent-build-log-episode-012.png)

With the same evals and the same effort level, Terra finished faster than Luna and made fewer tool calls.

My first thought was that Terra might be taking a shorter path.

Luna might do something like this:

Look up A, inspect the result, look up B, go back and confirm A, open another file, and then answer.

Terra might first decide that it needs A, B, and C, query them together, and then answer.

But that is only one possible explanation. I still don’t have enough evidence to say that Terra actually took a shorter path.

I was also worried that the execution order might affect the result.

If Terra always ran second, could it be benefiting from file cache left behind by the previous run?

So I changed the test to use a counterbalanced setup. Each case ran once as Terra → Luna, and once as Luna → Terra.

The results still showed Terra finishing slightly faster overall, but I can’t conclude that Terra is inherently faster than Luna.

The execution-order results also did not show that the second model consistently benefited from cache.

![Counterbalanced Terra versus Luna confirmatory study results](/assets/programming/agent-build-log/agent-build-log-episode-012-luna-vs-terra.png)

What really made me rethink the result was the DKS protocol data.

Terra made N tool calls.

Luna made roughly N + 10 tool calls.

That means Terra making fewer tool calls may not simply mean it was more efficient.

It may have found a shorter path, or it may have skipped some steps it was supposed to complete. The current data still can’t fully separate those two possibilities.

What makes this more interesting is that both models ended with the same accuracy, but they failed in different ways.

Terra was more likely to miss the required DKS protocol. Luna almost always called DKS, but was more likely to get the final answer wrong.

So this test was not simply about which model was better. The two models reached the same score in very different ways.

For now, Terra still looks like it could be a reasonable default choice.

It seems to move faster, but I still don’t know whether it really found a shortcut or simply skipped a few steps.

Before choosing the default model, I need to make sure that “more efficient” does not actually mean “more likely to skip the rules.”
