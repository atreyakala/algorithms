def dotProduct(list1, list2):
    c1 = compress(list1)
    c2 = compress(list2)
    return dp(c1, c2)

def dp(v1, v2):
    sum = 0
    pos1 = 0
    pos2 = 0
    while pos1 < len(v1) and pos2 < len(v2):
        multiplier = min(v1[pos1][1], v2[pos2][1])
        sum += multiplier * v1[pos1][0] * v2[pos2][0]
        v1[pos1][1] -= multiplier
        v2[pos2][1] -= multiplier
        if v1[pos1][1] == 0: pos1 += 1
        if v2[pos2][1] == 0: pos2 += 1
    return sum

def compress(nums):
    out = []
    i = 0
    while i < len(nums):
        curr = nums[i]
        count = 1
        while i + 1 < len(nums) and nums[i + 1] == curr:
            count += 1
            i += 1
        out.append([curr, count])
        i += 1
    return out

import pytest

def test_1():
    assert dotProduct([2, 2, 3, 3, 3], [5, 4, 4, 4, 4]) == 2*5 + 2*4 + 3*3*4
