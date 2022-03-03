# Graph

## Basic Operation

### BFS

```python
BFS(G, s):
  for each v in V:
    v.p = N
    v.d = inf
    v.visited = False
  s.p = N
  s.d = 0
  s.visited = True
  q = queue()
  q.enqueue(s)
  while q is not None:
    v = q.dequeue()
    for u in ADJ[v]:
      if u.visited is False:
        u.visited = True
        u.p = v
        u.d = v.d + 1
        q.enqueue(u)
```

### DFS

```python
DFS(G):
  for each v in V:
    v.p = N
    v.visited = False
  for each v in V:
    if v.visited is False:
      DFS_helper(G, v)
```

```python
DFS_helper(G, v):
  v.visited = True
  for u in G.ADJ[v]:
    if u.visited is False:
      u.p = v
      DFS_helper(G, u)
```

## Shortest Path

### Dijkstra

Directed, non-negative weighted

$O((V+E)\lg V)$

```python
Dijkstra(G, s):
  for each v in V:
    v.p = None
    v.d = inf
  s.d = 0
  Q = PriorityQueue()  // keyed by v.d
  Q.insert(s)
  while Q is not empty:
    u = Extract-min(Q)
    for each v in G.ADJ[u]:
      Relax(u, v, G)
```

```python
Relax(u, v, G):
  if v.d > u.d + G.w(u, v):
    v.d = u.d + G.w(u, v)
    v.p = u
```

### Bellman-Ford

Directed, no restriction on weight

```python
Bellman-Ford(G, s):
  for each v in V:
    v.p = None
    v.d = inf
  s.d = 0
  for i = 1 to |V|-1:
    for each edge (u, v) in E:
      Relax(u, v, G)
  for each edge (u, v) in E:
    if d[v] > d[u] + G.w(u, v):
      return False
  return True
```

### Topology

Directed, acyclic

## MST

### Prim

$O(E\lg V)$

```python
Prim(G, r):
  for each v in V:
    v.p = None
    v.key = inf
    v.visited = False
  r.key = 0
  Q = PriorityQueue()  // keyed by v.key
  Q.insert(V)
  while Q is not empty:
    u = Extract-min(Q)
    u.visited = True
    for v in G.ADJ[u]:
      if v.visited is False and G.w(u, v) < v.key:
        v.p = u
        v.key = w(u, v)
```

### Kruskal

```python
Kruskal(G, w):
  X = emptyset
  for each v in V:
    v.p = v
    v.rank = 0
  Sort(E)  // Sort egdes by weight increasingly
  for each edge (u, v) in E:
    if Find(u) != Find(v):
      X.add((u, v))
      Union(u, v)
  return X
```

```python
Find(x):
  while x != x.p:
    x = x.p
  return x
```

```python
Union(x, y):
  if x.rank > y.rank:
    y.p = x
  else:
    x.p = y
    if x.rank = y.rank:
      y.rank += 1
```

