def subArraySum(nums, k):
    allSums = {0: 1}
    cumulative = 0
    count = 0
    for num in nums:
        cumulative += num
        requiredSum = cumulative - k
        if requiredSum in allSums:
            count += allSums[requiredSum]
        if cumulative not in allSums:
            allSums[cumulative] = 1
        else:
            allSums[cumulative] += 1
    return count

import pytest

def test_1():
    assert subArraySum([1, 1, 1], 2) == 2

def test_2():
    assert subArraySum([1, 2, 1, 3], 3) == 3

def test_3():
    assert subArraySum([1, -1, 2, 1, 0, -2, 2], 3) == 6
