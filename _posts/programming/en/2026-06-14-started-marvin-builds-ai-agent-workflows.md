---
layout: single
title: "I Started Marvin Builds to Document Real AI-Agent Workflows"
date: 2026-06-14 17:00 +0800
category: programming
author: Marvin Lin
tags: [AI, AI Agent, Coding Agents, Workflow, YouTube, Marvin Builds]
lang: en
summary: "I started Marvin Builds, a YouTube channel about real AI-agent workflows: giving agents real tasks, watching them run, fixing mistakes, deploying, and verifying the result."
description: "I started Marvin Builds, a YouTube channel about real AI-agent workflows: giving agents real tasks, watching them run, fixing mistakes, deploying, and…"
image: /assets/programming/marvin-builds-ai-agent-workflows/marvin-builds-channel-banner.jpg
---

AI-agent demos are everywhere now. The part I care about is harder:

**Can an agent workflow be repeated, verified, and still controlled by a human builder?**

That is why I started a YouTube channel called **Marvin Builds**.

[![Marvin Builds YouTube channel banner](/assets/programming/marvin-builds-ai-agent-workflows/marvin-builds-channel-banner.jpg)](https://www.youtube.com/@MarvinBuildsAI){:target="_blank" rel="noopener"}

Marvin Builds is where I turn AI-agent experiments into visible build logs: real tasks, real mistakes, real verification, and workflows I can reuse instead of one-off prompts that only worked once.

## What I Want to Show

The channel is about what happens between the prompt and the result:

- how an agent reads requirements
- how it changes existing files
- where it makes wrong assumptions
- how I debug and review the work
- what I verify before trusting the output

That messy middle is usually the useful part. It shows whether an AI agent is only producing a demo, or whether it can fit into a workflow a builder can actually control.

## Examples

These are the kinds of episodes I want the channel to make easier to understand.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin: 1em 0;">
  <article style="border: 1px solid #e5e7eb; border-radius: 8px; padding: 12px;">
    <a href="https://youtu.be/CcRcaeP1mw8" target="_blank" rel="noopener"><img src="/assets/programming/marvin-builds-ai-agent-workflows/ai-agent-memory-workflow-cover.jpg" alt="YouTube cover for moving AI memory between agents" style="width: 100%;"></a>
    <h3 style="margin-top: 0.75em;">Move AI Memory Between Agents</h3>
    <p>A controlled context handoff from Codex to Claude: extract useful memory, review what should move forward, import it, then verify what the receiving agent learned.</p>
    <img src="/assets/programming/marvin-builds-ai-agent-workflows/ai-memory-workflow-keyframe.png" alt="Key frame showing the extract review import verify workflow" style="width: 100%;">
    <p><small>Key frame: the useful pattern is not blind sync. It is extract, review, import, verify.</small></p>
    <p><a href="https://youtu.be/CcRcaeP1mw8" target="_blank" rel="noopener">Watch the video</a></p>
  </article>
  <article style="border: 1px solid #e5e7eb; border-radius: 8px; padding: 12px;">
    <a href="https://youtu.be/WVxG1Ekkf_I" target="_blank" rel="noopener"><img src="/assets/programming/marvin-builds-ai-agent-workflows/codex-automations-baseball-research.png" alt="YouTube thumbnail for Codex Automations baseball research workflow" style="width: 100%;"></a>
    <h3 style="margin-top: 0.75em;">Codex Automations for Baseball Research</h3>
    <p>A recurring research workflow using baseball as the example: scan public sources, surface candidate signals, explain uncertainty, and leave the final call to human review.</p>
    <img src="/assets/programming/marvin-builds-ai-agent-workflows/baseball-research-workflow-keyframes.png" alt="Key frames from the Codex Automations baseball research workflow" style="width: 100%;">
    <p><small>Key frame: the agent prepares context and questions; the human still makes the judgment.</small></p>
    <p><a href="https://youtu.be/WVxG1Ekkf_I" target="_blank" rel="noopener">Watch the video</a></p>
  </article>
</div>

This blog will still be where I write notes and decisions. Marvin Builds is where I show the workflow in motion.

[Watch Marvin Builds on YouTube](https://www.youtube.com/@MarvinBuildsAI/videos){:target="_blank" rel="noopener"}
