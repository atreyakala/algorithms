"""
162. Find Peak Element https://leetcode.com/problems/find-peak-element/

A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. You must write an algorithm that runs in O(log n) time.

Input: nums = [1,2,3,1]
Output: 2

Input: nums = [1,2,1,3,5,6,4]
Output: 5

Constraints:
    1 <= nums.length <= 1000
    -231 <= nums[i] <= 231 - 1
    nums[i] != nums[i + 1] for all valid i
"""

from typing import List


def find_peak_element(nums: List[int]) -> int:
    lo = 0
    hi = len(nums) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if nums[mid] > nums[mid - 1]:
            hi = mid
        else:
            lo = mid + 1

    return lo

# O(logn) | O(1)


def test_0():
    assert find_peak_element([4, 5]) == 1


def test_1():
    assert find_peak_element([5, 2]) == 0


def test_2():
    assert find_peak_element([1, 2, 1, 3, 5, 6, 4]) == 1
