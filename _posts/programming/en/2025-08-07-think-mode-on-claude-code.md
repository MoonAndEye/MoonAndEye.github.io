---
layout: single
title: Using Plan Mode to Let Claude Code Plan Before Implementation
date: 2025-08-07 12:05 +0800
category: programming
author: Marvin Lin
tags: [Claude, AI, AI Agent]
summary: This article introduces how to use think mode for code editing on macOS and provides detailed step-by-step instructions.
---

When using Claude Code, you can first enable plan mode to let AI help you plan the code architecture and logic before starting implementation. You can wait until you approve and confirm Claude Code's plan before letting Claude Code execute.

## How to Switch to Plan Mode - Shift + Tab

In Claude Code, you can use the shortcut Shift + Tab to switch modes. The first switch is to auto accept mode. You can see the prompt at the bottom of the terminal to know which mode you're currently in. Press Shift + Tab a second time to enter plan mode. When you enable plan mode, Claude enters a state focused on thinking and planning. At this time, Claude Code will not modify your code but will list the steps it will take and the implementation blueprint. So you can safely conduct various confirmations and divergent thinking.

### First Press of Shift + Tab - Enter Auto Accept Mode
![auto accept mode](/assets/programming/claude-code-think-mode/claude-code-accept-mode.png)

### Use Shift + Tab to Enter Plan Mode
![claude code think mode](/assets/programming/claude-code-think-mode/claude-code-think-mode.png)

## Advantages of Think Mode

### Plan First, Then Execute
![think mode request prompt](/assets/programming/claude-code-think-mode/think-mode-request-prompt.png)

When you make a request to Claude in think mode, Claude will first analyze and think about your requirements, then provide a detailed plan blueprint.

### View Implementation Blueprint
![plan mode blueprint](/assets/programming/claude-code-think-mode/plan-mode-blueprint.png)

In plan mode, Claude will display a complete implementation plan, allowing you to understand the entire implementation process before actual execution.

### Execute After Confirmation
![action after planning](/assets/programming/claude-code-think-mode/action-after-planing.png)

When you confirm the plan, Claude will start executing actual code modifications based on the previous planning.

### Personal Thoughts
Before knowing about plan mode, I used prompts to prevent Claude Code from directly modifying code, instead asking it to give me a general direction and steps first. However, when using prompts alone, sometimes Claude Code would still directly initiate modifications. Moreover, since I mostly develop iOS apps, it would often directly execute Xcode build or other Xcode CLI commands.

In plan mode, I feel the quality of modification context has improved, and the solutions it proposes in plan mode have preserved the concept of Canvas or artifacts in the UI, allowing for minor modifications to the same file without affecting the overall structure and logic.

This is what I like most about it. After all, I need to get things done right first before I can start asking AI to do things well.

## Related Articles

- [How to Paste Screen Captures to Claude Code Editor on macOS](/en/programming/paste-capture-image-to-claude-code/) (English)

- [將螢幕的截圖貼上到 Claude 的程式碼編輯器的方法，macOS 適用](/zh/programming/paste-capture-image-to-claude-code/) (Chinese)
