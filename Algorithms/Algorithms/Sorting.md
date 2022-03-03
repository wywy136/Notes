# 排序算法

## 冒泡排序

从后向前比较后一个元素和前一个元素，这样比单纯两两比较要有更少的swap次数

## 选择排序

通过n-i次关键字间的比较，从n-i+1个记录中选出关键字最小的记录，并和第i个记录交换

比较次数和冒泡排序一样多，但交换次数相当少：O(n)

## 直接插入排序

## 希尔排序

## 堆排序

利用大顶堆：每个节点的值都大于其两个孩子的值的二叉树

```python
def HeapSort(L: list):
    for i in range(len(L)//2-1, -1, -1):  # 先从最后一个父节点（下标为len(L)//2-1）往上构建一个最大堆（依次调用heapify），构建的结果是堆顶元素是所有节点中最大的；这一步必须从最后一个父节点开始，否则无法保证堆顶元素大于所有堆中元素
        HeapAdjust(L, i, len(L)-1)

    for i in range(len(L)-1, 0, -1):
        swap(L, 0, i)  # 交换堆顶元素和当前未经排序的子序列的最后一个记录
        HeapAdjust(L, 0, i-1)  # 重新调整L[0...i-1]，即未排序部分 - 只需要logk复杂度


def swap(L: list, i: int, j: int):
    L[i], L[j] = L[j], L[i]

# Heapify - logk
def HeapAdjust(L: list, s: int, m: int)  # s：初始父节点位置；m：最大位置
    temp = L[s]
    j = 2 * s + 1
    while j <= m:  # 可能在调整一部分节点后，剩下的部分不满足大顶堆
        if j < m and L[j] < L[j+1]:  # 找到更大的孩子
            j += 1
        if L[j] <= temp:  # 是否父节点比孩子节点大
            break
        L[s] = L[j]  # 使父节点值=孩子节点值
        s = j  # 准备修改孩子节点的值（L[s]），同时是继续调整的父节点
        j = j * 2 + 1  # 下一个孩子节点
    L[s] = temp


exp = [4, 1, 6, 3, 2, 5, 9, 7, 8]
HeapSort(exp)
print(exp)
```

## 归并排序

非递归方法：从长度为1的相邻片段开始排序，之后是长度为2的相邻片段

```python
def MergeSort(L: list, left: int, right: int):
    if left >= right:
        return
    mid = (left + right) // 2
    MergeSort(L, left, mid)
    MergeSort(L, mid+1, right)
    Merge(L, left, mid, right)


def Merge(L: list, left: int, mid: int, right: int):
    temp = [0 for _ in range(right - left + 1)]
    i, j, k = left, mid+1, 0
    while i <= mid and j <= right:
        if L[i] > L[j]:
            temp[k] = L[j]
            j += 1
        else:
            temp[k] = L[i]
            i += 1
        k += 1
    while i <= mid:
        temp[k] = L[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = L[j]
        k += 1
        j += 1
    for t in range(len(temp)):
        L[left + t] = temp[t]


exp = [4, 1, 6, 3, 2, 5, 9, 7, 8]
MergeSort(exp, 0, len(exp)-1)
print(exp)
```

## 快速排序

partition选取数组最后一个作为比较对象，返回其位于数组的位置，并将数组中小于此对象的移动至此对象最终位置的左侧；**counter**负责记录最终比较对象应该位于的位置，并负责将较大的元素交换至后面

```python
def QuickSort(L: list, left: int, right: int):
    if left >= right:
        return
    pivot = Partition(L, left, right)
    QuickSort(L, left, pivot-1)
    QuickSort(L, pivot+1, right)


def Partition(L: list, left: int, right: int) -> int:
    pivot, counter = right, left
    for i in range(left, right, 1):
        if L[i] < L[pivot]:
            L[i], L[counter] = L[counter], L[i]
            counter += 1
    L[pivot], L[counter] = L[counter], L[pivot]
    return counter


exp = [4, 1, 6, 3, 2, 5, 9, 7, 8]
QuickSort(exp, 0, len(exp)-1)
print(exp)
```

## TopK问题

### 最小堆

利用前k个元素构建一个k个元素的最小堆，之后遍历所有的数据，若新数据大于堆顶，则入堆尾，删除堆顶最小元素，之后重新构建最小堆