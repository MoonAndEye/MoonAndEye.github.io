---
layout: single
title: Cloudflare Tunnel：我現在會用它取代 ngrok
date: 2026-04-27 21:00 +0800
category: programming
author: Marvin Lin
tags: [Cloudflare, Cloudflare Tunnel, ngrok, Reverse Proxy, AI Agent, Webhook]
summary: 如果你已經在用 Cloudflare 做 domain 和部署，把 localhost 暴露到外網這件事，Cloudflare Tunnel 會比 ngrok 更順手。
---

在做 AI agent coding 的時候，有一件事比想像中還常發生：你需要把 local 跑的服務暴露到外網。

可能是要接 webhook、可能是要讓朋友先試一下你還沒部署的版本、可能是要讓某個第三方服務 callback 進來。

以前我都用 ngrok。它很有名、很方便、`ngrok http 3000` 就跑起來了。

但這幾年我幾乎都改用 Cloudflare Tunnel（`cloudflared`）。

如果你已經跟著我前一篇 [AI Agent Coding - 為什麼我會推薦 Cloudflare]({% post_url /programming/zh/2026-04-23-ai-agent-coding-cloudflare %}) 把 domain 放在 Cloudflare 上，那 Cloudflare Tunnel 幾乎是順理成章的下一步。

## 反向代理是什麼，為什麼你會用到

簡單講：你 local 跑了一個服務在 `localhost:3000`，你希望外面的人可以透過一個公開網址打進來。

中間需要一個東西，把外網的 request 轉到你的 local。這就是反向代理在做的事。

ngrok 和 Cloudflare Tunnel 都是這個角色，差別在背後接的是誰。

ngrok 接的是 ngrok 自己的網域和服務。Cloudflare Tunnel 接的是 Cloudflare 的整張全球網路，還有你自己在 Cloudflare 上的 domain。

## ngrok 的問題

ngrok 真的方便，但用久了會遇到幾個痛點。

免費版每次重開，URL 都會換。你要拿這個 URL 去設定 webhook、貼給朋友、寫進 `.env`，重啟之後又要重來一次。

要綁自己的 domain，要付錢。要讓多個人同時跑 tunnel，要付錢。要保留固定 URL，也要付錢。

而且 ngrok 的免費版有連線數和流量限制。你做 AI agent 相關的 demo，常常會打很多 request，很容易撞到限制。

這些都不是大問題，但會讓你每次都覺得「為什麼我又要處理一次這件事」。

## Cloudflare Tunnel 為什麼順

如果你的 domain 已經在 Cloudflare，`cloudflared` 可以做兩件 ngrok 免費版做不到的事：

**第一，URL 是你自己的 domain。** 你可以指定 `dev.yourdomain.com` 直接打進你的 localhost。這個 URL 重開不會變，webhook 設定一次就好。

**第二，沒有那種「免費版限制」的感覺。** Cloudflare Tunnel 對個人和小型使用基本上是免費的，沒有 ngrok 那種強迫你升級的牆。

設定也不複雜。裝 `cloudflared`，登入一次，建立一個 tunnel，把它指到 `localhost:3000`，最後在 Cloudflare DNS 上加一筆 CNAME。下次你只要 `cloudflared tunnel run` 就會跑起來。

```bash
brew install cloudflared
cloudflared tunnel login
cloudflared tunnel create my-dev
cloudflared tunnel route dns my-dev dev.yourdomain.com
cloudflared tunnel run my-dev
```

跑起來之後，`https://dev.yourdomain.com` 就會直接打到你 local 的 service，HTTPS 也已經幫你處理好了。

## 對 AI agent coding 的差別

當你在跑 AI agent 開發的流程，你常常需要快速驗證某個外部 callback、某個 webhook、某個第三方 API 的串接。

如果你的 tunnel URL 一直在換，AI agent 幫你寫的設定就要一直改。`.env` 改、webhook 後台改、測試 script 改。

如果你的 tunnel URL 固定是 `dev.yourdomain.com`，這些設定寫一次就成立。AI agent 也不用每次重新理解現在的 URL 是什麼。

整個 dev loop 會比較安靜，你可以專心在功能本身上。

## 什麼時候我還是會用 ngrok

如果只是要快速 demo 一次、或是你完全沒有 Cloudflare 帳號，ngrok 還是最快的選擇。打一個指令就有 URL，這件事 Cloudflare Tunnel 沒辦法贏。

但只要你會做超過一次的事情，或者你已經有 Cloudflare 上的 domain，我會直接推薦 Cloudflare Tunnel。

---

下一篇，我想寫 Cloudflare Workers AI。它可以讓你在同一個平台上跑 AI 推論，搭配 Tunnel 和 Workers，整個 AI side project 的部署成本會低到很有趣。
