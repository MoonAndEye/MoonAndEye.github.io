---
layout: single
title: 使用 think mode 先讓 claude code 規畫，再開始實作
date: 2025-08-07 12:02 +0800
category: programming
author: Marvin Lin
tags: [Claude, AI, AI Agent]
summary: 本文將介紹如何在 macOS 上使用 think mode 進行程式碼編輯，並提供詳細的步驟說明。
---

在使用 claude code 時，你可以先啟用 think mode，讓 AI 幫助你規劃程式碼的架構和邏輯，然後再開始實作。直到你認可和確認 Claude code 的規畫，再開始讓 claude code 執行。

## 切換 think mode 的方法 - shift + tab 

在 Claude code 中，你可以使用快捷鍵 shift + tab 來切換 mode。第一次的切換是 auto accept mode，你可以看 terminal 下方的提示，來知道現在的 mode 是哪一種。按第二次 shift + tab 就會進入 think mode。當你啟用 think mode 後，Claude 會進入一種專注於思考和規劃的狀態，這時候 claude code 並不會去更動你的程式碼，而是列出他會進行的步驟，以及如何實作的藍圖 (blueprint)。所以你可以放心的進行各種確認和發散的思考。

### 第一次按 shift + tab - 進入 auto accept mode
![auto accept mode](/assets/programming/claude-code-think-mode/claude-code-accept-mode.png)

### 用 shift + tab 進入 think mode
![claude code think mode](/assets/programming/claude-code-think-mode/claude-code-think-mode.png)

## think mode 的優點

### 先規劃再執行
![think mode request prompt](/assets/programming/claude-code-think-mode/think-mode-request-prompt.png)

當你在 think mode 中向 Claude 提出請求時，Claude 會先分析和思考你的需求，然後提供一個詳細的計劃藍圖。

### 查看實作藍圖
![plan mode blueprint](/assets/programming/claude-code-think-mode/plan-mode-blueprint.png)

在 think mode 中，Claude 會展示完整的實作計劃，讓你可以在實際執行之前就了解整個實作流程。

### 確認後執行
![action after planning](/assets/programming/claude-code-think-mode/action-after-planing.png)

當你確認計劃後，Claude 會根據之前的規劃開始執行實際的程式碼修改。

### 心得
在不知道 think mode 之前的我，是使用 prompt 讓 Claude code 不要直接修改程式碼，而是先給我一個大概的方向和步驟。只是，單純用 prompt 時，有時候 claude code 還是會直接發動修改。而且因為我大多時間是開發 iOS，常常會直接執行到 xcode build or 其他 xcode cli 指令。

在 think mode 下，我覺得修改的上下文品質有提高，而且他在 think mode 提出的方案， UI 有保留 Canvas or artifacts 的概念，可以做到同一份檔案做小幅度的修改，而不會影響到整體的結構和邏輯。

這是我最喜歡的地方，畢竟，要先把事情做對，我才可以開始要求 AI 把事情做好。