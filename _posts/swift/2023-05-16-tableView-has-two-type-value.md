---
layout: single
title: 如果 table view 中有兩種以上的資料型態，你可以這樣處理程式碼
date: 2023-05-18 21:37 +0800
category: swift
author: Marvin Lin
tags: [Swift, iOS, UI, TableView]
summary: When your table view has two or more type of data, you can do this. This article make an example of if you have two type of data, post and ad, you can use this way to handle it.
permalink: /swift/:title:output_ext
classes: wide
---

清單型的 UI 在 iOS App 上是非常常見的設計，從內建 App 的「聯絡人」、「通話紀錄」、「設定」都是用 Table(在另一個平台叫 list) 清單型的 UI 做出來的。TableView 在手機上有個很大的優點，他可以在有限的螢幕上，呈現超過螢幕的資訊，使用者只需要往一個方向滑，就會看到更多的資訊。在 iOS 的設計上， UITableView 預設是帶有 bounce 的，當你滑到最後一個資料的時候，Table 還會維持著一定的慣性滑動，之後再彈回到頂部。這個 bounce 的行為，在「創意競擇」中也有提到，是很早就做進 iOS 系統裡面的設計。

如果列表中的資料量很多，使用者很難一次找到目標，通常還會加上搜尋框等功能，進行 filter。像是 電話 app 中的聯絡人，如果你的聯絡人有 500 個，但要找的聯絡人是 Marvin，就可以透過搜尋來進行。

## 上述的 Table 都是一種類型的資料，如果 Table 要呈現兩種不同的資料時，可以怎麼做？

在論壇型 app，像是 Facebook，Twitter，Instagram，Line 聊天室的頁面，就不會只有「單一種類的資料」。以 Facebook 的訊息牆為例，在我的 FB app 上，第 0 個 row 是限時動態，第 1 個 row 開始就是貼文，第 2 個 row 是廣告。然後會不斷穿插社團的貼文、廣告、粉絲群、Ad、直播等等。在資料上，這些不同的 row 應該都是來自不同的資料結構，如果你的接到類似這樣的需求，你可以這樣進行開發。

#### 大原則，在 Apple iOS 的架構上， Model 不會碰到 View

### 建立不同的 data model - Post(貼文), AdModel(廣告)

```swift
/// 貼文的 data model
struct Post {
    
    let id: String
    
    let contentText: String
}

/// 廣告的 data model
struct AdModel {
    
    let id: String

    let vendorID: String
    
    let adContent: String
    
    let adImage: String
}

```

上面兩個 data model 是呈現貼文/廣告，雖然這兩個類都有宣告 id 這個屬性，但不能保證 ad 的 id 和 post 的 id 合併在一起，還能保持唯一。

我們先使用 ChatGPT 快速的生出假物件。

```swift
/// posts 的假資料
func createPostsArray() -> [Post] {
    let post1 = Post(id: "1", contentText: "今天的天氣真好！")
    let post2 = Post(id: "2", contentText: "剛剛看完一本很好看的小說。")
    let post3 = Post(id: "3", contentText: "和朋友一起去爬山，感覺很棒！")
    let post4 = Post(id: "4", contentText: "新上市的手機真的很吸引人。")
    let post5 = Post(id: "5", contentText: "剛剛學會了一個新的烹飪技巧。")
    let post6 = Post(id: "6", contentText: "今天在市集上買了好多新鮮蔬菜。")
    let post7 = Post(id: "7", contentText: "去了一趟美術館，受到了很多靈感。")
    let post8 = Post(id: "8", contentText: "和家人一起過了一個溫馨的晚餐。")
    let post9 = Post(id: "9", contentText: "剛看完一場很精彩的電影，值得推薦！")
    let post10 = Post(id: "10", contentText: "今天終於把長時間的專案完成了，感覺很有成就感！")

    let posts: [Post] = [post1, post2, post3, post4, post5, post6, post7, post8, post9, post10]
    return posts
}
```

