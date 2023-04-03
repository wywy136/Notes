# Binary Search

## No-duplicate

Searching in a both-closed range. Target in the array.

```python
def binarySearch(nums:List[int], target:int) -> int:
    left = 0; 
    right = len(nums) - 1; # 注意

    while(left <= right):
        mid = left + (right - left) // 2; # 防止整型溢出
        if(nums[mid] == target):
            return mid; 
        elif(nums[mid] < target):
            left = mid + 1; # 注意
        elif(nums[mid] > target):
            right = mid - 1; # 注意

    return -1;
```

## Duplicate-left

Search left edge in a half closed range. Target in the array.

```python
def left_bound(nums: List[int], target: int) -> int:
    left = 0
    right = nums.length; # 注意
    
    while left < right: # 注意
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid; # 注意

    return left
```

## Duplicate-right

Search right edge in a half closed range. Target in the array.

```python
int right_bound(int[] nums, int target) {
    int left = 0, right = nums.length;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            left = mid + 1; // 注意
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid;
        }
    }
    return left - 1; // 注意
}
```

