---
layout: single
title: "Agent Build Log — Episode 012"
date: 2026-07-26 00:18:18 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-012.png
summary: "以 counterbalanced evals 比較 Terra 與 Luna：兩者正確率相同，但 Terra 稍快、tool calls 較少，也更常漏掉要求的 DKS protocol。"
description: "以 counterbalanced evals 比較 Terra 與 Luna：兩者正確率相同，但 Terra 稍快、tool calls 較少，也更常漏掉要求的 DKS protocol。"
---

今天我原本以為，自己找到了一個更有效率的預設模型。

![Agent Build Log Episode 012：比較 Terra 與 Luna](/assets/programming/agent-build-log/agent-build-log-episode-012.png)

在相同的 evals 和相同 effort 下，Terra 的總耗時比 Luna 少，tool calls 也比較少。

第一眼看到這個結果時，我的直覺是：Terra 可能走了一條比較短的路。

例如 Luna 可能會先查 A、看完結果再查 B，接著回頭確認 A，最後再打開另一個檔案。

而 Terra 可能先判斷自己需要 A、B、C，接著一次查完，再直接回答。

不過這只是一個可能的解釋，我目前沒有足夠的證據可以證明 Terra 真的採用了比較短的路徑。

我也擔心執行順序會影響結果。

假如 Terra 總是第二個跑，它有沒有可能吃到前一次留下來的 file cache？

所以後來我把測試改成 counterbalanced 的方式。每一道題目都跑一次 Terra → Luna，再跑一次 Luna → Terra。

結果顯示，Terra 整體上還是稍微快一點，但目前還不能直接下結論說 Terra 本質上一定比 Luna 快。

執行順序的結果，也沒有證明第二個執行的模型會穩定得到 cache 帶來的加速。

![Terra 與 Luna 的 counterbalanced confirmatory study 結果](/assets/programming/agent-build-log/agent-build-log-episode-012-luna-vs-terra.png)

真正讓我重新思考的，是 DKS protocol 的資料。

Terra 的 tool calls 是 N 次。

Luna 的 tool calls 大約是 N + 10 次。

這代表 Terra 的 tool calls 比較少，未必只是因為它比較有效率。

它可能真的找到了一條比較短的路，也可能只是有幾次跳過了原本應該完成的步驟。目前這份資料還不能把這兩種情況完全分開。

更有意思的是，兩個模型最後的正確率雖然一樣，但失敗的方式不一樣。

Terra 比較常沒有走完要求的 DKS protocol；Luna 幾乎都有呼叫 DKS，卻更常在最後答案上出錯。

所以這次測到的並不是單純的「哪個模型比較好」，而是兩個模型用不同的方式，拿到了相同的分數。

Terra 目前看起來，仍然可能是一個不錯的預設選擇。

Terra 看起來走得比較快，但我還不能確定它是真的找到了捷徑，還是只是少做了幾步。

在決定預設模型之前，我得先確保「更有效率」不是「更容易跳過規則」。
