---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜Git 的技巧：別一直在 main 上做，開分支、開 release、打 tag - Tip 04"
date: 2026-09-16 13:01:57 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - Git
  - Branch
  - Release
  - Tag
summary: "我把 Git 的基本習慣定成三件事：功能不直接堆在 main、要出版本開 release branch、每次發布都打 tag。"
description: "我把 Git 的基本習慣定成三件事：功能不直接堆在 main、要出版本開 release branch、每次發布都打 tag。"
---

我用 git 的原則很簡單：**別一直在同一條 branch 上做**，尤其是 main。要有開分支的習慣。

## 為什麼

Vibe Coding 的時候，他改東西很快，量也大。全部堆在 main 上，哪一次改壞了、想退回去，會很難挑。一條 branch 只做一件事，做壞了整條丟掉，main 還是乾的。

## 我怎麼做

三個習慣：

1. **開 feature branch**。一個功能一條 branch，做完再併回 main。mobile 或 client 端也照這個習慣，main 上只留做好的東西。
2. **開 release branch**。要出一個版本，從 main 開一條 release branch，這個版本要修的東西都在這條上，main 可以繼續往前走。
3. **打 tag**。出去的版本打一個 tag，之後要回頭看某一版長什麼樣子，直接 checkout 那個 tag。

指令就這幾行：

```bash
# 開一條 branch 做事
git switch -c feat/login

# 做完、測過，併回 main
git switch main
git merge feat/login

# 要出版本：從 main 開 release branch
git switch -c release/1.2.0

# 版本出去了：打 tag
git tag -a v1.2.0 -m "1.2.0"
git push origin v1.2.0
```

這些事也可以直接叫他做。開始一件事之前跟他說「先開一條 branch 再改」，做完再叫他併回去、打 tag。

## 小結

一個功能一條 feature branch；要出版本時開 release branch，發布的版本打 tag。

明天講它要放到哪裡去給人用：我做原型的時候，domain、前端、後端、資料庫都放在 Cloudflare。
