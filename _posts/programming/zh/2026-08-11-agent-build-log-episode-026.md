---
layout: single
title: "Agent Build Log — Episode 026"
date: 2026-08-11 21:29:08 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-026.png
summary: "打造 Bug Blame，從 Jira bug 追查相關程式碼、commit，以及最適合參與調查的開發者。"
description: "打造 Bug Blame，從 Jira bug 追查相關程式碼、commit，以及最適合參與調查的開發者。"
---

今天，我做了 Agent 的另一個「專有技」。

![Agent Build Log Episode 026：Bug Blame 從 Jira bug 追查程式碼、commit 與開發者](/assets/programming/agent-build-log/agent-build-log-episode-026.png)

這次叫做 Bug Blame。

這個名字來自 git blame。

它從一張 Jira ticket 開始。

Agent 會先理解 ticket 裡描述的 bug，以及可能受到影響的功能和程式碼範圍。

接著，它會透過 repo 的 commit history 和 git blame 往回追查，找出和這個問題最相關的修改。

最後，再把這些 commits 對應到實際的開發者。

整個流程大概是：

Jira ticket → related code → git blame → commit → developer

我把它叫做 Bug Blame，是因為 git blame 是這個 capability 背後的重要線索之一。

但它的目的不只是回答：「這個 bug 是誰寫的？」

git blame 可以告訴我，某一行程式碼最後是誰修改的，但這不代表 bug 就是那個人造成的。

所以我希望最後的結果能有清楚的信心程度。

如果某個 commit 和 bug 之間的關聯很強，Agent 可以指出最相關的開發者。

如果這個功能曾經由多位開發者修改，它應該列出可能相關的開發者，以及各自對應的 commits。

如果證據不足，它就直接說：「無法判定。」

我不希望 Agent 為了給出答案而勉強判斷。我希望它反映真實情況。

這個專有技真正想解決的是，當一張 Jira bug ticket 出現時，我希望可以快速知道：

這部分的功能過去是怎麼被修改的。

哪些 commits 最可能和問題有關。

以及接下來應該找哪些開發者一起調查。

所以，它雖然叫做 Bug Blame，但我真正想要的，是一個能快速找出開發歷史，以及和 bug 最相關人員的方法。
