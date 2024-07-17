---
layout: single
title: "Meet WeatherKit at WWDC22"
date: 2022-06-09 15:17 +0800
category: swift
author: Marvin Lin
lang: en
tags: [Swift, WWDC]
summary: "The article provides an overview of WeatherKit, a new framework introduced at WWDC22, designed to supply comprehensive weather data for applications and services. Here are the key points covered in the article"
---

### Meet WeatherKit at WWDC22

![](https://cdn-images-1.medium.com/max/800/1*US6DQ8qy70XLbCBAEnQ9sQ.png)

WWDC22: Key Takeaways from Meet WeatherKit

[**Meet WeatherKit - WWDC22 - Videos - Apple Developer**  
_WeatherKit provides valuable weather data for your apps and services, helping people stay informed about the latest weather conditions._](https://developer.apple.com/videos/play/wwdc2022/10003/)

### Data Provided

- Current weather
- Weather forecast: daily/hourly/minute granularity
- Wind direction and strength
- Sunrise/sunset phases and moon phases
- Historical weather data
- More details available in the documentation

### Pricing Model (Platform State of the Union)

- Free for up to 500K calls/month
- Higher tiers available, e.g., 1M calls/month at $49.99

![](https://cdn-images-1.medium.com/max/800/1*Mqmsvyr6NmcWK-PjcimjYA.png)

Free under 500k calls

![](https://cdn-images-1.medium.com/max/800/1*QsIiuiTd5Abg9lkyr1GgHA.jpeg)

Various plans available for higher traffic needs

It's foreseeable that a multitude of weather apps will sprout up following this release.

Accessing WeatherKit with just a few lines of code:

```swift
import WeatherKit
import CoreLocation

let weatherService = WeatherService()

let syracuse = CLLocation(latitude: 43, longitude: -76)

let weather = try! await weatherService.weather(for: syracuse)

let temperature = weather.currentWeather.temperature

let uvIndex = weather.currentWeather.uvIndex
```

Apple also offers a method to call WeatherKit via RESTful API:

```plaintext
/* Request a token */
const tokenResponse = await fetch('https://example.com/token');
const token = await tokenResponse.text();

/* Get my weather object */
const url = "https://weatherkit.apple.com/1/weather/en-US/41.029/-74.642?dataSets=weatherAlerts&country=US"

const weatherResponse = await fetch(url, {headers: {"Authorization": token}});
const weather = await weatherResponse.json();

/* Check for active weather alerts */
const alerts = weather.weatherAlerts;
const detailsUrl = weather.weatherAlerts.detailsUrl;
```

Apple WeatherKit documentation:  
[https://developer.apple.com/documentation/weatherkit](https://developer.apple.com/documentation/weatherkit)

By [Marvin Lin](https://medium.com/@atimis19) on [June 9, 2022](https://medium.com/p/b48aaf4589b2).

[Canonical link](https://medium.com/@atimis19/meet-weatherkit-in-wwdc22-b48aaf4589b2)