---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜Unit test 寫什麼：購物車打 30% off，加總再打和每件各打是兩個 case - Tip 09"
date: 2026-09-21 13:00 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - Unit Test
  - JavaScript
  - 購物車
  - 金額精度
summary: "用購物車折扣拆解 unit test：加總後打折與每件各自打折是兩條規則，還要測到金額精度與空車邊界。"
description: "用購物車折扣拆解 unit test：加總後打折與每件各自打折是兩條規則，還要測到金額精度與空車邊界。"
---

本文同步刊登於 [iT 邦幫忙](https://ithelp.ithome.com.tw/articles/10414812)。

Unit test 要寫。寫什麼？拿購物車打折當例子：全部加總再打 30% off，跟每一件各打 30% off 再加總，是兩個 case，兩個都要寫。

## 為什麼

這兩種算法聽起來一樣，算出來的錢可能差一點。三件 19.99 的東西：加總是 59.97，打 30% off 是 41.98；每件先打 30% off 變 13.99，三件加起來是 41.97。差了 0.01，帳對不起來常常就是差在這裡。

產品要的是哪一種，得先定下來。定下來之後寫成測試，他改購物車的程式時，哪一種算法被動到，測試會先叫。

## 我怎麼做

至少這幾個 case：

1. 空的購物車，總價 0
2. 一件 100 元，30% off，總價 70
3. 三件 19.99，加總再打 30% off，總價 41.98
4. 三件 19.99，每件各打 30% off 再加總，總價 41.97

寫成測試大概像這樣（用 JavaScript 的測試框架當例子）：

```js
test("空車", () => {
  expect(discountOnTotal([], 0.3)).toBe(0);
});

test("加總再打 30% off", () => {
  expect(discountOnTotal([19.99, 19.99, 19.99], 0.3)).toBe(41.98);
});

test("每件各打 30% off 再加總", () => {
  expect(discountPerItem([19.99, 19.99, 19.99], 0.3)).toBe(41.97);
});
```

第三、第四個 case 一起寫，規則才說得清楚：要的是哪一種，另一種算出來會差多少。

## 坑

- 浮點數。19.99 × 0.7 是 13.993，59.97 × 0.7 是 41.979，兩個函式算完都要先四捨五入到分再比，測試才過得了；或者一開始就用整數的「分」算。
- 空車、一件、多件都要有 case，邊界最容易漏。

## 小結

Unit test 寫的是規則：加總再打折和每件各打折，各一個 case，數字要算到分。

明天講 iOS 開發另一個好用的東西：XcodeBuildMCP，讓他自己 build、自己跑 simulator。
