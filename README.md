## MoonAndEye.github.io 網站

## Marvin Lin - 一個喜歡使用 Swift 進行開發的工程師

[![網站的圖片](./assets/landing.png)](https://moonandeye.github.io/)

## 客制化 Jekyll 加上去的 script
### 每月贊助的 banner，現在放在左邊 side bar
檔名: joinMembership.html

## 所有頁面上方的共用元件
是在 masthead.html 裡面，從 title 到 subtitle 都可以改

## 要加 <head></head> 或是 <body></body> 的地方
找到 _layouts/default.html, 在裡面添加對應的 html 即可

## 要加 <script></script> 的地方，如果你想添加 js 代碼
找到 _includes/scripts.html, 在裡面添加對應的 js 即可

### language switcher - for i18n
檔名: custom/language-switch.html
插在 _layouts/masthead.html title 後面

## 在上方 masthead.html 的分頁中