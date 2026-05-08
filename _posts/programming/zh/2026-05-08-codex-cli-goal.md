---
layout: single
title: Codex CLI 的 /goal：讓 AI agent 記住一個長線目標
date: 2026-05-08 11:00 +0800
category: programming
author: Marvin Lin
tags: [Codex CLI, OpenAI, AI Agent, AI Agent Coding]
summary: /goal 是 Codex CLI 新增的實驗功能，它可以把一個長線任務變成可持續追蹤、暫停和恢復的工作目標，但目前需要新版 CLI 並手動打開 feature flag。
---

Codex CLI 最近多了一個我覺得很值得注意的新功能：`/goal`。

我會把它理解成「讓 Codex 記住一個長線目標」的功能。以前我們在 terminal 裡跟 AI agent 協作，大多是一輪一輪對話。你丟一個任務，它做一段；你再補充，它再做下一段。

這樣對短任務很好用。

但如果任務變長，例如整理一個 repo、做一個跨檔案 refactor、追一串測試失敗、或是讓 agent 持續往某個產品目標前進，單純靠每一輪 prompt 其實很容易散掉。

`/goal` 想解決的就是這個問題。

## /goal 不是預設開啟

這點要先講，因為很容易踩到。

就算你已經更新 Codex CLI，也不代表你打開 Codex 後就會直接看到 `/goal`。目前 `/goal` 還是 experimental feature，預設是關的。

我寫這篇時，最新的 npm 版本是 `0.129.0`。在這個版本裡，`codex features list` 會看到：

```bash
goals    experimental    false
```

也就是功能存在，但預設沒有打開。

要開啟它，指令是：

```bash
codex features enable goals
```

打開後，`~/.codex/config.toml` 會多一段：

```toml
[features]
goals = true
```

接著重新進入 Codex CLI，就可以使用 `/goal`。

如果你只是想暫時測一次，也可以用：

```bash
codex --enable goals
```

以上這些作業，你並不需要手動執行。你可以直接叫 Codex App、Claude App、Claude Code 這類 AI agent 幫完成，你只要下一個 prompt。
```
把 codex cli 的 goals 功能打開，讓我可以用 /goal。
```

## 版本要在 0.128.0 以上

另一個要注意的地方是版本。

`/goal` 不是所有 Codex CLI 都有。OpenAI 在 [Codex CLI 0.128.0 release note](https://github.com/openai/codex/releases/tag/rust-v0.128.0) 裡加入 persisted `/goal` workflow，包含 create、pause、resume、clear 這些 TUI controls。到了 [0.129.0 release note](https://github.com/openai/codex/releases/tag/rust-v0.129.0)，goals 被標成 experimental，並改善 discoverable、resume 後維持 paused、validation 和 duration 顯示。


## 在 Codex app 裡面，升起 terminal 的區域使用 codex cli

在 codex app 中，是可以使用 terminal 的，快速鍵是 cmd + J，這會升起 terminal，你再輸入 codex 指令，就可以進入 codex cli 的環境。
