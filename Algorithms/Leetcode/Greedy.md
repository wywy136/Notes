## leetcode题解

### 406 根据身高重建队列

假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例

```
输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
```

解题思路：矮个子对于高个子来说“视而不见”，所以高个子排好序后，矮个子可以随意插入队列而不影响规则；相反，高个子对矮个子百分百满足题目的要求，所以在高个子排好序后，矮个子可以根据自身的k值来决定插入到队列的哪个位置。同时，同等身高的人也要被考虑，所以先插入k值小的，再插入k值大的以考虑同等身高的

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output
```

### 665 非递减数列

给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]

```
示例 1:
输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。

示例 2:
输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
```

解题思路：看作是消除一次向下拐点的问题。消除向下拐点时要考虑拐点前和拐点后元素的大小关系，来决定是将拐点下移还是拐点的后一点上移。同时注意开始时永远要将拐点下移，因为没有前一个元素的约束，可以看作前一个元素为负无穷

```python
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if not nums:
            return False
        time = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                time += 1
                if time == 2:
                    return False
                if i >=2 and nums[i-2] > nums[i]:
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i]
        return True
```

### 763 划分字母区间

字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

```
示例：
输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
```

解题思路：首先记录每个字母最后出现的位置，之后有如下事实：对于属于一个span的字母，这个span的end位置取决于这里面所有字母最后位置的最大值。所以遍历S，每次都记录最大的最后位置，当遍历到最后位置时，一个span结束。

```python
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return [0]
        last = {}
        for i in range(len(S)):
            last[S[i]] = i
        start, end = 0, 0
        ans = []
        for i in range(len(S)):
            end = max(last[S[i]], end)
            if i == end:
                ans.append(end-start+1)
                start = end + 1
        return ans
```

### 55 跳跃游戏

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

```
示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
```

思路关键：从后往前进行贪心，每一步找能达到上一步起点的起点