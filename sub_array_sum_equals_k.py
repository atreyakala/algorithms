"""
560. Subarray Sum Equals K https://leetcode.com/problems/subarray-sum-equals-k/
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""

from collections import defaultdict
from typing import List


# O(n) | O(n)
def sub_array_sum(nums: List[int], k: int) -> int:
    all_sums = defaultdict(lambda: 0)
    all_sums[0] = 1

    count = 0
    running_sum = 0
    for num in nums:
        running_sum += num
        required_sum = running_sum - k
        if required_sum in all_sums:
            count += all_sums[required_sum]
        all_sums[running_sum] += 1
    return count


# O(n**2) | O(1)
def sub_array_sum(nums: List[int], k: int) -> int:
    count = 0
    n = len(nums)
    for start_idx in range(n):
        running_sum = 0
        for end_idx in range(start_idx, n):
            num = nums[end_idx]
            running_sum += num
            if running_sum == k:
                count += 1
    return count


def test_1():
    assert sub_array_sum([1, 1, 1], 2) == 2


def test_2():
    assert sub_array_sum([1, 2, 1, 3], 3) == 3


def test_3():
    assert sub_array_sum([1, -1, 2, 1, 0, -2, 2], 3) == 6
