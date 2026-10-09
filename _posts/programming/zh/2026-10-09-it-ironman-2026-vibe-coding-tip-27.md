---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜收款：mobile 用 RevenueCat，paywall 在後台換；網頁付費用 Lemon Squeezy - Tip 27"
date: 2026-10-09 13:00 +0800
category: programming
author: Marvin Lin
tags: [IT鐵人賽, 2026鐵人賽, Vibe Coding, Vibe Coding 技巧, RevenueCat, Lemon Squeezy, Mobile]
summary: "mobile 訂閱交給 RevenueCat 管理，paywall 在後台換；網頁付款用 Lemon Squeezy 處理 checkout、訂閱與客戶入口。"
description: "mobile 訂閱交給 RevenueCat 管理，paywall 在後台換；網頁付款用 Lemon Squeezy 處理 checkout、訂閱與客戶入口。"
---

本篇 iT 鐵人賽文章：[前往 iT 閱讀](https://ithelp.ithome.com.tw/articles/10422658)。

app 要收錢，我不自己接商店的 API。mobile 用 RevenueCat，paywall 在它的後台換、不用重新上架；網頁上的付費用 Lemon Squeezy。

## 為什麼

自己接 App Store 和 Google Play 的內購，要處理收據驗證、訂閱狀態，兩個平台各一套；網頁上收錢還多了訂閱管理、發票、稅。這些都有人包好了。

RevenueCat 的 README 說它是「免費可用的內購 server」：一個 SDK 包住 StoreKit 和 Google Play Billing，收據在它的 server 驗，訂閱狀態它幫你追，使用者在 iOS、Android 或網頁訂的都看得到，產品在它的 dashboard 設定。paywall 那一頁也在 dashboard 設，SDK 的 PaywallView 把 offering 上設好的 paywall 畫出來。換版面、換價格組合在後台改，app 不用重新送審。

Lemon Squeezy 負責網頁那一邊：一次性付款、訂閱、試用期、暫停訂閱、發票、客戶自助的 Customer Portal，一個 API 加幾個官方 SDK。

## 我怎麼做

**mobile：RevenueCat**

1. 到 RevenueCat 開專案，把 App Store、Google Play 的 app 接上去
2. 建 product（對應商店裡的內購 ID）、entitlement（像 `premium`）、offering（一組 package，像 Monthly、Annual）
3. app 裝 SDK，開起來用你的 API key 初始化；付費牆用 `PaywallView` 顯示目前的 offering；有沒有解鎖看 entitlement
4. 之後 paywall 要換樣子、換價格組合，在 dashboard 改 offering 和 paywall，app 下次開起來就換了

**網頁：Lemon Squeezy**

1. 開 store，建 product 和 variant（月費、年費）
2. 後端用官方 SDK 建 checkout，把使用者導過去付；付完 webhook 打回來，記下 subscription 的狀態
3. 客戶要改卡、要取消，導去它的 Customer Portal，這一段不用自己做

```bash
npm install @lemonsqueezy/lemonsqueezy.js
```

```ts
import { lemonSqueezySetup, createCheckout } from "@lemonsqueezy/lemonsqueezy.js";

lemonSqueezySetup({ apiKey: process.env.LEMONSQUEEZY_API_KEY });
const { data, error } = await createCheckout(storeId, variantId);
// 付款頁的網址在回來的 checkout 物件裡（attributes.url），把使用者導過去
```

## 坑

- Lemon Squeezy 的 API key 只放後端。README 特別警告：放到瀏覽器裡等於把整個 store 的權限給出去
- 先在 test mode 走完一輪再開 live，兩種 mode 的 key 分開
- RevenueCat 那一端，商店那邊的 Paid Applications Agreement、銀行和稅務資料要先簽完，內購才測得起來

## 小結

mobile 收錢用 RevenueCat，paywall 在後台換；網頁收錢用 Lemon Squeezy。兩邊的商店 API 都不用自己接。

明天講免費的 LLM 額度：Cloudflare、OpenRouter、OpenAI 各給多少。

參考：
- RevenueCat purchases-ios https://github.com/RevenueCat/purchases-ios
- Lemon Squeezy JavaScript SDK https://github.com/lmsqueezy/lemonsqueezy.js
