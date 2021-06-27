"""
674. Longest Continuous Increasing Subsequence https://leetcode.com/problems/longest-continuous-increasing-subsequence/

Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.
A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element 4.

Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly increasing.

Constraints
    1 <= nums.length <= 104
    -109 <= nums[i] <= 109
"""


from typing import List


def find_length_of_lcis(nums: List[int]) -> int:
    max_length = 1
    current_length = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_length += 1
        else:
            current_length = 1
        max_length = max(max_length, current_length)
    return max_length


def test_0():
    assert find_length_of_lcis([1, 3, 5, 4, 7]) == 3


def test_1():
    assert find_length_of_lcis([2]) == 1


# O(n) | O(1)
