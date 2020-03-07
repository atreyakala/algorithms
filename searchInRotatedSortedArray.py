# [4, 5, 0, 1, 2, 3]
def findPivotIndex(nums):
    if len(nums) == 1:
        return 0
    if nums[0] < nums[-1]:
        return 0
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            return mid + 1
        if nums[mid - 1] > nums[mid]:
            return mid
        if nums[mid] > nums[left]:
            left = mid + 1
        else:
            right = mid - 1

def binarySearch(nums, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            left =  mid + 1
        else:
            right = mid - 1
    return -1

def search(nums, target):
    size = len(nums)
    if nums is None or size == 0:
        return -1
    pivotIndex = findPivotIndex(nums)
    if target == nums[pivotIndex]:
        return pivotIndex
    elif nums[pivotIndex] < target <= nums[-1]:
        return binarySearch(nums, target, pivotIndex + 1, size - 1)
    else:
        return binarySearch(nums, target, 0, pivotIndex - 1)

import pytest

def test_0():
    assert search([], 1) == -1

def test_1():
    assert search([1, 2, 3], 1) == 0

def test_2():
    assert search([4, 5, 6, 7, 0, 1, 2], 5) == 1

def test_3():
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1

def test_2():
    assert search([4, 5, 0, 1, 2, 3], 5) == 1
