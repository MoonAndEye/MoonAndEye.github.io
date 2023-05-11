---
layout: single
title: Alerts 出現選項時，主要動作要放哪一邊？左？右？(Apple 的 OS 請放右邊(也就是最後面))
date: 2023-05-10 13:13 +0800
category: swift
author: Marvin Lin
tags: [Swift, iOS, UI]
summary: When you design an alert, ok/cancel button should put ok on right? or left? Each platform has there guideline on this design, please follow the documents. If you are developing iOS or Android Apps, you should put your primary action button on trail (right).
permalink: /swift/:title:output_ext
---

Alerts 出現選項時，主要動作要放哪一邊？左？右？
Alerts 是一種常見的用戶反饋機制，它可以提醒用戶發生了什麼事情，或者需要用戶做出一些決定。Alerts 通常會有一個或多個選項按鈕，讓用戶可以選擇接受、取消、確認、忽略等不同的動作。那麼，這些選項按鈕應該放在 Alerts 的哪一邊呢？左邊還是右邊？

![left or right](/assets/swift/left-or-right/left_right.jpeg)

## 如果這個平台有設計的文件，請先看文件

### Apple 的設計規範: 主要動作放在右邊(也就是最後面)

**主要動作放在右邊(也就是最後面)**

主要動作放在右邊(也就是最後面)

這邊是 [Apple 的設計文件](https://developer.apple.com/design/human-interface-guidelines/alerts)，在文件中有提到 buttons 的位置。

![Apple demo icon](/assets/swift/left-or-right/apple-demo.jpeg)

> Place buttons where people expect. In general, place the button people are most likely to choose on the trailing side in a row of buttons or at the top in a stack of buttons. Always place the default button on the trailing side of a row or at the top of a stack. Cancel buttons are typically on the leading side of a row or at the bottom of a stack.

在 Apple 的文件中提到，應將按鈕放置在使用者預期的位置上。一般而言，在按鈕行中或按鈕堆疊的頂部，應將使用者最有可能選擇的按鈕放置在末尾位置。同樣地，預設按鈕應放置在按鈕行的末尾或按鈕堆疊的頂部。取消按鈕通常位於按鈕行的開始位置或按鈕堆疊的底部。如果你去看每一個 Apple 預設的 Apps，像是「設定」「天氣」等，都是符合這設計文件的。

### 為什麼 Apple 把主要動作按鈕放在最後面

根據 [Nielsen Norman Group 的文章](https://www.nngroup.com/articles/ok-cancel-or-cancel-ok/) 的文章，將主要動作放在最後一個位置可以使對話框的流程更加順暢，因為它以一個結論作為結束。同樣地，你可以認為主要動作是使用者繼續前進的選項，而取消則是讓使用者返回的選項。因此，把主要動作放在與下一步相同的位置上，也就是靠右邊。這樣做可以使使用者在操作上更加直觀和自然。

## 其他關於 Alert 要注意的事情

> Create succinct, logical button titles. Aim for a one- or two-word title that describes the result of selecting the button. Prefer verbs and verb phrases that relate directly to the alert text — for example, “View All,” “Reply,” or “Ignore.” In informational alerts only, you can use “OK” for acceptance, avoiding “Yes” and “No.” Always use “Cancel” to title a button that cancels the alert’s action. As with all button titles, use title-style capitalization and no ending punctuation.

> Avoid using OK as the default button title unless the alert is purely informational. The meaning of “OK” can be unclear even in alerts that ask people to confirm that they want to do something. For example, does “OK” mean “OK, I want to complete the action” or “OK, I now understand the negative results my action would have caused”? A specific button title like “Erase,” “Convert,” “Clear,” or “Delete” helps people understand the action they’re taking.

請選擇簡潔且容易理解的按鈕標題。盡量使用一個或兩個詞來描述按鈕的選擇結果。優先使用與警示內容直接相關的動詞或動詞片語，比如「查看全部」、「回覆」或「忽略」。在信息提示中，可以使用「確定」表示接受，而不要使用「是」或「否」。取消操作的按鈕應該總是標為「取消」。按照一般的標題風格，使用首字母大寫而不要加上結尾標點符號。

除非警示純粹是提供信息的，否則不要將「確定」設為預設按鈕標題。在一些警示中，「確定」的含義可能不太清楚，即使在要求用戶確認是否執行某項操作時也是如此。例如，「確定」可能被理解為「好的，我想要執行這個操作」或「好的，我明白這個操作可能帶來的負面結果」。為了幫助使用者理解他們將要執行的操作，請使用具體的按鈕標題，比如「刪除」、「轉換」、「清除」或「刪除」。

## 同場加映 Android 的 dialog 的規範

[Android 的 dialog](https://m3.material.io/components/dialogs/specs)

![Android dialog pic](/assets/swift/left-or-right/dialog.jpeg)

在 Android 的 material design 中，dialog 的 primary action 也是放在右邊。

## 參考網址

[Apple 文件中關於 Alerts 的部分](https://developer.apple.com/design/human-interface-guidelines/alerts)

[Google 對於 Dialog 的文件](https://m3.material.io/components/dialogs/specs)

[Nielsen Norman Group 的文章](https://www.nngroup.com/articles/ok-cancel-or-cancel-ok/)