```swift
/// ad 的假資料
func createAdArray() -> [AdModel] {
    let ad1 = AdModel(id: "1", vendorID: "vendor1", adContent: "精彩折扣，限時特賣！", adImage: "ad1.jpg")
    let ad2 = AdModel(id: "2", vendorID: "vendor2", adContent: "全新產品上市，快來試用！", adImage: "ad2.jpg")
    let ad3 = AdModel(id: "3", vendorID: "vendor3", adContent: "獨家優惠，不容錯過！", adImage: "ad3.jpg")
    let ad4 = AdModel(id: "4", vendorID: "vendor4", adContent: "最新科技，滿足您的需求！", adImage: "ad4.jpg")
    let ad5 = AdModel(id: "5", vendorID: "vendor5", adContent: "環保商品，共同守護地球！", adImage: "ad5.jpg")

    let adArray: [AdModel] = [ad1, ad2, ad3, ad4, ad5]
    return adArray
}
```

### 建立一個 Model，將不同的 data model 轉換成同一種 data model (想命名為 ViewModel 當然也行)

```swift

/// 訊息牆 VC 會使用這個 Model 來呈現 Cell 的資料
class PostListModel {
    
    /// 在整個 list 上的資料，有可能是 Post，也有可能是 Ad
    var displayItems: [Any] {
        
        var items: [Any] = []
        
        /// 特殊邏輯需求，如果貼文低於 4 則，就把廣告加在最後一個
        if posts.count < 4 {
            items = posts
            items.append(ad)
            return items
        }
        
        /// 如果超過 4 則，就插在 index = 2 的位置
        items = posts
        items.insert(ad, at: 2)
        return items
    }
    
    /// 貼文資料
    private var posts: [Post] = createPostsArray()
    
    /// 單一廣告資料 (範例用)
    private let ad = AdModel(id: "1", vendorID: "vendor1", adContent: "精彩折扣，限時特賣！", adImage: "ad1.jpg")
    
    /// 多則廣告 (範例用)
    private var ads: [AdModel] = createAdArray()
    
    var itemCount: Int {
        return displayItems.count
    }
    
    /// 取得第 n 個 indexPath，如果是 AdModel 的資料
    func getAd(at indexPath: IndexPath) -> AdModel? {
        let index = indexPath.row
        if displayItems.indices.contains(index),
           let ad = displayItems[index] as? AdModel {
            return ad
        }
        return nil
    }
    
    /// 取得第 n 個 indexPath，如果是 Post 的資料
    func getPost(at indexPath: IndexPath) -> Post? {
        let index = indexPath.row
        if displayItems.indices.contains(index),
           let post = displayItems[index] as? Post {
            return post
        }
        return nil
    }
}
```

那 VC 在使用的時候，會這樣取得資料，這邊只列出 `UITableViewDataSource` 的部分

```swift
extension PostListViewController: UITableViewDelegate, UITableViewDataSource {
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        /// cell count 包含 post 的數量和 ad 的數量
        return model.itemCount
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let defaultCell = UITableViewCell()
        
        let cell = tableView.dequeueReusableCell(withIdentifier: "MyCellIdentifier", for: indexPath)
        
        if let post = model.getPost(at: indexPath) as? Post {
            // 拿到 Post, 將 post 的資料裝截進 post cell
            // update(cell, with: post)
            return cell
        }
        
        if let ad = model.getAd(at: indexPath) as? AdModel {
            // 拿到 Ad，將 ad 的資料裝載進 ad cell
            // update(cell, with: ad)
            return cell
        }
        
        return defaultCell
    }

}
```

VC 職責：在拿到 Ad 資料的時候，將廣告資料渲染在 AdCell 上，拿到 post 資料的時候，將 post 資料渲染在 cell 上。VC 不處理含有資料的邏輯。

Model (ViewModel) 職責：將不同的 data model merge，並且處理邏輯，例如：如果貼文低於 4 則，就把廣告加在最後一個，如果超過 4 則，就插在 index = 2 的位置。

### 實務上的應用 - Google AdMob

[Google AdMob 在 iOS 上的說明](https://firebase.google.com/docs/admob?hl=zh-tw)

上面的連結是 Google AdMob 的應用，當你選擇 Native Ad 的時候，UITableView 中就會有 Ad 的資料，你可以用前面的方式，將 AdMob 的資料轉換成你的 data model，然後在 tableView 中顯示出來。

## 參考網站

[Apple 對於 UITableView 的 tutorial project](https://developer.apple.com/tutorials/app-dev-training/creating-a-list-view)

[Apple 的 UITableView 文件](https://developer.apple.com/documentation/uikit/uitableview)

[Firebase AdMob 文件](https://firebase.google.com/docs/admob?hl=zh-tw)
