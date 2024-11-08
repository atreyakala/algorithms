# 26. Remove Duplicates from Sorted Array https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
#
# Example 2:
# Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Output: 5, nums = [0, 1, 2, 3, 4]
# Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.It doesn't matter what values are set beyond the returned length.

# Constraints:
# 0 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# nums is sorted in ascending order.


from typing import List


def remove_duplicates(nums: List[int]) -> int:
    write_idx = 1
    for i in range(1, len(nums)):
        if nums[write_idx - 1] != nums[i]:
            nums[write_idx], nums[i] = nums[i], nums[write_idx]
            write_idx += 1

    return write_idx


def test_0():
    assert remove_duplicates([1]) == 1


def test_1():
    assert remove_duplicates([1, 1, 1, 2]) == 2


# O(N) | O(1)
