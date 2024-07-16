---
layout: single
title: "WWDC18, Session-712 Turi Create Highlights - Making ML Models is No Longer a Difficult Task"
date: 2018-08-12 15:28 +0800
category: swift
author: Marvin Lin
tags: [MLKit, Machine Learning, Turi Create, Swift]
lang: en
summary: "This article summarizes the highlights from WWDC18, Session-712, focusing on Turi Create, a powerful tool for building machine learning models. Originally known as Dato and part of the Graph Lab project from the University of Washington, Turi Create was acquired by Apple in 2016. The session detailed the capabilities of this Python package, emphasizing its ease of use for non-specialists and its ability to generate Core ML models efficiently. Turi Create supports multiple platforms like Mac and Linux and simplifies the machine learning model development process. It requires minimal coding, often less than 20 lines to create a functional object recognition model. The tool is particularly beneficial for iOS developers, allowing them to focus on APIs rather than the complexities of machine learning algorithms. The article also walks through the process of building a machine learning model using Turi Create, from defining the task and preparing data to training the model and deploying it in an app. The session demonstrated the accessibility of machine learning, making it approachable for a broader audience and integrating it seamlessly into app development."
---

### WWDC18, Session-712 Turi Create Highlights - Making ML Models Is No Longer Difficult

![](https://cdn-images-1.medium.com/max/800/0*V4Kohj_1SGVxoqQt)

Photo by [Jens Johnsson](https://unsplash.com/@jens_johnsson?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

### What is Turi Create?

Before being acquired by Apple, it was known as Dato, a project developed under Graph Lab, funded by Prof. Carlos Guestrin from the University of Washington. It raised over $6 million in Series A and $18 million in Series B funding, before being bought by Apple in mid-2016. At WWDC17, there was a session that introduced this module, back then at version 4.0. At WWDC18, Session-712 provided a detailed introduction to this Python package, which also featured in 'What's new in Core ML' (Sessions 708, 709), where the speaker directly demoed the software. (Ref1)

### The Purpose of Turi Create

- It's a Python Package that can create Core ML models and is open source.
- Simple and user-friendly, accessible even to those not specialized in ML.
- Allows iOS developers to focus solely on APIs.
- Cross-platform (Mac, Linux).
- Low learning curve, especially on Mac where Python 2.7 is pre-installed. Just need `pip install turicreate`. Creating an object recognition model requires less than 20 lines of code. Using Jupyter Notebook as shown at WWDC18 is not mandatory. For installation, see (Ref2).

### Identifying Whether a Person in a Photo is Takeshi Kaneshiro

The following article uses Turi Create to make a simple Takeshi Kaneshiro recognition App. If you're interested in trying it out, check this out:

[**Using Turi Create to Build an Image Recognition App - Core ML and Vision**  
_Turi Create is a Python module for making machine learning models featured in multiple sessions at WWDC18. It enables iOS developers to use Core ML..._ medium.com](https://medium.com/@atimis19/using-turi-create-build-an-image-classification-app-core-ml-b3071ffde3af)

### Five Steps Needed Before Building a Machine Learning Model

![](https://cdn-images-1.medium.com/max/800/1*mywU7P1855THvlFe2WErtQ.png)

Steps Required for Machine Learning

Step 1: Clearly define your task as Turi Create (or ML in general) might offer different optimal algorithms depending on your specific task. If you choose the wrong one, your model might not perform as expected.

Step 2: Gather the necessary data for your task. For image recognition, you need images in folders named after their labels. For object detection, you need labels and coordinates in a JSON file.

Step 3: Generate your model file using Turi Create, which can be done in under 20 lines of code.

Step 4: Validate your model. Typically, training data is split in an 80:20 ratio. Use the 20% to test the model. If accuracy is low, consider increasing the `max_iterations` or adjusting other parameters.

Step 5: If validation is successful, integrate the model into your app and publish.

* * *

### 1. Defining the Task

![](https://cdn-images-1.medium.com/max/800/1*INdNWx4wC55KQh4Q51ExMw.png)

Tasks executable within Turi Create

![](https://cdn-images-1.medium.com/max/800/1*x_bHxyElNQYb5OQHpnvmkQ.png)

Common ML Tasks used in Apps

All types of tasks available in Turi Create are listed in the table above. You can select the corresponding API based on your project needs. The four tasks shown are the most commonly used in apps. Note that the style transfer feature is only available from version 5.0 beta; it was not included in 4.0.

### 2. Input Data for Model Training

![](https://cdn-images-1.medium.com/max/800/1*6kzzIfc4KVf3N1pya6wMtQ.png)

The top row shows image classification tasks requiring only images and folder names. The bottom row shows object detection tasks needing labels and bounding box information in addition to images.

![](https://cdn-images-1.medium.com/max/800/1*qCVLHh7UM3o8zuGj_1sPJA.png)

For object detection, you must input annotation data, usually a JSON file that allows multiple objects to be tagged in one image, each element containing a label and coordinates for a bounding box.

Depending on your task, input the appropriate data. For image classification tasks, simply place images in their respective folders. For object detection, you will need to provide additional information about the names and coordinates of objects to be recognized in the images.

![](https://cdn-images-1.medium.com/max/800/1*JYJqIggoRQptI5HwKgj65g.png)

Note that in Turi Create, the X and Y coordinates represent the center point of the bounding box, not the top-left corner as in UIKit.

### 3. Generating the ML Model

The WWDC18 sessions used Jupyter Notebook for demonstrations, requiring minimal coding—only 11 lines. Let's use "Is this a photo of Takeshi Kaneshiro?" as an example.

```python
import turicreate as turi

url = “dataset/”

data = turi.image_analysis.load_images(url)

# If the photo is not in the 'Kaneshiro' folder, label it 'Unknown'
data["kaneshiroOrNot"] = data["path"].apply(lambda path: "Kaneshiro" if "kaneshiro" in path else "Unknown")

data.save("kaneshiro_or_not.sframe")

data.explore()
```

The above code outputs the data in SFrame format, including the URL line, in just 5 lines.

### Steps to Create the ML Model:

1. **Load the Data:**
   Load your data into an SFrame.

2. **Split into Training and Test Data:**
   Randomly split the data into training (80%) and testing (20%) sets. Adjust the ratio as needed.

3. **Create the Model:**
   Use `image_classifier.create` from Turi Create, specifying the task type and other parameters like `max_iterations`.

```python
# Load the data
data = turi.SFrame("kaneshiro_or_not.sframe")

# Split the data
train_data, test_data = data.random_split(0.8)

# Create the model
model = turi.image_classifier.create(train_data, target="kaneshiroOrNot", max_iterations=100)

# Make predictions
predictions = model.predict(test_data)

# Evaluate the model
metrics = model.evaluate(test_data)
print(metrics["accuracy"])

# Save the model
model.save("kaneshiro.model")

# Export to Core ML format
model.export_coreml("kaneshiro.mlmodel")
```

### 4. Validating the Model

**Making Predictions:**
Use the trained model to make predictions on the test data that was not used during training.

**Validating the Model:**
Check the accuracy of the model. If it is low, consider adjusting parameters like `max_iterations`.

![](https://cdn-images-1.medium.com/max/800/1*Ntd4jyjkvF5IFc2PXc9hqw.png)

Two key points to validate: 1) The labeling is correct, 2) The labeled bounding box covers at least 50% of the correct area.

**Saving the Trained Model:**
After training, save the model file.

**Converting to Core ML Format:**
Convert the trained model into a format usable by Core ML.

### 5. Deploying to an App

Integrate the exported .mlmodel file into your project.

This completes the creation of your ML model.

For further reference, the Jupyter Notebook code used in the demonstrations is available on the following GitHub repository. Navigate to the Jupyter Notebook folder to find three examples: KaneshiroOrNot, SoupOrRice, and Adventure, which distinguish images of Takeshi Kaneshiro, identify whether an image is of soup or rice, and recognize which character from the Avengers is depicted, respectively.

[**MoonAndEye/TuriCreateDemo**  
_GitHub is where people build software. More than 28 million people use GitHub to discover, fork, and contribute to over…_github.com](https://github.com/MoonAndEye/TuriCreateDemo/)

* * *

**References:**

- [Turi company acquired by Apple](https://en.wikipedia.org/wiki/GraphLab)
- [Setting up Jupyter Notebook on Mac](https://medium.com/@atimis19/%E5%9C%A8-mac-%E4%B8%8A%E6%9E%B6%E8%A8%AD-jupiter-notebook-%E7%92%B0%E5%A2%83-4a983b70af4)
- [Example Code](https://tinyurl.com/y93ey7ds)
- [Implementing a Takeshi Kaneshiro Recognizer](https://medium.com/@atimis19/using-turi-create-build-an-image-classification-app-core-ml-b3071ffde3af)

By [Marvin Lin](https://medium.com/@atimis19) on [August 12, 2018](https://medium.com/p/a46cb9420b34).

[Canonical link](https://medium.com/@atimis19/overview-of-wwdc18-session-712-turi-create-build-an-app-with-core-ml-is-not-that-difficult-a46cb9420b34)