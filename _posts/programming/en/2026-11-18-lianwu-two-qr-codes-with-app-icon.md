---
layout: single
title: "One link, two QR codes with my app icon, made in Lian Wu"
date: 2026-11-18 00:40 +0800
category: programming
author: Marvin Lin
tags: [Lian Wu, QR Code, AI, Mac]
lang: en
summary: "One link, two QR codes with the app icon in the middle, each styled for where it is seen. Then Painter puts each in a scene, and I read both pictures back before using them."
description: "One link, two QR codes with the app icon in the middle, each styled for where it is seen. Then Painter puts each in a scene, and I read both pictures back before using them."
---

*The step-by-step version, with every setting and both Painter requests, is on [Lian Wu's use cases](https://lianwu.app/use-cases/one-link-two-qr-codes-with-your-app-icon).*

Lian Wu's QR code is going to be seen in more than one place. A plain black-and-white code works, but it looks the same everywhere, and nobody can tell whose it is.

So I made the code the way I'd want any small shop to make theirs: one link, two codes, the app icon in the middle of both, each styled for where people will see it.

## Code one: a card at a street show

A street show is playful, so the code should be too. In QR Coder I picked the Bubbles look: round dots and round corner markers. The dots get a coral gradient, the markers their own leaf green.

Then I dropped the app icon on the code. It goes in the middle, and error correction goes up to the strongest by itself, so the icon doesn't cost the code its scan. QR Coder reads the code again after every change, so I always know it still works.

## Code two: a giant sign outside a café

Same link, different place. A sign seen from the street gets a plainer, stronger look: Classic squares in one dark green, coral corner markers, a bigger icon on a square, and 2048 px for print.

I didn't start over. QR Coder keeps every code under Saved, so I opened code one and changed it.

## Then Painter puts each code in its scene

Bring into Painter sends the code over with a request that already says to keep the corner squares and the pattern. I added the mascot picture as a reference and described the scene: two mascots busking with code one on a card, and one mascot outside Lian Wu Café holding a giant phone-shaped sign with code two.

## The step I never skip: read it back

A drawing can change a code's squares. So before I use a picture, I drop it on QR Coder's Read. Apple's Vision reads it on the Mac and shows what it says. I keep a picture only if it reads back as the link.

Both scenes read back as `https://lianwu.app` on the first draw.

Two honest limits. I read them on the Mac with Vision, not yet with a phone at a real street show. And in my test, both codes stopped reading when I shrank them to about 50 pixels wide, so print them big.

## The film

Four and a half minutes, no voice, captions only, every click at its own speed.

{% include youtube.html id="E7oaOCFQMes" title="Make one link into two QR codes with your app icon, each styled for where it is seen" %}
