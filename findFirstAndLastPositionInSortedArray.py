def searchRange(nums, target):
    finalRange = [-1, -1]
    binarySearch(nums, target, 0, len(nums) - 1, finalRange, True)
    if finalRange[0] == -1:
        return finalRange
    binarySearch(nums, target, finalRange[0], len(nums) - 1, finalRange, False)
    return finalRange

def binarySearch(nums, target, left, right, finalRange, goLeft):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            if goLeft:
                if mid == 0 or nums[mid - 1] != target:
                    finalRange[0] = mid
                    return
                else:
                    right = mid - 1
            else:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    finalRange[1] = mid
                    return
                else:
                    left = mid + 1
