---
layout: single
title: Flyweight Pattern - Lightweight Mode (Flyweight Pattern)
date: 2024-07-17 13:35 +0800
category: swift
author: Marvin Lin
tags: [Swift, Design Pattern, Flyweight Pattern]
lang: en
summary: This article introduces the Flyweight Pattern using examples and scenarios from refactoring.guru.
classes: wide
---

### Flyweight Pattern - Lightweight Mode (Flyweight Pattern)

This article introduces the Flyweight Pattern using examples and scenarios from [refactoring.guru](https://refactoring.guru/design-patterns/flyweight).

Source: [https://refactoring.guru/design-patterns/flyweight](https://refactoring.guru/design-patterns/flyweight)

---

#### Scenario:

You've developed an FPS game featuring missiles, bullets, and various cool effects, which you and your friends have started to play.

### But, However, "It works on your machine"

On your friend's computer, the game crashes after a few minutes! The gaming experience on your friend's system is terrible. After debugging for several hours and sifting through the logs, you pinpoint the issue to RAM insufficiency. Your computer has superior specs, but your friend's doesn't, leading to RAM depletion.

The RAM consumption issues stem from the particle system you developed. Each particle, like bullets or missiles, spawns a particle object whenever it appears on the screen, eventually crashing the system due to RAM overload.

As shown in the image below, each particle takes up 21 KB. With 1,000,000 particles, that would require 21 GB of RAM.

![](https://cdn-images-1.medium.com/max/800/1*G4GebBvS7ZChon7wEhSvZg.png)

from refactoring.guru

Here's a scene from Overwatch.

![](https://cdn-images-1.medium.com/max/800/1*bZSGkmXGYofMadtii2wyGQ.png)

![](https://cdn-images-1.medium.com/max/800/1*UzKC0uTVHQXLaqTyZhmNNA.png)

How can the Flyweight pattern improve your game's performance?

---

### How Flyweight Reduces System Load

Revisiting the "Particle" class, consider the following:

![](https://cdn-images-1.medium.com/max/800/1*4dPir95Ideb9wzMRjK9hbg.png)

You'll notice two properties that can be made immutable (internal data):

*   color
*   sprite

Other attributes that vary (external data) include:

*   particle
*   coordinates
*   vector
*   speed

![](https://cdn-images-1.medium.com/max/800/1*5r80IzFWvGH9MCL0Kgm8nA.png)

Looking back at the system:

![](https://cdn-images-1.medium.com/max/800/1*5yXJEnkUFcrlOgFIqbz86g.png)

The most resource-intensive element remains the sprite. With the same number of particles and without initializing new internal data, the requirement is 32MB of RAM. In contrast to the non-design pattern scenario requiring 21 GB, this design allows the game to run smoothly even on your friend's computer.

---

Is it over? Have we fully utilized the design pattern?

### **Design patterns can be layered!**

---

### Adding an External Object Pool for Further Optimization

In practice, an "object pool" is often added to store the "internal information."

In this case, since there is a main class, Game, that stores Particles, the system first checks the pool for unused particles to reuse them by injecting "external information" (vector, speed, coordinates). If no suitable particles are in the pool, a new one is initialized.

![](https://cdn-images-1.medium.com/max/800/1*9oTHsQUlMpuXtZcj47OviA.png)

Once a particle is no longer needed, it is returned to the pool for future use.

This can be seen as a combination of the Object Pool and Flyweight patterns. In UIKit, an essential component uses this hybrid approach.

Further optimizations are made even to the external information using another layer of the Flyweight pattern.

Flyweight of a Flyweight. There's always room for finer detail.

---

Further into your career, you might not start in a "real" game company in Taiwan; you could be an iOS frontend developer. No matter your field, everyone starts with frameworks in 2022. If you are an iOS frontend developer, consider which system components in iOS might be applying the "Flyweight Pattern (Flyweight Pattern)."

By [Marvin Lin](https://medium.com/@atimis19) on [August 10, 2022](https://medium.com/p/a5ab3b6054f).

[Canonical link](https://medium.com/@atimis19/flyweight-pattern-%E8%A0%85%E9%87%8F%E7%B4%9A%E6%A8%A1%E5%BC%8F-%E4%BA%AB%E5%85%83%E6%A8%A1%E5%BC%8F-a5ab3b6054f)