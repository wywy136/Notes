# Random Forest & Bagging

## Bagging

**Bagging** is a homogeneous weak learners’ model that learns from each other. 

Bagging is an acronym for ‘Bootstrap Aggregation’ and is used to decrease the variance in the prediction model. Bagging is a parallel method that fits different, considered learners independently from each other, making it possible to train them simultaneously.

Bagging generates additional data for training from the dataset. This is achieved by random sampling with replacement from the original dataset. Sampling with replacement may repeat some observations in each new training data set. Every element in Bagging is equally probable for appearing in a new dataset. 

These multi datasets are used to train multiple models in parallel. The average of all the predictions from different ensemble models is calculated. The majority vote gained from the voting mechanism is considered when classification is made. Bagging decreases the variance and tunes the prediction to an expected outcome.

## Random Forest

Random Forest is kind of Bagging. Each decision tree in the forest is trained on selected features. 

