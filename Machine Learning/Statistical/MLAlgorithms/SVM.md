# SVM

## Theory

### General

The goal of the SVM algorithm is to create the best line, or decision boundary, that can segregate the n-dimensional space into distinct classes, so that we can easily put any new data point in the correct category, in the future. This best decision boundary is called a hyperplane. The best separation is achieved by the hyperplane that has the largest distance to the nearest training-data point of any class.

The SVM algorithm chooses the extreme points that help in creating the hyperplane. These extreme cases are called support vectors. The maximum-margin hyperplane is chosen in a way that the distance between the two classes is maximised.

### Kernal

When the data is linearly arranged, we can separate it by using a straight line. However, for non-linear data, we cannot draw a single straight line.

In order to find the hyperplane with the SVM algorithm, we do not need to add another dimension manually: the SVM algorithm uses "kernel trick". The SVM kernel is a function which takes a low dimensional input, and it transforms it to a higher dimensional space, i.e., it converts non-linearly separable data to linearly separable data.