---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜用 Cloudflare 快速建原型：domain、前端、後端、資料庫都在同一個平台 - Tip 05"
date: 2026-09-17 13:00:33 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - Cloudflare
  - Cloudflare Pages
  - Cloudflare Workers
  - D1
  - KV
  - Workers AI
  - Deployment
summary: "我做原型時，會先想部署：用 Cloudflare 把 domain、前端、API、資料與快取放在同一個平台。"
description: "我做原型時，會先想部署：用 Cloudflare 把 domain、前端、API、資料與快取放在同一個平台。"
---

本文同步刊登於 [iT 邦幫忙](https://ithelp.ithome.com.tw/articles/10412468)。

這一篇改寫自我部落格的《AI Agent Coding - 為什麼我會推薦 Cloudflare》，照這個系列的格式重寫過。原始文章：https://www.marvinswift.com/zh/programming/ai-agent-coding-cloudflare/

要快速做出一個原型，前端加後端，我會從「哪裡部署成本最低」開始想。我的答案是 Cloudflare：domain、前端、API、資料庫、快取都放在同一個平台。

## 為什麼

這個時代要快速做出一款 app，工具很多：Claude 系列、Codex 系列，GitHub 上也有直接在網頁裡寫程式的服務，未來只會更多。

但真的想讓別人試試看寫出來的東西，還是要找個地方部署。

一開始用 coding agent 的時候，大家通常專注在「他能不能幫我寫程式」。真的開始做產品，很快會遇到另一個問題：寫出來的東西要放在哪裡，才可以被別人打開、試用，甚至真的開始運作。這時候要處理的是一整條產品上線的路徑：domain、前端部署、API、資料庫、快取，還有這些設定要怎麼維護。

很多人會先決定 tech stack，再去找免費或成本低的地方部署。我建議反過來，先想部署，才不會只停在 demo。

Cloudflare 可以把一個小型產品需要的基礎設施放在同一個平台裡：買 domain、管理 DNS、部署靜態網站、建立 API、存資料、做快取。對 coding agent 來說，這代表整個產品的部署邊界很清楚。我不用一開始就規劃很複雜的 cloud architecture，也不用先決定要維護哪一種 server。先把產品做出來，再用 Cloudflare 的服務推出去。「寫出程式」到「真的上線」中間的距離，因此變短。

## 我怎麼做

一個小產品常用的幾塊，各放哪裡：

| 要放的東西 | Cloudflare 上用什麼 |
| --- | --- |
| domain、DNS | Registrar |
| landing page、文件站、blog、前端 app | Pages |
| API、webhook、第三方服務的 proxy、排程工作 | Workers |
| users、posts、orders、settings 這種有結構的資料 | D1 |
| 快取、feature flags、user preference、routing config | KV |
| 想試的 AI feature | Workers AI |

**Domain 先買。** 一個產品要有自己的入口，domain 和 DNS 也放在 Cloudflare。購買與接上 Pages、Workers 的操作，下一篇再講。

**前端放 Pages。** 產品一開始只是 landing page、文件站、blog、前端 app 的話，Pages 就很適合。它可以從 Git repo 部署，也可以上傳 build 好的靜態檔案。對 coding agent 的好處是：前端專案、build 指令、部署設定都在同一個 repo 裡，他一起讀得到。他本來就會讀 `package.json`、framework config、README、部署設定，這些規則寫清楚，他比較容易幫我修 build error，也比較容易幫我調部署流程。這也是 Tip 02 把東西都放同一個 repo 的延伸：部署設定也一起放進來。程式碼在 repo、部署設定在另一個平台的 UI 裡，那種擺法比較難維護。

**後端先夠用就好。** 很多產品一開始要的只是一個 API、一個 webhook、第三方服務的 proxy，或一點點排程工作。Workers 很適合，我不用先開一台 server，也不用處理 server 維護。產品開始有資料就接 D1，它是 Cloudflare 的 serverless SQL database，語法接近 SQLite，他也很容易理解；資料是 users、posts、orders、settings 這種結構，用 SQL 先定下來很直覺。KV 放快取、feature flags、user preference、routing config 這種 key-value 的東西。分法很簡單：資料需要查詢和關聯，放 D1；只是用 key 拿 value，放 KV。

**想做 AI feature，先用 Workers AI。** 一開始就自己接一堆模型供應商、處理 API key、處理部署和後端串接，可以先不用。Workers AI 讓我在同一個平台上快速測想法，而且有一定的免費額度，side project、MVP、只是想驗證某個功能，起步成本很低。

一句話：**Pages 放前端，Workers 做後端，D1 存資料，KV 做快取。** 他在理解專案時，會看到一個比較清楚的產品邊界。

## 小結

Vibe Coding 的下一步，除了讓他把程式寫出來，還要讓寫出來的東西真的上線。以這個方向看，Cloudflare 是我現在會優先推薦的部署底座。

明天把自己的 domain 接上 Pages 或 Workers。

原文：https://www.marvinswift.com/zh/programming/ai-agent-coding-cloudflare/
