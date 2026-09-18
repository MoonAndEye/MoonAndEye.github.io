---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜買自己的 domain，在 Cloudflare 買：原價、HTTPS 自動、接 Pages 或 Workers 幾分鐘上線 - Tip 06"
date: 2026-09-18 13:03:21 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - Cloudflare
  - Domain
  - DNS
  - HTTPS
  - Cloudflare Registrar
  - Cloudflare Pages
  - Cloudflare Workers
summary: "買自己的 domain 時，我會選 Cloudflare：原價、DNS 和 HTTPS 自動接好，Pages 或 Workers 幾分鐘就能上線。"
description: "買自己的 domain 時，我會選 Cloudflare：原價、DNS 和 HTTPS 自動接好，Pages 或 Workers 幾分鐘就能上線。"
---

這篇是 2026 iT 邦幫忙鐵人賽《Vibe Coding：30 個開發實用技巧》的 Tip 06。

做出來的東西要給人用，先買一個自己的 domain。我推薦在 Cloudflare 買：照 registry 的原價賣、DNS 和 HTTPS 都在同一個地方，接上 Pages 或 Workers 幾分鐘就上線。

## 為什麼

昨天把前端、API 和資料庫要放哪裡排好了，今天把自己的 domain 接上去：

- **原價，沒有加價。** Cloudflare Registrar 只收 registry 和 ICANN 收的那個價，續約也照 registry 的定價，沒有續約漲價那一套。
- **DNS 在同一個地方。** 在 Cloudflare 買的 domain 直接用 Cloudflare 的 nameserver，買完 DNS 就設好了，少一個要登入的地方。
- **HTTPS 自動。** domain 在 Cloudflare 上，Universal SSL 免費、自動簽、自動續，root domain 和第一層子網域都蓋到。憑證這件事從此不用想。
- **WHOIS 資料預設遮掉。** registry 允許的話，個人資料不會被 WHOIS 查到，免費。DNSSEC 一鍵開，也免費。
- **接 Pages、Workers 一個畫面搞定。** 部署好的 Pages 專案或 Worker 加上 custom domain，Cloudflare 自己建 DNS 記錄、自己發憑證。

## 我怎麼做

1. **買**：Cloudflare dashboard 的 Register domains，搜名字、選年數、填聯絡資料、付款。文件寫註冊本身最多三十秒，auto-renew 預設開著。
2. **接 Pages**：Workers & Pages 選你的 Pages 專案，Custom domains，Set up a domain，打 domain 按 Continue。domain 是這個帳號上的 zone，CNAME 會自動建好。
3. **接 Worker**：Worker 的 Settings，Domains & Routes，Add，Custom Domain。或者在 wrangler 設定裡寫：

```jsonc
{
  "routes": [
    { "pattern": "api.example.com", "custom_domain": true }
  ]
}
```

`npx wrangler deploy` 之後 Cloudflare 自己建 DNS、自己發憑證。

前端用 `app.example.com`，API 用 `api.example.com`。開發時要把另一個網址接回 localhost，下一篇再講 Tunnel。

叫他做也行：

```
把 example.com 接到 Pages 專案 my-app，api.example.com 接到 Worker my-api，用 wrangler 設定加 custom domain。
```

## 坑

- 在 Cloudflare Registrar 買的 domain 一定用 Cloudflare 的 nameserver，換不到別家 DNS。想用別家 DNS 的，domain 就去別家買再把 DNS 指過來，Cloudflare 的服務照樣能用。
- Worker 的 Custom Domain 要 hostname 完全一致，`example.com` 和 `www.example.com` 是兩個。要兩個都通，設一條轉址規則。
- Registrar 目前不支援中文這類 IDN 網域。

## 小結

domain 在 Cloudflare 買：原價、DNS 現成、HTTPS 自動、WHOIS 遮掉。接 Pages 或 Workers 幾分鐘上線。

明天講開發時怎麼讓外面連進 localhost：Cloudflare Tunnel 和 ngrok。

參考：
- Cloudflare 文件：Registrar https://developers.cloudflare.com/registrar/
- Cloudflare 文件：Pages custom domains https://developers.cloudflare.com/pages/configuration/custom-domains/
- Cloudflare 文件：Workers Custom Domains https://developers.cloudflare.com/workers/configuration/routing/custom-domains/
- Cloudflare 文件：Universal SSL https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/
