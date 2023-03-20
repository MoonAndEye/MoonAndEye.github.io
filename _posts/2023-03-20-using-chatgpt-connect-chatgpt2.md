---
layout: post
title: 使用 ChatGPT 串接 ChatGPT：(2)
date: 2023-03-20 13:03 +0800
category: swift
author: Marvin Lin
tags: [Swift, Programming, AI, ChatGPT]
permalink: /chatgpt/using-chatgpt-connect-chatgpt2.html
summary: 使用 ChatGPT 串接 ChatGPT
---

## 前情提要

**[使用 ChatGPT 串接 ChatGPT：(1)](/chatgpt/using-chatgpt-connect-chatgpt1.html)**

在 [前一篇文章](/chatgpt/using-chatgpt-connect-chatgpt1.html)中，我們使用了 python 語言串接了 ChatGPT API。但我現在是個 iOS 開發者，所以會想要試試看能不能直接用 ChatGPT，省時省力(？)的幫我完成一個串接 ChatGPT 的 App。

## 開始用 ChatGPT 產生 iOS App 程式碼

## 先從 api request 開始

```
問：
我已經有 ChatGPT 的 api key 了，請問怎麼用 Swift 串接 ChatGPT
```

```
答：
要使用 Swift 串接 ChatGPT，您可以使用以下步驟：

請確保您已經安裝了 Alamofire 套件，該套件可以讓您在 Swift 中輕鬆進行 HTTP 請求。

準備一個 HTTP POST 請求，並傳遞以下參數：

網址：https://api.openai.com/v1/engines/davinci-codex/completions
標題：Authorization
值：Bearer YOUR_API_KEY
標題：Content-Type
值：application/json
請求正文：{"prompt": "YOUR_PROMPT"}
在這裡，YOUR_API_KEY 是您的 ChatGPT API 金鑰，YOUR_PROMPT 是您想要傳遞給 ChatGPT 的提示。

使用 Alamofire 套件發送 HTTP POST 請求，並處理返回的 JSON 格式回應：
```

```
import Alamofire

let apiURL = "https://api.openai.com/v1/engines/davinci-codex/completions"
let headers: HTTPHeaders = [
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
]
let parameters: Parameters = [
    "prompt": "YOUR_PROMPT"
]

AF.request(apiURL, method: .post, parameters: parameters, encoding: JSONEncoding.default, headers: headers).responseJSON { response in
    switch response.result {
    case .success(let value):
        // 處理返回的 JSON 格式回應
        if let json = value as? [String: Any],
            let choices = json["choices"] as? [[String: Any]],
            let text = choices.first?["text"] as? String {
            // 在這裡處理您收到的文本回應
            print(text)
        }
    case .failure(let error):
        // 在這裡處理 HTTP 請求失敗的錯誤
        print(error)
    }
}

```

```
這樣您就可以使用 Swift 串接 ChatGPT 了。請注意，這只是一個簡單的範例，您可能需要根據您的具體需求進行更多調整和擴展。
```

<hr>

## 接下來加上一個簡單的畫面，包含 prompt 輸入，api request button，response 呈現

```
問：
幫我生成一個 iOS App 畫面，來串接 ChatGPT，畫面上要有個文字輸入框，這個輸入框的內容就是 ChatGPT API 的 prompt，下方有一個 button，按下去後會發送 api request。再下方要能顯示 ChatGPT回應的 response text。請使用 SwiftUI 來寫這個頁面
```

