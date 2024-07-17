---
layout: single
title: "Turi Create - Core ML and Vision"
date: 2018-08-20 15:33 +0800
category: swift
author: Marvin Lin
tags: [Core ML, MLKit, Swift]
lang: en
summary: "The article discusses how to create an image recognition app using Turi Create, a Python module for developing machine learning models. Presented during WWDC18, Turi Create facilitates the creation of Core ML models, allowing iOS developers to focus more on API functionalities. The process involves preparing and categorizing image data into specific folders, training the model with this data, and ultimately producing a Core ML model file that can be integrated into iOS applications.The demonstration included in the article explains how to train a model to recognize images of Takeshi Kaneshiro, a famous actor. It covers setting up the dataset, training the model with Turi Create, and adjusting parameters like `max_iterations` to enhance model accuracy. The model’s performance is evaluated by its ability to accurately identify and classify new images based on the training it received. The article also touches on the need for sufficient and relevant training data to improve the accuracy and reliability of the machine learning model."
---

Creating an Image Recognition App with Turi Create - Core ML and Vision
=======================================================================

Turi Create is a Python module for building machine learning models, prominently featured in multiple sessions at WWDC18 with live demos. It allows iOS developers to focus more on API functionalities when using the Core ML module.

### Creating an Image Recognition App with Turi Create - Core ML and Vision

![](https://cdn-images-1.medium.com/max/800/0*azSEH7drAK07vjkT)

“A person's hand holding a camera lens over a mountain lake” by [Paul Skorupskas](https://unsplash.com/@pawelskor?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

Turi Create, a Python module for machine learning model development, was extensively demoed live at WWDC18. It simplifies the use of Core ML for iOS developers, allowing them to concentrate on APIs. Moreover, if you have basic ideas, you don't need to seek an ML expert or become one to create a preliminary ML model for prototyping and further enhancement.

During WWDC18 Session 712, Turi Create was highlighted extensively. For more details on that session, you can refer to the following Medium article:

[**WWDC18, Session-712 Turi Create Highlights - Making ML model creation no longer a difficult task**  
_What is Turi Create?_medium.com](https://medium.com/@atimis19/overview-of-wwdc18-session-712-turi-create-build-an-app-with-core-ml-is-not-that-difficult-a46cb9420b34 "https://medium.com/@atimis19/overview-of-wwdc18-session-712-turi-create-build-an-app-with-core-ml-is-not-that-difficult-a46cb9420b34")

Let's start by demoing the APIs used in Turi Create and how they are implemented. Our example will involve determining if a photo contains Takeshi Kaneshiro. The sample video is available on YouTube and includes confidence levels alongside the identity checks.

Confidence levels indicate how confident your model is about its results, with a range between 0 and 1.0. If it determines a photo is not Takeshi Kaneshiro with a confidence level of 0.97, it means the model is 97% certain of its judgment.

Before doing image classification, you need image data. You should create folders for each category and fill them with corresponding images. The more data, the better, but at a minimum, it’s suggested to use at least 40 images per category.

As shown below, I searched online for 40 images of Takeshi Kaneshiro and placed them in a "kaneshiro" folder. The challenge is determining what to include in the "non-Kaneshiro" data. For this example, I used several non-Kaneshiro portraits for demonstration purposes. When undertaking such projects, it's advisable to consult with data science professionals on how best to train your model.

![](https://cdn-images-1.medium.com/max/800/1*VMSfkj3qJ7fyl2Eo4bGSLw.png)

"Kaneshiro" images in the dataset, "unknown" contains images that are not the target.

Once your data is organized, you can use the following code to train your model and export it to Core ML. The amount of code required is minimal, only about 12 lines (excluding comments). You can download the Jupyter Notebook file directly from (Ref-1).

Turi Create smartly handles file reading. If it encounters an unsupported file type, it will issue an error message but continue executing. The following image demonstrates this behavior where a .DS_Store file, used by macOS for storing custom attributes of a folder, is ignored.

![](https://cdn-images-1.medium.com/max/800/1*t0JaxQccx312PWr5GRGLHQ.png)

If this is your first time running the Jupyter Notebook, the process will connect to Apple's model website to download necessary data.

![](https://cdn-images-1.medium.com/max/800/1*6t9nmsXsDbavxS3lYYbpnQ.png)

Here is the output during model training in Turi Create:

```
Analyzing and extracting image features.

Number of examples: 74

Number of classes: 2

Number of feature columns: 1

Number of unpacked features: 2048

Number of coefficients: 2049

Starting L-BFGS
```

Turi Create also provides helpful tips if the model may not be optimal, suggesting adjustments such as increasing `max_iterations` if necessary.

After the process, you will obtain an .mlmodel file, which includes details about the training model, inputs, and outputs. For this project, the outputs are a label of "Kaneshiro" or "Unknown" and a dictionary of confidence levels for each label.

![](https://cdn-images-1.medium.com/max/800/1*v4W8f-kJWTirPfbDiKU77g.png)

![](https://cdn-images-1.medium.com/max/800/1*np33KUxG7F-Q6MA50KxbVQ.png)

Finally, integrate the model into an app project. Ensure to adjust privacy settings in info.plist if your app uses the camera or photo library.

![](https://cdn-images-1.medium.com/max/800/1*XtZzzm2T_CwVxDkaw1iq9Q.png)

The complete project, including XCode files and Turi Create code, is available on the GitHub repository linked below.

* * *

Ref-1: [GitHub repository](https://github.com/MoonAndEye/TuriCreateDemo "https://github.com/MoonAndEye/TuriCreateDemo")

Ref-2: [App Coda tutorial on using Python and Turi Create for custom Core ML models](https://www.appcoda.com/core-ml-model-with-python/ "https://www.appcoda.com/core-ml-model-with-python/")

By [Marvin Lin](https://medium.com/@atimis19) on [August 20, 2018](https://medium.com/p/b3071ffde3af).

[Canonical link](https://medium.com/@atimis19/using-turi-create-build-an-image-classification-app-core-ml-b3071ffde3af)
