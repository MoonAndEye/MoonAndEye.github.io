---
layout: single
title: The Cause of Crashes in Charts Issues 4049 & 4132
date: 2023-04-23 15:30 +0800
category: swift
author: Marvin Lin
tags: [Swift, Charts]
lang: en
summary: While using Charts version 3.4.1, I experienced crashes when updating datasets and then rendering charts, as referenced in issues 4049 and 4132. This article summarizes these issues and explores solutions to the chart crashes.
---

Charts is a widely used charting package in iOS project development. However, this year, I encountered an unusual situation in my project. Sporadic crashes kept occurring, which were visible on the Firebase Crashlytics Dashboard and happened within the renderer of the Charts package. Moreover, during releases to QA, crashes occurred after the iPhone was powered off for an extended period and then turned back on. There were no similar crashes reported on Crashlytics last year, and the difference now is that I had upgraded the Charts package to `3.4.1` and continued to upgrade to `3.5.0` and `3.6.0` after discovering the crash issue.

When attempting to reproduce the problem using the same steps on simulators or my physical device, the issue could not be replicated, validating the software world's adage: "It works on my machine." However, the crash could be reproduced when switching the scheme to release mode. The problem seems to be concentrated on the following points:

- The crash is related to Charts and occurs during the rendering process, specifically when the chart is about to be updated.
- This crash does not occur in Debug mode, but it consistently reproduces in Release mode (the most troubling aspect since the issue arises only in Release).
- In my project, the trigger point is when data is re-fetched and a chart update is requested.
- The actual cause of the crash occurs after the data update when Charts tries to redraw during initialization with an iterator, but the input parameters for min and max are reversed, leading to a crash. This issue only appears in Release mode, not in Debug.

## Searching for Similar Issues on GitHub

### Other Developers Also Reported This Problem

caloon also reported a similar issue in his project, but the crash does not happen 100% of the time; according to caloon, it occurs about 5% of the time.

![](/assets/swift/charts-crash/developer-found-stable-321.jpeg)

Upon investigation, issues 4049 and 4132 were found to be related.

[Charts Issue - 4049](https://github.com/danielgindi/Charts/issues/4049)

[Charts Issue - 4132](https://github.com/danielgindi/Charts/issues/4132)

### About Issue 4049

The scenario described in issue 4049 is similar to what I experienced in my project. Developer bweavgolfanatic explained his crash scenario, which coincides with my experience.

[Developer bweavgolfanatic's Description of the Crash](https://github.com/danielgindi/Charts/issues/4049#issuecomment-550577869)

[Charts Crash in Iterator](/assets/swift/charts-crash/charts-crash-in-iterator.jpeg)

From the debug console above, you can see that max is 1 and min is 98, which causes a crash at runtime when calling min...max. This phenomenon was also reproducible in my project. After reading through the discussion thread on the issue, I found a solution proposed by developer gordondove.

```swift
    self.downloadDataSet.append(newThroughtputPoint)
    self.downloadDataSet.calcMinMax()
    chartView.data?.calcMinMax()
    self.chartView.notifyDataSetChanged()
```

[gordondove's Solution](/assets/swift/charts-crash/crash-solution.jpeg)

### About Issue 4132

Issue 4132 is related to the PR and the integration of multiple issue posts. The primary information, however, was found from issue 4049.

## Solution Selection

1. Upgrade Charts, as subsequent PR 4132 stated it was fixed, but the major version after integration is 4.0.0 and beyond.
2. Locate the PR related to issue 4132 and merge this change into another forked Charts repo and tag it.
3. Revert Charts back to version 3.2.0 (before the iterator modification).
4. Use bweavgolfanatic's method by re-invoking the dataset's calMinMax().

Ultimately, `Option 4` was chosen because once the version jumped to the major version 4, the entire project could not be built. This situation underscored the importance of the adapter pattern. Those interested can refer to [Wrapping Third-Party Libraries to Reduce Upgrade Pains](https://moonandeye.github.io/swift/using-adapter-pattern-to-libs.html). Options 2 and 3 were not used because the project utilized a modified version of a forked repo, and reverting could introduce other risks, hence the final choice of Option 4.

## Reference Articles

[Using Adapters to Wrap Third-Party Libraries](/en/swift/using-adapter-pattern-to-libs/)

[Charts Repository - iOS](https://github.com/danielgindi/Charts)

[MPCharts Repository - Android](https://github.com/PhilJay/MPAndroidChart)

[Semantic Versioning](https://semver.org)