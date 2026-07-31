---
layout: single
title: "Agent Build Log — Episode 017"
date: 2026-07-31 22:56:21 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-017.png
summary: "I started implementing an Agent memory system that uses SQLite for indexing and Markdown for date- and session-based memory content."
description: "I started implementing an Agent memory system that uses SQLite for indexing and Markdown for date- and session-based memory content."
---

Today, I officially started implementing the Agent’s memory system.

![Agent Build Log Episode 017: implementing Agent memory with SQLite and Markdown](/assets/programming/agent-build-log/agent-build-log-episode-017.png)

The first version will not begin with a vector database or a complex RAG architecture.

I plan to use SQLite and Markdown to build a memory system that is simple, transparent, and easy to inspect directly.

This design is mainly inspired by OpenClaw’s approach to memory.

For historical memory, the system will organize records by date.

Each day will have a directory named in the yyyy-mm-dd format to store what happened that day.

But within a single day, the Agent may have many different conversations and tasks.

So I do not plan to put everything into one Markdown file.

Each session within the same day can have its own separate Markdown file.

This preserves the context of each session and prevents different tasks from being mixed together.

Markdown is responsible for storing memory content that people can read directly.

SQLite is responsible for storing structured data, such as the session time, title, file location, status, and the relationships between different memories.

When the Agent needs to find a past memory, it can first use SQLite to locate potentially relevant dates and sessions, then read the corresponding Markdown files.

Today, I am starting with the simplest structure:

SQLite handles the index.

Markdown remembers what happened.

And every memory begins with a date and a session.
