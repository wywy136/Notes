# Linear Regression

## Theory

### Variance-Bias Tradeoff

Low MSE = Low Variance + Low Bias

- Variance: the amount by which $\hat{f}$ would change if we used different training data.
- Bias is the error introduce by modeling a real-life problem with a simpler model.

Generally, as flexibility increases, variance will increase and bias will decrease.

### Parameters Updating

$$
\theta_j \leftarrow \theta_j + \alpha(y^{(i)}-h_\theta(x^{(i)})x^{(i)}_j
$$
## Pseudo Code

```python
LinearRegression(epoch, learning_rate, X, Y, feature_size, epsilon):
    thetas[feature_size + 1] = 0
    for i = 1 to epoch:
        grads[feature_size + 1] = 0
        for j = 1 to X.size:
            for k = 1 to featuer_size:
                grads[k] += X[j][k] * (Y[j] - Hypo(thetas, X[j], feature_size))
            grads[k + 1] += Y[j] - Hypo(thetas, X[j], feature_size)
        for k = 1 to feature_size + 1:
            thetas[k] += learning_rate * grads[k] / X.size
        if Norm(grads) < epsilon:
            break
    return thetas
```

```python
Hypo(thetas, x, feature_size):
    h = 0
    for i in feature_size:
        h += thetas[i] * x[i]
    return h
```

```python
Norm(x):
    n = 0
    for i = 1 to x.size:
        n += x[i] * x[i]
    return sqrt(n)
```

