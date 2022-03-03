### 160

判断链表相交点

solution:

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB
        while(a != b):
            if a == None:
                a = headB
            else:
                a = a.next
            if b == None:
                b  = headA
            else:
                b = b.next
        return a
```

- 思路关键：相交时，a和b指针都会在交换链表之后在交点相遇；不相交时，a和b会同时等于None

### 206

递归解法：

```python
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverse(head):
            if head == None or head.next == None:
                return head
            p = reverse(head.next)
            head.next.next = head
            head.next = None
            return p
        p = reverse(head)
        return p
```

- 关键点：递归函数必须有返回值

### 21

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

```
示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```

solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def merge(l1, l2):
            if l1 == None:
                return l2
            elif l2 == None:
                return l1
            elif l1.val > l2.val:
                l2.next = merge(l1, l2.next)
                return l2
            else:
                l1.next = merge(l1.next, l2)
                return l1
        return merge(l1, l2)
```

- 采用递归的典型做法。从最下层开始，每返回一层都是改变一次原始链表的指针指向。比较当前哪个数更小，就在哪个数后面改变指针方向。

### 445

给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

```
示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7
```

solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = []
        s2 = []
        ans = None
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        carry = 0
        while len(s1) > 0 or len(s2) > 0 or carry:
            if len(s1) > 0:
                add1 = s1.pop()
            else:
                add1 = 0
            if len(s2) > 0:
                add2 = s2.pop()
            else:
                add2 = 0
            curr = add1 + add2 + carry
            carry = curr // 10
            val = curr % 10
            newnode = ListNode(val)
            newnode.next = ans
            ans = newnode
        return ans
```

- tips：涉及到逆序的问题，比如这个题中的求和是逆序，记得用栈！python实现栈非常简单高效，

### 234

请判断一个链表是否为回文链表。

```
示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
```

- 精彩解法：设置快慢指针，快指针每次前进两个节点，慢指针每次前进一个节点；当快指针走到末尾，慢指针恰好走到链表的后一半。与此同时，设置另一个指针随时保持在慢指针之前，负责反转前一半链表。最后同时比较慢指针和另一个指针的值。空间复杂度O(1)