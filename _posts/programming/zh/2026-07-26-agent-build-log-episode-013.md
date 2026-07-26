---
layout: single
title: "Agent Build Log — Episode 013"
date: 2026-07-26 23:35:39 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-013.png
summary: "以 medium 與 xhigh 比較 Sol、Terra、Luna：範圍明確的 DKS lookup 任務優先使用 Terra xhigh；嚴格流程完整性優先選 Sol。"
description: "以 medium 與 xhigh 比較 Sol、Terra、Luna：範圍明確的 DKS lookup 任務優先使用 Terra xhigh；嚴格流程完整性優先選 Sol。"
---

今天，我把 GPT-5.6 Sol 也加入了模型比較。

![Agent Build Log Episode 013：比較 Sol、Terra 與 Luna 的模型 routing](/assets/programming/agent-build-log/agent-build-log-episode-013.png)

之前我只測 Terra 和 Luna。

在 Episode 012 裡，Terra 看起來很適合當預設模型，因為它比較快。但我一直沒有辦法回答一個問題：

它是真的找到了更好的路徑，還是只是跳過了一些應該完成的步驟？

所以這一次，我使用同一組 DKS eval，同時比較 Sol、Terra 和 Luna，並且分別測試 medium 和 xhigh 兩種 effort level。

這次真正改變我看法的，不只是 Terra 的速度，而是它在 xhigh effort 下的表現。

在 medium effort 下，Terra 的確很快，但它有 6 次沒有呼叫必要的 DKS tool，最後正式通過 20/29。

到了 xhigh effort，Terra 只漏掉 1 次必要的 DKS call，正式通過率也提升到 26/29。

這個結果剛好接住了我在 Episode 012 留下的疑問。

Terra 的速度不一定只是來自跳過步驟。至少在提高 effort 之後，它大幅補上了流程完整性的問題，同時仍然保留速度優勢。

在 xhigh effort 下，Terra 和 Sol 都正式通過了 26/29。

但 Sol 平均每題大約需要 29.1 秒，Terra 則大約是 21.2 秒。

Terra 不再只是「比較快，但要接受品質取捨」的選項。至少在這類範圍明確、工具固定的 DKS lookup 任務裡，Terra xhigh 可以同時做到夠快，也夠可靠。

Luna 也不一定比較快。

在這次測試中，不論 medium 還是 xhigh effort，Terra 的平均完成時間都比 Luna 短。

所以單靠速度，已經不是我會優先選 Luna 而不是 Terra 的理由。

Sol 的優勢則在另一個地方。

不論 medium 還是 xhigh effort，Sol 都完整執行了所有必要的 DKS protocol。

所以當流程完整性比速度更重要時，我仍然會優先考慮 Sol。

![Sol、Terra 與 Luna 在 medium、xhigh effort 下的 benchmark 結果](/assets/programming/agent-build-log/agent-build-log-episode-013-benchmark-report.png)

對於範圍清楚、知道該使用哪個工具，也知道該怎麼驗證結果的任務，我目前會先使用 Terra xhigh。

當任務更重視嚴格流程，或我願意用更多時間換取穩定性時，我會選 Sol。

至於 Luna，它依然有自己的使用場景，但至少在這一輪裡，速度已經不是它相對於 Terra 的優勢。

不過，這次六個設定是按照固定順序執行的，還不是完全平衡的實驗。

所以我會把這些結果當成目前的 routing signal，而不是最後的定論。

這次比較沒有給我一個可以用在所有事情上的模型。

它給了我一個更好的模型路由規則。
