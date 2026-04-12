---
layout: single
title: "The First Step to Better Vibe Coding: Keep Frontend & Backend in One Folder"
date: 2026-04-12 08:00 +0800
category: programming
author: Marvin Lin
tags: [AI, Vibe Coding, Mono Repo, Frontend, Backend, Workflow]
lang: en
summary: Want your AI agent to write better full-stack code? Step one is using a mono repo — keep your frontend and backend in the same folder.
---

After heavily using Codex and Claude Code, I now almost always use this structure.

**Keep your frontend and backend in the same folder.**

This isn't a new concept. Mono repos have been around forever. But in the age of Vibe Coding, their value multiplies.

## Why Mono Repo Matters for AI Agent Coding

When you use an AI agent to write code, its understanding is limited to the context you give it.

If your frontend and backend live in two separate repos:

- The AI can only see one side at a time
- It doesn't know what the other side's API looks like
- You become the translator, manually feeding information back and forth

But if they're in the same repo:

- The AI can read your frontend's call logic and your backend's API definition at the same time
- When you change a backend response format, it can automatically update the corresponding frontend fields
- Shared types, schemas, and configs stay in sync — no more drift between two repos

In short, **a mono repo gives the AI complete context**. Complete context means more accurate code generation.

## Recommended Folder Structure

It doesn't need to be complicated. This is enough:

```
my-project/
├── frontend/          ← React / Next.js
├── backend/           ← Node.js / Express / FastAPI
├── package.json
└── README.md
```

If you have shared type definitions or utility functions, add another layer:

```
my-project/
├── frontend/          ← React / Next.js
├── backend/           ← Node.js / Express / FastAPI
├── shared/            ← Shared types, constants, utilities
├── package.json
└── README.md
```

The point isn't a perfect structure — it's that **frontend and backend live under the same root directory**.

## Separate Repos vs Mono Repo

| | Separate Repos | Mono Repo |
|---|---|---|
| What AI can see | Only one side | Both frontend & backend |
| Updating frontend after API changes | Manual sync | AI can update both at once |
| Shared types / schemas | Easily out of sync | Single source of truth |
| Dev experience | Two windows, two terminals | One project, one workspace |

When you're Vibe Coding, these differences get amplified. The more you rely on AI, the more its context window matters.

## How to Get Started

If your current project already has separate repos, no need for a big migration. You can:

1. Create a new folder and pull both repos in (via submodules or just move them)
2. Start your next project with a mono repo structure from day one
3. Try letting an AI agent modify both frontend and backend in a mono repo — feel the difference

## Wrap Up

The key to Vibe Coding isn't just which AI tool you use — it's how you organize your project so the AI can do its best work.

A mono repo is the lowest-cost, highest-return move you can make.

Try it. You'll find it surprisingly efficient.
