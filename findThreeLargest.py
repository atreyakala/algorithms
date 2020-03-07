def findThreeLargest(nums):
    threeLargest = [None] * 3
    for num in nums:
        updateLargest(threeLargest, num)
    return threeLargest

def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num >= threeLargest[2]:
        shiftAndInsert(threeLargest, num, 2)
    elif threeLargest[1] is None or num >= threeLargest[1]:
        shiftAndInsert(threeLargest, num, 1)
    elif threeLargest[0] is None or num >= threeLargest[0]:
        shiftAndInsert(threeLargest, num, 0)
    return

def shiftAndInsert(arr, num, idx):
    for i in range(idx + 1)
        if i == idx:
            arr[i] = num
        else:
            arr[i] = arr[i + 1]

import pytest

def test_1():
    assert findThreeLargest([1, -1, 0, 10, 10, 12]) == [10, 10, 12]
