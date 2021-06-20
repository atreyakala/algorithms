# 53. Maximum Subarray https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
# Example 2:
# Input: nums = [1]
# Output: 1
#
# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

# Constraints:
#
# 1 <= nums.length <= 3 * 104
# -105 <= nums[i] <= 105

from typing import List


def max_sub_array(nums: List[int]) -> int:
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]

    return max(nums)


def max_sub_array(nums: List[int]) -> int:
    max_ending_here = nums[0]
    max_so_far = nums[0]

    for num in nums[1:]:
        max_ending_here = max(max_ending_here + num, num)
        max_so_far = max(max_ending_here, max_so_far)

    return max_so_far


def test_0():
    assert max_sub_array([-10, -15]) == -10


def test_1():
    assert max_sub_array([-10, 100, -15, 4]) == 100


def test_2():
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

# O(N) | O(1)
