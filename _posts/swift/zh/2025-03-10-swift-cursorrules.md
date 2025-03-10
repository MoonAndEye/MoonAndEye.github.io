---
layout: single
title: 在 iOS 開發上，現在使用的 cursorrules (2025.Mar.10th)
date: 2025-03-10 15:28 +0800
category: swift
author: Marvin Lin
tags: [Cursor, AI, Swift]
summary: With the introduction of Agent mode in Cursor, I have been actively using cursorrules for iOS development. While prompt-based development is now possible, I have started by leveraging cursorrules, though the MCP server is not yet set up. Currently, there are some great community-driven cursorrules resources available, but none specifically for iOS UIKit. To address this, I have drafted UIKit-specific cursorrules and submitted a pull request (PR) to the repository owner. However, I removed the ViewModel (VM) section, as its usage may not align with broader community consensus. The cursorrules emphasize Auto Layout with SnapKit, programmatic UI, MVC-compliant component access, ViewModel separation, closure-based event handling, and structured file organization. Once the PR is merged, iOS developers will have a well-structured UIKit cursorrules guide to follow.
---

在 Cursor 有 Agent 模式後，我已經大量的在使用 cursorrules 開發。當然現在開發可以下各種 prompt 進行，也還沒架出 MCP server。但先從 cursorrules 開始。現在網路上不錯 awesome cursorrules. 

[Awesome CursorRules](https://github.com/PatrickJS/awesome-cursorrules)

[SwiftUI CursorRules](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/swiftui-guidelines-cursorrules-prompt-file/.cursorrules)

### 但是，現在的 repo 沒有 iOS UIKit 的 cursorrules，這邊先試寫一本
我已經提交了 PR 給 repo 的擁有者，這邊可以看後續的狀況，等到 PR 合併了，那就會有 iOS UIKit 的 cursorrules。只是我把 VM 那一段拿掉了，這個規範圍是在公司 code base style 的狀況下擬出來的，VM 的用法可能無法和 iOS 開發者社群取得共識，所以在提交時移除了 ViewModel 的 practice.

#### iOS - UIKit cursorrules


```
// Start of Selection
{% raw %}
you are an expert in coding with swift, iOS, UIKit. you always write maintainable code and clean code.
focus on latest documentation and features.
your descriptions should be short and concise.
don't remove any comments.


UIKit UI Design Principles:
1. Auto Layout: Implement responsive layouts using SnapKit only (avoid NSLayoutConstraint for better readability), support Dynamic Type and Safe Area
2. Programmatic UI: Avoid Storyboards/XIBs, implement all UI components directly in code (UIView, UIButton, UITableViewCell). Use view composition and custom view subclasses for reusability
3. UI Components must not directly access models or DTOs. Use ViewController, Factory, or Builder patterns following OOP/MVC/MVVM principles. Below are good and bad practice examples:

good practice:
```swift
let user = User(name: "Alice", email: "john@example.com")
let factory = UserFactory()
/// This way UserView doesn't access User model directly, following Apple's MVC principles
let userView = factory.createUserView(user: user)
```

bad practice:
```swift
let user = User(name: "Alice", email: "john@example.com")
/// This exposes UserView to User model, violating MVC principles
let userView = UserView(user: user)
```
4. Every UIViewController should have a corresponding ViewModel that handles all UI-related logic. Follow naming conventions: if the VC is named UserListViewController, the ViewModel should be named UserListViewModel. Communication between UIViewController and ViewModel should use closures.

```swift
class UserListViewModel {
    let users: [User]
    var didFetchUsers: (() -> Void)?
    func fetchUsers() {
        // fetch users from network
        didFetchUsers?()
    }
}

class UserListViewController: UIViewController {
    private lazy var viewModel: UserListViewModel = {
        let viewModel = UserListViewModel()
        viewModel.didFetchUsers = { [weak self] in
        guard let self else { return }
            tableView.reloadData()
        }
        return viewModel
    }()
    let tableView = UITableView()
}
``` 

5. UI components should pass events using closures, and the closure must pass 'self' as a parameter to allow external objects to identify the source component

```swift
class SampleView: UIView {
    var didTapButton: ((SampleView) -> Void)?
    private let button = UIButton()
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupUI()
        button.addTarget(self, action: #selector(buttonTapped), for: .touchUpInside)
    }

    private func setupUI() {
        // setup UI
    }

    @objc private func buttonTapped() {
        didTapButton?(self)
    }
}
```


File Structure
Each Scene is an independent module containing ViewController and ViewModel. UITableViewCell should be placed under UI/Elements. For future page requirements, each page will have its own dedicated directory containing ViewController and ViewModel
```
Project
├── UI
│   ├── MainTabBar
│   │   ├── ViewControllers
│   │   ├── ViewModels
│   │   └── Views
│   ├── Scenes
│   │   ├── ArticleFeed
│   │   │   ├── ViewController
│   │   │   ├── ViewModel
│   │   │   
│   │   │   
│   │   └── UserProfile
│   │       ├── ViewController
│   │       ├── ViewModel
│   │       
│   │       
```
{% endraw %}