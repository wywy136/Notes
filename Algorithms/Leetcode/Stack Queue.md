### 学习笔记

- 实现队列的出队操作，可以用python list类的pop(0)函数。但这样效率低下。

### 739

请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

solution:

```python
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        days = list(0 for i in range(len(T)))
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                p = stack.pop()
                days[p] = i - p
            stack.append(i)
        return days
```

- 思路关键：栈内保存的元素是“数组下标”，也就是天数，而不是温度。这样在出栈的时候，就得到了之前的天对应的下标。且利用当前的下标和之前的下标的差，正好是题目所需的隔天数！