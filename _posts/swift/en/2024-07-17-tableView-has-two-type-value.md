---
layout: single
title: Handling Multiple Data Types in a TableView in Swift
date: 2024-07-17 13:25 +0800
category: swift
author: Marvin Lin
tags: [Swift, iOS, UI, TableView]
lang: en
summary: When your table view contains more than one type of data, you can manage it using this approach. This article provides an example of handling two types of data—posts and ads—within a table view.
classes: wide
---

List-type UIs are very common in iOS apps, as seen in built-in apps like "Contacts," "Call History," and "Settings," all of which utilize a table (or list in other platforms) UI format. One of the significant advantages of TableViews on mobile devices is their ability to display more information than the screen can hold at one time; users simply need to scroll in one direction to see more content. In the design of iOS, UITableViews are inherently bouncy, maintaining a bit of momentum when scrolled to the last item before bouncing back. This behavior, also mentioned in "Creative Choices," has been an integral part of iOS from early on.

If there is a large amount of data in the list, making it difficult for users to find what they are looking for at once, features like a search bar are often added to filter results. For example, in the Phone app, if you have 500 contacts but are looking for 'Marvin,' you can use the search functionality to narrow down the results.

![UITableView has two types of data](/assets/swift/tableview-two-type-data/two-type-list.png)

## How can you handle a table that needs to display two different types of data?

In forum-like apps, such as Facebook, Twitter, Instagram, or Line chat pages, you don't just see one type of data. For instance, on my Facebook feed, the first row is for stories, followed by posts from the second row onwards, and interspersed with ads, group posts, fan pages, ads, live streams, etc. These different rows likely come from different data structures. If you face a similar requirement, here's how you can approach development.

#### Basic Principle in Apple iOS architecture: Models do not interact with Views

### Creating different data models - Post and AdModel

```swift
/// Data model for posts
struct Post {
    let id: String
    let contentText: String
}

/// Data model for ads
struct AdModel {
    let id: String
    let vendorID: String
    let adContent: String
    let adImage: String
}

```

The two data models above represent posts and ads. Although both classes declare an 'id' property, you cannot guarantee that the combination of ad and post ids will remain unique.

Let's quickly generate some mock objects using ChatGPT.

```swift
/// Mock data for posts
func createPostsArray() -> [Post] {
    let posts = [
        Post(id: "1", contentText: "The weather is great today!"),
        Post(id: "2", contentText: "Just finished a great novel."),
        Post(id: "3", contentText: "Went hiking with a friend, had a blast!"),
        Post(id: "4", contentText: "The new smartphone on the market is really tempting."),
        Post(id: "5", contentText: "Just learned a new cooking technique."),
        Post(id: "6", contentText: "Bought lots of fresh vegetables at the market today."),
        Post(id: "7", contentText: "Visited an art museum, got lots of inspiration."),
        Post(id: "8", contentText: "Had a cozy dinner with family."),
        Post(id: "9", contentText: "Just watched a fantastic movie, highly recommend!"),
        Post(id: "10", contentText: "Finally completed a long-term project today, feeling accomplished!")
    ]
    return posts
}

/// Mock data for ads
func createAdArray() -> [AdModel] {
    let ads = [
        AdModel(id: "1", vendorID: "vendor1", adContent: "Exciting discounts, limited time offer!", adImage: "ad1.jpg"),
        AdModel(id: "2", vendorID: "vendor2", adContent: "Brand new products launched, come and try!", adImage: "ad2.jpg"),
        AdModel(id: "3", vendorID: "vendor3", adContent: "Exclusive offers you can't miss!", adImage: "ad3.jpg"),
        AdModel(id: "4", vendorID: "vendor4", adContent: "The latest technology meets your needs!", adImage: "ad4.jpg"),
        AdModel(id: "5", vendorID: "vendor5", adContent: "Eco-friendly products, let's protect the planet together!", adImage: "ad5.jpg")
    ]
    return ads
}
```

### Create a Model to transform different data models into a single type (also could be named ViewModel)

