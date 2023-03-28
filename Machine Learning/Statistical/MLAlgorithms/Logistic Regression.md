# Logistic Regression

## Theory

### Math

Sigmoid activation
$$
h(x)=\frac{1}{1+e^{-z}}
$$
Probability
$$
p(y|x;\theta)=h_\theta(x)^y(1-h_\theta(x))^{(1-y)}
$$
Likelihood of Parameters
$$
L(\theta)=\Pi^m_{i=1}h_\theta(x^{(i)})^{y^{(i)}}(1-h_\theta(x)^{(i)})^{(1-y^{(i)})}
$$
Log likelihood
$$
l(\theta)=\sum^m_{i=1}y^{(i)}\log h_\theta(x^{(i)})+(1-y^{(i)})\log (1-h_\theta(x^{(i)}))
$$
Unlike Linear Regression, we cannot use MSE because our prediction function is non-linear (due to sigmoid transform). Squaring this prediction as we do in MSE results in a non-convex function with many local minimums. If our cost function has many local minimums, gradient descent may not find the optimal global minimum.

Cross-Entropy Cost: $J(\theta)=\frac{1}{m}l(\theta)$.

Choose $\theta$ that maxmizes the $l(\theta)$
$$
\theta_j=\theta_j-\alpha\frac{\partial}{\partial \theta_j}J(\theta)\\=\theta_j+\alpha\frac{1}{m}\sum^m_{i=1}x^{(i)}(y^{(i)}-h_\theta(x^{(i)}))
$$

## Pseudo Code

```python
def LogisticRegression(features, labels, weights, lr, epoch):
    for i in epoch:
        weights = updateWeights(features, labels, weights, lr)
    return weights

def sigmoid(x):
    return 1 / (1 + exp(-x))

def h(features, weights):
    return sigmoid(np.dot(features, weights))

def updateWeights(features, labels, weights, lr):
    # features: [x, f]
    # labels: [x]
    # weights: [f]
    predictions = h(features, weights)  # [x, f] * [f] -> [x]
    gradient = np.dot(features.T, labels-predictions)  # [f, x] * [x] -> [f]
    gradient /= labels.size
    weights += lr * gradient
    return weights
```

