---
layout: single
title: "Agent Build Log — Episode 024"
date: 2026-08-08 21:32:39 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-024.png
summary: "Why model response latency does not predict how quickly an Agent will complete an entire task."
description: "Why model response latency does not predict how quickly an Agent will complete an entire task."
---

Today, I got a result that was completely opposite to what I expected.

![Agent Build Log Episode 024: comparing Agent task completion time across Sol, Terra, and Luna](/assets/programming/agent-build-log/agent-build-log-episode-024.png)

If I only look at the LLM itself, I would normally assume:

Models with more parameters tend to respond more slowly.

Models with fewer parameters tend to respond more quickly.

So if the task were simply answering one question, I would expect the speed order to be:

Luna fastest, Terra in the middle, and Sol slowest.

I had the same assumption for Agent tasks.

I expected the total task completion time to follow the same order: Luna first, then Terra, and Sol last.

But when I ran the same task today, the result was completely different.

This task was mainly used to tune tool calls and the final output.

All three models used the same Agent, the same tools, and performed the same task.

The results were roughly:

Sol: around 5 minutes.

Terra: around 8 minutes.

Luna: around 14 minutes.

Luna took almost three times as long as Sol to complete the task.

More importantly, Luna did not complete the task correctly.

Sol and Terra did.

That made me rethink something:

The response speed of the model itself does not directly tell you how fast an Agent will complete an entire task.

The total Agent execution time depends on more than how fast each inference is.

It also depends on how the model plans, how many tool calls it makes, whether it repeatedly checks the same things, whether it takes wrong turns, and whether it can finish the task in fewer steps.

A model with faster individual responses can still take longer overall if it needs more rounds of tool calls or follows more unnecessary paths.

This result also makes model selection more interesting.

If I only care about cost, I can choose Terra.

It completes the task correctly and is cheaper than Sol.

But it takes longer.

Sol completed this task the fastest and also produced the correct result, but it costs a bit more.

I used to think about model selection like this:

Bigger model = slower and more expensive.

Smaller model = faster and cheaper.

But with Agents, the most important thing may not be the speed of a single inference.

It may be:

How many steps does this model need to actually finish the task?

For the custom Agent I am building, this is an important discovery.

When choosing a model from now on, I cannot look only at token price or response latency.

I also need to look at the completion time of the entire task.
