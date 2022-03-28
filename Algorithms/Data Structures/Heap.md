# Heap

## Basic Operation

### Feature

Max Heap: node.value > node.left.value, node.value > node.right.value

Min Heap: vice versa

### Minheap-Insert

```python
Minheap-Insert(A, key):
  i = heapsize(A) + 1
  while i > 1 and A[parent(i)] > key:
    A[i] = A[parent(i)]
    i = parent(i)
  A[i] = key
```

The heap feature maintains after the insertion without need of heapify.

### Minheap-Extract

```python
Minheap-Extract(A):
  min = A[1]
  A[1] = A[heapsize(A)]
  heapsize(A) -= 1
  Minheap-heapify(A, 1)
  return min
```

### Minheap-Heapify

```python
Minheap-Heapify(A, i):
  left, right = 2i, 2i + 1
  if left <= heapsize(A) and A[left] < A[i]:
    minimum = left
  else:
    minimum = i
  if right <= heapsize(A) and A[right] < A[i]:
    minimum = right
  if minimum is not i:
    swap(A[i], A[minimum])
    Minheap-Heapify(A, minimum)
```

### Minheap-Build

```python
Minheap-Build(A):
  for i = A.length // 2 to 1:
    Minheap-Heapify(A, i)
```

