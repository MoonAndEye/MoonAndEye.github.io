---
layout: single
title: "Agent Build Log — Episode 019"
date: 2026-08-02 23:00:52 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-019.png
summary: "Pi Agent 不支援 ultra effort；Agent 將依 Pi 宣告的能力顯示並驗證 effort 選項。"
description: "Pi Agent 不支援 ultra effort；Agent 將依 Pi 宣告的能力顯示並驗證 effort 選項。"
---

今天，我發現 Pi Agent 的 effort 並不支援 ultra。

![Agent Build Log Episode 019：依 Pi Agent 能力限制 effort 選項](/assets/programming/agent-build-log/agent-build-log-episode-019.png)

目前可用的值是：

off、minimal、low、medium、high、xhigh、max

如果把 ultra 傳給現在的 Pi，它不會被當成比 max 更高的設定。

它反而會被轉成 off。

這代表使用者以為自己選了最高推理強度，實際上卻把 reasoning 關掉了。

所以 effort 不能只看模型名稱，也不能因為模型屬於 GPT-5.6，就假設它支援 ultra。

之後，Agent 會依照 Pi 對目前模型實際宣告的能力，決定可以顯示哪些 effort。

如果模型不支援 ultra，UI 就不會顯示。

runtime 也會驗證 effort，避免 CLI、設定檔或 session restore 傳入不支援的值。

目前 Sol、Terra 等模型，都先以 Pi 實際支援的最高值 max 為上限。

只有當 Pi 明確回報某個模型支援 ultra 時，Agent 才會對那個模型開放。

今天學到了一點，雖然我使用的 agent (Codex) 的有 Ultra effort，但不表示我在 pi agenet 中的轉接，這個 ultra effort 可以正常運作，甚致有可能因為 effort 在 pi agent 中不存在，所以會回到 no reasoning。
