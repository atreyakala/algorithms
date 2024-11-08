"""
31. Next Permutation https://leetcode.com/problems/next-permutation/

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Example 4:
Input: nums = [1]
Output: [1]

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

from typing import List


def next_permutation(nums: List[int]) -> None:
    inversion_point = len(nums) - 2
    while inversion_point >= 0 and nums[inversion_point] >= nums[inversion_point + 1]:
        inversion_point -= 1

    if inversion_point == -1:
        nums[:] = reversed(nums)
        return

    for i in reversed(range(inversion_point + 1, len(nums))):
        if nums[i] > nums[inversion_point]:
            nums[i], nums[inversion_point] = nums[inversion_point], nums[i]
            break

    nums[inversion_point + 1:] = reversed(nums[inversion_point + 1:])
    return


def test_0():
    nums = [1, 1, 5]
    next_permutation(nums)
    assert nums == [1, 5, 1]


def test_1():
    nums = [3, 2, 1]
    next_permutation(nums)
    assert nums == [1, 2, 3]


def test_0():
    nums = [1]
    next_permutation(nums)
    assert nums == [1]


# O(n) | O(1)
