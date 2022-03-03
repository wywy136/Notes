## 283

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

```
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
```

说明:

    必须在原数组上操作，不能拷贝额外的数组。
    尽量减少操作次数。

solution: 参考了[这里](https://github.com/CyC2018/CS-Notes/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3%20-%20%E6%95%B0%E7%BB%84%E4%B8%8E%E7%9F%A9%E9%98%B5.md)

```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for num in nums:
            if num != 0:
                nums[idx] = num
                idx += 1
        for _ in range(len(nums) - idx):
            nums[idx] = 0
            idx += 1
```

## 485

- 最开始没有考虑全1的情况

## 240

编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

    每行的元素从左到右升序排列。
    每列的元素从上到下升序排列。

示例:

现有矩阵 matrix 如下：

```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```

给定 target = 5，返回 true。

给定 target = 20，返回 false。

solution: 参考了[这里](https://github.com/CyC2018/CS-Notes/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3%20-%20%E6%95%B0%E7%BB%84%E4%B8%8E%E7%9F%A9%E9%98%B5.md)

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        x = len(matrix)
        if x == 0:
            return False
        else:
            y = len(matrix[0])
            if y == 0:
                return False
            else:
                row = 0
                col = y - 1
                while(row < x and col >= 0):
                    if matrix[row][col] == target:
                        return True
                    elif matrix[row][col] < target:
                        row += 1
                    
                    elif matrix[row][col] > target:
                        col -= 1
                return False
```

- 逐行比较时，如果一个数字大于目标值，则后面所有行的这一列都不会出现目标值，因此col-=1
- 注意边界情况：[], [[]]
- 注意while循环里，elif的作用

### 378

给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

示例

```
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。
```

solution: 参考[这里](https://github.com/CyC2018/CS-Notes/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3%20-%20%E6%95%B0%E7%BB%84%E4%B8%8E%E7%9F%A9%E9%98%B5.md)

```python
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        x = len(matrix)
        y = len(matrix[0])
        low = matrix[0][0]
        high = matrix[x-1][y-1]
        while(low <= high):
            mid = int(low + (high - low) / 2 )
            cnt = 0
            for i in range(x):
                for j in range(y):
                    if matrix[i][j] <= mid:
                        cnt += 1
                    else:
                        break
            
            if cnt < k:
                low = mid + 1
            else:
                high = mid - 1
        return low
```

- 二分法：计算中间值，看小于中间值的数的个数，从而判断第k小的数在前一部分还是后一部分；直到最后low即为要寻找的结果

### 645

集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。

给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1:

输入: nums = [1,2,2,4]
输出: [2,3]

注意:

    给定数组的长度范围是 [2, 10000]。
    给定的数组是无序的。

solution: 使用map

```python
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        ans = [0, 0]
        for i in range(1, len(nums) + 1):
            dic[i] = 0
        for i in nums:
            dic[i] += 1
        for k, v in dic.items():
            if v == 2:
                ans[0] = k
            if v == 0:
                ans[1] = k
        return ans
```

- 开始时用顺序遍历做，但是忽略了各种边界情况
- 这种无序、有严格一对一的情况，适合用map做

### 287

给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

```
示例 1:

输入: [1,3,4,2,2]
输出: 2

示例 2:

输入: [3,1,3,4,2]
输出: 3
```

说明：

    不能更改原数组（假设数组是只读的）。
    只能使用额外的 O(1) 的空间。
    时间复杂度小于 O(n2) 。
    数组中只有一个重复的数字，但它可能不止重复出现一次。

solution: 二分查找

```python
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums) - 1
        while(low <= high):
            cnt = 0
            mid = int(low + (high - low)/2)
            for n in nums:
                cnt += (n <= mid)
            if cnt > mid:
                high = mid - 1
            else:
                low = mid + 1
        return low
```

- 要保证：mid = cnt的情况下，是low+=1！
- 这个题思考了很久，还有一种快慢指针的做法，现在还不会，等学过后再看

### 667

给定两个整数 n 和 k，你需要实现一个数组，这个数组包含从 1 到 n 的 n 个不同整数，同时满足以下条件：

① 如果这个数组是 [a1, a2, a3, ... , an] ，那么数组 [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] 中应该有且仅有 k 个不同整数；.

② 如果存在多种答案，你只需实现并返回其中任意一种.

```
示例 1:

输入: n = 3, k = 1
输出: [1, 2, 3]
解释: [1, 2, 3] 包含 3 个范围在 1-3 的不同整数， 并且 [1, 1] 中有且仅有 1 个不同整数 : 1

示例 2:

输入: n = 3, k = 2
输出: [1, 3, 2]
解释: [1, 3, 2] 包含 3 个范围在 1-3 的不同整数， 并且 [2, 1] 中有且仅有 2 个不同整数: 1 和 2
```

solution：

```python
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = list(range(1, n + 1))
        for i in range(1, k):
            res[i:] = res[:i - 1:-1]
        return res
```

- 首先初始化顺序的数组1，2，3，...，n，这时有且仅有一个差值
- 从第二个数字开始，整体翻转，每翻转一次就会新产生一个差值

python知识积累

- 获得数组下标i元素之前的部分数组：list[:i]
- 获得数组下标i元素之后的部分数组的倒序：list[:i:-1]
- 获得包含数组下标i元素之后的部分数组：list[i:]
- 获得包含数组小标i元素之前的部分数组的倒序：list[i::-1]

### 697

给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

```
示例 1:

输入: [1, 2, 2, 3, 1]
输出: 2
解释: 
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.

示例 2:

输入: [1,2,2,3,1,4,2]
输出: 6
```

solution:

```python
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = {}
        right = {}
        count = {}
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
        
        degree = max(count.values())
        ans = len(nums)
        for k, v in count.items():
            if v == degree:
                ans = min(ans, right[k] - left[k] + 1)
        return ans
```

- right、left的设置很巧妙
- python积累：字典的get方法、min的使用方法

### 565

索引从0开始长度为N的数组A，包含0到N - 1的所有整数。找到最大的集合S并返回其大小，其中 S[i] = {A[i], A[A[i]], A[A[A[i]]], ... }且遵守以下的规则。

假设选择索引为i的元素A[i]为S的第一个元素，S的下一个元素应该是A[A[i]]，之后是A[A[A[i]]]... 以此类推，不断添加直到S出现重复的元素。

```
示例 1:

输入: A = [5,4,0,3,1,6,2]
输出: 4
解释: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

其中一种最长的 S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
```

提示：

    N是[1, 20,000]之间的整数。
    A中不含有重复的元素。
    A中的元素大小在[0, N-1]之间。

solution: 

```python
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        for i in range(len(nums)):
            cnt = 0
            j = i
            while(nums[j] != -1):
                cnt += 1
                t = nums[j]
                nums[j] = -1
                j = t
            max_len = max(max_len, cnt)
        return max_len
```

### 769

数组arr是[0, 1, ..., arr.length - 1]的一种排列，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。

我们最多能将数组分成多少块？

```
示例 1:

输入: arr = [4,3,2,1,0]
输出: 1
解释:
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。

示例 2:

输入: arr = [1,0,2,3,4]
输出: 4
解释:
我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。
```

solution:

```python
class Solution(object):
    def maxChunksToSorted(self, arr):
        ans = ma = 0
        for i, n in enumerate(arr):
            ma = max(ma, n)
            if i == ma:
                ans += 1     
        return ans
```

- 思路关键点：可切一刀的标准：前i个元素的最大值，等于下标i

