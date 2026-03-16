---
layout: single
title: If You Don’t Give the AI Direction, It Can’t Drive You to the Destination
date: 2026-03-16 08:00 +0800
category: programming
author: Marvin Lin
tags: [AI, AI Agent, Product, Mobile, Workflow]
lang: en
summary: A real-world Figma Make trap: I gave the agent a demo link, so it treated the demo as the spec. The real fix is defining behavior first—your launch state machine.
---

## Writer

If you don’t give the AI direction, it can’t drive you to the destination.

I hit a surprisingly common trap while building an app demo with Figma Make.

My instruction to the agent was simple:

> Please implement based on what’s in my Figma Make share link.

Sounds reasonable.

But here’s the problem: **a share link is usually a demo, not a behavioral spec**.

### What I got wrong

To move fast, I made the *starting screen* the main tab bar in my Figma Make project.

The agent did exactly what it saw:
- it treated the demo as the requirement
- it implemented “launch → main tab”

For a demo, that can be fine.

For a real product, it’s usually wrong.

### A real mobile app launch is a state machine

On mobile, a standard launch flow is not “whatever the first UI looks like.”

Typically, after app launch you enter a dedicated launch activity/view controller and run a state machine, for example:

1) Force update / soft update / OK

2) Only if OK → check whether we can auto-login
- if yes → go to main tab
- if not → go to login

Those conditions and branches are the *direction*.

The UI is just the outcome.

### Why I thought the agent was “overwriting” my work

At first, I kept thinking the agent wasn’t following my instructions and kept changing my implementation.

Then I checked the React site Figma Make actually built.

The flow was already “locked in” by my demo.

In other words:
- the demo defined the world I gave the agent
- the agent simply inferred behavior from visible states

The agent didn’t fail.

My direction did.

### Takeaway: define behavior before UI

If you want AI to build the right UI, define behavior first:
- entry states
- branching conditions
- success criteria

UI is the outcome.

The flow is the direction.

## Editor

Strengths:
- Strong hook and clear single point.
- Concrete details (Figma Make, React build verification, update/auth branches) make it credible.

Edits for the final:
- Move “demo ≠ spec” earlier so the main contrast shows up faster.
- End with a tight checklist readers can reuse.

## Final

If you don’t give the AI direction, it can’t drive you to the destination.

I hit a common trap while building an app demo with Figma Make.

My instruction to the agent was:

> Please implement based on what’s in my Figma Make share link.

Sounds reasonable—until you realize **the link is a demo, not a behavioral spec**.

To move fast, I made the starting screen the main tab bar.

So the agent did exactly what it saw:
- it treated the demo as the requirement
- it implemented “launch → main tab”

But real mobile app launch is a state machine.

Typically, after app launch you enter a dedicated launch activity/view controller and run checks like:

1) Force update / soft update / OK

2) Only if OK → check whether we can auto-login
- if yes → main tab
- if not → login

At first, I thought the agent was ignoring instructions and “overwriting” my work.

Then I checked the React site Figma Make actually built—the flow was already locked in by my demo.

The agent didn’t fail.

My direction did.

Takeaway: **define behavior before UI.**

A minimal checklist:
- entry states
- branching conditions
- success criteria

UI is the outcome.

The flow is the direction.
