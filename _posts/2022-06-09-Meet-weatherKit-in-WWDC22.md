---
layout: post
title: "Meet WeatherKit in WWDC22"
date: 2022-06-09 15:17 +0800
category: Swift
author: Marvin Lin
tags: [Swift, WWDC]
summary: "WWDC22 新 framework - Meet WeatherKit 重點結錄"
---

Meet WeatherKit in WWDC22
=========================

WWDC22: Meet WeatherKit 重點結錄

* * *

### Meet WeatherKit in WWDC22

![](https://cdn-images-1.medium.com/max/800/1*US6DQ8qy70XLbCBAEnQ9sQ.png)

WWDC22: Meet WeatherKit 重點結錄

[**Meet WeatherKit - WWDC22 - Videos - Apple Developer**  
_WeatherKit offers valuable weather data for your apps and services to help people stay up to date on the latest…_developer.apple.com](https://developer.apple.com/videos/play/wwdc2022/10003/ "https://developer.apple.com/videos/play/wwdc2022/10003/")[](https://developer.apple.com/videos/play/wwdc2022/10003/)

### 提供的資料

*   現在天氣
*   天氣預報: 日/時/分 等級
*   風向/風力
*   日出/日落/月相
*   歷史天氣資料
*   有更多沒列出來的，都在文件上

### 收費標準 (Platform State of the Union)

*   500K calls/ month 以下是免費
*   有更高需求的話，也有其他附費方案 1M calls/ Month 定價 $49.99

![](https://cdn-images-1.medium.com/max/800/1*Mqmsvyr6NmcWK-PjcimjYA.png)

500k 以下免費

![](https://cdn-images-1.medium.com/max/800/1*QsIiuiTd5Abg9lkyr1GgHA.jpeg)

需要有更高流量，也有各種 plan 可選

可以想見，接下來的 weather app ，會像雨後春筍一般冒出來

呼叫 WeatherKit 的方法短短幾行就能做到

{% highlight swift %}
    import WeatherKitimport CoreLocation

    let weatherService = WeatherService()

    let syracuse = CLLocation(latitude: 43, longitude: -76)

    let weather = try! await weatherService.weather(for: syracuse)

    let temperature = weather.currentWeather.temperature

    let uvIndex = weather.currentWeather.uvIndex
{% endhighlight %}

Apple 也提供了 RESTful API 的方法呼叫 WeatherKit

    /* Request a token */const tokenResponse = await fetch('<https://example.com/token>');const token = await tokenResponse.text();

    /* Get my weather object */const url = "<https://weatherkit.apple.com/1/weather/en-US/41.029/-74.642?dataSets=weatherAlerts&country=US>"

    const weatherResponse = await fetch(url, {headers: {"Authorization": token}});const weather = await weatherResponse.json();

    /* Check for active weather alerts */const alerts = weather.weatherAlerts;const detailsUrl = weather.weatherAlerts.detailsUrl;

Apple WeatherKit document  
[https://developer.apple.com/documentation/weatherkit](https://developer.apple.com/documentation/weatherkit)

By [Marvin Lin](https://medium.com/@atimis19) on [June 9, 2022](https://medium.com/p/b48aaf4589b2).

[Canonical link](https://medium.com/@atimis19/meet-weatherkit-in-wwdc22-b48aaf4589b2)