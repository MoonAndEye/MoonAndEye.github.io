---
layout: single
title: 讓 AI Agent 不要動手，先呈現設計結果的 prompt
date: 2025-04-26 11:39 +0800
category: programming
author: Marvin Lin
tags: [Cursor, AI, AI Agent]
summary: 
---

今年開始，我大量的使用 AI Agent 在程式開發。除了一般 debug 以外，Agent 也會參與我的程式設計過程。但是，AI Agent 如果沒有特別提到「不要動手，我要先 review 你的設計」時，AI Agent 會直接開始寫程式碼。而依這幾個月的經驗，AI Agent 很難一次就設計到我想要的結果。但如果我不斷的 review Agent 提出來的方案，在討論的過程中，AI Agent 會越來越接近我想要的結果。

如果你用的是 cursor，你可以把 rules 寫在 .cursor/rules/think-mode.mdc

如果你是用 VSCode insiders，你可以先按 cmd + shift + P，然後選擇 create prompt，接著他就會開到 user setting 下。在下指令時，你按下 add context 的 short cut 時，就會把這段 prompt 加在 context 裡面了，可以結省你打字的時間。

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

