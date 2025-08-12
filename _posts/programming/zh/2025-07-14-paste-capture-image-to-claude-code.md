---
layout: single
title: 將螢幕的截圖貼上到 Claude 的程式碼編輯器的方法，macOS 適用
date: 2025-07-14 16:20 +0800
category: programming
author: Marvin Lin
tags: [Claude, AI, AI Agent]
summary: 本文將介紹如何在 macOS 上將螢幕截圖貼上到 Claude 的程式碼編輯器中，並提供詳細的步驟說明。
---

現在的我，已大量使用 Claude code 進行開發，Claude code 是個 terminal 型的 AI coding 界面，以文字為主。所以在開發的時候，合作起來的感覺就是，我標記檔案，或是框起某些程式碼，在 VSCode terminal 中的 claude code 會知道我現在想要討論的程碼是哪些，在執行 Calude code 的界面也會標記出來。

## Cmd + ctrl + K - 就可以把另一個檔案框起來的程式碼，傳給 claude code

如圖，在 terminal 的右下方，就會看到 1 line selected

![claude-code-select-lines](/assets/programming/claude-code/claude-code-select-lines.png)

## 那圖案呢？當然也有方法傳給 claude code

在 macOS 上，你可以使用以下方法將螢幕截圖貼上到 Claude 的程式碼編輯器中：

- 按下 ctrl + cmd + shift + 4，然後選擇你想要截圖的區域。
- 截圖完成後，切換到 claude code 的程式碼編輯器。
- 按下 ctrl + v (注意，是 ctrl)，將截圖貼上。

![claude-code-paste-image](/assets/programming/claude-code/claude-code-screen-capture.png)

這時候，你會看到 image 的文字被貼上輸入框，你可以使用這個技巧，讓 claude 針對顏色/排版，進行修改。

## 相關文章

- [Using Plan Mode to Let Claude Code Plan Before Implementation](/programming/en/2025-08-07-think-mode-on-claude-code/) (English)

- [使用計劃模式讓 Claude Code 在實作前先規劃](/programming/zh/2025-08-07-think-mode-on-claude-code/) (Chinese)