```
答：

import SwiftUI
import Alamofire

struct ContentView: View {
    @State var promptText: String = ""
    @State var responseText: String = ""
    let apiURL = "https://api.openai.com/v1/engines/davinci-codex/completions"
    let headers: HTTPHeaders = [
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json"
    ]
    
    var body: some View {
        VStack {
            TextField("Enter prompt here", text: $promptText)
                .padding()
                .border(Color.gray)
            
            Button(action: {
                sendRequest()
            }) {
                Text("Send Request")
            }
            .padding()
            
            Text(responseText)
                .padding()
        }
    }
    
    func sendRequest() {
        let parameters: Parameters = [
            "prompt": promptText
        ]
        
        AF.request(apiURL, method: .post, parameters: parameters, encoding: JSONEncoding.default, headers: headers).responseJSON { response in
            switch response.result {
            case .success(let value):
                if let json = value as? [String: Any],
                    let choices = json["choices"] as? [[String: Any]],
                    let text = choices.first?["text"] as? String {
                    DispatchQueue.main.async {
                        responseText = text
                    }
                }
            case .failure(let error):
                print(error)
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
```

```
在這個程式碼中，我們使用了 @State 屬性來管理 promptText 和 responseText 的狀態。當使用者輸入提示文本後，我們可以從 promptText 中取得輸入的值。當使用者按下“Send Request”按鈕時，我們會使用 Alamofire 發送一個 HTTP POST 請求，並處理返回的 JSON 格式回應，將回應文本更新到 responseText 中。最後，我們在畫面上顯示了這個回應文本。

請注意，此程式碼僅為示範，實際使用中可能需要添加更多的錯誤處理和用戶體驗。
```

## 驗證 AI 寫出來的專案會不會動

![ChatGPT 生出來的畫面](/assets/swift/chatgpt/chatgpt-connect-ios-app.jpeg){:width="250px"}

畫面上看起來不錯，那我們就來試試看會不會動吧。我試著輸入"tell me a joke"

![原始 ChatGPT 的結果](/assets/swift/chatgpt/chatgpt-connect-codex-result.jpeg){:width="250px"}

他出現了很奇怪的結果，所以我把原始 response print 出來看看

```
success({
    choices =     (
                {
            "finish_reason" = length;
            index = 0;
            logprobs = "<null>";
            text = ":\"))\n            self.nw.append(utils.normalizeString";
        }
    );
    created = 1679291111;
    id = "cmpl-6w2cRytpMNtkDeuiuH15Pl8qky62C";
    model = "davinci-codex";
    object = "text_completion";
    usage =     {
        "completion_tokens" = 16;
        "prompt_tokens" = 3;
        "total_tokens" = 19;
    };
})
```

這時候，就需要開發者介入了，在他的 model 中，使用了 `davinci-codex` model，這並不是網頁版那個大家覺得好用的 model，所以我們對 endpoint 進行置換。

```
/// 置換前
    let apiURL = "https://api.openai.com/v1/engines/davinci-codex/completions"

/// 置換後
    let apiURL = "https://api.openai.com/v1/engines/text-davinci-003/completions"
```

![davinci 的結果](/assets/swift/chatgpt/chatgpt-connect-davinci-result.jpeg){:width="250px"}

```
success({
    choices =     (
                {
            "finish_reason" = stop;
            index = 0;
            logprobs = "<null>";
            text = " feeling?\n\nI'm feeling great thank you.";
        }
    );
    created = 1679290920;
    id = "cmpl-6w2ZMgsKECySpi2OFONc9HX31FJm6";
    model = "text-davinci-003";
    object = "text_completion";
    usage =     {
        "completion_tokens" = 11;
        "prompt_tokens" = 3;
        "total_tokens" = 14;
    };
})
```

## 結論 - 這個階段，人類開發者還是需要去看 ChatGPT 的程式碼，並進行 debug

從上面的例子可以得到幾個結論

- 程式碼會動
- UI 看起來符合最低 demo 的標準
- 但如果 prmopt 不夠精確，要經過調整才能得得人類預期的結果

第三點這邊，我並不認為是單純是現在的 ChatGPT 的問題，畢竟，人類在溝通上，是省略了很多「已知」，或是直接假設對方「已知」的前提下，進行交談。或許在接下來的時間，人類會開始學著和 ChatGPT 進行溝通，改變人類自己的交談習慣，讓 ChatGPT 可以更快的了解人類要的結果。

