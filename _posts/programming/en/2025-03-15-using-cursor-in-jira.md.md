---
layout: single
title: Using Cursor for Writing GWT (Given-When-Then) Requirements in Jira for Non-Development Roles
date: 2025-03-15 11:37 +0800
category: programming
author: Marvin Lin
tags: [Cursor, AI]
summary: 
---


Since 2025, I have been extensively using Cursor in my daily development work. However, if we think broadly, Cursor's text output capabilities can extend beyond just "programming". If Project Managers in the team use Cursor for creating tickets, could developers quickly bridge the gap between natural language and programming language, leading to faster development? Let's start with downloading Cursor IDE.

## [Cursor IDE Download](https://www.cursor.com/)

[![Cursor IDE Landing Page](/assets/programming/cursor-in-jira/cursor_landing.png)](https://www.cursor.com/)

## Expanding Model Selection in Cursor

By default, model expansion includes Claude series and ChatGPT4o-mini, cursor-small, but Gemini 2.0 or ChatGPT o1 are not enabled by default. To use other models, you need to enable them in Cursor settings.

![Cursor settings](/assets/programming/cursor-in-jira/cursor_setting_touch.png)

Here you can choose different models by selecting the ones you want to use. Each model has its characteristics - for example, deepseek-v3 is very fast, while deepseek-r1 or claude-sonnet 3.7 with think have thinking capabilities.

![Cursor models choose](/assets/programming/cursor-in-jira/cursor_models_choose.png)

## Right Sidebar - Start Using AI Assistance (cmd + shift + B)

In this sidebar, you can write your questions, task requirements, or ask about architecture. For project management roles, you can certainly write GWT (Given-When-Then) Jira tickets.

![Cursor right bar](/assets/programming/cursor-in-jira/cursor_right_bar.png)

## Left Sidebar - Folder Navigation, Search, Installed Plugins (cmd + B)

**File Navigation (Folder Navigation)**
- Displays project directory tree structure
- Supports quick file/folder creation (right-click > New File/Folder)
- Drag and drop files to move them
- Shortcut: Cmd + 1 to focus on file navigation

**Global Search**
- Cross-file content search (supports regex)
- Filter search scope: file types/symbol types (classes/methods/properties)
- Shortcut: Cmd + Shift + F

**Plugin Management**
- Shows list of installed extensions
- One-click access to [Cursor Marketplace](https://www.cursor.com/marketplace)
- Shortcut: Cmd + Shift + X to open extension management

![Cursor left bar](/assets/programming/cursor-in-jira/cursor_left_bar.png)

If you have too many installed plugins to display, they will be listed in a dropdown menu that you can expand

![Cursor left drop list](/assets/programming/cursor-in-jira/cursor_left_drop_list.png)

## Installing Jira Project Management Plugin - [Jira Atlassian](https://marketplace.visualstudio.com/items?itemName=Atlassian.atlascode)

Working without switching windows naturally improves efficiency. In this marketplace, there's a Jira plugin available. First select marketplace, then search for Jira, and click install. You can then start editing/modifying Jira tickets directly in VSCode or Cursor.

![Jira plug in](/assets/programming/cursor-in-jira/cursor_jira_plug_in.png)

## Create a Folder to Start Writing Jira Tickets or Any Documents
Basic usage - use folders to manage your documents, regardless of their type. While git version control has a learning curve, non-developers can use fileName_yyyyMMdd_version for version control. This is because document writing differs from programming - documents might need multiple versions for comparison, while code only needs one version for release.

First, create a folder

![create folder image](/assets/programming/cursor-in-jira/create_demo_folder.png)

Open Cursor and select that folder

![choose folder by folder](/assets/programming/cursor-in-jira/open_by_cursor.png)

You can use this icon to create files directly
![create files](/assets/programming/cursor-in-jira/create_files.png)

Now you can start writing with AI
![Using AI create](/assets/programming/cursor-in-jira/start_with_ai.png)

## Explanation of Agent, Ask, and Edit Modes

Cursor allows you to select different models for your tasks.

Ask: Similar to ChatGPT's interface, it responds to your prompts and displays responses in the sidebar.

Edit: AI gains the ability to modify files based on instructions. After modifications, you can Accept or Reject the changes.

Agent: Can handle more abstract commands and has the ability to create new files, rename files, and control the terminal. Due to its abstract nature and increased control capabilities, when using YOLO mode, it's recommended to monitor its responses closely. For example: you can request to translate a file into English/German/Russian/Japanese, saving each translation with different language codes. "If successful," Agent will complete the translations and create my_text_en.txt, my_text_ge.txt, my_text_ru.txt, my_text_jp.txt.

![Chat with diff models](/assets/programming/cursor-in-jira/chat_with_diff_models.png)

Now you can start using AI to assist in creating Jira tickets.

---

Next, you can try this section to generate documents in Agent mode.

```
Please write the following requirements in GWT (Given-When-Then) format:
login
logout
reset password
```


I'll help you write the login, logout, and reset password requirements using the Given-When-Then format:

### Login Function

```gherkin
Feature: User Login

Scenario: Successful Login
Given user is on the login page
When user enters correct username and password
And clicks the login button
Then system should successfully log in
And redirect to homepage
And display login success message

Scenario: Login Failure - Invalid Credentials
Given user is on the login page
When user enters incorrect username or password
And clicks the login button
Then system should display error message
And user remains on login page
```

### Logout Function

```gherkin
Feature: User Logout

Scenario: Successful Logout
Given user is logged into the system
When user clicks the logout button
Then system should log out the user
And clear user's login status
And redirect to login page
And display logout success message
```

### Reset Password Function

```gherkin
Feature: Reset Password

Scenario: Request Password Reset
Given user is on the forgot password page
When user enters their registered email
And clicks the reset password button
Then system should send a password reset link to the email
And display confirmation message

Scenario: Use Password Reset Link
Given user clicks the reset password link from email
When user enters new password
And confirms new password
And clicks confirm button
Then system should update user's password
And display password reset success message
And redirect to login page

Scenario: Reset Password Failure - Invalid Password Rules
Given user is on the reset password page
When user enters a password that doesn't meet requirements
And clicks confirm button
Then system should display password rule error message
And user remains on reset password page
```

These GWT format requirement descriptions cover the main use cases and expected results. Each function includes both success and failure scenarios, and clearly states:
1. Initial state (Given)
2. User actions (When)
3. Expected system responses (Then)

If you need more detailed scenarios or other special cases, I can help you further supplement them.
