---
layout: single
title: Prompt to Make AI Agents Present Design First Without Implementation
date: 2025-04-26 11:50 +0800
category: programming
author: Marvin Lin
tags: [Cursor, AI, AI Agent]
summary: 
---

This year, I've been heavily using AI Agents in program development. Besides general debugging, Agents also participate in my program design process. However, if I don't specifically mention "don't start coding, I want to review your design first," the AI Agent will immediately start writing code. Based on my experience over the past few months, it's rare for an AI Agent to design exactly what I want on the first try. But if I continuously review the solutions proposed by the Agent and discuss them, the AI Agent gradually gets closer to the results I'm looking for.

If you're using Cursor, you can write the rules in `.cursor/rules/think-mode.mdc`

If you're using VSCode Insiders, you can press `cmd + shift + P`, then choose "create prompt", which will open up the user settings. When giving commands, pressing the "add context" shortcut will add this prompt to the context, saving you typing time.

## Think-mode prompt

```markdown
# Thinking Mode Only: Ideas and Proposals Without Implementation

Act as a consultant for this conversation only. Help me think through problems without implementing code.

## Guidelines:
- Analyze the problem or request I present
- Explore possible implementation approaches and architectures
- Provide high-level solutions or design considerations
- Explain pros and cons of different approaches
- Suggest technology choices and potential concerns

## Do NOT:
- Do not write complete implementation code
- Do not modify my existing code
- Do not provide code blocks that can be directly copied and pasted

Help me clarify my thinking and provide direction for my implementation. If I need specific code assistance later, I will explicitly request it.
```

