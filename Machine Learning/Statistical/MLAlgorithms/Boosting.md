# Boosting

## Theory

**Boosting** is also a homogeneous weak learners’ model but works differently from Bagging. In this model, learners learn sequentially and adaptively to improve model predictions of a learning algorithm.

Boosting is a sequential ensemble method that iteratively adjusts the weight of observation as per the last classification. If an observation is incorrectly classified, it increases the weight of that observation. The term ‘Boosting’ in a layman language, refers to algorithms that convert a weak learner to a stronger one. It decreases the bias error and builds strong predictive models.

### Learning with weighted intances

We want to encode this in our algorithms by assigning weights to different instances and this can be done as follows:

- changing the classification algorithm (expensive)
- duplicate instances such that an instance with wight n is duplicated n times

### Bagging vs Boosting

- Bagging decreases variance, not bias, and solves over-fitting issues in a model. Boosting decreases bias, not variance.

- In Bagging, each model receives an equal weight. In Boosting, models are weighed based on their performance.
- In Bagging, each sample is equally weighted, while in Boosting the misclassified samples will be given more weights.

- Models are built independently in Bagging. New models are affected by a previously built model’s performance in Boosting.

### Adaboost

#### General Algorithm

1. Build a model and make predictions.
2. Assign higher weights to miss-classified points.
3. Build next model.
4. Repeat steps 3 and 4.
5. Make a final model using the weighted average of individual models.

#### Details

https://www.youtube.com/watch?v=LsK-xG1cLYA

For step $t$ where a classifier is trained

- Error $\epsilon$: sum of weight of misclassified samples
- Amount of say $\alpha$: $\frac{1}{2}\log(\frac{1-\epsilon}{\epsilon})$
- Increasing sample weight for misclassified ones: $w' = w*e^{\alpha}$
- Decreasing sample weight for correctly classified ones: $w'=w*e^{-\alpha}$

Learning with weight

- Normalize the new weights
- Resample the data based on the values of a randomly picked number in range (0,1)
- Samples with large weights would be selected more frequently than those with minor weights.