---
layout: single
title: Starting a Series of Compact Source Prompts
date: 2026-04-06 09:50 +0800
category: programming
author: Marvin Lin
tags: [AI, Prompt Engineering, Knowledge Base, Gumroad, Claude]
lang: en
summary: I’m starting a small product line of compact, one-shot prompt artifacts. The first is LLM Knowledge Base Source Prompt, a source spec for generating a markdown-first internal wiki and LLM-friendly knowledge base starter.
---

I’ve been thinking about a product format that sits somewhere between a gist, a spec, and a starter kit.

Not a full SaaS.
Not a long course.
Not a bloated template bundle.

Just a **small, focused prompt artifact** that does one job clearly.

That is the format I want to explore more deliberately.

So I’m starting a small series of **compact source prompts**: one-shot prompt products designed around specific workflows, with each one acting as a reusable technical artifact rather than a piece of content dressed up as a product.

The first one is:

**LLM Knowledge Base Source Prompt**  
<https://marvinsight.gumroad.com/l/llm-knowledge-base-source-prompt>

## The idea behind this product line

There are already plenty of large products for AI builders:
- full frameworks
- heavy starter kits
- video courses
- giant prompt packs

Those can be useful.

But I think there is also room for something smaller and sharper: artifacts that are compact enough to study in one sitting, specific enough to be immediately useful, and structured enough to be reused or adapted in real work.

That is the bet behind this series.

I’m interested in making **tiny, high-leverage prompt products** that behave more like source artifacts than marketing assets.

## Why start with a knowledge base prompt

A lot of AI work eventually runs into the same problem:

How do you turn raw notes, scattered decisions, working files, and project context into something durable?

Not just searchable.

Not just pretty.

Actually durable.

For me, that usually means:
- markdown-first structure
- Git-friendly organization
- content that humans can maintain
- content that agents can also read and extend
- a system that does not collapse into a thin docs UI with weak information architecture

That is why the first product in this series is centered on a knowledge base.

## Karpathy, X, and the gist-like artifact

A key part of the inspiration came from **Andrej Karpathy**, and I want to be explicit about that.

This product direction was not something I came up with in isolation. It was shaped in part by seeing Karpathy frame markdown, text files, and compact source artifacts as serious interfaces for LLM workflows.

In particular, these references mattered:
- Karpathy’s gist: <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- Karpathy’s X post: <https://x.com/karpathy/status/2039805659525644595?ref=anduril.tw>

What I found compelling there was not just the specific content, but the format itself: a compact, portable artifact that carries a lot of implementation direction without pretending to be an entire product by itself.

That framing mattered to me.

I did not want to sell “AI vibes.”

I wanted to package a **source specification** that someone could actually use, inspect, adapt, and build from.

## What this first prompt is for

**LLM Knowledge Base Source Prompt** is designed to generate a markdown-first internal wiki and LLM-friendly knowledge base starter.

The target output includes:
- **Next.js App Router**
- **Fumadocs**
- **MDX-based content**
- **static export compatibility**
- a **dashboard-style homepage**
- structured content for **Tasks / Repos / Topics / Decisions / People / Daily**
- **English-first** content with **Traditional Chinese** as an alternate locale

The point is not to create a generic docs shell.

The point is to give builders a stronger starting structure for long-term knowledge capture.

In other words, this is less about “generate me a docs site” and more about:

> generate me a usable knowledge system from a compact source artifact.

## What you are buying

You are buying the **prompt itself**.

More specifically, you are buying a focused source prompt that you can:
- paste into Claude
- adapt for other coding models
- fork into your own internal wiki workflow
- use as a starting point for agent memory or team knowledge infrastructure

So the product is not the finished website.

It is the **source-level artifact** that helps produce one.

## Why this format matters to me

I like products that are small enough to understand.

A compact prompt artifact can still contain:
- product thinking
- information architecture
- implementation direction
- editorial judgment about what belongs in the system

That makes it a surprisingly good product form.

It is easy to ship, easy to revise, easy to remix, and easy for other builders to evaluate quickly.

That is exactly why I think this format is worth exploring as a series, not just as a one-off experiment.

## The first entry in a broader series

This knowledge base prompt is the first entry.

It will not be the last.

My goal is to build a line of one-shot prompt products where each one has:
- a clear use case
- a concrete output shape
- a compact but serious source artifact behind it

This first release happens to be about markdown-first knowledge systems.

Future ones may target other focused workflows with the same philosophy.

## Product link

If this specific workflow is relevant to you, you can check it out here:

<https://marvinsight.gumroad.com/l/llm-knowledge-base-source-prompt>

I’m less interested in making prompt products that feel disposable.

I’m more interested in making small technical artifacts that people can actually build with.

This is the first one.