---
layout: single
title: "Agent Build Log — Episode 024"
date: 2026-08-08 21:32:38 +0800
category: programming
author: Marvin Lin
tags: [agent]
image: /assets/programming/agent-build-log/agent-build-log-episode-024.png
summary: "模型單次回應速度不等於 Agent 完成整個任務的速度，真正重要的是完成任務需要多少步。"
description: "模型單次回應速度不等於 Agent 完成整個任務的速度，真正重要的是完成任務需要多少步。"
---

今天，我遇到一個和原本直覺完全相反的結果。

![Agent Build Log Episode 024：比較 Sol、Terra 和 Luna 完成 Agent 任務的時間](/assets/programming/agent-build-log/agent-build-log-episode-024.png)

如果只看 LLM 本身，我原本會認為：

參數量比較大的模型，回應通常會比較慢。

參數量比較小的模型，回應通常會比較快。

所以如果只是回答一個問題，我原本預期速度大概會是：

Luna 最快，Terra 居中，Sol 最慢。

換成 Agent 任務，我原本也有一樣的假設。

我以為完成整個任務的時間，應該也是 Luna 最快，接著 Terra，最後才是 Sol。

但今天實際跑同一個任務時，結果完全不是這樣。

這個任務主要是拿來 tune tool calls 和最後的輸出。

三個模型使用同一套 Agent、同一組 tools，也做同一件事。

結果大概是：

Sol：5 分鐘左右。

Terra：8 分鐘左右。

Luna：14 分鐘左右。

Luna 完成這個任務的時間，接近 Sol 的三倍。

更重要的是，Luna 最後還沒有把任務做好。

反而是 Sol 和 Terra，都有把事情正確完成。

這讓我重新理解一件事：

模型本身的單次回應速度，不能直接推論 Agent 完成整個任務的速度。

Agent 的總時間，不只取決於每一次 inference 有多快。

它還取決於模型怎麼規劃、呼叫多少次 tools、會不會重複確認、會不會走錯路，以及能不能在比較少的步驟裡把任務完成。

一個單次回應比較快的模型，如果需要更多輪 tool calls，或是在過程中走了更多不必要的路，最後反而可能花更久。

這次的結果也讓模型選擇變得更有意思。

如果只看成本，我可以選 Terra。

它可以把事情做對，而且比 Sol 便宜一些。

但它花的時間比較久。

Sol 則是在這個任務上最快完成，而且結果也是正確的，只是成本會再高一點。

以前我比較容易把模型選擇想成：

更大的模型 = 更慢、更貴。

更小的模型 = 更快、更便宜。

但在 Agent 裡，真正重要的可能不是單次 inference 的速度。

而是：

這個模型到底需要多少步，才能把事情做完。

對我現在正在做的客製化 Agent 來說，這是一個很重要的發現。

因為之後選模型時，我不能只看 token price 或 response latency。

我還要看整個任務的 completion time。
