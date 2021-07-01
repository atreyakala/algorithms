"""
88. Merge Sorted Array https://leetcode.com/problems/merge-sorted-array/

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order. The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109
"""

from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    idx_1 = m - 1
    idx_2 = n - 1
    write_idx = m + n - 1

    while idx_1 >= 0 and idx_2 >= 0:
        num1 = nums1[idx_1]
        num2 = nums2[idx_2]

        if num1 >= num2:
            nums1[write_idx] = num1
            idx_1 -= 1
        else:
            nums1[write_idx] = num2
            idx_2 -= 1
        write_idx -= 1

    while idx_2 >= 0:
        nums1[write_idx] = nums2[idx_2]
        idx_2 -= 1
        write_idx -= 1

# O(m + n) | O(1)
