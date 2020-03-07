def nextPermutation(nums):
    if nums is None: return
    i = len(nums) - 1
    while i > 0:
        if nums[i] > nums[i - 1]:
            indexToSwap = findIndexToSwap(nums, nums[i - 1])
            nums[i - 1], nums[indexToSwap] = nums[indexToSwap], nums[i - 1]
            reverseArrayFrom(nums, i)
            return
        i -= 1
    nums.sort()
    return

def findIndexToSwap(arr, num):
    i = len(arr) - 1
    while i > 0:
        if arr[i] > num:
            return i
        i -= 1

def reverseArrayFrom(arr, start):
    if arr is None or len(arr) == 0: return
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

import pytest

def test_1():
    assert nextPermutation([1, 2, 3]) == [1, 3, 2]

def test_2():
    assert nextPermutation([3, 2, 1]) == [1, 2, 3]

def test_3():
    assert nextPermutation([1, 3, 2]) == [2, 1, 3]
