### 110

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

    一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

```
示例 1:

给定二叉树 [3,9,20,null,null,15,7]

3

   / \
  9  20
    /  \
   15   7

返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

   1
  / \
 2   2
/ \

   3   3
  / \
 4   4

返回 false 。
```

solution: 

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isBalancedHelper(node):
            if node == None:
                return True, -1
            isleftb, lefth = isBalancedHelper(node.left)
            if not isleftb:
                return False, 0  // 这个地方高度返回多少都可以，因为不会用到这个值
            isrightb, righth = isBalancedHelper(node.right)
            if not isrightb:
                return False, 0
            return (abs(righth-lefth)<2), 1 + max(righth, lefth)
        return isBalancedHelper(root)[0]
```

- 从底至上遍历，一次判断左右子树是否平衡。如果不平衡直接return；平衡的话，判断左右节点的高度差是否小于2，并返回自己的高度

### 543

solution: 

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_path = 1
        def depth(node):
            if node == None:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            self.max_path = max(self.max_path, L + R + 1)
            return 1 + max(L, R)
        depth(root)
        return self.max_path - 1
```

- 仍然是递归的思路：以节点p为根的子树，自己的直径是L+R+1，但对于上一层来说，对直径的贡献是max(L, R)+1

### 437

给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

  10
 /  \
5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1. 5 -> 3
2. 5 -> 2 -> 1
3. -3 -> 11
```

solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def pathSumAll(node, sum):
            if node == None:
                return 0
            result = countPath(node, sum)
            a = pathSumAll(node.left, sum)
            b = pathSumAll(node.right, sum)
            return result+a+b
        
        def countPath(node, sum):
            if node == None:
                return 0
            sum -= node.val
            result = 0
            if sum == 0:
                result = 1
            
            return result + countPath(node.left, sum) + countPath(node.right, sum)
        
        return pathSumAll(root, sum)
```

- 史上遇到的第一道双递归：第一层在每个节点上递归，用于计算整个树的路径数量之和，就是经典的先序遍历；第二层用于计算一个节点对应的所有路径数量之和
- 对于每个点，判断路径存在的方法：sum -= node.val，如果sum减到0，说明存在一条路径；在这一条路径上，每个点都要-=node.val
- 这个题是easy难度，但是想了好久没做出来。。对递归的返回值理解还是不够深入

### 572

给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

```
示例 1:
给定的树 s:

 3
/ \

   4   5
  / \
 1   2

给定的树 t：

   4 
  / \
 1   2

返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
给定的树 s：

 3
/ \
4   5
  / \
 1   2
    /
   0

给定的树 t：

   4
  / \
 1   2

返回 false。
```

solution:

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def equal(n1, n2):
            if n1 == None and n2 == None:
                return True
            if (n1 == None and n2) or (n1 and n2 == None) or (n1.val != n2.val):
                return False
            return equal(n1.left, n2.left) and equal(n1.right, n2.right)
        
        def sub(s, t):
            if s == None:
                return False
            return equal(s, t) or sub(s.left, t) or sub(s.right, t)

        return sub(s, t)
```

- 判断两个子树是否相等的方法：当一个子节点为空一个不为空、或值不等时，都不等

### 101

给定一个二叉树，检查它是否是镜像对称的。

```
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
	1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
	1
   / \
  2   2
   \   \
    3   3
```

solution:

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(n1, n2):
            if n1 == None and n2 == None:
                return True
            if (n1 == None and n2 != None) or (n1 != None and n2 == None):
                return False
            return (n1.val == n2.val) and check(n1.left, n2.right) and check(n1.right, n2.left)
        
        return check(root, root)
```

- 最开始的思路：翻转二叉树，之后判断是否相等。但这样时间、空间复杂度都很高
- 优化思路：使用两个最开始指向根节点的指针，之后让这两个指针**相反地移动**，依次判断两个节点的值是否相等。

### 687

给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示。

```
示例 1:
输入:
          5
         / \
        4   5
       / \   \
      1   1   5
输出:
2
示例 2:
输入:
          1
         / \
        4   5
       / \   \
      4   4   5
输出:
2
```

