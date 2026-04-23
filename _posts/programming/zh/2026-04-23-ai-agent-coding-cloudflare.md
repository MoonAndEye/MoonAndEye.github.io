---
layout: single
title: AI Agent Coding - 為什麼我會推薦 Cloudflare
date: 2026-04-23 21:00 +0800
category: programming
author: Marvin Lin
tags: [AI, AI Agent, Cloudflare, Workers, Pages, D1, KV, Deployment]
summary: 如果要讓 AI agent coding 不只停在 demo，我會把 Cloudflare 當作最推薦的部署底座：domain、Pages、Workers、D1、KV 都在同一個平台。
---

這個時代 (2026)，要快速的做出一款 app 應用，你有很多工具可以用， claude 系列， codex 系列，現在 github 也有很多直接在網頁上就可以寫程式的服務，未來只會愈來愈多。

但如果真的想要讓別人可以試試看寫出來的產品，你還是要找個地方部署。

你可以先決定你的 tech stack，然後再去找哪些 免費 or 成本低的地方，可以讓你部署 app。

但我更建議你，從「哪裡部署成本最低」開始想。

## 先想部署，才不會只停在 Demo

一開始使用 AI agent coding 時，大家通常會專注在「它能不能幫我寫程式」。

但當你真的開始做產品，你很快會遇到另一個問題：寫出來的東西要放在哪裡，才可以被別人打開、試用，甚至真的開始運作。

這時候你要處理的就不只是程式碼，而是一整條產品上線的路徑：domain、前端部署、API、資料庫、快取，還有這些設定要怎麼維護。

所以我非常推薦 Cloudflare。

它可以把一個小型產品需要的基礎設施放在同一個平台裡：買 domain、管理 DNS、部署靜態網站、建立 API、存資料、做快取。對 AI agent coding 來說，這代表整個產品的部署邊界很清楚。

你不用一開始就規劃很複雜的 cloud architecture，也不用先決定要維護哪一種 server。你可以先把產品做出來，然後用 Cloudflare 的服務把它推出去。

這就是 Cloudflare 很適合 AI agent coding 的原因：它讓「寫出程式」到「真的上線」中間的距離變短。

## Domain：先從網域開始

一個產品如果要被使用，第一步就是要有 domain。

Cloudflare Registrar 可以直接購買和管理網域，而且網域買完後，DNS 本來就在 Cloudflare 裡面。這件事看起來很小，但在 AI agent coding 的工作流裡很重要。

因為 domain、DNS、部署驗證、HTTPS 這些事情，本來就是產品上線時會連在一起處理的事情。如果它們都在 Cloudflare 裡，整個流程會比較直覺，也比較不容易在設定時分散掉。

當 domain 和部署環境在同一個平台，整個 mental model 會簡單很多。

## Pages：靜態網站和前端部署

如果你的產品一開始只是 landing page、文件站、blog、前端 app，Cloudflare Pages 就很適合。

它可以從 Git repo 部署，也可以上傳 build 好的靜態檔案。對 AI agent coding 來說，這代表一件事：

**AI 可以把前端專案、build 指令、部署設定放在同一個 repo 裡理解。**

這會比「程式碼在 repo，部署設定在另一個平台的 UI 裡」更容易維護。

尤其是現在很多 AI agent 都會讀 `package.json`、framework config、README、部署設定。如果你把這些規則寫清楚，agent 比較容易幫你修 build error，也比較容易幫你調整部署流程。

## Workers、D1、KV：後端能力先夠用就好

很多產品一開始不需要很重的後端。你可能只是需要一個 API、webhook、第三方服務的 proxy，或是一點點排程工作。這時候 Cloudflare Workers 就很適合，因為你不用先開一台 server，也不用先處理 server 維護問題。

只要產品開始有資料，就可以接 D1。D1 是 Cloudflare 的 serverless SQL database，語法接近 SQLite，對 AI agent 來說也很容易理解。資料如果是 users、posts、orders、settings 這種結構，用 SQL 先定下來就很直覺。

KV 則適合放快取、feature flags、user preference、routing config 這種 key-value 型態的資料。資料如果需要查詢和關聯，就放 D1；資料如果只是用 key 拿 value，就放 KV。

所以 Cloudflare 對 AI agent coding 最大的價值，是它把小產品常用的幾個部分接在一起：Pages 放前端，Workers 做後端，D1 存資料，KV 做快取。這樣 AI agent 在理解專案時，會看到一個比較清楚的產品邊界。

AI agent coding 的下一步，不只是讓 AI 幫你把程式寫出來，而是讓寫出來的東西可以真的上線。以這個方向來看，Cloudflare 是我現在會優先推薦的部署底座。

而且 Cloudflare 還有一個很適合 AI agent coding 時代的功能：Workers AI。

如果你想做 AI feature，不一定要一開始就自己接一堆模型供應商、處理 API key、處理部署和後端串接。你可以先用 Cloudflare 的 AI worker 能力，在同一個平台上快速測試你的想法。

更重要的是，它有一定的免費額度，對 side project、MVP、或只是想驗證某個 AI 功能的人來說，這個起步成本很低。

下一篇，我會寫 Cloudflare 的 AI worker 功能。這個功能可以讓你快速，而且用相對低的成本，去測試你想做的 AI feature。
