---
layout: single
title: 在 iOS 專案加上測試-You need testing
date: 2023-12-06 17:15 +0800
category: unitTesting
author: Marvin Lin
tags: [Unit Testing, Swift, Xcode]
summary: The article emphasizes the significance of incorporating unit testing into iOS projects. It begins with a quote comparing writing code to building cathedrals, highlighting the need for a prayer-like phase after completion. The author argues that unit testing is crucial for improving code quality, readability, and maintenance. Unit testing aids in verifying program logic, meeting requirements, and identifying bugs, allowing for code refactoring without affecting other functionalities. Additionally, the article asserts that unit testing saves time and costs by preventing post-release bug issues, ultimately enhancing development efficiency and product quality. The concept of the testing pyramid is introduced, categorizing tests into unit tests, integration tests, and UI tests. The principles of F.I.R.S.T. for unit testing (Fast, Independent, Repeatable, Self-validating, Timely) are outlined to guide developers in effective testing practices. The article concludes by encouraging readers to embrace unit testing as a practical skill with broad applications, applicable to iOS projects of any scale.
permalink: /swift/:title:output_ext
---

> 「寫程式就像蓋教堂- 當完成之後，
我們就開始祈禱。」
> 

> Software and cathedrals are much the same – first we build them, then we pray.Sam Redwine
> 

![You need testing](/assets/unitTesting/add-test-target-on-xcode/you-need-testing.png)

## 在 iOS 專案加上測試 You need testing

你是不是覺得 Unit testing 很麻煩，很浪費時間，很沒必要？如果你這麼想，那你就錯了！Unit testing 對 iOS 專案的好處可不少。

首先，Unit testing 可以幫你提高程式碼的品質和可讀性。你可以透過 Unit testing 來檢查你的程式邏輯是否正確，是否符合需求，是否有 bug 或錯誤。你也可以透過 Unit testing 來重構你的程式碼，讓它更簡潔，更清晰，更容易維護。你不用擔心重構後會影響到其他功能，因為你有 Unit testing 來保證你的程式還是能正常運作。

其次，Unit testing 可以幫你節省時間和成本。你可能覺得寫 Unit testing 很花時間，但是你有沒有想過，如果你不寫 Unit testing，你可能會花更多時間在 debug 和修復 bug 上。而且，如果你的 bug 在上線後才被發現，那麼後果可能更嚴重，不僅會影響到用戶的體驗和信任，也會增加你的維護成本和風險。相比之下，如果你有 Unit testing，在開發階段就能及時發現和解決問題，那麼你就能提高你的開發效率和產品質量。

最後，Unit testing 可以幫你提升自信和專業度。當你有 Unit testing 來支持你的程式碼時，你就能更有信心地面對需求的反饋和需求。你也能更有信心地與其他開發者合作和分享你的程式碼。而且，Unit testing 也是一種展示你的專業態度和技能的方式。當別人看到你的程式碼有完善的 Unit test 時，他們就會對你的水平和責任感有更高的評價。

總之，Unit testing 對 iOS 專案的好處是多多益善的。如果你還沒有開始寫 Unit test，那就趕快行動吧！相信我，Unit test 會讓你的開發生活更美好！

## 測試金字塔

![測試金字塔](/assets/unitTesting/add-test-target-on-xcode/ui-integrate-unit-testing.png)

這是網路上常見的關於測試金字塔的圖案。它將不同類型的測試分為三層：單元測試、整合測試和 UI 測試。

- 單元測試（Unit Test）：位於金字塔的底層，是最基本和最快速的測試類型，主要針對軟體的最小可測單元（如函數、方法或類別）進行驗證，確保代碼的邏輯正確性和健壯性。單元測試通常由開發人員自行編寫和執行，並使用各種工具和框架來自動化和簡化測試過程。單元測試應該佔據金字塔的最大比例，因為它們可以及時發現和修復代碼中的錯誤，提高代碼質量和可維護性。
- 整合測試（Integration Test）：位於金字塔的中層，是在單元測試之後進行的測試類型，主要針對軟體的不同模組或組件之間的交互和協作進行驗證，確保整合後的系統能夠正常運作。整合測試通常由開發人員或測試人員負責，並使用 Mock 或 Stub 等技術來隔離外部依賴和影響。整合測試應該佔據金字塔的中等比例，因為它們可以檢查系統的內部結構和邏輯是否符合設計規範和需求。
- UI Test：位於金字塔的頂層，是最接近真實使用場景和用戶體驗的測試類型，主要針對軟體的完整功能和流程進行驗證，確保系統能夠按照預期提供服務。端對端測試通常由測試人員或用戶代表負責，並使用自動化或手動的方式來模擬用戶操作和行為。端對端測試應該佔據金字塔的最小比例，因為它們通常比較耗時和昂貴，且難以涵蓋所有可能的情況和變數。

## 單元測試的 F.I.R.S.T 原則

- Fast：Unit test 應該快速執行，不要花費太多時間或資源。
- Independent：Unit test 應該獨立於其他測試，不要互相影響或依賴。
- Repeatable：Unit test 應該可以在任何環境或情況下重複執行，並得到一致的結果。
- Self-validating：Unit test 應該有明確的通過或失敗的標準，不要需要人工檢查或驗證。
- Timely：Unit test 應該及時編寫，最好在開發程式碼之前或同時進行，以驅動設計和重構。

希望這一系列的文章，能讓你能體會 Unit Testing 的好處。Unit Testing是一項實用的技能，它具有廣泛的應用範疇，無論是應用程式的規模大小，都能受惠於它。持之以恆地精進這項技能，並積極將其運用於您的iOS專案中，是一個不斷學習和成長的過程。

