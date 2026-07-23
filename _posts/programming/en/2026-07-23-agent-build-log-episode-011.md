---
layout: single
title: "Agent Build Log — Episode 011"
date: 2026-07-23 21:12:11 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-011.png
summary: "I replaced the first memory-system plan with a smaller Markdown-and-SQLite design inspired by OpenClaw, keeping memory readable, editable, and easier to ship."
description: "I replaced the first memory-system plan with a smaller Markdown-and-SQLite design inspired by OpenClaw, keeping memory readable, editable, and easier to ship."
---

Today, I decided to undo the decision I made in Episode 010.

![Agent Build Log Episode 011: replacing embeddings with Markdown and SQLite](/assets/programming/agent-build-log/agent-build-log-episode-011.png)

Yesterday, I chose LanceDB with Qwen3 Embedding 0.6B for the first version of the memory system. The idea made sense until I looked more closely at the model size.

The embedding model alone is around 600 MB.

If I bundle that directly into the app, the whole app could easily end up over 1 GB. That feels like too much baggage for a first version, especially when I’m still trying to prove that the memory flow itself works.

So today, I stepped back and dropped embeddings for now.

The first version of the memory system will use Markdown files and SQLite, with the overall approach inspired by OpenClaw.

Markdown will hold the actual memory content. SQLite will help organize the index, timestamps, sources, sessions, and anything else needed for lookup.

Using July 23 as an example, the workspace will look something like this:

```text
workspace/
├── MEMORY.md
├── DREAMS.md
└── memory/
    ├── 2026-07-22.md
    ├── 2026-07-23.md
    └── 2026-07-23-session-name.md
```

MEMORY.md will hold stable, long-term memories that are likely to be useful again.

Daily events will first go into date-based files under memory/. If a session has a clear topic, it can also have its own named file.

DREAMS.md will be a place for unfinished ideas, patterns that still need observation, and thoughts worth revisiting later.

One thing I like about this setup is that I can open the files myself and see exactly what the Agent remembers. I can edit them, move them, and debug them without depending on an embedding model or a vector database.

SQLite won’t replace the Markdown files. It will sit beside them as a lightweight support layer for indexing and retrieval.

Yesterday’s plan was more technically ambitious. Today’s plan is smaller, easier to ship, and much more realistic for the first version.

Changing my mind after one day doesn’t feel like going backward. It feels like finally choosing the right size for the first step.
