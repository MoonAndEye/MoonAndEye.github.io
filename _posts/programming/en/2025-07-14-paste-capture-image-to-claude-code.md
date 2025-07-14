---
layout: single
title: How to Paste Screen Captures to Claude Code Editor on macOS
date: 2025-07-14 16:25 +0800
category: programming
author: Marvin Lin
tags: [Claude, AI, AI Agent]
summary: This article introduces how to paste screen captures to Claude's code editor on macOS, with detailed step-by-step instructions.
---

Currently, I'm extensively using Claude code for development. Claude code is a terminal-based AI coding interface that primarily works with text. So when developing, the collaboration feels like I mark files or highlight certain code sections, and Claude code in the VSCode terminal knows which code I want to discuss, and it also highlights them in the Claude code interface.

## Cmd + ctrl + K - You can send highlighted code from another file to Claude code

As shown in the image, you'll see "1 line selected" in the bottom right of the terminal

![claude-code-select-lines](/assets/programming/claude-code/claude-code-select-lines.png)

## What about images? There's definitely a way to send them to Claude code too

On macOS, you can use the following method to paste screen captures to Claude's code editor:

- Press ctrl + cmd + shift + 4, then select the area you want to capture.
- After taking the screenshot, switch to Claude code's editor.
- Press cmd + v to paste the screenshot.

![claude-code-paste-image](/assets/programming/claude-code/claude-code-screen-capture.png)

At this point, you'll see the text "image" pasted into the input box. You can use this technique to have Claude make modifications based on colors/layout.