---
layout: single
title: UITableViewDataSource Can Be Implemented as an Independent Object - An Example with Skeleton Effect
date: 2024-12-06 15:03 +0800
category: swift
author: Marvin Lin
tags: [Xcode, Swift]
summary: 
---

Usually, we set the UITableView's Delegate and DataSource within the ViewController and implement the DataSource logic directly in the ViewController, as shown in the example below:

```swift
private lazy var tableView: UITableView = {
    let tableView = UITableView()
    tableView.delegate = self
    tableView.dataSource = self
    return tableView
}()

/// Then implement the DataSource protocol in the ViewController
```

However, UITableViewDataSource can also be implemented as a separate object:

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

Then, set the DataSource in the ViewController:

```swift
private var isSkeletonDataSource = true

private var skeletonDataSource = SkeletonDataSource()

private lazy var tableView: UITableView = {
    let tableView = UITableView()
    tableView.delegate = self /// Delegate can still be defined in the ViewController
    tableView.dataSource = SkeletonDataSource() /// DataSource is assigned to SkeletonDataSource
    return tableView
}()

/// A function in the ViewController to switch between DataSources; this will be triggered by a button
@objc 
private func toggleDataSource() {
    isSkeletonDataSource.toggle()
    if isSkeletonDataSource {
        print("Switching to my data source")
        tableView.dataSource = skeletonDataSource
    } else {
        print("Switching to VC data source")
        tableView.dataSource = self
    }
    tableView.reloadData()
}
```

## Example of Skeleton Effect with a Button to Switch DataSources

![skeleton effect on table view](/assets/swift/datasource-single-obj/skeleton_effect.gif)

## Additional Thoughts

I learned this approach from a Unit Testing TDD book, which mentioned that separating the DataSource allows for better unit testing. In practice, I mostly use it for Skeleton effects because the Skeleton use case is straightforward and independent.

### Appendix

Complete code:

### SkeletonDataSource Code
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

### ViewController Code

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
            print("Switching to my data source")
            tableView.dataSource = skeletonDataSource
        } else {
            print("Switching to VC data source")
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