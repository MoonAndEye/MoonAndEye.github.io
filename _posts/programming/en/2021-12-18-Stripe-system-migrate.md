---
layout: single
title: "The Process of Stripe's Incremental System Upgrade"
date: 2021-12-18 15:11 +0800
category: programming
author: Marvin Lin
tags: [system design, migration]
lang: en
summary: "Stripe is a well-known payment service. This article discusses the process of Stripe's incremental system upgrades."
---

Historically, if a railway track's width needed to be upgraded, they wouldn't just add two more tracks over the existing ones. Instead, they would build a new track alongside the old, allowing trains of different gauges to run simultaneously. Only when all the trains of one gauge were phased out would the unused track be removed.

### The Process of Stripe's Incremental System Upgrades

![](https://cdn-images-1.medium.com/max/800/1*kVy_4E7Jw81-keZ1SwVu1g.png)

### Stripe's Online Migrations

[**Online migrations at scale**  
_Jacqueline Xu on February 2, 2017, in Engineering Engineering teams face a common challenge when building software: they…_stripe.com](https://stripe.com/blog/online-migrations "https://stripe.com/blog/online-migrations")

The following is organized after reading the Stripe article:

Online payments are the main business, and if you want the ability to receive payments from abroad, it's much faster to go directly through Stripe than dealing with local banks. Moreover, expanding business into different countries can mostly be handled on Stripe.

One of Honest Bee's online payment solutions is Stripe.

Why "one of"? Because among the seven Asian countries where it was operating at the time, a few were not within Stripe's operational scope, prompting the introduction of another third-party payment platform.

### Scale of Stripe Users

The article mentions the Subscription object, which might represent individual companies or businesses. The quantity is in the hundreds of millions, so by 2017, the figures were in the hundreds of millions.

These hundreds of millions of records are stored in a table and are heavily utilized across several places in the codebase.

Moreover, the payment service cannot be disrupted, so the migrations used by Stripe are always online.

### Online Migration Pattern — Four Steps

1: **Dual writing** to the existing and new tables to keep them in sync.

Data must be written to both the existing and the new table simultaneously.

2: **Changing all read paths** in our codebase to read from the new table.

All reading paths must be switched.

3: **Changing all write paths** in our codebase to only write to the new table.

All writing paths must be switched.

4: **Removing old data** that relies on the outdated data model

The old data (likely archived) should be removed.

### Migration Example

### Initial Business Logic

Each customer would have a Subscription, but initially, it was designed with just one.

    class Customer  Subscription subscriptionend

As the business grew and customer needs became more complex, features such as coupons, discounts, and invoices were added, necessitating the change from subscription to subscriptions.

    class Customer  array: Subscription subscriptionsend

As the customer base reached a certain size, it became necessary to partition the database, which you can refer back to CH6.

The left side shows the existing design, and the right side shows the structure to be migrated.

Now, let’s revisit the four-step migration pattern.

1: **Dual writing** to the existing and new tables to keep them in sync.

2: **Changing all read paths** in our codebase to read from the new table.

3: **Changing all write paths** in our codebase to only write to the new table.

4: **Removing old data** that relies on the outdated data model

### Part1: Dual Writing

Any new data entry triggers a program that moves this subscription data to the new table. Then, backfilling occurs, moving previous data into the new table.

Stripe uses the Scalding package for backfilling, which is built on the Hadoop cluster, thus also using MapReduce. It only needs about ten lines of code.

Steps for backfilling include:

*   Write a Scalding job that provides a list of all subscription IDs that need to be copied over.
*   Run a large, multi-threaded migration to efficiently duplicate these subscriptions with a fleet of processes operating in parallel.
*   Once the migration is complete, run the Scalding job again to ensure no existing subscriptions are missing from the Subscriptions table.

### Part2: Changing All Read Paths

The previous action synchronized the old and new tables. Now, all reading paths originally using the old table must be redirected to the new table.

To ensure the data read from the new subscriptions table is accurate (and matches the old table), Stripe used the Scientist package to validate this process.

[https://github.com/github/scientist](https://github.com/github/scientist)

Scientist, a Ruby library, is used for experimental comparison of results. It reads from both the new and old tables, cross-verifies the values, and triggers an error alert if discrepancies are found.

Once the new and old tables are confirmed to be identical, the reading paths are switched to the new subscriptions table.

### Part3: Changing All Write Paths

The initial writing paths were set for dual writing. Now, the dual write would first write data to the old customers table and then to the subscriptions table. In the step of Changing All Write Paths, we reverse this order, first writing to Subscriptions and then to customers. Note, this step does not immediately remove writing to the customers table; it reverses the order to allow monitoring and prevent significant errors from continuing unknowingly.

Switching writing paths is the biggest challenge of the migration. In Stripe, thousands of lines of code related to subscriptions are scattered across various services.

To carefully validate each step during refactoring, Stripe minimized the code paths as much as possible, replacing them step by step to ensure synchronization of the new and old tables.

In replacing, great care was taken to prevent new records from directly overwriting old records, as any miss could cause data inconsistency. Stripe also used the functionalities provided by the Scientist package to confirm data accuracy before and after the switch.

Finally, in the Customer object, writing 'raise error' ensures that any call to the original subscriptions will trigger an error.

    class Customer  def subscriptions    Opus::Error.hard("Accessing subscriptions array on customer")  endend

Part4: **Removing Old Data**

The last step involves removing the code that writes data into the old table. Finally, once all code accesses data only from the subscriptions table, the old writing paths can be removed.

At the end, the migration completes, and data for subscriptions is fetched from the new table.

By [Marvin Lin](https://medium.com/@atimis19) on [December 18, 2021](https://medium.com/p/d2c7e73e298b).

[Canonical link](https://medium.com/@atimis19/stripe-%E7%B3%BB%E7%B5%B1%E6%BC%B8%E9%80%B2%E5%BC%8F%E5%8D%87%E7%B4%9A%E7%9A%84%E9%81%8E%E7%A8%8B-d2c7e73e298b)