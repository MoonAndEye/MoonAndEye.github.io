---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜先讓他把設計攤出來、不動手：一段 think-mode prompt - Tip 14"
date: 2026-09-26 13:07 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - AI Agent
  - Prompt Engineering
  - Cursor
  - VS Code
summary: "用 think-mode prompt 讓 AI Agent 先提出設計方案，再逐輪討論；將規則存成 Cursor rules 或 VS Code prompt，讓每段對話都能沿用。"
description: "用 think-mode prompt 讓 AI Agent 先提出設計方案，再逐輪討論；將規則存成 Cursor rules 或 VS Code prompt，讓每段對話都能沿用。"
---

本文同步刊登於 [iT 鐵人賽第二系列](https://ithelp.ithome.com.tw/articles/10417393)。

這一篇改寫自我部落格的《讓 AI Agent 不要動手，先呈現設計結果的 prompt》，照這個系列的格式重寫過。原始文章：https://www.marvinswift.com/zh/programming/ai-agent-coding-prompt/

要他先講設計、先別寫 code，得明講。沒特別說，他會直接開始寫。我用一段固定的 prompt 把他切成「只出主意、不動手」。

## 為什麼

從 2025 年開始，我大量用 coding agent 開發。除了一般 debug，設計程式的過程他也會參與。只是沒有特別講「不要動手，我要先 review 你的設計」，他就直接開始寫程式碼。而那幾個月的經驗是：他很難一次就設計到我想要的結果。反過來，如果我一輪一輪 review 他提出來的方案，在討論的過程中，他會越來越接近我要的東西。

所以先讓他把設計攤出來，我看過、改過，再讓他動手。

## 我怎麼做

我把這件事寫成一段 prompt，需要的時候整段貼給他：

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

用 Cursor 的話，把它寫成 rules 放在 `.cursor/rules/think-mode.mdc`。用 VS Code Insiders 的話，按 cmd + shift + P 選 create prompt，它會開到 user setting 底下；之後下指令時按 add context 的快捷鍵，這段 prompt 就會加進 context，省掉每次打字。

## 坑

這段 prompt 開頭寫的是 for this conversation only，只管這一段對話。開新的一段沒貼，他又會直接動手，所以才把它寫成 rules 或 prompt file，讓每一段都帶著。要他動手的時候也得明講一句，像「照第二個方案做」，他才會從顧問切回來。prompt 最後那一句「之後要 code 我會明說」，留的就是這一步。

## 小結

要他先想、別動手，得明講；寫成一段固定的 prompt，每次貼。

明天講另一個坑：我把 demo 當 spec 給他，他就照 demo 做。

原文：https://www.marvinswift.com/zh/programming/ai-agent-coding-prompt/
