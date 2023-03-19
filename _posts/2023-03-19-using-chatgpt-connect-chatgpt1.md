---
layout: post
title: 使用 ChatGPT 串接 ChatGPT：(一)
date: 2023-03-19 12:36 +0800
category: swift
author: Marvin Lin
tags: [swift, programming, ai, chatgpt, python]
summary: 
---

## 申請 ChatGPT api key

ChatGPT 是有開放 API 讓使用者串接的，申請是免費的，但免費額度的用量是 18 USD，或是三個月到期，之後就需要升級成 plus 才能繼續使用。詳細情況，建議關注 open.ai 的網站，因為上面的資訊才是最新且最正確的。

### [Open.ai 價格說明網頁](https://openai.com/pricing)

那麼，我們就開始串接 ChatGPT 了，要進行 client 的串接，我們需要 api key。

### [申請 api key的網頁](https://platform.openai.com/account/api-keys)

你可以在這個網頁申請 api key，記得，拿到 key 後要馬上找到地方存起來，不然就再也看不到 keys 了。

**這個網頁也有提醒，api key 不要放在 client 端，也不要放在公開的 repo 上**

接下來，我們就不斷的去問 ChatGPT，怎麼串接 ChatGPT。

## 使用 ChatGPT 來串接 ChatGPT

```
問：
怎麼串接 ChatGPT
```

```
答：
要使用 ChatGPT API，您需要遵循以下步驟：

1 註冊 ChatGPT API 帳戶。前往 ChatGPT API 官方網站，點擊「註冊」按鈕，並填寫必要的註冊信息。

2 創建 API 金鑰。登錄到您的 ChatGPT API 帳戶後，創建一個新的 API 金鑰。API 金鑰是連接到 ChatGPT API 的唯一憑證，您需要使用它才能訪問 API 服務。

3 選擇適合的 API。ChatGPT API 提供了多個 API 功能，例如文字生成、對話系統、語言翻譯等。選擇適合您需求的 API。

4 創建 API 請求。使用您的 API 金鑰和適合的 API 端點創建 API 請求。API 端點是 API 服務的網址，您可以在 API 文檔中找到相關信息。在 API 請求中，您可以傳遞相應的參數和數據以訪問 API 服務。

5 處理 API 響應。一旦發送 API 請求，您會收到一個響應，其中包含 API 服務返回的結果。您可以根據響應中的數據進行下一步處理。

以上是使用 ChatGPT API 的一般步驟。您可以參考 ChatGPT API 官方文檔，以了解更多關於 API 的詳細信息，並且可以通過使用相關的庫和SDKs，使API集成更加容易。
```

```
問：
給我一個串接 chat gpt 的範例
```

```
答：
好的，以下是一個使用 Python 語言，並且使用 ChatGPT API 文本生成功能的簡單範例：

```

```
答：
import openai
import os

# 設置 API 金鑰
openai.api_key = os.getenv("OPENAI_API_KEY")

# 準備 API 請求
prompt = "Once upon a time,"
model_engine = "text-davinci-002"
temperature = 0.5
max_tokens = 50

# 訪問 API 服務
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=temperature,
)

# 處理 API 響應
generated_text = response.choices[0].text.strip()

# 輸出結果
print(generated_text)
這個範例會生成一段文本，該文本是在「Once upon a time,」這個開頭之後，使用 ChatGPT API 文本生成功能生成的。在這個例子中，我們使用了 openai Python 包，並且將 API 金鑰設置為環境變量。我們使用 openai.Completion.create 方法向 API 服務提交了一個文本生成的請求，並且通過處理 API 響應來獲得了生成的文本結果。
```

## 直接拿 code 去跑的結果

把 ChatGPT 給你的 Code 直接拿去跑，並照著指示換掉 api key，到底會不會動呢? 我們來看一下。

```
# 結果

Traceback (most recent call last):
  File "/Users/cm0679/5python/foo.py", line 14, in <module>
    response = openai.Completion.create(
  File "/Users/cm0679/anaconda3/lib/python3.8/site-packages/openai/api_resources/completion.py", line 25, in create
    return super().create(*args, **kwargs)
  File "/Users/cm0679/anaconda3/lib/python3.8/site-packages/openai/api_resources/abstract/engine_api_resource.py", line 149, in create
    ) = cls.__prepare_create_request(
  File "/Users/cm0679/anaconda3/lib/python3.8/site-packages/openai/api_resources/abstract/engine_api_resource.py", line 106, in __prepare_create_request
    requestor = api_requestor.APIRequestor(
  File "/Users/cm0679/anaconda3/lib/python3.8/site-packages/openai/api_requestor.py", line 130, in __init__
    self.api_key = key or util.default_api_key()
  File "/Users/cm0679/anaconda3/lib/python3.8/site-packages/openai/util.py", line 186, in default_api_key
    raise openai.error.AuthenticationError(
openai.error.AuthenticationError: No API key provided. You can set your API key in code using 'openai.api_key = <API-KEY>', or you can set the environment variable OPENAI_API_KEY=<API-KEY>). If your API key is stored in a file, you can point the openai module at it with 'openai.api_key_path = <PATH>'. You can generate API keys in the OpenAI web interface. See https://onboard.openai.com for details, or email support@openai.com if you have any questions.
```

