---
layout: single
title: Using GitHub Copilot in Xcode. Conclusion Not Ideal, I Turn It Off When Using Xcode
date: 2023-05-24 12:00 +0800
category: swift
author: Marvin Lin
tags: [Swift, Xcode, Copilot]
summary: This post details my experience using GitHub Copilot in Xcode. Conclusion - it's not very effective, and I prefer to turn it off while using Xcode.
---

In a previous discussion, I shared my experience with purchasing and trying GitHub Copilot in a side project. My primary work involves iOS app development with native development tools, and I have also experimented with Copilot in Xcode. For those interested in similar integrations, there are various resources available that provide tutorials on how to integrate tools like Copilot with Xcode.

## But, I No Longer Use Copilot in Xcode

The experience of using Copilot in Xcode isn’t as smooth as in VScode. While I’m typing, the Copilot plugin in Xcode interferes with the auto-complete response time of Xcode itself. My "sensation" is that I'm waiting for Xcode's auto-complete to pop up so I can select one of the auto-completion suggestions.

On the other hand, the code suggestions provided by Xcode Copilot often don’t quite fit the context, possibly because it hasn’t sufficiently adapted to my machine/account yet. In a VC or class or struct, we always have property declarations outside functions, but when Copilot encounters scenarios that interact with these variables, the suggested code isn’t very useful (and such global variables aren’t always easy to understand, which is why design patterns exist).

After turning it off, I felt better about my development experience, although it’s hard to objectively compare the difference in speed. From my understanding, Copilot should improve with use, but currently, the experience in Xcode isn’t good enough.

## In Xcode, You Can Use Code Snippets for Similar Code Suggestion Features

Snippets are a feature available in most IDEs. You can create a template for commonly used code, and leave placeholders for the parts to be filled in. When calling a snippet, you only need to fill in the remaining parts. Below is a snippet I frequently use to return to the main queue. After iOS 13, using UI components off the main queue can cause crashes.

```swift
        // This is a snippet I often use
        DispatchQueue.main.async {
            
        }
```