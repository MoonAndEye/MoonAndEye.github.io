---
layout: single
title: Cloudflare Tunnel：我現在會用它取代 ngrok
date: 2026-04-27 10:00 +0800
category: programming
author: Marvin Lin
tags: [Cloudflare, Cloudflare Tunnel, ngrok, Webhook, AI Agent]
summary: 如果 domain 已經放在 Cloudflare，當你需要把 localhost 穩定暴露到外網時，Cloudflare Tunnel 會比 ngrok 更像開發流程的一部分。
---

AI agent coding 讓你很快把功能做出來，但進到整合測試時，會遇到一個很實際的問題：外部服務要怎麼打進你的 local 環境。

可能是要接 webhook、可能是要讓朋友先試一下還沒部署的版本、也可能是要讓某個第三方服務 callback 回你的開發環境。

以前我都用 ngrok。它很有名，也真的很方便。`ngrok http 3000` 打下去，就會給你一個可以從外面連進來的 URL。

ngrok 到現在也還是很適合臨時測試。

只是如果這件事不是只做一次，我現在會比較常改用 Cloudflare Tunnel（`cloudflared`）。

原因不是 ngrok 不好，而是我現在會把 domain、Pages、Workers 這些東西都放在 Cloudflare 上。既然正式部署的入口在 Cloudflare，開發時用的入口也放在 Cloudflare，整個流程會更直覺。

如果你已經跟著我前一篇 [AI Agent Coding - 為什麼我會推薦 Cloudflare]({% post_url /programming/zh/2026-04-23-ai-agent-coding-cloudflare %}) 把 domain 放在 Cloudflare 上，那 Cloudflare Tunnel 幾乎是下一個自然會用到的工具。

## 優點是把 domain、部署和開發入口放在一起

ngrok 和 Cloudflare Tunnel 解決的是同一類問題：你 local 跑了一個服務在 `localhost:3000`，但外部服務需要一個公開的 HTTPS URL 才能打進來。

這件事 ngrok 可以，Cloudflare Tunnel 也可以。

我會選 Cloudflare Tunnel，是因為它可以直接接在我原本的 Cloudflare 流程裡。

domain 在 Cloudflare，前端可能用 Pages，後端可能用 Workers。現在連 local dev 的公開入口也可以用 `dev.example.com` 放在同一個地方管理。

這樣開發和部署就會比較像同一條路，而不是程式碼一套、正式部署一套、臨時測試網址又是另一套。

## ngrok 適合臨時測試，Cloudflare Tunnel 適合放進流程

ngrok 最大的優點就是快。

你不用先買 domain，不用先設定 DNS，也不用管 Cloudflare。只要本機服務跑在 `3000`，打一行指令就可以拿到公開網址。

如果只是 demo 一次，或是臨時讓朋友看一下，ngrok 很適合。

但如果這個開發入口會反覆出現，我會希望它跟自己的 domain 綁在一起。

例如 `dev.example.com` 打到 local service，`app.example.com` 是正式環境，`api.example.com` 是 Workers API。這些入口都在 Cloudflare 底下，DNS、HTTPS、routing 的設定都在同一個地方。

這就是我覺得 Cloudflare Tunnel 順的地方。它不是多一個臨時工具，而是把 local dev 也接進同一套產品基礎設施。

## 設定不難，但要把 localhost 指清楚

如果你用 Cloudflare dashboard 建 tunnel，流程大概是：建立 tunnel、安裝並執行 Cloudflare 給你的 `cloudflared` command，然後新增一個 published application，把 `dev.example.com` 指到 `http://localhost:3000`。

如果用本機 config 管理，概念會像這樣：

```bash
brew install cloudflared
cloudflared tunnel login
cloudflared tunnel create my-dev
cloudflared tunnel route dns my-dev dev.example.com
```

接著在 `~/.cloudflared/config.yml` 裡把 hostname 和 local service 接起來：

```yaml
tunnel: <TUNNEL_ID>
credentials-file: /Users/you/.cloudflared/<TUNNEL_ID>.json

ingress:
  - hostname: dev.example.com
    service: http://localhost:3000
  - service: http_status:404
```

最後跑起 tunnel：

```bash
cloudflared tunnel run my-dev
```

之後 `https://dev.example.com` 就會打到你本機的 service，HTTPS 也會由 Cloudflare 處理。

## 對 AI agent coding 的差別

AI agent coding 會讓你更快做出可以測的東西。

以前可能要花幾天才會碰到 webhook、OAuth callback、第三方服務串接。現在 AI agent 幫你把功能先做出來，你很快就會需要一個可以從外面打進 local 的入口。

這時候 Cloudflare Tunnel 的價值，不是讓 AI 比較懂你的 context，而是讓你的開發、測試、部署路徑更一致。

你可以很自然地把 `https://dev.example.com` 當成開發入口，把 `https://app.example.com` 當成正式入口。兩者都在同一個 domain 和同一個 Cloudflare 帳號底下。

這樣做的好處是，你在測 webhook、測 callback、給別人試用時，不需要額外切到另一個服務去想公開 URL 的事情。

開發入口也是產品架構的一部分。當它跟 domain、Pages、Workers 放在一起，整個 side project 的路徑會比較清楚。

下一篇，我想寫 Cloudflare Workers AI。它可以讓你在同一個平台上測 AI 推論，搭配 Tunnel、Pages 和 Workers，整個 AI side project 的開發到部署路徑會變得更短。
