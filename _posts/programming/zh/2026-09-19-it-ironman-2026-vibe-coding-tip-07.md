---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜把 localhost 開給別人測：Cloudflare Tunnel、ngrok 與自己的 domain - Tip 07"
date: 2026-09-19 13:02:35 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - Cloudflare
  - Cloudflare Tunnel
  - ngrok
  - localhost
  - Webhook
  - DNS
summary: "把 localhost 暫時開出去，我會按使用期限選工具：Quick Tunnel 做一次測試、ngrok 給固定 dev domain、Cloudflare Tunnel 綁自己的 domain。"
description: "把 localhost 暫時開出去，我會按使用期限選工具：Quick Tunnel 做一次測試、ngrok 給固定 dev domain、Cloudflare Tunnel 綁自己的 domain。"
---

這一篇改寫自我部落格的《Cloudflare Tunnel：我現在會用它取代 ngrok》，並補上快速 tunnel 與 ngrok 的比較。原始文章：https://www.marvinswift.com/zh/programming/cloudflare-tunnel-vs-ngrok/

本機跑了一個服務，要讓朋友試用、接 webhook 或測 OAuth callback，我會先決定網址要用多久。臨時測一下用快速 tunnel；需要固定網址，就用 ngrok 的 dev domain，或把 Cloudflare Tunnel 綁到自己的 domain。

## 為什麼

這幾種做法都能把外面的 HTTPS 請求帶進 localhost。差別在準備工作，以及下次測試要不要重新填網址。

我已經把 domain 和部署放在 Cloudflare，反覆使用的開發入口也會放在那裡，例如 `dev.example.com`。只想給別人看一次，就先拿一個臨時網址，測完關掉。

## 我怎麼做

先選情境：

| 需要什麼 | 用法 | 準備 |
| --- | --- | --- |
| 現在就拿網址，臨時測一下 | Cloudflare Quick Tunnel | 安裝 cloudflared，不用帳號或 domain |
| 測試網址固定，方便重複填在 webhook 設定裡 | ngrok dev domain | ngrok 帳號、authtoken |
| 用自己的開發網域，放進固定流程 | Cloudflare Tunnel | Cloudflare 帳號、可設定 DNS 的 domain |

**臨時網址：Cloudflare Quick Tunnel。** 本機服務跑在 8080，裝好 cloudflared 後執行：

```bash
cloudflared tunnel --url http://localhost:8080
```

terminal 會印出隨機的 `*.trycloudflare.com` 網址，連進去就是本機的 8080。用完按 Ctrl+C。

**固定 dev domain：ngrok。** 裝好 ngrok，從 dashboard 拿 authtoken 綁帳號，再開服務：

```bash
ngrok config add-authtoken $YOUR_TOKEN
ngrok http 8080
```

免費方案有一個分配給帳號的 dev domain，下次使用可以沿用。兩種快速測試方式的限制放在一起看：

| | Cloudflare Quick Tunnel | ngrok 免費方案 |
| --- | --- | --- |
| 網址 | 隨機的 trycloudflare.com 子網域 | 帳號配發的 dev domain |
| 瀏覽器開啟 | 直接進服務 | HTML 瀏覽器流量會先看到提示頁 |
| 額度 | 最多 200 個進行中的請求，超過回 429 | 每月 1 GB 傳出流量、20,000 個 HTTP 請求，最多 3 個 endpoint 同時在線 |
| 其他限制 | 不支援 SSE，沒有 SLA | 免費方案無法使用自己的 domain |

額度依服務方案而定，使用前看文末官方文件。

**自己的 domain：Cloudflare Tunnel。** 用 dashboard 建立 tunnel，照畫面安裝並執行 cloudflared，再把 published application 的 hostname 指到本機服務即可。要用本機 config 管理，也可以這樣設：

```bash
brew install cloudflared
cloudflared tunnel login
cloudflared tunnel create my-dev
cloudflared tunnel route dns my-dev dev.example.com
```

在 `~/.cloudflared/config.yml` 放入：

```yaml
tunnel: <TUNNEL_ID>
credentials-file: /Users/you/.cloudflared/<TUNNEL_ID>.json

ingress:
  - hostname: dev.example.com
    service: http://localhost:8080
  - service: http_status:404
```

啟動：

```bash
cloudflared tunnel run my-dev
```

之後 `https://dev.example.com` 就會連到本機的 8080。正式服務照 Tip 05 部署，這個網址留給開發測試。

## 坑

- hostname 要與 DNS 設定一致，service 的 port 要指向本機真正在跑的服務，最後一條 404 兜底保留。
- 已經有 `~/.cloudflared/` 的 config 時，Quick Tunnel 可能無法啟動。官方文件提醒先暫時改名；測完恢復，避免影響原本的固定 tunnel。
- Quick Tunnel 給開發測試用，不支援 SSE，也沒有 SLA。
- ngrok 的提示頁針對瀏覽器 HTML 流量；程式請求可依文件帶 `ngrok-skip-browser-warning` header。

## 小結

臨時測試先用 Quick Tunnel；需要固定測試網址，用 ngrok 的 dev domain；開發入口要跟自己的 domain 一起管理，就設 Cloudflare Tunnel。

明天講 iOS 的基本必備：SwiftLint 和 SwiftFormat，基本的要用。

參考：
- Cloudflare Quick Tunnels https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/
- ngrok Share Localhost https://ngrok.com/docs/share-localhost/quickstart/
- ngrok Free Plan Limits https://ngrok.com/docs/pricing-limits/free-plan-limits/

原文：https://www.marvinswift.com/zh/programming/cloudflare-tunnel-vs-ngrok/
