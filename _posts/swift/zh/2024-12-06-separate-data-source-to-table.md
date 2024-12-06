---
layout: single
title: UITableView, UICollectionView 的 DataSource 可以獨立一個物件
date: 2024-12-06 15:03 +0800
category: swift
author: Marvin Lin
tags: [Xcode, Swift]
summary: 
---

## UITableViewDataSource 是可以實作一個獨立物件的，範例用 Skeleton 效果為例子

通常我們會在 ViewController 中設定 UITableView 的 Delegate 和 DataSource，並把 DataSource 的實作寫在 ViewController 中。範例如下

```swift
    private lazy var tableView: UITableView = {
        let tableView = UITableView()
        tableView.delegate = self
        tableView.dataSource = self
        return tableView
    }()

    /// 然後在 ViewController 中實作 DataSource 的 protocol
```

但 UITableViewDataSource 也可以實作一個獨立物件的。

```swift
class SkeletonDataSource: NSObject, UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 20
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: SkeletonTableViewCell.reuseIdentifier, for: indexPath)
        return cell
    }
}
```

然後在 ViewController 中設定 DataSource 即可。

```swift
    private var isSkeletonDataSource = true
    
    private var skeletonDataSource = SkeletonDataSource()

    private lazy var tableView: UITableView = {
        let tableView = UITableView()
        tableView.delegate = self /// delegate 可以使定義在 ViewController 中
        tableView.dataSource = SkeletonDataSource() /// dataSource 則是 SkeletonDataSource
        return tableView
    }()

    /// ViewController 中切換 DataSource 的 function, 之後我們會用 button 來發動這個 function
    @objc 
    private func toggleDataSource() {
        isSkeletonDataSource.toggle()
        if isSkeletonDataSource {
            print("change to my data source")
            tableView.dataSource = skeletonDataSource
        } else {
            print("change to vc data source")
            tableView.dataSource = self
        }
        tableView.reloadData()
    }
```

## Skeleton 範例結果，使用 button 切換 DataSource

![skeleton effect on table view](/assets/swift/datasource-single-obj/skeleton_effect.gif)

## 其他延伸

這個方法我是看 Unit Testing TDD 的書學到的，在書中有提到，DataSource 獨立出來，可以更好的在 Unit Test 中進行測試。不過在實際開發中，我大多是用在 Skeleton 效果上，因為 skeleton 效果和場景單純。

### 附錄

整個 code

### SkeletonDataSource 程式碼
```swift
/// SkeletonDataSource.swift
class SkeletonDataSource: NSObject, UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 20
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: SkeletonTableViewCell.reuseIdentifier, for: indexPath)
        return cell
    }
}
```

### ViewController 程式碼

```swift
/// ViewController.swift
class ViewController: UIViewController {
    
    private lazy var toggleButton: UIButton = {
        let button = UIButton(type: .system)
        button.setTitle("Toggle Data Source", for: .normal)
        button.setTitleColor(.blue, for: .normal)
        button.addTarget(self, action: #selector(toggleDataSource), for: .touchUpInside)
        return button
    }()
    
    private var isSkeletonDataSource = true
    
    private var skeletonDataSource = SkeletonDataSource()
    
    @objc
    private func toggleDataSource() {
        isSkeletonDataSource.toggle()
        if isSkeletonDataSource {
            print("change to my data source")
            tableView.dataSource = skeletonDataSource
        } else {
            print("change to vc data source")
            tableView.dataSource = self
        }
        tableView.reloadData()
    }
    
    private lazy var tableView: UITableView = {
        let tableView = UITableView()
        tableView.delegate = self
        tableView.dataSource = skeletonDataSource
        return tableView
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        registerCell()
    }
    
    private func setupUI() {
        
        view.addSubview(toggleButton)
        toggleButton.translatesAutoresizingMaskIntoConstraints = false
        toggleButton.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor).isActive = true
        toggleButton.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
        toggleButton.widthAnchor.constraint(equalToConstant: 200).isActive = true
        toggleButton.heightAnchor.constraint(equalToConstant: 50).isActive = true
        
        view.addSubview(tableView)
        tableView.translatesAutoresizingMaskIntoConstraints = false
        tableView.topAnchor.constraint(equalTo: toggleButton.bottomAnchor).isActive = true
        tableView.leadingAnchor.constraint(equalTo: view.leadingAnchor).isActive = true
        tableView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor).isActive = true
        tableView.trailingAnchor.constraint(equalTo: view.trailingAnchor).isActive = true
    }
    
    private func registerCell() {
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "UITableViewCell")
        tableView.register(SkeletonTableViewCell.self, forCellReuseIdentifier: SkeletonTableViewCell.reuseIdentifier)
    }
}

extension ViewController: UITableViewDelegate, UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 10
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "UITableViewCell", for: indexPath)
        cell.textLabel?.text = "Cell \(indexPath.row)"
        return cell
    }
}

```