```swift
/// This model will be used by the Feed VC to display cell data
class FeedListModel {
    /// Data in the entire list could be either Post or Ad
    var displayItems: [Any] {
        var items: [Any] = []
        
        /// If there are fewer than 4 posts, add the ad at the end
        if posts.count < 4 {
            items = posts + [ad]
            return items
        }
        
        /// If there are more than 4 posts, insert the ad at position 2
        items = posts
        items.insert(ad, at: 2)
        return items
    }
    
    /// Post data
    private var posts: [Post] = createPostsArray()
    
    /// Single ad data (for example)
    private let ad = AdModel(id: "1", vendorID: "vendor1", adContent: "Exciting discounts, limited time offer!", adImage: "ad1.jpg")
    
    /// Multiple ads (for example)
    private var ads: [AdModel] = createAdArray()
    
    var itemCount: Int {
        return displayItems.count
    }
    
    /// Get the nth indexPath data if it's an AdModel
    func getAd(at indexPath: IndexPath) -> AdModel? {
        let index = indexPath.row
        if displayItems.indices.contains(index), let ad = displayItems[index] as? AdModel {
            return ad
        }
        return nil
    }
    
    /// Get the nth indexPath data if it's a Post
    func getPost(at indexPath: IndexPath) -> Post? {
        let index = indexPath.row
        if displayItems.indices.contains(index), let post = displayItems[index] as? Post {
            return post
        }
        return nil
    }
}
```

The VC would then use this model to retrieve data, and here we only list the `UITableViewDataSource` part:

```swift
extension PostListViewController: UITableViewDelegate, UITableViewDataSource {
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        /// Cell count includes the number of posts and ads
        return model.itemCount
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let cell = tableView.dequeueReusableCell(withIdentifier: "MyCellIdentifier", for: indexPath)
        
        if let post = model.getPost(at: indexPath) {
            // Got a Post, load post data into the post cell
            // update(cell, with: post)
            return cell
        }
        
        if let ad = model.getAd(at: indexPath) {
            // Got an Ad, load ad data into the ad cell
            // update(cell, with: ad)
            return cell
        }
        
        return UITableViewCell()
    }
}
```

Responsibilities in VC: When retrieving Ad data, render the ad data on an AdCell, and when retrieving post data, render the post data on a cell. The VC does not handle the logic containing the data.

Responsibilities in Model (ViewModel): Merge different data models and handle logic, such as adding the ad at the last position if there are fewer than 4 posts, or inserting it at position 2 if there are more.

### Practical Application - Google AdMob

[Google AdMob on iOS](https://firebase.google.com/docs/admob?hl=en)

The link above is an application of Google AdMob. When you choose Native Ad, there will be ad data in your UITableView. You can use the method described above to transform AdMob data into your data model and then display it in the tableView.

## Complete code (requires installation of SnapKit, example uses SnapKit for Auto Layout)

### View Part

```swift
import SnapKit
import UIKit

extension AdTableViewCell {
    static var cellIdentifier: String {
        "AdTableViewCell"
    }
}

class AdTableViewCell: UITableViewCell {
    // UI setup omitted for brevity
}

extension PostTableViewCell {
    static var cellIdentifier: String {
        "PostTableViewCell"
    }
}

class PostTableViewCell: UITableViewCell {
    // UI setup omitted for brevity
}
```

### Model Part

```swift
import Foundation

func createAdArray() -> [AdModel] {
    // Example code for generating ad models
}

func createPostsArray() -> [Post] {
    // Example code for generating post models
}

class PostListModel {
    // Logic for combining posts and ads into a unified list
}
```

### VC Part

```swift
import SnapKit
import UIKit

class PostListViewController: UIViewController {
    // VC setup and UITableViewDataSource implementation
}
```

## Reference Websites

[Apple's Tutorial Project on UITableView](https://developer.apple.com/tutorials/app-dev-training/creating-a-list-view)

[Apple's Documentation on UITableView](https://developer.apple.com/documentation/uikit/uitableview)

[Firebase AdMob Documentation](https://firebase.google.com/docs/admob?hl=en)