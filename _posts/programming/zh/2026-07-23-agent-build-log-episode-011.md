---
layout: single
title: "Agent Build Log — Episode 011"
date: 2026-07-23 21:12:10 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-011.png
summary: "推翻 Episode 010 的向量檢索方案，第一版改採參考 OpenClaw 的 Markdown 與 SQLite 架構，讓記憶可閱讀、可修改，也更容易放進 App。"
description: "推翻 Episode 010 的向量檢索方案，第一版改採參考 OpenClaw 的 Markdown 與 SQLite 架構，讓記憶可閱讀、可修改，也更容易放進 App。"
---

今天決定推翻 Episode 010 的方案。

![Agent Build Log Episode 011：以 Markdown 與 SQLite 取代 embedding](/assets/programming/agent-build-log/agent-build-log-episode-011.png)

昨天原本選了 LanceDB 搭配 Qwen3 Embedding 0.6B，想把第一版記憶系統直接做成向量檢索。但真的開始看模型大小後，才發現光是 Qwen3 Embedding 的檔案就接近 600 MB。

如果直接把這個模型包進 App，整個 App 很可能會超過 1 GB。對第一版來說，這個代價太高了。

所以今天決定退一步，先不做 embedding。

第一版的記憶系統改成使用 Markdown 檔案加上 SQLite，整體方向先參考 OpenClaw 的做法。Markdown 負責保存真正的記憶內容，SQLite 則用來整理索引、時間、來源和查詢需要的資料。

以今天 07-23 為例，workspace 會先長成這樣：

```text
workspace/
├── MEMORY.md
├── DREAMS.md
└── memory/
    ├── 2026-07-22.md
    ├── 2026-07-23.md
    └── 2026-07-23-session-name.md
```

MEMORY.md 用來保存比較穩定、之後還會反覆用到的長期記憶。

每天發生的事情先寫進 memory/ 裡的日期檔案。如果某次 session 有比較明確的主題，也可以另外留下帶有 session name 的紀錄。

DREAMS.md 則先拿來放還沒有整理成熟的想法、待觀察的模式，以及之後可能需要回頭反思的內容。

這樣做的好處是，就算沒有 embedding model，我仍然可以直接打開檔案查看、修改或搬移記憶。資料不會被鎖在某個模型或向量資料庫裡，除錯時也比較容易知道 Agent 到底記住了什麼。

SQLite 暫時不負責取代 Markdown，而是當它的輔助層。之後可以用來記錄檔案位置、時間、標籤、session，以及哪些記憶曾經被讀取或更新。

昨天選的是技術上比較完整的方向，今天選的則是第一版真的能放進 App、能維護，也能繼續往下做的方向。

有時候推翻昨天的決定，不是走回頭路，只是終於看清楚第一步應該做多大。
