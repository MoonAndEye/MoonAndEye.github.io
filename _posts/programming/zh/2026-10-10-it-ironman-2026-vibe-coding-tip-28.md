---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜免費的 LLM 額度：Cloudflare Workers AI 每天 10,000 Neurons、OpenRouter 免費模型每天 50 次，規則列出來 - Tip 28"
date: 2026-10-10 13:00 +0800
category: programming
author: Marvin Lin
tags: [IT鐵人賽, 2026鐵人賽, Vibe Coding, Vibe Coding 技巧, LLM, OpenAI, Cloudflare, OpenRouter]
summary: "Cloudflare Workers AI、OpenRouter 與符合資格 OpenAI API 組織的免費額度、重置時間、超額規則與資料分享條件。"
description: "Cloudflare Workers AI、OpenRouter 與符合資格 OpenAI API 組織的免費額度、重置時間、超額規則與資料分享條件。"
---

原型階段先別付錢給模型。Cloudflare、OpenRouter 都有免費額度，OpenAI 也有一部分。這一篇把額度和規則列出來。

## 為什麼

做原型的時候呼叫量很小，免費額度夠用。重點是知道天花板在哪、撞到的時候看得懂錯誤，再決定要付錢給誰。

## 我怎麼做

**Cloudflare Workers AI**（照它的 pricing 和 limits 頁）

- 免費額度：每天 10,000 Neurons，Free 和 Paid 方案都有。每天 00:00 UTC 重置，超過就回錯誤；Free 方案要用更多得升級 Workers Paid，超過的部分 $0.011 / 1,000 Neurons
- Neuron 是它算 GPU 用量的單位。拿 `@cf/meta/llama-3.1-8b-instruct-fp8-fast` 換算：每百萬 output token 約 34,868 Neurons，10,000 Neurons 一天大約能吐 28 萬個 output token
- 文字生成的 rate limit 是每分鐘 300 次
- 有幾顆大模型（像 kimi、glm 那幾顆）要先有付費方式才能叫

**OpenRouter**（照它的 Limits 頁和 FAQ）

- 模型 ID 後面加 `:free` 就是免費版；或者 model 填 `openrouter/free`，它從當下可用的免費模型裡隨機挑一顆
- 規則：免費模型每分鐘 20 次、每天 50 次。帳號一生中買過至少 10 美元的 credits，每天變 1,000 次
- 超過回 429；帳號餘額是負的，免費模型也會回 402
- 新帳號有一小筆免費 allowance 試用。文件自己說免費模型通常不適合 production

```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "openrouter/free", "messages": [{"role": "user", "content": "Hello!"}]}'
```

**OpenAI**

OpenAI 的 API 免費額度不是所有帳號都有。符合資格的組織可以選擇分享指定專案的 API 輸入與輸出資料，換取每天的免費 token；分享設定預設關閉，只有組織擁有者能開啟，且 Zero Data Retention 組織不能參加。先到組織的資料分享設定頁確認是否顯示符合資格，再決定要不要開。

- Launch、Grow 方案：兩組模型額度各自計算，每天最多 100 萬與 1,000 萬 tokens；Build 方案分別是 25 萬與 250 萬 tokens。各組內的模型共用額度，每天 00:00 UTC 重置（台灣時間 08:00）。
- 只計入已選擇分享的專案和指定模型；微調模型、微調訓練、evals、工具呼叫不包含在內。帳號餘額須大於零。
- 單次請求若會超過當日上限，整筆請求按正常價格計費；超過每日額度的部分也按正常價格計費。不要為了免費額度分享敏感、機密或專有資料。

參考：OpenAI 說明中心〈Sharing feedback, evaluation and fine-tuning data, and API inputs and outputs with OpenAI〉https://help.openai.com/en/articles/10306912-sharing-feedback-evaluation-and-fine-tuning-data-and-api-inputs-and-outputs-with-openai

## 坑

- 免費模型的限制是整個帳號算的，多開幾把 API key 沒有用，OpenRouter 文件直接這樣寫
- OpenRouter 每天 50 次很快就沒了，買 10 美元 credits 直接變 1,000 次，原型階段這樣最划算
- Workers AI 的 10,000 Neurons 是每天，00:00 UTC 重置，換成台灣時間是早上八點

## 小結

Cloudflare Workers AI 每天 10,000 Neurons；OpenRouter 免費模型每天 50 次，買過 10 美元變 1,000 次；符合資格且選擇分享資料的 OpenAI API 組織，每天最多有 100 萬與 1,000 萬 tokens 兩組免費額度（Build 方案較低）。

明天講實作時的 prompt：補上 SOLID、FIRST，以及適合任務的 design patterns。

參考：
- Cloudflare 文件：Workers AI pricing https://developers.cloudflare.com/workers-ai/platform/pricing/
- Cloudflare 文件：Workers AI limits https://developers.cloudflare.com/workers-ai/platform/limits/
- OpenRouter 文件：Limits https://openrouter.ai/docs/api-reference/limits
- OpenRouter 文件：Free Models Router https://openrouter.ai/docs/guides/routing/routers/free-router
