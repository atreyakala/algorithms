def searchRange(nums, target):
    if nums is None or len(nums) == 0:
        return [-1, -1]
    left = searchLeft(nums, target)
    if left == -1:
        return [-1, -1]
    return left, searchRight(nums, target, left)

def searchLeft(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return left if left < len(nums) and nums[left] == target else -1

def searchRight(nums, target, left):
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return right
