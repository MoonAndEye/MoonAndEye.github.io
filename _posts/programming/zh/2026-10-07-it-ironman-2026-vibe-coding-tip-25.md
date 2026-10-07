---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜紀錄放 GitHub Issues：一件事一張票，open source 常用的方法直接拿來用 - Tip 25"
date: 2026-10-07 13:00 +0800
category: programming
author: Marvin Lin
tags: [IT鐵人賽, 2026鐵人賽, Vibe Coding, Vibe Coding 技巧, GitHub Issues, GitHub]
summary: "用 GitHub Issues 做專案紀錄：一件事一張票，搭配 label、milestone、PR 關聯與 issue template，把開源專案的工作方法直接用在自己的 repo。"
description: "用 GitHub Issues 做專案紀錄：一件事一張票，搭配 label、milestone、PR 關聯與 issue template，把開源專案的工作方法直接用在自己的 repo。"
---

本篇 iT 鐵人賽文章：[前往 iT 閱讀](https://ithelp.ithome.com.tw/articles/10421970)。

專案的紀錄放哪裡？我放 GitHub Issues。想到的功能、發現的 bug、討論過的決定，一件事一張 issue。開源專案用這套用了很多年，方法都是現成的，直接拿來用。

## 為什麼

紀錄跟 code 在同一個 repo 裡，不用另外開一套工具。每一張 issue 有編號，別的 issue 或 PR 裡打 `#12` 就連起來，之後回頭找得到來龍去脈。他也讀得到：GitHub 有官方的 MCP server（Tip 23 講的那種插座），接上之後他能開票、讀票、關票；用 `gh` 這支 CLI 也行。

我這次鐵人賽兩個系列的稿子，就全放在一個 repo 的 issues 裡，一篇一張。

## 我怎麼做

開源專案常用的方法，照 GitHub 的文件列出來：

1. **一件事一張 issue。** bug、想加的功能、要做的事、要記下來討論的東西，各開一張。標題一句話講清楚，內文寫發生了什麼、原本期待什麼、怎麼重現。
2. **用 label 分類。** 每個新 repo 預設就有一組 label：`bug`、`enhancement`、`documentation`、`question`、`duplicate`、`wontfix`、`good first issue`、`help wanted` 這些。先用預設的，不夠再加。
3. **用 milestone 綁版本。** 要出 1.2.0，開一個 milestone，這一版要做的 issue 都掛上去，milestone 那一頁會算完成百分比。
4. **內文用 task list 拆小步。** `- [ ]` 一行一步，勾完就是進度；哪一步要另外追，滑過去按一下就能轉成一張新的 issue。
5. **PR 連 issue。** PR 的描述寫 `Fixes #12`，merge 進 main 那張 issue 自動關。關鍵字有三組：close、fix、resolve，各自的時態都認。Tip 04 開的那條 branch，收尾的 PR 就這樣寫。
6. **放 issue template。** `.github/ISSUE_TEMPLATE/` 底下放模板，開票的人照格式填，該有的欄位不會漏。
7. **問答和看板另外放。** 問題、想法、公告放 Discussions；要看全貌用 Projects，table、board、roadmap 三種排法。

第 6 點的模板可以直接抄。`.github/ISSUE_TEMPLATE/bug.yml`：

```yaml
name: Bug
description: 回報一個問題
title: "[Bug] "
labels: ["bug"]
body:
  - type: textarea
    attributes:
      label: 發生了什麼
      description: 你做了什麼、畫面上出現什麼
    validations:
      required: true
  - type: textarea
    attributes:
      label: 原本期待什麼
    validations:
      required: true
  - type: textarea
    attributes:
      label: 怎麼重現
      placeholder: |
        1. 打開……
        2. 按……
        3. 看到……
```

開票這件事也能交給他。接了 GitHub 的 MCP，一句話：

```
把剛剛那個問題開成一張 issue，掛 bug 這個 label，內文寫發生了什麼、原本期待什麼、怎麼重現。
```

## 坑

一張 issue 只講一件事。討論岔出去了，把那則留言轉成一張新的 issue（留言選單裡的 Reference in new issue），或者整張轉成 Discussion，原本那張留給原本的事。

## 小結

紀錄放 GitHub Issues：一件事一張、label 分類、PR 寫 `Fixes #編號`、模板放 `.github/ISSUE_TEMPLATE/`。開源專案的方法直接用。

明天講另一件不一定要在本機做的事：Claude Code 和 Codex 都有雲端版。

參考：
- GitHub 文件：About issues https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues
- GitHub 文件：Managing labels https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels
- GitHub 文件：Linking a pull request to an issue https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue
- GitHub 文件：Syntax for issue forms https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms
- GitHub MCP Server https://github.com/github/github-mcp-server