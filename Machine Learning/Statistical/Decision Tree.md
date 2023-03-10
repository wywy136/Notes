# Decision Tree

```python
Learn-Decision-Tree(examples, attributes, parent_examples):
  if examples is None:
    return MajorLabel(parent_examples)
  elif all examples have same label:
    return the label
  elif attributes is None:
    return MajorLabel(examples)
  else:
    A = argmax_(a in attributes) Importance(a, examples)
    tree = a new decision tree with root splitting on A
    for each value v of A:
      exs = {e:e in examples, e.A = v}
      subtree = Learn-Decision-Tree(exs, attributes - A, examples)
      add a brach to tree with label (A = v) and subtree subtree
    return tree
```

MajorLabel: select the most common label among a set of examples

Importance(a, examples): Information gain by splitting on attribute a
$$
Importance(a, examples)=H(examples)-\sum\frac{n_i}{n}H(child_i)
$$
H(V): entropy of set V
$$
H(V)=\sum_kP(v_k)\log_2 \frac{1}{P(v_k)}=-\sum_kP(v_k)\log_2 P(v_k)
$$

- $v_k$: examples with label $k$

