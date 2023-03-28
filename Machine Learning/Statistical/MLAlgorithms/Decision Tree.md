# Decision Tree

## Theory

### Type of Decision Trees

- ID3 creates a multiway tree. For each node, it trys to find the categorical feature that will yield the largest information gain for the target variable.
- C4.5 is the successor of ID3 and remove the restriction that the feature must be categorical by dynamically define a discrete attribute that partitions the continuous attribute in the discrete set of intervals.
- CART is similar to C4.5. But it differs in that it constructs binary tree and support regression problem.

### Improtance of an attribute

Importance(a, examples): Information gain by splitting on attribute a
$$
Importance(a, examples)=H(examples)-\sum\frac{n_i}{n}H(child_i)
$$
H(V): entropy of set V
$$
H(V)=\sum_kP(v_k)\log_2 \frac{1}{P(v_k)}=-\sum_kP(v_k)\log_2 P(v_k)
$$

- $v_k$: examples with label $k$
- $P(v_k)$: fraction of examples with label $k$ in the whole dataset
- $child_i$: i-th set of samples splitted by attribute a
- $n_i$: size of $child_i$

## Pseudo Code

```python
def learnDecisionTree(examples, attributes):
  if all examples have same label:
    return the label
  elif attributes is None:
    return MajorLabel(examples)
  else:
    A = argmax_(a in attributes) Importance(a, examples)
    tree = a new decision tree with root splitting on A
    for each value v of A:
      splitted = {e:e in examples, e.A = v}
      subTree = learnDecisionTree(splitted, attributes - A)
      add a brach to tree with label (A = v) and subtree subTree
    return tree
```

MajorLabel: select the most common label among a set of examples
