# Dynammic Programming

## General

1. Decide where to start the base case
   1. Starting at start
   2. Starting at end
   3. Starting at `dp[i][i]`
2. Decide what's the subprobem - what to store in dp table
   1. Optimal solution, then find the optimal solution at dp[1] or dp[n]
   2. Partial solution, then find the optimal solution based on the whole table

## Examples

### Knapsack

*Given n items, with values v1, v2, ..., vn and weights w1, w2, ..., wn, and a limit W, find the a subset of item maximizing the total values while the total weight is restricted by W.*

Starting from start, store the optimal solution. When selecting the ith item, only 2 choices: select it or not. Max is used to decide which to choose.

$dp[i][j]$: the maximum value restricted to item 1...i such that the sum of the weight is at most j

Recurrence
$$
dp[i][j]=max(dp[i-1][j], dp[i-1][j-w_i]+v_i)
$$

### Longest Common Subsequence

Given to string x[1...m] and y[1...n], find a subsequence common to both of longest length

Starting from start, store the optimal solution. There are two strings, so we need 2d table. When compare the ith and jth character, only two situations: same or not. If same, +1, if not, becomes subproblem of either x[1...i-1] - y or y[1...j-1] - x. 

$dp[i][j]$: the length of LCS for x[1...i] and y[1...j]

Recurrence
$$
dp[i][j]=dp[i-1][j-1]+1, if\ x[i]=y[j] \\
dp[i][j] = \max(dp[i-1][j], dp[i][j-1]), otherwise
$$

### Rod Cutting

*Given a rod of length n, and an array that contains rod prices of length i, where 1 ≤ i ≤ n, determine the maximum profit you could obtain from cutting up the rod and selling its pieces.*

Starting from start, store the optimal solution. At each length, select where to be the start point of this piece. 

$dp[i]$: the maximum profit obtained from cutting up rod with length i

Recurrence
$$
dp[i] = \max_{j=1}^i(dp[i-j]+v[j])
$$

### Box Stack

*Given a collection of n rectangular three-dimensional boxes of integer dimensions b1,..., bn, where bi = (li x wi x hi), i.e., the ith box has length li, width wi, and height hi. calculate the height of the tallest stack of boxes you can form under the following constraints: A box cannot be rotated, and a box bi can only be stacked on bj if the base of bi*

First sort the arrays by length, breaking ties by width. Then we can ignore the length dimension. 

```
c = sorted(b, key = b.l)
```

Starting from start, store the optimal solution. At each box, we can either select it or not. If we select it, we should continue to select which lower box is should be based on.

$dp[i]$: the maximum height using box 1...i. 
$$
dp[i]=\max(dp[i-1], \max_{j=1}^{i}([dp[i-j] + c[j].H\ if\ c[j].W \geq c[i].W \ else \ C[i].H]))
$$

### Candy Swap

*Visit n animals in order and each animal has a candy, which has one of three types.*

- *If you swap your candy for another candy of the same type, you earn one point.*
- *If you swap your candy for a candy of a different type, you lose one point. (Your score can be negative.)*
- *If you visit an animal and decide not to swap candy, your score does not change.*

*Find the maximum possible score.*

Starting from end, store the partial solution. Starting from end because when we can only fill the current steps based on the candy types we at next step. And we should always look afterwards to make a decision. Behavious in the past is helpless for our current status. 

$dp[i][j]$: the maximum possible score when I start visiting animal j till the end with candy i.

Recurrence
$$
dp[i][j]=dp[i][j+1]+1,\ if \ c[j]=i\\
dp[i][j]=\max(dp[i][j+1], -1 + dp[c[j]][j+1])
$$

### When to plant

*In each year can plant 0, 1, 2 seeds*

- *No plant, no harvest*
- *1 seeds, harvest A[i], but no planting the next year*
- *2 seeds, harvest `2 * A[i]`, but no planting the next two years*

*Find the maximum possible amount.*

Starting from end, store the optimal solution. We should always look afterwards to make decisions.

$dp[i]$: the maximum possible amount start from year i till the end.

Recurrence
$$
dp[i]=\max(dp[i+1], s[i] + dp[i+2], 2 * s[i]+dp[i+3])
$$

### Most Likely Number of Wins

*Your favorite sports team is about to play a season consisting of n games. Due to variables such as opponent strength and days of rest before the game, the probability of winning each game varies. Your friend has a model which predicts these probabilities—they are provided to you as P [1..n] where P [i] contains the probability that your team wins the ith game. Determine what is the most likely number of wins your team will have after the entire season is played.*

Starting from start, since state is irrelevant to following behaviours.

