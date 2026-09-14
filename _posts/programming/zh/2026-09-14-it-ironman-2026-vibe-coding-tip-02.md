---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜Mono repo：前端、後端、mobile 放同一個資料夾 - Tip 02"
date: 2026-09-14 13:03:00 +0800
category: programming
author: Marvin Lin
tags: [IT鐵人賽, 2026鐵人賽, Vibe Coding, Vibe Coding 技巧, Mono repo, AI Agent, 軟體開發]
summary: "我把前端、後端和 mobile 放在同一個 repo，讓 coding agent 同時讀到 API 定義與呼叫邏輯。這篇整理資料夾結構、共用型別的放法，以及既有專案分開時可以怎麼開始。"
description: "我把前端、後端和 mobile 放在同一個 repo，讓 coding agent 同時讀到 API 定義與呼叫邏輯。這篇整理資料夾結構、共用型別的放法，以及既有專案分開時可以怎麼開始。"
---

這是 2026 iThome 鐵人賽《Vibe Coding：30 個開發實用技巧》系列的 Tip 02。

這一篇改寫自我部落格的《Vibe Coding 的第一步：把前後端放在同一個資料夾》，照這個系列的格式重寫過。原始文章：https://www.marvinswift.com/zh/programming/mono-repo-vibe-coding/

開始大量用 Codex、Claude Code 之後，我開新專案幾乎都用同一個架構：**前端和後端放在同一個資料夾裡**。有 mobile app 的話，mobile 也放進來。

## 為什麼

用 coding agent 寫程式，他的理解範圍就是我給他的 context。

前端和後端分成兩個 repo 的時候，他只看得到其中一邊。他不知道另一邊的 API 長什麼樣，我得自己當翻譯，把另一邊的資訊手動餵給他。

放在同一個 repo 裡，情況就變了。他可以同時讀到前端的呼叫邏輯和後端的 API 定義。後端的 response format 改了，他能順手把前端對應的欄位一起更新。共用的 type、schema、config 放在一起，兩邊不會不同步。

簡單說，**mono repo 讓他的 context 變完整了**。Context 完整，生成的程式碼就更準確。

Mono repo 這個做法存在很久了。到了 Vibe Coding 的時代，它的價值被放大了好幾倍。

## 我怎麼做

結構不用複雜，這樣就夠：

```
my-project/
├── frontend/          ← React / Next.js
├── backend/           ← Node.js / Express / FastAPI
├── package.json
└── README.md
```

有共用的型別定義或工具函式，再加一層 `shared/`：

```
my-project/
├── frontend/
├── backend/
├── shared/            ← 共用型別、常數、工具函式
├── package.json
└── README.md
```

有 mobile app 的話，我會再開一個 `mobile/`，跟前後端並排。App 打的 API 跟網頁打的是同一套，放在一起，他改 API 的時候三邊都看得到。

```
my-project/
├── frontend/
├── backend/
├── mobile/            ← iOS / Android
├── shared/
├── package.json
└── README.md
```

重點只有一個：**前後端在同一個根目錄下**。結構多完美沒有那麼要緊。

分開和合在一起的差別，列成一張表：

| | 分開兩個 repo | Mono repo |
| --- | --- | --- |
| 他能看到的範圍 | 只有一邊 | 前後端都能看到 |
| 改 API 後更新前端 | 手動同步 | 他可以一起改 |
| 共用型別／schema | 容易不同步 | 同一份檔案，不會分歧 |
| 開發體驗 | 要開兩個視窗、兩個 terminal | 一個專案搞定 |

Vibe Coding 的時候，這些差異會被放大。依賴他的程度越高，他能掌握的 context 就越重要。

## 專案已經分開了怎麼辦

現在的專案已經是前後端分開的，不用急著大改。可以這樣：

1. 開一個新資料夾，把兩個 repo 用 submodule 或直接搬進來
2. 下一個新專案，直接用 mono repo 結構開始
3. 試著讓他在 mono repo 裡同時修改前後端，感受一下差異

## 小結

Vibe Coding 的關鍵，除了用哪個工具，還有怎麼組織專案，讓他能發揮最大效果。Mono repo 是成本最低、回報最高的一步。試試看，效率很高。

資料夾擺好了，明天講專案一開始就要放進去的三樣東西：lint、formatter、unit test。程式大多是他寫的，我自己不逐行看，這三道關替我看。

原文：https://www.marvinswift.com/zh/programming/mono-repo-vibe-coding/
