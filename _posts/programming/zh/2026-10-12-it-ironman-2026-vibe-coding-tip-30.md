---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜Design prototype：用 Claude Design 或 HTML 先做 mobile 畫面 - Tip 30"
date: 2026-10-12 01:00 +0800
permalink: /zh/programming/it-ironman-2026-vibe-coding-tip-30/
category: programming
author: Marvin Lin
tags: [IT鐵人賽, 2026鐵人賽, Vibe Coding, Vibe Coding 技巧, Claude Design, Mobile]
summary: 先用 Claude Design 或 HTML 做 mobile prototype，確認版面和流程後再進 app 實作。
---

做 mobile 畫面，我建議先做 design prototype。可以用 Claude Design，也可以請 coding agent 用 HTML、CSS 和少量 JavaScript 先做一版。在還要反覆改版面的階段，這樣比直接進 app 實作快。

## 為什麼

畫面還沒定的時候，我要先看資訊怎麼排、按鈕放哪裡、下一步往哪走。先用瀏覽器能打開的原型看這些東西，就可以暫時省下 app 的建置、SDK 串接和資料處理。

排版或流程要換，直接改原型。方向確認後，再把畫面與行為規格交給他實作。

## 我怎麼做

**用 Claude Design。** 在 Claude Design 建專案，提供參考畫面、要呈現的內容與主要操作，請他先做出可以看的版本。看完可以透過對話或畫面上的留言，指出哪個地方要改。

額度怎麼算，用之前先看官方 Usage 頁上當時的說明，這一段規則會變。

**用 HTML 設計 mobile 畫面。** 不一定要先選正式 app 的 framework，先請他產出瀏覽器能開的原型。例如：

```text
幫我做一個 mobile app 的設計原型，使用 HTML、CSS 和少量 JavaScript。

產品：<產品與使用者>
主要任務：<使用者要完成什麼>
需要的畫面：<畫面列表>

這一版只做設計原型：
- 用假資料，先不接 API、登入服務或付款。
- 以 390px 寬的手機畫面設計，也檢查 360px 與 430px。
- 主要按鈕能點，能切換畫面、返回，讓我走完主要流程。
- 需要的空資料、載入中、錯誤狀態，也做成可以切換查看的畫面。
- 放在獨立的 prototype 資料夾，附上開啟方式。
- 列出哪些互動是假資料模擬、哪些產品規則還沒決定。

做完打開瀏覽器檢查畫面，附上截圖與發現的排版問題。
```

我會先走一次主要流程，再改畫面。想比較不同排版，可以請他保留目前版本，再做另一版，兩個一起看。

## 坑

Tip 15 講過我把 demo 當 spec 的問題。這次交付原型時，一樣要把入口狀態、分支條件、成功條件補清楚。原型用假資料直接進主頁，正式 app 可能還要處理更新、登入和錯誤流程。

HTML 可以先看版面與互動，但原生鍵盤、安全區域、系統返回手勢等行為，仍要在實際 app 裡驗收。原型確認後，這些項目一起交給實作的人或 agent。

## 小結

先用 Claude Design 或 HTML 做 mobile 原型，把版面與主要流程確認好，再帶著行為規格進 app 實作。

參考：
- Claude Design 官方入門與額度說明 https://support.claude.com/en/articles/14604416-get-started-with-claude-design
