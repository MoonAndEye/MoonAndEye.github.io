---
layout: single
title: "I Read X's Algorithm Code. Here's What Changed in November."
date: 2026-11-17 16:00 +0800
category: programming
author: Marvin Lin
tags: [X, Twitter, Recommendation Algorithm, Growth, Open Source]
lang: en
summary: "I read X's open-source recommendation code. In November, likes and dwell time went up, copy-link shares went to zero, and small accounts still get a 2-hour cold-start window."
description: "I read X's open-source recommendation code. In November, likes and dwell time went up, copy-link shares went to zero, and small accounts still get a 2-hour cold-start window."
---

I went through X's open-source recommendation code, the [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) repo, so you don't have to.

Everything below comes from the code as of commit [a284320](https://github.com/xai-org/x-algorithm/commit/a284320b66a9dce35e6f5d6b052ee308eeb12326) (November 17, 2026). X pushed 11 updates in November, and 403 files changed since the last October snapshot. Most of that is plumbing. A few lines matter a lot if you're a small account trying to grow.

One caveat first: the weight file says it is "mirrored from config feature-switch defaults." These are defaults. X can run experiments that override them for some users. Treat this as the best public map we have, not a guarantee.

## How X scores a post in your For You feed

For each candidate post, a model predicts how likely you are to do each action: like, reply, repost, share, dwell, mute, report, and so on. Each prediction is multiplied by a weight, and the results are added up into one score.

The code comment is very clear that these weights multiply *predicted probabilities*, not raw counts. So "one report cancels 468 likes" is wrong, and the comment says so directly. Reports are rare, so the report weight is large just to make it matter at all.

Keep that in mind. A weight tells you what X values. It doesn't give you an exchange rate between likes and replies.

## What changed in November

### November 5: likes and dwell up, clicks down

Commit [021afa4](https://github.com/xai-org/x-algorithm/commit/021afa4) changed these weights in [`home-mixer/params/param.rs`](https://github.com/xai-org/x-algorithm/blob/a284320b66a9dce35e6f5d6b052ee308eeb12326/home-mixer/params/param.rs):

| Signal | Before | After |
|---|---|---|
| Like | 0.66 | 0.708 |
| Continuous dwell time | 0.006 | 0.0075 (+25%) |
| Click | 0.3 | 0.274 |
| Dwell time after clicking in | 0.4 | 0.385 |
| Video open | 0.02 | 0 |
| Share | 2.0 | 2.118 |
| Not interested | −52.272 | −53.07 |

The +25% is for continuous dwell time only. The weight for dwell after clicking into a post went *down* slightly.

The same commit switched on `EnableHomeExcursionScores` and moved the model aggregation to `DENSE_WITH_LONG_DWELL_HOME_EXCURSION`. In plain words, X now also looks at what you do after leaving the feed from a post. But in the open-sourced ranker defaults, the related seconds weights (video continuation, profile visit seconds) are still 0.0. So the code doesn't yet show how much this counts.

### November 14: copy link went from 20 to 0

Commit [590f392](https://github.com/xai-org/x-algorithm/commit/590f392) (November 13, 21:42 UTC) dropped "share via copy link" from 20 to 0.

That was one of the two biggest positive weights. It was tied with a reply from a mutual follower (5 + 15 = 20). Now copying a link to your post adds nothing. Sharing by DM still carries 5.

### November 14–17: ranker plumbing

Commit [30647a8](https://github.com/xai-org/x-algorithm/commit/30647a8) turned on sending ranking history to the value-model ranker. Then [a284320](https://github.com/xai-org/x-algorithm/commit/a284320b66a9dce35e6f5d6b052ee308eeb12326) turned it back off, and added a `ValueModelMode` setting (default `weighted`) plus new "not dwelled" power parameters that default to 0. Nothing here changes how you should post today, but the ranker is clearly in motion.

## What did *not* change

These weights are the same as before November:

| Signal | Weight |
|---|---|
| Reply | 5 |
| Extra boost: reply from a mutual follower | +15 |
| Quote | 5 |
| Share via DM | 5 |
| Follow the author | 4.0 |
| Repost | 1 |
| Open a link | +0.2 |
| Profile click | 0 |
| Block author | −31.2 |
| Mute author | −58.8 |
| Report | −234 |

Two things stand out:

- **Links aren't penalized in the weight table.** Opening a link is a small *positive* (+0.2).
- **Video, by itself, earns nothing.** Video open, video quality view and "post has video" weights are all 0. A video only helps if it makes people like, reply, stay or follow.

## The distribution rules that matter more than weights

### Cold start: a free slot for small accounts

[`author_cold_start.rs`](https://github.com/xai-org/x-algorithm/blob/a284320b66a9dce35e6f5d6b052ee308eeb12326/home-mixer/scorers/author_cold_start.rs) gives small authors a shot. A post is eligible when:

- the author has 50,000 followers or fewer,
- it's an original post (not a reply or a repost),
- it's no more than 2 hours old,
- and it has fewer than 200 home-timeline impressions.

From the eligible posts, X samples by like rate (likes ÷ home impressions, with a prior of about 1.5%), keeps the top 2, and picks the one the model scores higher. That post gets lifted to around the 16th position of the feed (the code uses slot 15 to 16).

It runs as an experiment with treatment and control groups, so not everyone sees it. But it's the clearest rule in the repo written for small creators.

### Out of network costs 25%

When your post is shown to people who don't follow you, the score is multiplied by 0.75 (`OonWeightFactor` in [`vm-ranker/params.rs`](https://github.com/xai-org/x-algorithm/blob/a284320b66a9dce35e6f5d6b052ee308eeb12326/vm-ranker/params.rs)).

### Replies don't travel out of network

`OONRetweetReplyFilter` removes replies and reposts from For You for people outside your network. (A switch to allow some replies exists, but it's off by default.) Your replies are seen by your followers and in the thread, not by strangers' feeds.

### Posting a lot has diminishing returns

Author diversity is on. In [`xai-value-model/scoring.rs`](https://github.com/xai-org/x-algorithm/blob/a284320b66a9dce35e6f5d6b052ee308eeb12326/xai-value-model/scoring.rs), the multiplier is `0.75 × 0.5^k + 0.25`, where k is how many higher-ranked posts of yours are already in that feed. Your second post gets ×0.625, your third ×0.4375, and it keeps sliding toward a floor of ×0.25.

### 48 hours and it's gone

`MAX_POST_AGE` is 48 hours. After that, a post isn't a For You candidate anymore.

## What this means for small creators

**1. Make your first 2 hours count.** Cold start only looks at original posts under 2 hours old with under 200 home impressions, and picks by like rate. Post when your audience is awake, and write something people will like *right away*.

**2. Optimize for like rate, not just likes.** The cold-start pick uses likes divided by impressions. A tight post that a few people love beats a broad post that many people scroll past.

**3. Make people stay.** Continuous dwell got the biggest relative bump (+25%), and likes went up too. A clear first line, a useful screenshot, a short list: anything that earns a few more seconds.

**4. Ask for replies, then answer them.** A reply is worth 5, and a reply from a mutual follower adds 15 more. Replying to the people who reply to you builds mutuals, and mutuals' replies are the biggest positive signal left.

**5. Stop asking people to "copy the link."** It's 0 now. Ask them to repost, quote, DM it to a friend (5) or follow.

**6. Post originals to reach strangers.** Replies won't show up in non-followers' feeds, and only originals get cold start. Use replies to build relationships and originals to grow reach.

**7. Spread posts out.** Your second post in the same feed gets ×0.625, the third ×0.4375, heading toward ×0.25. Two good posts spaced apart beat five in a row.

**8. Don't fear links. Do fear mutes.** Links aren't penalized here, but mute (−58.8), not interested (−53.07) and report (−234) are heavy. Generic, spammy replies under strangers' posts are how you collect those. If you engage, say something specific to their post.

**9. Use video for what it causes, not for being video.** Video gets no bonus by itself. Hook people early so they stay and like.

**10. Earn the follow.** Following the author is worth 4.0, and profile clicks are 0. A post that makes people hit Follow directly, by promising more of the same, does more than one that just sends them to your profile.

## The short version

X rewards posts people like quickly, stay on, reply to and follow from. It quietly stopped rewarding copied links and video opens. And it still gives small accounts a 2-hour window to prove a post is good.

I'll keep reading the commits as they land. If something big changes, I'll write it up.

*Based on the open-sourced code in [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) as of commit a284320 (November 17, 2026). Weights are published defaults and may differ from what runs in production.*