solution:

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def act(node):
            if node is None:
                return 0
            left_length = act(node.left)
            right_length = act(node.right)
            left = 0
            right = 0
            if node.left and node.left.val == node.val:
                left = left_length + 1
            if node.right and node.right.val == node.val:
                right = right_length + 1
            self.ans = max(self.ans, left+right)
            return max(left, right)
        act(root)
        return self.ans
```

- 对每个节点，找到左右两边最长的一条路径。如果这个节点的值等于左/右孩子，那就路径长度+=1；否则，路径长度=0并返回。在每次计算完路径长度之后，都保留当前所有路径长度最大值。
- 这道题看了题解才有思路，所以要重点反攻。

### 337

在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

```
示例 1:
输入: [3,2,3,null,3,null,1]
     3
    / \
   2   3
    \   \ 
     3   1
输出: 7 
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:
输入: [3,4,5,1,3,null,1]
     3
    / \
   4   5
  / \   \ 
 1   3   1
输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
```

solution1: 暴力递归+最优子结构。虽然正确，但是超时。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rob(node):
            if node == None:
                return 0
            math = 0
            if node.left != None:
                math += rob(node.left.left) + rob(node.left.right)
            if node.right != None:
                math += rob(node.right.left) + rob(node.right.right)
            return max(node.val + math, rob(node.left) + rob(node.right))
        
        return rob(root)
```

- 问题：会重复计算很多每个节点的最大金钱。

solution2: 动态规划+记忆化。把每个节点的金钱存起来。如果遇到一个已经计算过的节点，那就直接查字典。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.storage = {}
        def rob(node):
            if node == None:
                return 0
            if node in self.storage:
                return self.storage[node]
            math = 0
            if node.left != None:
                math += rob(node.left.left) + rob(node.left.right)
            if node.right != None:
                math += rob(node.right.left) + rob(node.right.right)
            self.storage[node] = max(node.val + math, rob(node.left) + rob(node.right))
            return self.storage[node]
        
        return rob(root)
```

solution3:

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rob_(node):
            if node == None:
                return [0, 0]
            result = [0, 0]
            left_result = rob_(node.left)
            right_result = rob_(node.right)
            result[0] = max(left_result) + max(right_result)
            result[1] = left_result[0] + right_result[0] + node.val
            return result
        return max(rob_(root))
```

- 减少了回溯次数：在每个点计算偷和不偷分别带来的收益。

### 94

迭代实现二叉树的中序遍历

solution:

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.stack = []
        self.ans = []
        node = root
        while node is not None or self.stack:
            while node is not None:
                self.stack.append(node)
                node = node.left
            node = self.stack.pop()
            self.ans.append(node.val)
            node = node.right
        return self.ans
```

### 145

迭代实现二叉树后序遍历。

solution:

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.stack = []
        self.ans = []
        node = root
        last = root
        while node or self.stack:
            while node:
                self.stack.append(node)
                node = node.left
            node = self.stack[-1]
            if node.right == None or node.right == last:
                self.stack.pop()
                self.ans.append(node.val)
                last = node
                node = None
            else:
                node = node.right
        return self.ans
```

- 需要设置last来保存上一次访问过的右节点。如果访问过，那说明此时该访问根节点；否则，访问右节点。且由于只有根节点访问之后才能pop根节点，所以必须node=stack[-1]，而不能直接pop

#### [剑指 Offer 07. 重建二叉树](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/)

输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

返回如下的二叉树：

```
	3
   / \
  9  20
    /  \
   15   7
```

重点思路：先序遍历和中序遍历可对齐，先序遍历的根节点（出现在[0]）恰好会出现在中序遍历以这一点为根节点的子树的节点序列的末尾！

```python
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:inorder.index(preorder[0])+1], inorder[:inorder.index(preorder[0])])
        root.right = self.buildTree(preorder[inorder.index(preorder[0])+1:], inorder[inorder.index(preorder[0])+1:])
        return root
```