Storing partial solutions: probabilities. The outcome is determined by probabilities which is provided by input, so we should store probability.

$dp[i][j]$: the probability that wins i games in the first j games. The final answer would be argmax_i(`dp[i][n]`)

Recurrence
$$
dp[i][j]=max(p[j]*dp[i-1][j-1], (1-p[j])*dp[i][j-1])
$$

### Expotential Sequences

*Given two integers k and n, find the number of possible sequences of length n of positive integers such that each of the next element is greater than or equal to twice of the previous element but less than or equal to k. Should be in O(kn) time.*

> ```
> Input : k = 10, n = 4
> Output : 4
> There should be n elements and value of last element should be at-most k.
> The sequences are {1, 2, 4, 8}, {1, 2, 4, 9}, {1, 2, 4, 10}, {1, 2, 5, 10}
> ```

Starting from start, since current state is irrelavant to upcoming states.

Storing optimal solutions: $dp[i,j]$ is the # of sequences of length i with elements less than or equal to j

Recurrence
$$
dp[i][j]=dp[i][j-1]+dp[i-1][\frac{j}{2}]
$$
Initial state: $dp[i][j]=0$ for $j<2^{(i-1)}, dp[1][j]=1$

## Leetcode

### 213 打家劫舍2

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

```
示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

示例 2:

输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。偷窃到的最高金额 = 1 + 3 = 4 。
```

**思路**：分别进行两次动态规划，第一次只关注从第一个屋子到倒数第二个屋子；第二次只关注第二个屋子到最后一个屋子，这样保证头尾两个屋子不同时被选中

```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        self.s1 = [0] * len(nums)
        self.s2 = [0] * len(nums)
        for i in range(len(nums) - 1):
            if i == 0:
                self.s1[i] = nums[i]
                self.s2[i+1] = nums[i+1]
            elif i == 1:
                self.s1[i] = max(nums[i], nums[i-1])
                self.s2[i+1] = max(nums[i+1], nums[i])
            else:
                self.s1[i] = max(self.s1[i-2] + nums[i], self.s1[i-1])
                self.s2[i+1] = max(self.s2[i-1] + nums[i+1], self.s2[i])
        return max(self.s1[-2], self.s2[-1])
```

### 279 完全平方数

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

```
示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4

示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9
```

关键思路：动态规划递推公式：$dp[i]=\min(dp[i], dp[i-k]+1)$，k是所有比i小的完全平方数

```python
import math

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        
        dp = [float('inf')] * (n+1)
        # bottom case
        dp[0] = 0
        
        for i in range(1, n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        
        return dp[-1]
```

### 1143 最长公共子序列

给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。

```
示例 1:

输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace"，它的长度为 3。

示例 2:

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。

示例 3:

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0
```

关键思路：将`dp[i][j]`定义为str1[0...i]和str2[0...j]的最长公共子序列。如果str[i] == str[j]，说明这个字母同时出现在两个字符串中，是最长公共子序列的一部分；否则，说明当前这两个字母至少有一个不属于最长公共子序列，从而这个位置的dp值取决于分别去掉i和j之后的最长的那个

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2)+1) for _ in range((len(text1)+1))]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[-1][-1]
```

### 416 分割等和子集

给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200

```
示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11]

示例 2:
输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集
```

关键思路

- 类比为01背包问题：从num中选取一定的元素，看能否装进容量为sum/2的背包
- dp数组的定义：`dp[i][j]`表示在下标为[0,i]的num元素中，取一些值可以使他们的和为j

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        else:
            target = s // 2
            dp = [[0] * (target+1) for _ in range(len(nums))]
            if nums[0] < target:
                dp[0][nums[0]] = 1
            for i in range(1, len(nums)):
                for j in range(0, target+1):
                    if j == nums[i]:
                        dp[i][j] = 1
                        continue
                    elif j > nums[i]:
                        dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                    else:
                        dp[i][j] = dp[i-1][j]
        return bool(dp[-1][-1])
```

### 474 一和零

给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

```
示例 1：
输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。

示例 2：
输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
```

将这道题看成price固定为1，体积为0或1的个数的01背包问题。`dp[i][j]`表示i个0，j个1能包含的最多字符串数量，则有`dp[i][j]=max(dp[i][j], 1+dp[i-num(0)][j-num(1)])`，从字符串列表的第1个开始遍历字符串，同时倒序更新dp，因为要防止上一轮的结果被提前改变

```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if not strs:
            return False
        dp = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            zeros, ones = s.count('0'), s.count('1')
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i-zeros][j-ones])
        return dp[-1][-1]
```

