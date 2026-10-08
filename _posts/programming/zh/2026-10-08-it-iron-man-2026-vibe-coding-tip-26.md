---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜雲端的 Claude Code 和 Codex：不一定要在本機跑，每個裝置看到的是同一個 session - Tip 26"
date: 2026-10-08 13:00 +0800
category: programming
author: Marvin Lin
tags: [IT鐵人賽, 2026鐵人賽, Vibe Coding, Vibe Coding 技巧, Claude Code, Codex, AI Agent]
summary: "Claude Code 和 Codex 的雲端 session 可以跨瀏覽器、手機與 terminal 接續；我也整理了 --teleport 產生本機副本時要留意的差異。"
description: "Claude Code 和 Codex 的雲端 session 可以跨瀏覽器、手機與 terminal 接續；我也整理了 --teleport 產生本機副本時要留意的差異。"
---

本篇 iT 鐵人賽文章：[前往 iT 閱讀](https://ithelp.ithome.com.tw/articles/10422338)。

Claude Code 和 Codex 都有雲端版。任務在雲端的機器上跑，我從瀏覽器、手機、terminal 看到的是同一個 session。他不一定要在我的電腦上跑。

## 為什麼

跑在本機，session 綁在那一台電腦上：terminal 關了就停，換一台電腦就看不到。跑在雲端，session 在雲端的機器上，瀏覽器關掉它繼續做，做完等我回來。好處是所有 client 端對這個 session 是一致的：筆電上開的任務，手機上接著看、接著回，terminal 也能把它拉下來繼續。

Claude Code 的文件列了幾種它適合的場景：好幾個獨立任務平行跑、本機沒有 clone 的 repo、下好指令就不用一直盯的任務、對一個 codebase 問問題。要用到本機設定和工具的工作，還是在本機跑。

## 我怎麼做

**Claude Code on the web**，照文件的步驟：

1. 到 claude.ai/code 登入，連 GitHub。私有 repo 要在那個帳號或組織裝 Claude GitHub App。第一次會建一個叫 Default 的雲端環境，網路存取、環境變數、setup script 都在那裡設
2. 選 repo 和 branch，選權限模式（Accept edits、Plan、Auto 三種），把任務打進去送出。他把 repo clone 到一台隔離的 VM 裡改、跑測試，做到一個段落把 branch 推上 GitHub
3. 看 diff、在某一行上留意見、按 Create PR。分頁關掉 session 照樣跑；手機上 Claude app 的 Code 那一頁看到的是同一個 session

從 terminal 也能開、也能接：

```bash
# 從 terminal 開一個雲端 session（clone 的是這個 repo 在 GitHub 上的目前 branch，先 push）
claude --cloud "把 src/cart 底下的測試補齊"

# 在 Claude Code 裡看所有雲端 session 的進度
/tasks

# 在任何一台登入同一個帳號的機器上，補一句話給正在跑的 session
claude -p "測試名稱用中文" --cloud <session-id>

# 把雲端 session 拉回 terminal 繼續，要在同一個 repo 的 checkout 裡跑
claude --teleport
```

**Codex 也有雲端版。** OpenAI 的 README 把 chatgpt.com/codex 上的 Codex Web 叫做雲端跑的 agent，本機的 Codex CLI 和 Desktop App 是另外兩個入口。怎麼用照它的文件。

## 坑

- `--teleport` 拉回 terminal 之後，terminal 那一份是另一份 copy：之後在本機做的東西留在本機，雲端那個 session 和手機上看不到。還想從手機接著控制，在本機那個 session 裡開 `/remote-control`
- 雲端 session 只有 repo 裡的東西，沒有你本機的設定和工具；要改設定就用環境變數，或者把設定檔 commit 進 repo
- 額度跟帳號裡其他 Claude 的用量共用，同時開很多個 session 就吃得快。文件寫它還在 research preview，Pro、Max、Team 能用，Enterprise 看座位種類

## 小結

他不一定要在本機跑。任務丟到雲端，筆電、手機、terminal 對的是同一個 session，螢幕關掉它繼續做。

明天講收款：mobile 用 RevenueCat，網頁用 Lemon Squeezy。

參考：
- Claude Code 文件：Get started with Claude Code on the web https://code.claude.com/docs/en/web-quickstart
- Claude Code 文件：Use Claude Code on the web https://code.claude.com/docs/en/claude-code-on-the-web
- openai/codex https://github.com/openai/codex