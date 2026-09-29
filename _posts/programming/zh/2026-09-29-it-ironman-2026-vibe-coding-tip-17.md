---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜Codex 的 /goal：給他一個長線目標，CLI 和 Desktop App 都有 - Tip 17"
date: 2026-09-29 13:00 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - Codex
  - CLI
  - Desktop App
  - goal
summary: "我整理 Codex /goal 在 Desktop App 與 CLI 的使用方式，補上 CLI 舊版啟用步驟、新版功能狀態檢查，以及一段可交給 agent 執行的 prompt。"
description: "我整理 Codex /goal 在 Desktop App 與 CLI 的使用方式，補上 CLI 舊版啟用步驟、新版功能狀態檢查，以及一段可交給 agent 執行的 prompt。"
---

本文同步刊登於 [iT 鐵人賽第二系列](https://ithelp.ithome.com.tw/articles/10418742).

這一篇改寫自我部落格的《Codex CLI 的 /goal：讓 AI agent 記住一個長線目標》，照這個系列的格式重寫過。原始文章：https://www.marvinswift.com/zh/programming/codex-cli-goal/

Codex 有一個我覺得很值得注意的功能：`/goal`。我把它理解成「讓 Codex 記住一個長線目標」。Codex CLI 有，一般的 Desktop App 也有。

## 為什麼

以前在 terminal 裡跟他協作，大多是一輪一輪對話：丟一個任務，他做一段；再補充，他再做下一段。短任務這樣很好用。任務變長就不一樣了，像整理一個 repo、跨檔案 refactor、追一串測試失敗，或者讓他持續往某個產品目標前進，單靠每一輪 prompt 很容易散掉。`/goal` 要解的就是這個：把一個長線任務變成可以持續追蹤、暫停、恢復的工作目標。

## 我怎麼做

**Desktop App 直接用。** 現在 Codex 的 Desktop App 也有 `/goal`，不用進 CLI 就能用。

**CLI 的話，看版本、開功能。** 我寫原文（2026 年 5 月）的時候，`/goal` 在 CLI 還是 experimental feature：OpenAI 在 0.128.0 的 release note 加入 persisted `/goal` workflow，包含 create、pause、resume、clear 這些 TUI controls；0.129.0 把 goals 標成 experimental、預設關著。當時 `codex features list` 會看到：

```bash
goals    experimental    false
```

打開它：

```bash
codex features enable goals
```

`~/.codex/config.toml` 會多一段：

```toml
[features]
goals = true
```

重新進 Codex CLI 就能用 `/goal`。只想暫時試一次，也可以 `codex --enable goals`。

2026 年 9 月再看 Codex 的原始碼，goals 這個開關已經標成 stable、預設打開，新版裝好就有 `/goal`，上面那幾步是舊版才需要的。拿不準就 `codex features list` 看一眼，goals 那一行已經是 true 就不用再開。

這些步驟不用自己動手。叫 Codex App、Claude App、Claude Code 這類 agent 幫你做，一句 prompt：

```
把 codex cli 的 goals 功能打開，讓我可以用 /goal。
```

順帶一提，Codex App 裡按 cmd + J 會升起 terminal，在那裡輸入 `codex` 就進到 Codex CLI 的環境。

## 小結

長線任務用 `/goal` 釘住。Desktop App 直接用；CLI 要 0.128.0 以上，新版預設就開著，舊版照上面的步驟開。

明天講一個開發以外的用法：PM 用 Codex App 或 Claude App 寫 Jira 的需求單。

參考：
- Codex CLI 0.128.0 release note https://github.com/openai/codex/releases/tag/rust-v0.128.0
- Codex CLI 0.129.0 release note https://github.com/openai/codex/releases/tag/rust-v0.129.0

原文：https://www.marvinswift.com/zh/programming/codex-cli-goal/
