---
layout: single
title: Vibe Coding 的第一步：把前後端放在同一個資料夾
date: 2026-04-12 08:00 +0800
category: programming
author: Marvin Lin
tags: [AI, Vibe Coding, Mono Repo, Frontend, Backend, Workflow]
summary: 想讓 AI agent 幫你寫出更好的全端程式碼？第一步就是用 mono repo，把前後端放在同一個資料夾裡。
---

在開始大量使用 Codex, Claude Code 後，我現在幾乎都使用這個架構。

**把前端和後端放在同一個資料夾裡。**

這不是什麼新概念，mono repo 已經存在很久了。但在 Vibe Coding 的時代，它的價值被放大了好幾倍。

## 為什麼 Mono Repo 對 AI Agent Coding 很重要？

當你用 AI agent 來寫程式，它的理解範圍就是你給它的 context。

如果你的前端和後端分成兩個 repo：

- AI 只看得到其中一邊
- 它不知道另一邊的 API 長什麼樣
- 你得自己當翻譯，把另一邊的資訊手動餵給它

但如果它們在同一個 repo 裡：

- AI 可以同時讀到前端的呼叫邏輯和後端的 API 定義
- 改了後端的 response format，它能自動幫你更新前端的對應欄位
- 共用的 type、schema、config 放在一起，不會出現兩邊不同步的問題

簡單來說，**mono repo 讓 AI 的 context 變完整了**。Context 完整，生成的程式碼就更準確。

## 推薦的資料夾結構

不需要太複雜，這樣就夠了：

```
my-project/
├── frontend/          ← React / Next.js
├── backend/           ← Node.js / Express / FastAPI
├── package.json
└── README.md
```

如果你有共用的型別定義或工具函式，可以再加一層：

```
my-project/
├── frontend/          ← React / Next.js
├── backend/           ← Node.js / Express / FastAPI
├── shared/            ← 共用型別、常數、工具函式
├── package.json
└── README.md
```

重點不是結構多完美，而是**前後端在同一個根目錄下**。

## 分開 vs 合在一起的差別

| | 分開兩個 Repo | Mono Repo |
|---|---|---|
| AI 能看到的範圍 | 只有一邊 | 前後端都能看到 |
| 改 API 後更新前端 | 手動同步 | AI 可以一起改 |
| 共用型別 / Schema | 容易不同步 | 同一份檔案，不會分歧 |
| 開發體驗 | 要開兩個視窗、兩個 terminal | 一個專案搞定 |

當你在 Vibe Coding 的時候，這些差異會被放大。因為你依賴 AI 的程度越高，它能掌握的 context 就越重要。

## 怎麼開始？

如果你現在的專案已經是前後端分開的，不用急著大改。可以：

1. 開一個新資料夾，把兩個 repo 用 submodule 或直接搬進來
2. 下一個新專案，直接用 mono repo 結構開始
3. 試著讓 AI agent 在 mono repo 裡同時修改前後端，感受一下差異

## 結語

Vibe Coding 的關鍵不只是用哪個 AI 工具，更是你怎麼組織你的專案讓 AI 能發揮最大效果。

Mono repo 就是最低成本、最高回報的一步。

試試看，你會發現這個效率很高
