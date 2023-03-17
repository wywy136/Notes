# Algorithms

### Office hours

Olivia: Monday at 1:00 pm in JCL 346
Nathan: Monday at 4:00 pm in JCL 346
Andrew Wang: Thursday at 2:30 pm in JCL 346
Gerry: Thursday at 8:30 pm in JCL 346
Joseph: Friday at 4:00 pm in JCL 346
Benjamin: Saturday at 1:00 pm via [Zoom](https://canvas.uchicago.edu/courses/39932)
Jason: Sunday at 4:00 pm in JCL 346

## Notes

### Master Theorem

$$
T(n)=aT(\frac{n}{b})+O(n^d)
$$

T(n)=

- $O(n^d)$ if $d > \lg_ba$
- $O(n^d\lg n)$ if $d=\lg_ba$
- $O(n^{\lg_ba})$ if $d < \lg_ba$

## Midterm

Covered:

- the divide and conquer design technique and applications of divide and conquer to solve problems
- the sorting and searching algorithms from lecture and homework
- asymptotic analysis and algorithm correctness
- randomizing and hashing
- the dynamic programming design technique and applications of dynamic programming to solve problems
- heaps and binary search trees.

## Final

1. **Sorting and searching**
2. **Divide-and-conquer**
3. **Hashing & randomized algorithms**
4. **Heaps & Binary search trees**
5. **Dynamic programming**
6. **Graph search**
7. Shortest paths in graphs
   - **Complexity of Dijkstra**
8. Minimum spanning trees
   - **Use BFS/DFS to find MST components**
   - **Complexity of Kruskal**
9. Network flow
   - **Use BFS/DFS to find min s-t cut from residual graphs**
   - **Complexity of Ford-Fulkerson and Edmonds-Karp**
   - **Application of Network Flow**
   - **Question 7**

### Quick notes

Often if you see a O(log n) in the runtime of an algorithm, then either there was 1. sorting 2. binary search 3. min/max heap.

For O(nlogk) algorithms, where k < n, it indicates recursing on k and merging on n

- $T(n)=2T(\frac{k}{2})+O(n)$

If you see “expected time” you need to use a randomized algorithm. This could be a random number generator or hashing.

MST

- An edge e appears in all MSTs if and only if e is not one of the heaviest edges in any cycle.

- An edge e appears in all MSTs if and only if there is a cut (S, T) of the graph such that e is the unique lightest edge crossing that cut.

Some applications of max-flow

- vertex-disjoint path: assign c(v) = 1 to each vertex and replace each vertex as v_in and v_out

