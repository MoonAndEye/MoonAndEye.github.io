---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜截圖直接貼進 Claude Code：畫面上的問題用圖講 - Tip 16"
date: 2026-09-28 13:12 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - Claude Code
  - macOS
  - 截圖
summary: "我整理了 macOS 把截圖貼進 Claude Code 的方式，也對照 terminal、iTerm2 與 VS Code 擴充套件在貼圖和行號參照上的差異。"
description: "我整理了 macOS 把截圖貼進 Claude Code 的方式，也對照 terminal、iTerm2 與 VS Code 擴充套件在貼圖和行號參照上的差異。"
---

本文同步刊登於 [iT 鐵人賽第二系列](https://ithelp.ithome.com.tw/articles/10418244)。

這一篇改寫自我部落格的《將螢幕的截圖貼上到 Claude 的程式碼編輯器的方法，macOS 適用》，照這個系列的格式重寫過。原始文章：https://www.marvinswift.com/zh/programming/paste-capture-image-to-claude-code/

顏色、排版這種畫面上的問題，用字很難講清楚。截一張圖，直接貼進 Claude Code。

## 為什麼

Claude Code 是 terminal 型的介面，以文字為主。合作起來的感覺是：我標記檔案，或者框起某幾行程式碼，VS Code terminal 裡的 Claude Code 就知道我現在要討論的是哪一段，他的介面上也會標出來。畫面上的東西也一樣可以給他，只是要知道怎麼貼。

## 我怎麼做

**框起來的程式碼傳給他：** 在 VS Code 裡選好那幾行，按 cmd + ctrl + K，terminal 右下方會看到「1 line selected」這類字樣，他就收到了。

**截圖貼給他（macOS）：**

1. 按 ctrl + cmd + shift + 4，框選要截的區域
2. 切到 Claude Code 的輸入框
3. 按 ctrl + v 貼上。注意是 ctrl，跟平常貼文字的 cmd + v 不一樣

輸入框會出現一個 image 的字樣，圖就進去了。接著就能請他針對顏色、排版改。

## 坑

快捷鍵會隨版本變。上面是 2025 年 7 月的做法，2026 年 9 月再對一次 Claude Code 的文件：

- terminal 裡貼圖還是 ctrl + v（iTerm2 是 cmd + v）。貼進去之後輸入框會出現 `[Image #1]` 這種標記，prompt 裡可以直接指它。把圖檔拖進視窗也行
- VS Code 裝了 Claude Code 的擴充套件之後，選起來的那幾行會自動附給他，輸入框底下會顯示選了幾行。要在 prompt 裡指到那幾行，按 option + K 會插一個帶檔名和行號的參照，像 `@app.ts#5-10`
- 在擴充套件自己的面板裡貼圖，就是平常的貼上

哪一個版本是哪一套，以你手上 Claude Code 的說明為準。

## 小結

畫面的問題用圖講：ctrl + cmd + shift + 4 截圖，到 Claude Code 按 ctrl + v。

明天換到 Codex CLI：給他一個長線目標，用 /goal。

原文：https://www.marvinswift.com/zh/programming/paste-capture-image-to-claude-code/
