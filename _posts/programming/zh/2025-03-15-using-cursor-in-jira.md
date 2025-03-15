---
layout: single
title: 在非開發職能上，使用 Cursor 在 Jira 寫 GWT (Given - When - Then) 需求單
date: 2025-03-15 11:39 +0800
category: programming
author: Marvin Lin
tags: [Cursor, AI]
summary: 
---

2025 年開始，我已經在開發的日常中，大量的使用 Cursor。但如果想法打開，Cursor 輸出的「文字」本來就可以超過「程式」的範圍。如果團隊中一起合作的 PM，使用 Cursor 開單，是不是開發者可以快速的跨越自然語言和程式語言的隔閤，然後快速的進入程式開發呢？首先，先從 Cursor IDE 下載開始。

## [Cursor IDE 下載](https://www.cursor.com/)

[![Cursor IDE Landing Page](/assets/programming/cursor-in-jira/cursor_landing.png)](https://www.cursor.com/)

## Cursor Model 選擇的擴充

Model 的擴充，預設是 claude 系和 ChatGPT4o-mini, cursor-small, 預設不會打開 Gemini 2.0 或 ChatGPT o1，所以要打開才能使用其他模型。在這邊選擇 cursor setting。

![Cursor settings](/assets/programming/cursor-in-jira/cursor_setting_touch.png)

這邊可以選擇在使用不同的 models，只要把想使用的 models 勾選起來，就可以選擇更多的 models。每一個 model 都有特性，像是 deepseek-v3 速度就很快，但選到 deepseek-r1 或 calude-sonnet 3.7 with think 就具備思考的特性。

![Cursor models choose](/assets/programming/cursor-in-jira/cursor_models_choose.png)

## 右側欄 - 開始使用 AI 開始輔助 (cmd  + shift + B)

你可以在右邊這一欄，寫上你想要問的，要求任務，問架構，所以在管理專案的職能上，當然可以寫出 GWT (Give - When - Then) 的 jira 單

![Cursor right bar](/assets/programming/cursor-in-jira/cursor_right_bar.png)


## 左側欄 - folder navigation, search, 裝載的外掛 (cmd + B)

檔案導覽 (Folder Navigation)**  
- 顯示專案目錄樹狀結構  
- 支援快速檔案/資料夾建立 (右鍵 > New File/Folder)  
- 拖曳檔案即可移動位置  
- 快捷鍵: Cmd + 1 聚焦檔案導覽

全域搜尋 (Global Search)**  
- 跨檔案內容搜尋 (支援正規表示式)  
- 過濾搜尋範圍: 檔案類型/符號類型(類別/方法/屬性)  
- 快捷鍵: Cmd + Shift + F

外掛管理 (Plugin Management)**  
- 顯示已安裝擴充套件列表  
- 一鍵連結至 [Cursor Marketplace](https://www.cursor.com/marketplace)  
- 快捷鍵: Cmd + Shift + X 開啟擴充管理

![Cursor left bar](/assets/programming/cursor-in-jira/cursor_left_bar.png)

其他你裝的外掛太多，無法顯示，都會列在後面，長度如果太長的話，要按一個下拉式選單，就可以展開

![Cursor left drop list](/assets/programming/cursor-in-jira/cursor_left_drop_list.png)

## Jira 專案管理外掛的安裝 - [Jira Atlassian](https://marketplace.visualstudio.com/items?itemName=Atlassian.atlascode)

如果能不切換視窗，對工作者的效率當然是好的，在這個 marketplace 裡面，是有 Jira 的外掛套件的，先選擇 marketplace，然後打上 Jira 開始找 Jira 套件，然後選擇 install。就可以開始在 VSCode or Cursor 中開始 編輯/修改 Jira 的票了。

![Jira plug in](/assets/programming/cursor-in-jira/cursor_jira_plug_in.png)

## 開一個 Folder 開始寫 Jira ticket 或是任何你要產生的文件
基本用法 - 用 folder (資料夾) 來管理你的文件，不論那是什麼文件，git 版控有學習門檻，因為 git 有學習曲線高的狀況，非開發者實際上可以用 fileName_yyyyMMdd_version 來當版本控制也可以。因為在文案的撰寫和程式不一樣，文案可能要複數時間版本比較內容，但程式只需要發佈時，就出去一份

先開一個資料夾

![create folder image](/assets/programming/cursor-in-jira/create_demo_folder.png)

打開 cursor ，選擇那個資料夾

![choose folder by folder](/assets/programming/cursor-in-jira/open_by_cursor.png)

可以用這個 icon 直接開 file
![create files](/assets/programming/cursor-in-jira/create_files.png)

接下來，就可以用 AI 來寫作了
![Using AI create](/assets/programming/cursor-in-jira/start_with_ai.png)


## Agent, Ask, Edit mode 解釋

Cursor 這邊可以選不同的 models 進行你的任務。

Ask: 就像 ChatGPT 的那個界面一樣，他會告訴你 prompt 指示的回應，然後出現在側邊欄。

Edit: 這時候 AI 具備可以修改檔案的能力，他在指令中進行檔案的修改。修改完後你如果滿意，可以按 Accept 接受修改，可以按 Reject 不接受修改

Agent: 可以接受更抽象化的指令，且具備開新檔案能力/改檔案名能力/操控 terminal 能力，但因為指令抽象化 + 可操控能力變強，在搭配 YOLO mode 時，建議最好一直盯著他的 respnose，要停手都還有機會。舉例: 你可以下，將這份檔案翻譯成 英文/德文/俄文/日文，並且把每種不同的翻譯都另存一份，並加上後綴 lang_code。「如果順利」，Agent 會在翻譯完成後，直接把檔案生出來，並完成 my_text_en.txt, my_text_ge.txt, my_text_ru.txt, my_text_jp.txt 。


![Chat with diff models](/assets/programming/cursor-in-jira/chat_with_diff_models.png)

接下來，你就可以用 AI 來輔助開 jira ticket 了。

---

## 試產 GWT

接下來，你可以試這一段，在 Agent mode 中產出文件。
```markdown
請依 Give - When - Then (GWT) 的格式，將下列需求寫成 GWT 文件。
login
logout
reset password
```

---

## 試產的結果

我會幫你將登入、登出和重設密碼的功能需求，用 Given-When-Then 的格式撰寫：

### 登入功能

```gherkin
Feature: 使用者登入

Scenario: 成功登入
Given 使用者在登入頁面
When 使用者輸入正確的帳號和密碼
And 點擊登入按鈕
Then 系統應該成功登入
And 導向到首頁
And 顯示登入成功訊息

Scenario: 登入失敗 - 錯誤的認證資訊
Given 使用者在登入頁面
When 使用者輸入錯誤的帳號或密碼
And 點擊登入按鈕
Then 系統應該顯示錯誤訊息
And 使用者停留在登入頁面
```

### 登出功能

```gherkin
Feature: 使用者登出

Scenario: 成功登出
Given 使用者已經登入系統
When 使用者點擊登出按鈕
Then 系統應該登出使用者
And 清除使用者的登入狀態
And 導向到登入頁面
And 顯示登出成功訊息
```

### 重設密碼功能

```gherkin
Feature: 重設密碼

Scenario: 申請重設密碼
Given 使用者在忘記密碼頁面
When 使用者輸入註冊的電子郵件
And 點擊重設密碼按鈕
Then 系統應該發送重設密碼連結到該電子郵件
And 顯示確認訊息

Scenario: 使用重設密碼連結
Given 使用者點擊重設密碼電子郵件中的連結
When 使用者輸入新密碼
And 確認新密碼
And 點擊確認按鈕
Then 系統應該更新使用者密碼
And 顯示密碼重設成功訊息
And 導向到登入頁面

Scenario: 重設密碼失敗 - 密碼不符合規則
Given 使用者在重設密碼頁面
When 使用者輸入不符合規則的新密碼
And 點擊確認按鈕
Then 系統應該顯示密碼規則錯誤訊息
And 使用者停留在重設密碼頁面
```

這些 GWT 格式的需求描述涵蓋了主要的使用情境和預期結果。每個功能都包含了成功和失敗的情況，並且清楚說明了：
1. 初始狀態（Given）
2. 使用者的操作（When）
3. 預期的系統回應（Then）

如果需要更詳細的情境或是其他特殊案例，我可以協助您進一步補充。
