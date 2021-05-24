# 75. Sort Colors https://leetcode.com/problems/sort-colors/

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
#
# Example 3:
# Input: nums = [0]
# Output: [0]
#
# Example 4:
# Input: nums = [1]
# Output: [1]

# Constraints:
#
# n == nums.length
# 1 <= n <= 300
# nums[i] is 0, 1, or 2.

from typing import List


def sort_colors(nums: List[int]) -> None:
    curr_idx = 0
    next_left_idx = 0
    next_right_idx = len(nums) - 1

    while curr_idx <= next_right_idx:
        if nums[curr_idx] == 0:
            nums[curr_idx], nums[next_left_idx] = nums[next_left_idx], nums[curr_idx]
            curr_idx += 1
            next_left_idx += 1
        elif nums[curr_idx] == 1:
            curr_idx += 1
        else:
            nums[curr_idx], nums[next_right_idx] = nums[next_right_idx], nums[curr_idx]
            curr_idx += 1
            next_right_idx -= 1


def test_0():
    l = [0]
    sort_colors(l)
    assert l == [0]


def test_1():
    l = [2, 0, 1]
    sort_colors(l)
    assert l == [0, 1, 2]


def test_2():
    l = [2,0,2,1,1,0]
    sort_colors(l)
    assert l == [0,0,1,1,2,2]


# O(N) | O(1)