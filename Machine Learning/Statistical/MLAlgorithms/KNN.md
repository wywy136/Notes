# KNN

## Pseudo Code

```python
def KNN(samples, test, k):
    neighbors = []
    for idx, data in enumerate(samples):
        neighbors.append((distance(data, test), idx))
    kNearest = sorted(neighbors, lambda x:x[0])[:k]
    kNLabels = [samples[kNearest[i][1]].label for i in range(k)]
    return majority(kNLabels)
```

