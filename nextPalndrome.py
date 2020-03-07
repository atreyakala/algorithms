def nextPalindrome(nums):
    if nums is None: return
    for i in xrange(len(nums) - 1, 1, -1):
        if nums[i] > nums[i - 1]:
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
            reverseSubArray(nums, i)
            return
    nums.reverse()
    return

def reverseSubArray(arr, start):
    if arr is None: return
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
    return

import pytest

def test_1():
    assert nextPalindrome([1, 2, 3]) == [1, 3, 2]

def test_2():
    assert nextPalindrome([3, 2, 1]) == [1, 2, 3]
