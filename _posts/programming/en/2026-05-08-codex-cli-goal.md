---
layout: single
title: "Codex CLI's /goal: Let an AI Agent Remember a Long-Term Goal"
date: 2026-05-08 11:01 +0800
category: programming
author: Marvin Lin
tags: [Codex CLI, OpenAI, AI Agent, AI Agent Coding]
lang: en
summary: "/goal is a new experimental feature in Codex CLI. It turns a long-running task into a goal that can be tracked, paused, and resumed, but it currently requires a newer CLI version and a manually enabled feature flag."
description: "/goal is a new experimental feature in Codex CLI. It turns a long-running task into a goal that can be tracked, paused, and resumed, but it currently…"
---

Codex CLI recently added a new feature that I think is worth paying attention to: `/goal`.

I understand it as a way to "let Codex remember a long-term goal." In the past, when working with an AI agent in the terminal, most collaboration happened one conversation turn at a time. You gave it a task, it did one part. You added more context, it moved to the next part.

That works well for short tasks.

But when a task becomes longer, such as organizing a repo, doing a cross-file refactor, tracking down a chain of test failures, or asking an agent to keep moving toward a product goal, relying only on each prompt can easily make the work drift.

`/goal` is trying to solve that problem.

## /goal Is Not Enabled by Default

This is the first thing to mention, because it is easy to miss.

Even if you have already updated Codex CLI, it does not mean you will see `/goal` as soon as you open Codex. Right now, `/goal` is still an experimental feature, and it is disabled by default.

At the time I am writing this, the latest npm version is `0.129.0`. In this version, `codex features list` shows:

```bash
goals    experimental    false
```

That means the feature exists, but it is not enabled.

To enable it, run:

```bash
codex features enable goals
```

After that, `~/.codex/config.toml` will include:

```toml
[features]
goals = true
```

Then restart Codex CLI, and you can use `/goal`.

If you only want to try it temporarily, you can also use:

```bash
codex --enable goals
```

You do not have to run all of this manually. You can ask an AI agent such as Codex App, Claude App, or Claude Code to do it for you. You only need to give it one prompt.

```text
Enable the goals feature in codex cli so I can use /goal.
```

## The Version Needs to Be 0.128.0 or Later

Another thing to watch is the version.

`/goal` is not available in every Codex CLI version. OpenAI added the persisted `/goal` workflow in the [Codex CLI 0.128.0 release note](https://github.com/openai/codex/releases/tag/rust-v0.128.0), including TUI controls for create, pause, resume, and clear. In the [0.129.0 release note](https://github.com/openai/codex/releases/tag/rust-v0.129.0), goals were marked experimental, with improvements to discoverability, keeping goals paused after resume, validation, and duration display.

## In the Codex App, Open the Terminal Area and Use Codex CLI

In the Codex app, you can use the terminal directly. The shortcut is `Cmd + J`, which opens the terminal area. From there, enter the `codex` command, and you can move into the Codex CLI environment.