### 322 零钱兑换

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。

```
示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0
```

递归方程：设F(i)为满足金额i所需要最少的硬币数量，则对每个硬币金额cj，有$F(i)=\min F(i-c_j)+1$

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin]+1)
        return dp[-1] if dp[-1] != float('inf') else -1
```

### 518 零钱兑换2

给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 

```
示例 1:
输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

示例 2:
输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。

示例 3:
输入: amount = 10, coins = [10] 
输出: 1
```

解题思路：对于每个金额coin，都可以使用/不使用它组成总金额为i的组合：$F_{c}(i)=F_{c'}(i)+F_{c'}(i-c)$，c‘为不考虑这个coin时的coin集合

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] += dp[x - coin]

        return dp[-1]
```

### 139 单词拆分

给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

    拆分时可以重复使用字典中的单词。
    你可以假设字典中没有重复的单词。

```
示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
```

解题思路：将dp[i]定义为字符串前i个字母组成的子串是否合法。那么，对于每个子串，判断方式就是依次遍历每个可以插入空格的地方，判断左右两个子串是否合法。将dp[0]设为True，则合法的子串在一开始遍历插入空格处就可以被检查到

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s)+1)
        dp[0] = 1
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = 1
        return bool(dp[-1])
```

### 309 最佳买卖股票时机含冷冻期

给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

```
示例:
输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
```

解题思路：这道题每一天结束后对应3种状态：手上有股票；没有股票但处于冷冻期；没有股票但处于非冷冻期

将`dp[i][0,1,2]`定义为上述3种状态下的第i日最大收益

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        f0, f1, f2 = -prices[0], 0, 0
        for i in range(1, n):
            newf0 = max(f0, f2 - prices[i])
            newf1 = f0 + prices[i]
            newf2 = max(f1, f2)
            f0, f1, f2 = newf0, newf1, newf2
        
        return max(f1, f2)
```

### 53 最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

```
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```

- dp[i]定义：以i为结尾元素的最大子序和

- 状态转移方程：每一步新的元素可以加入之前的子序列，也可以单独成为新的子序列，当它比加上之前的序列大的时候：$dp[i]=\max(dp[i-1]+nums[i], nums[i])$

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pre, cur, ans = nums[0], 0, nums[0]
        for i in range(1, len(nums)):
            cur = max(pre+nums[i], nums[i])
            pre = cur
            ans = max(ans, cur)
        return ans
```

### 10 正则表达式匹配[H]

给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

    '.' 匹配任意单个字符
    '*' 匹配零个或多个前面的那一个元素

所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。


示例 1：

输入：s = "aa" p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。

示例 2:

输入：s = "aa" p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3：

输入：s = "ab" p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4：

输入：s = "aab" p = "c*a*b"
输出：true
解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5：

输入：s = "mississippi" p = "mis*is*p*."
输出：false

思路：

- 状态：dp[i] [j]: s的前i个字符和p的前j个字符是否匹配上
- 状态转移方程：![](/Users/yuwang/Desktop/学习笔记/Study-scripts/Algorithms/Algorithms/..\img\正则表达式dp.png)

```
以一个例子详解动态规划转移方程：
S = abbbbc
P = ab*d*c
1. 当 i, j 指向的字符均为字母（或 '.' 可以看成一个特殊的字母）时，
   只需判断对应位置的字符即可，
   若相等，只需判断 i,j 之前的字符串是否匹配即可，转化为子问题 f[i-1][j-1].
   若不等，则当前的 i,j 肯定不能匹配，为 false.
   
       f[i-1][j-1]   i
            |        |
   S [a  b  b  b  b][c] 
   
   P [a  b  *  d  *][c]
                     |
                     j
   

2. 如果当前 j 指向的字符为 '*'，则不妨把类似 'a*', 'b*' 等的当成整体看待。
   看下面的例子

            i
            |
   S  a  b [b] b  b  c  
   
   P  a [b  *] d  *  c
            |
            j
   
   注意到当 'b*' 匹配完 'b' 之后，它仍然可以继续发挥作用。
   因此可以只把 i 前移一位，而不丢弃 'b*', 转化为子问题 f[i-1][j]:
   
         i
         | <--
   S  a [b] b  b  b  c  
   
   P  a [b  *] d  *  c
            |
            j
   
   另外，也可以选择让 'b*' 不再进行匹配，把 'b*' 丢弃。
   转化为子问题 f[i][j-2]:

            i
            |
   S  a  b [b] b  b  c  
    
   P [a] b  *  d  *  c
      |
      j <--
```

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]
```

