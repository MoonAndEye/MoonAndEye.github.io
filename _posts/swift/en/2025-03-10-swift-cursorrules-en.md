---
layout: single  
title: Current Usage of cursorrules in iOS Development (2025.Mar.10th)  
date: 2025-03-10 15:27 +0800  
category: swift  
author: Marvin Lin  
tags: [Cursor, AI, Swift]  
summary:  With the introduction of Agent mode in Cursor, I have been actively using cursorrules for iOS development. While prompt-based development is now possible, I have started by leveraging cursorrules, though the MCP server is not yet set up. Currently, there are some great community-driven cursorrules resources available, but none specifically for iOS UIKit. To address this, I have drafted UIKit-specific cursorrules and submitted a pull request (PR) to the repository owner. However, I removed the ViewModel (VM) section, as its usage may not align with broader community consensus. The cursorrules emphasize Auto Layout with SnapKit, programmatic UI, MVC-compliant component access, ViewModel separation, closure-based event handling, and structured file organization. Once the PR is merged, iOS developers will have a well-structured UIKit cursorrules guide to follow.
---

Since Cursor introduced the Agent mode, I have been extensively using cursorrules for development. Of course, now development can be done with various prompts, and the MCP server has not yet been set up. But let's start with cursorrules first. Currently, there are some great awesome cursorrules available online.

[Awesome CursorRules](https://github.com/PatrickJS/awesome-cursorrules)

[SwiftUI CursorRules](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/swiftui-guidelines-cursorrules-prompt-file/.cursorrules)

### However, there are no iOS UIKit cursorrules in the current repository, so I am drafting one here  
I have submitted a PR to the repository owner, and we can observe the progress. Once the PR is merged, there will be iOS UIKit cursorrules available. However, I have removed the VM section from it. This guideline was formulated based on our company’s codebase style, and the use of ViewModel may not reach a consensus with the wider iOS developer community, so I excluded the ViewModel practice when submitting it.

#### iOS - UIKit cursorrules  

```  
// Start of Selection  
{% raw %}  
you are an expert in coding with swift, iOS, UIKit. you always write maintainable code and clean code.  
focus on latest documentation and features.  
your descriptions should be short and concise.  
don't remove any comments.  

UIKit UI Design Principles:  
1. **Auto Layout:** Implement responsive layouts using SnapKit only (avoid NSLayoutConstraint for better readability), support Dynamic Type and Safe Area.  
2. **Programmatic UI:** Avoid Storyboards/XIBs, implement all UI components directly in code (UIView, UIButton, UITableViewCell). Use view composition and custom view subclasses for reusability.  
3. **UI Components must not directly access models or DTOs.** Use ViewController, Factory, or Builder patterns following OOP/MVC/MVVM principles. Below are good and bad practice examples:  

**Good Practice:**  
```swift  
let user = User(name: "Alice", email: "john@example.com")  
let factory = UserFactory()  
/// This way UserView doesn't access User model directly, following Apple's MVC principles  
let userView = factory.createUserView(user: user)  
```  

**Bad Practice:**  
```swift  
let user = User(name: "Alice", email: "john@example.com")  
/// This exposes UserView to User model, violating MVC principles  
let userView = UserView(user: user)  
```  

4. **Every UIViewController should have a corresponding ViewModel** that handles all UI-related logic. Follow naming conventions: if the VC is named `UserListViewController`, the ViewModel should be named `UserListViewModel`. Communication between UIViewController and ViewModel should use closures.  

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

5. **UI components should pass events using closures, and the closure must pass `self` as a parameter** to allow external objects to identify the source component.  

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

### File Structure  
Each Scene is an independent module containing ViewController and ViewModel. UITableViewCell should be placed under `UI/Elements`. For future page requirements, each page will have its own dedicated directory containing ViewController and ViewModel.  

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