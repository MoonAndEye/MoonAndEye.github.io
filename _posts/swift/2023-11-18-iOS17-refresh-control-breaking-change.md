---
layout: single
title: UIRefresh 在 iOS 17 有破壞性更新，生命周期要移到 viewIsAppearing, from Essential Developer
date: 2023-11-18 19:14 +0800
category: swift
author: Marvin Lin
tags: [Swift, iOS, UIRefreshControl]
summary: 
permalink: /swift/:title:output_ext
---

今天早上(2023/11/18)，今天發生了幾件大事

## Sam Altman 被 OpenAI 解僱了，幾小時後 Greg Brockman 也提辭職了

[解僱新聞 - CNN](https://edition.cnn.com/2023/11/17/tech/sam-altman-departs-open-ai/index.html)

[商周 - Sam Altman遭OpenAI解僱，代表什麼？程世嘉：OpenAI遇到極大經營問題](https://www.businessweekly.com.tw/international/blog/3013921)

嗯…因為寫文的當下，是週末，目前還不確定會對 OpenAI、ChatGPT 有什麼影響，但在新聞中，董事會解僱的理由是「Altman 沒有誠實的對董事會」，如果後續有新的報導或發展，請以最新的新聞為主。

---

## 第二個跟 iOS 相關的事，UIRefreshControl 在 iOS17 設定的生命週期要改，這是我從 Essential Developer 發的 email 電子報上看到的

### Essential Developer 的 YouTube 連結

<iframe width="560" height="315" src="https://www.youtube.com/embed/n9ObNkPP5GY?si=q8WjL7qejsfAWVeB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

email 提到，UIRefreshControl 在 iOS 17 有破壞性更新，生命周期要移到 viewIsAppearing, from Essential Developer


以下是 Essential Developer 在 Youtube 中 live 示範


在 iOS 17 以前，在 viewDidLoad() 將 UIRefreshControl 設定好，並執行 refresh() 是沒問題的。


**但是在 iOS 17** 同樣的程式碼，並不會看到 UIRefreshControl 的 animation，而且 console 下方也會有 warning message

### 改到 viewWillAppear(:) 或 viewDidAppear(:) 生命週期有用嗎？

答： 如果移到 viewWillAppear(:) 時機太早，UIRefreshControl 不會渲染。移到 viewDidAppear(:) 太晚，會需要拉動一下畫面才會看到 UIRefreshControl 的動畫。

### 改到 viewIsAppearing(:) 有用嗎？

答： 有用。但請注意 viewIsAppearing(:) 需在 iOS 13 以上。


Essential Developer 是品質很好的 iOS 開發資源，有興趣的朋友，歡迎給 Essential Developer 支持。不僅僅是買課程，按讚/留言/分享 都是某種形式的支持


### 雖然只要看完前半段，就可以知道解決這個問題的方法，但真心推薦將這隻影片看到最後。

<iframe width="560" height="315" src="https://www.youtube.com/embed/n9ObNkPP5GY?si=Fhhgpy6pvVsvSx91&amp;start=398" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

從這個時間點開始，Caio 和 Mike 不斷的優化程式碼，即使現在的程式碼已經在 production 上正常運作了。而修改的起點是 "Unit Testing"。這邊只節錄步驟，因為真的有料的東西都在影片裡面一段一段發生。

- sut 的 vc 沒有真的在 window hiearchy 上，所以創了一個 Window 讓 vc 可以掛上去
- 但掛上去到渲染又需要「一點」時間，所以用了個 delay 1 秒
- delay 1 秒在 Unit Testing 是很不好的事情，如果你測試愈寫愈多，就會愈來愈慢，而且測試通常只可以接受 0.01 秒的等級。這已經不是把 1 秒調到 0.3 或更低的差別，而是這個 delay 在 unit testing 中不應該存在
- 為了不動到在產品中的 UIRefreshControl，寫了個 FakeRefreshControl 加上內部參數，可以在測試的時候拿來進行 assert
- 接下來「只」在 Unit Testing 中擴充一個抽換 UIRefreshControl 的方法，這在測試 target 進行 private 宣告，所以正式的環境不會有
- 接下來解決 viewIsAppearing(:) 有可能被第二次呼叫的狀況。在 Unit testing 中「強迫」讓 sut vc 進行第二次渲染，然後 Unit testing 就會 fail
- 解法1: 在 vc 裡面加個狀態，此狀態表示是否已經過了第一次 viewIsAppearing(:)
- 但還有更好的解法，解法2: 將這個狀態改成 optional closure

## 參考文獻

[Apple 的 viewIsAppearing 文件](https://developer.apple.com/documentation/uikit/uiviewcontroller/4195485-viewisappearing)

[Essential Developer 的 Youtube](https://www.youtube.com/watch?v=n9ObNkPP5GY)

[Essential Developer 的網站](https://www.essentialdeveloper.com/articles/fixing-ios-17-breaking-changes-uirefreshcontrol-viewisappearing-testability-ios-dev-mentoring)