我們得到了 AuthenticationError，從結果來看，一定是 api key 的設定有問題。但現在先不人工介入，我們先試試看 ChatGPT 能不能從這個結果給我一個改正後的 code。

## 拿 Error 的結果去問 ChatGPT

```
# 問：
error message 如下
Traceback (most recent call last):
  File "/Users/cm0679/5python/foo.py", line 14, in <module>
    response = openai.Completion.create(
  File "/Users/cm0679/anaconda3/lib/python3.8/site-packages/openai/api_resources/completion.py", line 25, in create
    return super().create(*args, **kwargs)
  File "/Users/cm0679/anaconda3/lib/python3.8/site-packages/openai/api_resources/abstract/engine_api_resource.py", line 149, in create
    ) = cls.__prepare_create_request(
  File "/Users/cm0679/anaconda3/lib/python3.8/site-packages/openai/api_resources/abstract/engine_api_resource.py", line 106, in __prepare_create_request
    requestor = api_requestor.APIRequestor(
  File "/Users/cm0679/anaconda3/lib/python3.8/site-packages/openai/api_requestor.py", line 130, in __init__
    self.api_key = key or util.default_api_key()
  File "/Users/cm0679/anaconda3/lib/python3.8/site-packages/openai/util.py", line 186, in default_api_key
    raise openai.error.AuthenticationError(
openai.error.AuthenticationError: No API key provided. You can set your API key in code using 'openai.api_key = <API-KEY>', or you can set the environment variable OPENAI_API_KEY=<API-KEY>). If your API key is stored in a file, you can point the openai module at it with 'openai.api_key_path = <PATH>'. You can generate API keys in the OpenAI web interface. See https://onboard.openai.com for details, or email support@openai.com if you have any questions.
```

```
# 答：
這個錯誤信息顯示了在代碼中並沒有提供 ChatGPT API 金鑰。你需要設置你的 API 金鑰才能使用 ChatGPT API。你可以按照下列步驟操作：

訪問 OpenAI 控制台 (https://beta.openai.com/docs/quickstart)
創建一個帳戶 (如果你還沒有帳戶)
創建一個新的 API 金鑰 (https://beta.openai.com/docs/api-reference/authentication/create-api-key)
複製你的新 API 金鑰
在你的代碼中設置 openai.api_key 為你的 API 金鑰。
以下是代碼示例：
```

```

python
Copy code
import openai

# 設置你的 API 金鑰
openai.api_key = "YOUR_API_KEY_HERE"

# 調用 ChatGPT API 文本生成功能
prompt = "Once upon a time,"
model_engine = "text-davinci-002"
temperature = 0.5
max_tokens = 50

response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=temperature,
)

# 處理 API 響應
generated_text = response.choices[0].text.strip()

# 輸出結果
print(generated_text)
請務必將 YOUR_API_KEY_HERE 替換為你自己的 ChatGPT API 金鑰。
```

這次，ChatGPT 換掉了設定 api key 的那一段

```
# 更換前
openai.api_key = os.getenv("OPENAI_API_KEY")

# 更換後
openai.api_key = "YOUR_API_KEY_HERE"
```

然後，再跑一次，我們得到了

```
# response：
here was a little girl who loved to read. She would spend hours upon hours reading books of all kinds. She loved the smell of old books and the way they made her feel.

One day, she came across a book that she had
```

得到了一個故事的結果，因為我們的 prmopt 為 `Once upon a time,` 所以 ChatGPT 就把他接成一個故事了。

## ChatGPT API 的那些參數


```
prompt = "Once upon a time,"
model_engine = "text-davinci-002"
temperature = 0.5
max_tokens = 50
```

### prompt
詠唱詞，ChatGPT 會依這個輸入，來回傳 response

### model_engin
使用的 ai model，模型的種類不同，建議從官網去找你想完成任務的模型。
注意，雖然 ChatGPT 給的是 `text-davinci-002` 但後面還有個 `text-davinci-003`，然後2023年3月之後，還出了個 `gpt-3.5-turbo`。每個模型的用途不同，能力也不同，請依使用場景去調整。

### temperature
表示同樣的 prompt，給出一樣的 response 的機率，如果設定為 0，那一樣的 input 就會得到一樣的 response。調高一點，讓結果會不同。

### max_tokens
token 可以想成是 response 的字數限制，每個模型的 max_token 都是不同的，所以調到 500，1000 都是可以的。注意，這和使用量有關，token 是算費用的。價格在下方的參考資料有列出來

## 參考資料

**[open.ai pricing](https://openai.com/pricing)**

**[API 可以選擇的 model 列表和 model 說明](https://platform.openai.com/docs/models)**

