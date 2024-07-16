---
layout: single
title: 在 TableViewCell 中，使用 delegate pattern 反應使用者點擊 button 後的行為(按讚、追蹤、定閱、分享、小鈴噹)
date: 2023-05-06 22:47 +0800
category: swift
author: Marvin Lin
tags: [swift, design pattern, iOS]
summary: This article make an example of cell has an button, when user tapped the button, vc will response to the relative action. This article explained using delegate pattern to finish this feature.
permalink: /swift/:title:output_ext
classes: wide
---

如果要在 UITableViewCell 裡面的 UIButton 發動點擊，讓這個 button 點擊後，對這個 Cell 進行對應的動作，使用 delegate 的方法，是可以做到的。

從 [iOS 的 MVC 架構](https://moonandeye.github.io/swift/cocoa-framework-mvc.html) 這篇文章中，有解釋了 Cocoa design pattern 在設計上推薦使用 MVC 架構，而 View 和 VC 溝通的方式，是可以用 delegate pattern 進行實作的，如下圖(詳細可以看  [Delegate Pattern (委派模式)in Swift](https://moonandeye.github.io/swift/delegate-pattern-in-swift.html)  這篇文)。

[iOS MVC pattern](/assets/swift/mvc-pattern/mvc-ios.jpg)

## 以藝術家列表為例子

UI wireframe 如下，一個 cell 中有一張圖案，可能會放畫家的自畫像或代表作，然後旁邊有畫家的名字和流派，再加上一個可以 follow 的 button。按下去後，會收到系統對這個畫家的最新訊息，以及相關 feature。

![artist list](/assets/swift/deleagate-in-tableview/artistList.png)

### 藝術家 model 物件
```swift
/// 藝術家宣告
struct Artist {
    var id: Int
    var name: String
    var artStyle: String
    var isFollowed: Bool
}
```

### 藝術家 Cell，設定 delegate property

```swift
import UIKit
import SnapKit // 拿來拉 UI 的套件

/// VC conform 這個 delegate 後可以知道哪個 indexPath 的按鈕被點擊了
protocol ArtistInfoTableViewCellDelegate: AnyObject {
    
    func followButtonDidTap(indexPath: IndexPath)
}

class ArtistInfoTableViewCell: UITableViewCell {
    
    static let reuseIdentifier = "ArtistInfoTableViewCell"
    
    /// 讓 vc 成為 cell 的 delegate
    weak var delegate: ArtistInfoTableViewCellDelegate?
    
    /// 在 reuse 時，cell 需要知道自已是第幾個 cell
    var indexPath: IndexPath?
    
    /// artist image placeholder image，此範例用 SF symbol
    lazy var artistImageView: UIImageView = {
        let imageView = UIImageView()
        imageView.image = UIImage(systemName: "person.crop.circle.fill")
        return imageView
    }()
    
    /// artist name
    lazy var nameLabel: UILabel = .init()
    
    /// artist style
    lazy var artStyleLabel: UILabel = .init()
    
    /// follow button，在點擊的時候通知 delegate(也就是VC)，某個 indexPath 的 cell 被按了
    lazy var followButton: UIButton = {
        let button = UIButton(type: .system)
        button.setTitle("follow", for: .normal)
        button.addTarget(self, action: #selector(followButtonDidTap), for: .touchUpInside)
        return button
    }()
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        setupUI()
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
   
    private func setupUI() {
        /// UI layout，這邊沒有邏輯，都是 UI，可以略過
        contentView.addSubview(artistImageView)
        artistImageView.snp.makeConstraints { make in
            make.top.leading.equalToSuperview().offset(12)
            make.width.height.equalTo(50)
            make.bottom.lessThanOrEqualToSuperview().offset(-20)
        }
        
        contentView.addSubview(followButton)
        followButton.snp.makeConstraints { make in
            make.width.equalTo(120)
            make.height.equalTo(50)
            make.centerY.equalToSuperview()
            make.trailing.equalToSuperview().offset(-20)
        }
        
        nameLabel.text = "-"
        contentView.addSubview(nameLabel)
        nameLabel.numberOfLines = 2
        nameLabel.snp.makeConstraints { make in
            make.leading.equalTo(artistImageView.snp.trailing).offset(12)
            make.trailing.equalTo(followButton.snp.leading)
            make.top.equalToSuperview().offset(12)
        }
        
        artStyleLabel.text = "-"
        contentView.addSubview(artStyleLabel)
        artStyleLabel.snp.makeConstraints { make in
            make.leading.equalTo(nameLabel)
            make.top.equalTo(nameLabel.snp.bottom).offset(12)
        }
    }
    
    @objc private func followButtonDidTap() {
        guard let delegate = delegate,
              let indexPath = indexPath else {
            return
        }
        
        delegate.followButtonDidTap(indexPath: indexPath)
    }
}
```

### vc 在 cellForRowAt 中，設定好 cell 的 indexPath，並將自己設為 cell 的 delegate

```swift
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let index = indexPath.row
        
        guard let cell = tableView.dequeueReusableCell(withIdentifier: ArtistInfoTableViewCell.reuseIdentifier, for: indexPath) as? ArtistInfoTableViewCell,
              artists.indices.contains(index) else {
            return UITableViewCell()
        }
        
        /// 設定 index Path
        cell.indexPath = indexPath
        /// 讓 vc 成為 cell 的 delegate
        cell.delegate = self
        
        let artist = artists[index]
        
        cell.nameLabel.text = "name: \(artist.name)"
        cell.artStyleLabel.text = "style: \(artist.artStyle)"

        /// 省略 ui 的實作，有附在這篇文章的下面
        
        return cell
    }
```

### vc conform delegate

```swift
extension ArtistListViewController: ArtistInfoTableViewCellDelegate {
    
    /// 只要 button 被點擊了，這個 func 都會被發動
    func followButtonDidTap(indexPath: IndexPath) {
        /// 在這裡發動 follow / unfollow 
        print("you tapped button, indexPath: \(indexPath)")

        let isFollow = getIsFollow(at: indexPath)
        /// 後續實作省略，將 data model 的 isFollowed 狀態變更，並重新 reload cell at indexPath
    }
}
```

### VC 全部的程式碼

```swift

import UIKit
import SnapKit

class ArtistListViewController: UIViewController {
    
    /// 在範例中使用
    private lazy var artists: [Artist] = getMockArtists()
    
    private lazy var tableView: UITableView = {
        let tableView = UITableView()
        tableView.delegate = self
        tableView.dataSource = self
        return tableView
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        registerCell()
        setupUI()
        tableView.reloadData()
    }
    
    private func registerCell() {
        tableView.register(ArtistInfoTableViewCell.self, forCellReuseIdentifier: ArtistInfoTableViewCell.reuseIdentifier)
    }
    
    private func setupUI() {
        view.addSubview(tableView)
        tableView.snp.makeConstraints { make in
            make.leading.trailing.bottom.top.equalTo(view.safeAreaLayoutGuide)
        }
    }
}

extension ArtistListViewController: UITableViewDelegate, UITableViewDataSource {
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return artists.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let index = indexPath.row
        
        guard let cell = tableView.dequeueReusableCell(withIdentifier: ArtistInfoTableViewCell.reuseIdentifier, for: indexPath) as? ArtistInfoTableViewCell,
              artists.indices.contains(index) else {
            return UITableViewCell()
        }
        
        /// 指定 cell indexPath
        cell.indexPath = indexPath
        /// 將 vc 設定成 cell 的 delegate
        cell.delegate = self
        
        let artist = artists[index]
        
        cell.nameLabel.text = "name: \(artist.name)"
        cell.artStyleLabel.text = "style: \(artist.artStyle)"
        
        updateUI(cell, isFollowed: artist.isFollowed)
        
        return cell
    }
    
    private func updateUI(_ cell: ArtistInfoTableViewCell, isFollowed: Bool) {
        
        if isFollowed {
            cell.followButton.setTitle("unfollow", for: .normal)
            cell.followButton.layer.borderColor = UIColor.systemBlue.cgColor
        } else {
            cell.followButton.setTitle("follow", for: .normal)
            cell.followButton.layer.borderColor = UIColor.systemGray.cgColor
        }
    }
}

extension ArtistListViewController: ArtistInfoTableViewCellDelegate {
    
    func followButtonDidTap(indexPath: IndexPath) {
        
        print("you tapped button, indexPath: \(indexPath)")
        
        let index = indexPath.row
        
        guard artists.indices.contains(index) else {
            return
        }
        
        var artist = artists[index]
        artist.isFollowed = !artist.isFollowed
        /// 因為使用 struct，所以改完後要讓 artist 改
        artists[index] = artist
        
        /// 如果要有比較好的 UX 體驗，可以只 update 有變更的 row，並加上動畫
        tableView.reloadData()
    }
}

extension ArtistListViewController {
    
    /// 使用假資料
    private func getMockArtists() -> [Artist] {
        let mockArtists = [
            Artist(id: 1, name: "Vincent van Gogh", artStyle: "Post-Impressionism", isFollowed: false),
            Artist(id: 2, name: "Pablo Picasso", artStyle: "Cubism", isFollowed: false),
            Artist(id: 3, name: "Claude Monet", artStyle: "Impressionism", isFollowed: false),
            Artist(id: 4, name: "Salvador Dali", artStyle: "Surrealism", isFollowed: false),
            Artist(id: 5, name: "Leonardo da Vinci", artStyle: "Renaissance", isFollowed: false),
            Artist(id: 6, name: "Frida Kahlo", artStyle: "Surrealism", isFollowed: false),
            Artist(id: 7, name: "Edvard Munch", artStyle: "Expressionism", isFollowed: false),
            Artist(id: 8, name: "Georgia O'Keeffe", artStyle: "American Modernism", isFollowed: false),
            Artist(id: 9, name: "Gustav Klimt", artStyle: "Art Nouveau", isFollowed: false),
            Artist(id: 10, name: "Henri Matisse", artStyle: "Fauvism", isFollowed: false),
            Artist(id: 11, name: "Wassily Kandinsky", artStyle: "Abstract Art", isFollowed: false),
            Artist(id: 12, name: "Paul Cezanne", artStyle: "Post-Impressionism", isFollowed: false),
            Artist(id: 13, name: "Roy Lichtenstein", artStyle: "Pop Art", isFollowed: false),
            Artist(id: 14, name: "Rembrandt van Rijn", artStyle: "Baroque", isFollowed: false),
            Artist(id: 15, name: "Michelangelo", artStyle: "Renaissance", isFollowed: false),
            Artist(id: 16, name: "Johannes Vermeer", artStyle: "Baroque", isFollowed: false),
            Artist(id: 17, name: "Andy Warhol", artStyle: "Pop Art", isFollowed: false),
            Artist(id: 18, name: "Henri de Toulouse-Lautrec", artStyle: "Post-Impressionism", isFollowed: false),
            Artist(id: 19, name: "Gustave Courbet", artStyle: "Realism", isFollowed: false),
            Artist(id: 20, name: "Vincent Desiderio", artStyle: "Figurative Art", isFollowed: false)
        ]

        return mockArtists
    }
}
```

## 有沒有其他的方式可以做到一樣的事情

有，在 Swift 中另一個常用的傳值的方法，就是 closure。當然也可以使用 closure 讓 vc 被通知哪個 indexPath 的按鈕被按了。但 closure 的 coding style 會長得和 delegate style 不一樣。

## 參考網站

[iOS 的 MVC 架構](https://moonandeye.github.io/swift/cocoa-framework-mvc.html)

[Delegate Pattern (委派模式)in Swift](https://moonandeye.github.io/swift/delegate-pattern-in-swift.html)