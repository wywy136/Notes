# Binary Search Tree

## Basic Operation

### Feature

node.left.value < node.value < node.right.value

### Insertion

```python
Insertion(T, new):
  y = None
  x = T.root
  while x is not None:
    y = x
    if x.value < new.value:
      x = x.right
    else:
      x = x.left
      
  new.parent = y
  if x is None:  # T is empty
    T.root = new
  elif new.value < x.value:
    x.left = new
  else:
    x.right = new
```

### Successor

```python
Successor(x):
  if x.right is not None:
    return Min(x.right)
  y = x.parent
  while y is not None and x == y.right:
    x = y
    y = y.parent
  return y
```

### Deletion

```python
Transplant(T, u, v):
"""
Replaces the subtree rooted at node u with the subtree rooted at node v node u’s parent becomes node v's parent, and u’s parent ends up having v as its appropriate child.
"""
  if u.parent == None:  # u is root
    T.root = v
  elif u == u.parent.left:  # u is a left child
    u.parent.left = v
  else:
    u.parent.right = v
  if v is not None:
    v.parent = u.parent
```

```python
Delete(T, z):
  if z.left is None:
    Transplant(T, z, z.right)
  elif z.right is None:
    Transplant(T, z, z.left)
  else:
    y = Successor(z)  # y should not have left child
    if y.parent is not z:  # y is not right child of z
      Tranplant(T, y, y.right)  # move y.right to y
      y.right = z.right  # connect y with z.right
      y.right.p = y
    Transplant(T, z, y)  # move y to z
    y.left = z.left  # connect y.left with z.left
    y.left.parent = y
```

