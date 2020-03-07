def findMin(nums):
    if len(nums) == 1:
        return nums[0]
    if nums[0] < nums[-1]:
        return nums[0]
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid - 1] > nums[mid]:
            return nums[mid]
        if nums[mid] > nums[left]:
            left = mid + 1
        else:
            right = mid - 1

import pytest

def test_1():
    assert findMin([1]) == 1

def test_2():
    assert findMin([2, 1]) == 1

def test_3():
    assert findMin([4, 5, 0, 1, 2, 3]) == 0

# pytest.main()
