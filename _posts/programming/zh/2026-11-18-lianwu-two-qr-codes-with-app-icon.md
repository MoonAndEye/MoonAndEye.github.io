---
layout: single
title: "一個連結、兩個 QR Code，中間放 app icon：我用 Lian Wu 做的"
date: 2026-11-18 00:40 +0800
category: programming
author: Marvin Lin
tags: [Lian Wu, QR Code, AI, Mac]
lang: zh
summary: "同一個連結做成兩個 QR Code，中間都放 app icon，各自配合會被看到的地方。再交給 Painter 放進場景，用之前兩張圖都讀回來確認。"
description: "同一個連結做成兩個 QR Code，中間都放 app icon，各自配合會被看到的地方。再交給 Painter 放進場景，用之前兩張圖都讀回來確認。"
---

*每一個設定和兩段 Painter 指令，都寫在 [Lian Wu 的使用範例](https://lianwu.app/use-cases/one-link-two-qr-codes-with-your-app-icon)（英文）。英文版：[One link, two QR codes with my app icon, made in Lian Wu](/en/programming/lianwu-two-qr-codes-with-app-icon/)。*

Lian Wu 的 QR Code 會出現在不只一個地方。黑白的 QR Code 當然能掃，但放哪裡都長一樣，也看不出是誰的。

所以我照我會建議小店家的做法來做：同一個連結，做成兩個 QR Code，中間都放 app icon，各自配合會被看到的地方。

## 第一個：街頭表演的小卡

街頭表演很輕鬆，QR Code 也可以活潑一點。我在 QR Coder 選了 Bubbles：圓點加上圓形的定位角。點用珊瑚色漸層，定位角另外給葉子綠。

接著把 app icon 拖到 QR Code 上，它就會放到正中間。容錯等級會自己拉到最高，所以放了 icon 也不會掃不到。每改一次，QR Coder 都會重新讀一次，我隨時知道它還能用。

## 第二個：咖啡店門口的大看板

同一個連結，換個地方。從街上看的看板，我會用比較樸素、比較紮實的樣式：Classic 方塊、單一深綠、珊瑚色定位角、icon 放大放在方形底上，再輸出 2048 px 給印刷用。

不用從頭做。QR Coder 會把每個 QR Code 存在 Saved，我直接打開第一個來改。

## 再交給 Painter 放進場景

按 Bring into Painter，QR Code 會帶過去，指令開頭已經寫好要保留三個定位角和黑白格的排列。我把吉祥物的圖當參考圖加進去，再描述場景：兩隻吉祥物在廣場街頭表演，第一個 QR Code 印在小卡上；另一隻站在 Lian Wu Café 門口，舉著手機造型的大看板，上面是第二個 QR Code。

## 我一定不跳過的一步：讀回來

AI 畫圖可能會動到 QR Code 的格子。所以每張圖用之前，我都拖進 QR Coder 的 Read。Apple 的 Vision 在 Mac 上直接讀，顯示它讀到什麼。讀回來是原本的連結，我才留下這張圖。

兩個場景第一次畫出來，就都讀回 `https://lianwu.app`。

老實說兩個限制。我是在 Mac 上用 Vision 讀的，還沒拿手機到真的街頭現場掃。另外我測過，兩個 QR Code 縮到大約 50 像素寬就讀不到了，所以印的時候要印大一點。

## 影片

四分半，沒有旁白，只有字幕，每一次點擊都是原速。

{% include youtube.html id="E7oaOCFQMes" title="Make one link into two QR codes with your app icon, each styled for where it is seen" %}
