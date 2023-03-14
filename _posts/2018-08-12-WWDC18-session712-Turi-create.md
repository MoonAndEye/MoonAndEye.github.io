---
layout: post
title: "WWDC18, Session-712 Turi Create 重點整理 -製作ML model 不再是一個困難的事"
date: 2018-08-12 15:28 +0800
category: Swift
author: Marvin Lin
tags: [MLKit, Machine Learning, Turi Create, Swift]
summary: "WWDC18, Session-712 Turi Create 重點整理 -製作ML model 不再是一個困難的事"
---

### WWDC18, Session-712 Turi Create 重點整理 -製作ML model 不再是一個困難的事

![](https://cdn-images-1.medium.com/max/800/0*V4Kohj_1SGVxoqQt)

Photo by [Jens Johnsson](https://unsplash.com/@jens_johnsson?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

### Turi Create 是什麼?

在被 Apple 收購之前，他的名字是 Dato ，是 Graph Lab 裡面的一個開發項目，由華盛頓大學的 Prof. Carlos Guestrin 所資助。之後在 A 輪募了 6 百多萬美金， B 輪募了 1 千 8 百多萬美金，並在 2016 年中被 Apple 收購。在 WWDC17 的時候， 有一個 session 在介紹這個模組，當時的版本是 4.0。在 WWDC18 的時候， Session-712 有詳細介紹這個 Python package，除此之外， Turi Create 也在 \`What's new in Core ML\` (Session-708, 709)中，講者直接 Demo 試範。(Ref1)

### Turi Create 的用途

．他是一個 Python 的 Package，可以製作 Core ML models，而且有開源

．簡單易用，即使非 ML 專門也可以操作

．讓 iOS 開發者只需要專注在 APIs 上

．跨平台 (Mac, Linux)

．學習成本低，在 Mac 上因為 Python 2.7 已經內建了，你只需要 \`pip install turicreate\` 即可。要做出一個辨識物體 model 只要 20 行以內的程式碼。而 WWDC18 中使用的 Jupyter Notebook 並非必要package。如果你想裝，請看 (Ref2)。

### 辨識照片中的人是不是金城武

下面這篇文章是用 Turi Create 做出一個簡單的金城武辨識 App，如果你想試著實作，可以參考這一篇。

[**使用 Turi Create 製作圖案辨識的 App - Core ML and Vision**  
_Turi Create是一個拿來做 machine learning model 的 Python 模組，在 WWDC18 上，有多個 Session 直接在現場使用這個模組直接 Demo。他可以讓 iOS 開發者在使用 Core ML…_medium.com](https://medium.com/@atimis19/using-turi-create-build-an-image-classification-app-core-ml-b3071ffde3af "https://medium.com/@atimis19/using-turi-create-build-an-image-classification-app-core-ml-b3071ffde3af")[](https://medium.com/@atimis19/using-turi-create-build-an-image-classification-app-core-ml-b3071ffde3af)

### 建立 Machine Leaning model 前所需的五個步驟

![](https://cdn-images-1.medium.com/max/800/1*mywU7P1855THvlFe2WErtQ.png)

進行 Machine Leaning 所需要的五個步驟

Step 1: 你需要清楚的定義你的任務，因為 Turi Create (或者說是 ML 領域) 會因為你的任務不同，而出現不同的最佳解算法。如果你沒有選到正確率高的那一種，那你最後產生出來的 model 會達不到你要的效果。

Step 2: 這個任務所需要的 data。不同的任務，需要不同的 data。如果是圖片識別，那你需要不同 folder 裡面裝入和 folder name 相同的圖片。但如果是目標探測，你就必需要有目標標籤和標籤座標的 JSON 檔。

Step 3: 使用 Turi Create 產出你的 model 檔，這只需要低於 20 行的程式碼

Step 4: 你需要驗證你的 model 是不是正確的，通常會把訓練資料切成 8:2 或是其他比例。然後讓 model 去辨識沒丟入訓練的 20%資料，如果你的準確率很低，建議你拉高 max\_iterations 這個參數，或是做其他參數調整。

Step 5: 如果驗證後沒問題，那就把 model 放入App 裡面然後發佈。

* * *

### 1、定義任務

![](https://cdn-images-1.medium.com/max/800/1*INdNWx4wC55KQh4Q51ExMw.png)

Turi Create 內執行的Task種類有這麼多

![](https://cdn-images-1.medium.com/max/800/1*x_bHxyElNQYb5OQHpnvmkQ.png)

實際上常用的MLTask 有這四種

Turi Create 所有種類的任務就在上面那一張表格裡面，你可以依照你想做的事情選擇對應的 API。而上面這四張圖，表示的是 App 中最常用的四種。注意風格變換是在 5.0 beta 版以後才有的功能， 4.0 是沒有的。

### 2、輸入資料訓練模型

![](https://cdn-images-1.medium.com/max/800/1*6kzzIfc4KVf3N1pya6wMtQ.png)

上排是image classification task，只需要圖片和 folder name 即可。下排是object detect task，除了照片以外還需要一個 label 、和 bounding box 資訊。

![](https://cdn-images-1.medium.com/max/800/1*qCVLHh7UM3o8zuGj_1sPJA.png)

如果是 object detection ，你需要放入 annotation 的資料，他通常是一個 JSON檔，裡面的 Array 讓你可以塞複數個 objects。Array 內每個元素包含一個 label 和 bounding box 的座標資訊。

依照任務所需要的 data ，輸入對應資料，如果是 image classification 的 task ，你只需要在對應的 folder 裡面放入圖片。但如果是 object detection ，你會需要再加一欄資料，來表示圖片上該辨識出來的物體名字和 bounding box 的座標。而這個 annotation 資訊是一個 array ，Turi Create 是可以在一張圖片裡面進行多目標辨識的。

![](https://cdn-images-1.medium.com/max/800/1*JYJqIggoRQptI5HwKgj65g.png)

要特別注意的是，turi create裡面，X Y是 bounding box 的中心點

Turi Create 中的方框被叫做是 bounding box，要注意的一點是，在 UIKit 中， Frame 的 X 和 Y通常是指一個框的左上角，**但 Turi Create 資料中的 X 和 Y 是指 bounding box 的中心點。**

**在訓練資料、輸出框線的時候，請記得做轉換**。不然你的模型或是你的 View 一定看起來會怪怪的。

### 3、產生 ML model

WWDC18 就直接使用 Jupyter Notebook 進行 Demo，所需要的程式碼並不多，只需要 11 行即可，我們這邊用「辨識這張圖片是不是金城武」為例。

import turicreate as turi

url = “dataset/”

data = turi.image\_analysis.load\_images(url)

#如果他這張照片的不是放在 Kaneshiro 的 folder 內，他就是 Unknown  
data\[“kaneshiroOrNot”\] = data\[“path”\].apply(lambda path: “Kaneshiro” if “kaneshiro” in path else “Unknown”)

data.save(“kaneshiro\_or\_not.sframe”)

data.explore()

以上就是把 data 輸出成 SFrame 格式的程式碼，包含 url 那一行也才5行。

在下面的 #1 到 #3 步驟，就是把你的資料輸出成 CoreML 可以讀到的 Model. 以下分別解說 #1 ~ #3

#1: Load the data

把 SFrame 寫入 data 裡面

#2: Split to train and test data

把所有資料亂數切分成 8:2 (你也可以分成其他比例)，其中 8 成的資料是拿來訓練的，剩下的 2 成則是拿來驗證的。

#3 Create Model

turi 後面的第一個參數就是 task 的任務種類，這邊用 image classifier 當範例。

在 #3 的時候， max\_iterations 並不是必要，如果你沒設定，那就會用那個 task 模組的預設值。如果是 image classifier ，max\_iteration 的預設是 10。但因為效果不是很好，我這邊把他調成 100。而如果是 style transfer 的模組，預設是 5000。在我的 Mac Book Pro 上，一個 iteration 大約是 40 秒左右，依照網路上其他人的經驗，這大概是需要 2天左右才會跑出結果。

\# 1. Load the data  
data = turi.SFrame(“kaneshiro\_or\_not.sframe”)

\# 2. Split to train and test data  
train\_data, test\_data = data.random\_split(0.8)

\# 3. Create model  
model = turi.image\_classifier.create(train\_data, target=”kaneshiroOrNot”, max\_iterations=100)

\# 4. Predictions  
predictions = model.predict(test\_data)

\# 5. Evaluate the model and show metrics  
metrics = model.evaluate(test\_data)  
print(metrics\[“accuracy”\])

\# 6. Save the model  
model.save(“kaneshiro.model”)

\# 7. Export to CoreML format  
model.export\_coreml(“kaneshiro.mlmodel”)

### 4、驗證 Model

#4 Predictions

用做出來的 model 對沒進入訓練資料進行預測。

#5 對 model 做驗證

Turi Create 會告訴你這個模型準確率，如果太低，他還會問你要不要調整 \`max\_iterations\` 的參數。

![](https://cdn-images-1.medium.com/max/800/1*Ntd4jyjkvF5IFc2PXc9hqw.png)

標記有兩點要驗證: 1 標記是正確的 2標記範圍要和正確範圍有50%以四的覆蓋率

#6 把訓練好的 model 存起來

#7 把訓練好的 model 轉成 Core ML 可以吃的 model

### 5、 部署到 App 裡

把輸出的 mlmodel 放到專案裡面。

這樣，就完成了你的 ML Model

Jupyter Notebook 的程式碼放在下面這個 GitHub 裡面，直接去 Jupyter Notebook 的 folder 就可以直接用了。那個 folder 裡面有三個範例，KaneshiroOrNot 是驗證是不是金城武。SoupOrRice 是驗證圖片是湯或飯。Adventure 則是分辨圖片是復仇者聯盟的哪個角色。

[**MoonAndEye/TuriCreateDemo**  
_GitHub is where people build software. More than 28 million people use GitHub to discover, fork, and contribute to over…_github.com](https://github.com/MoonAndEye/TuriCreateDemo/ "https://github.com/MoonAndEye/TuriCreateDemo/")[](https://github.com/MoonAndEye/TuriCreateDemo/)

* * *

Ref-1: [Turi 公司被 Apple 收購, https://en.wikipedia.org/wiki/GraphLab](https://en.wikipedia.org/wiki/GraphLab)

Ref-2: [在 Mac 環境架設 Jupyter Notebook](https://medium.com/@atimis19/%E5%9C%A8-mac-%E4%B8%8A%E6%9E%B6%E8%A8%AD-jupiter-notebook-%E7%92%B0%E5%A2%83-4a983b70af4)

[**在 Mac 上架設 Jupyter Notebook 環境**  
_目前，我本身的職務裡面並沒有需要用到 Python 的地方，所以這一篇主要的重點並不是用 Jupyter Notebook 來做一個專案的主軸，重點是放在讓 Python…_medium.com](https://medium.com/@atimis19/%E5%9C%A8-mac-%E4%B8%8A%E6%9E%B6%E8%A8%AD-jupiter-notebook-%E7%92%B0%E5%A2%83-4a983b70af4 "https://medium.com/@atimis19/%E5%9C%A8-mac-%E4%B8%8A%E6%9E%B6%E8%A8%AD-jupiter-notebook-%E7%92%B0%E5%A2%83-4a983b70af4")[](https://medium.com/@atimis19/%E5%9C%A8-mac-%E4%B8%8A%E6%9E%B6%E8%A8%AD-jupiter-notebook-%E7%92%B0%E5%A2%83-4a983b70af4)

Ref-3: [範例程式碼](https://tinyurl.com/y93ey7ds)

[**MoonAndEye/TuriCreateDemo**  
_GitHub is where people build software. More than 28 million people use GitHub to discover, fork, and contribute to over…_tinyurl.com](https://tinyurl.com/y93ey7ds "https://tinyurl.com/y93ey7ds")[](https://tinyurl.com/y93ey7ds)

Ref-4: 實作金城武辨識器

[**使用 Turi Create 製作圖案辨識的 App - Core ML and Vision**  
_Turi Create是一個拿來做 machine learning model 的 Python 模組，在 WWDC18 上，有多個 Session 直接在現場使用這個模組直接 Demo。他可以讓 iOS 開發者在使用 Core ML…_medium.com](https://medium.com/@atimis19/using-turi-create-build-an-image-classification-app-core-ml-b3071ffde3af "https://medium.com/@atimis19/using-turi-create-build-an-image-classification-app-core-ml-b3071ffde3af")[](https://medium.com/@atimis19/using-turi-create-build-an-image-classification-app-core-ml-b3071ffde3af)

By [Marvin Lin](https://medium.com/@atimis19) on [August 12, 2018](https://medium.com/p/a46cb9420b34).

[Canonical link](https://medium.com/@atimis19/overview-of-wwdc18-session-712-turi-create-build-an-app-with-core-ml-is-not-that-difficult-a46cb9420b34)
