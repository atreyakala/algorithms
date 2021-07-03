"""
523. Continuous Subarray Sum https://leetcode.com/problems/continuous-subarray-sum/

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Input: nums = [23,2,6,4,7], k = 13
Output: false

Constraints:
    1 <= nums.length <= 105
    0 <= nums[i] <= 109
    0 <= sum(nums[i]) <= 231 - 1
    1 <= k <= 231 - 1
"""


from typing import List


# sum(i, j) = sum(0, j) - sum(0, i)
# sum(i, j) % k = 0
# sum(0, j) % k = sum (0, i) % k
def check_subarray_sum(nums: List[int], k: int) -> bool:
    seen = {0: -1}
    sum = 0

    for idx, num in enumerate(nums):
        sum += num
        if k != 0:
            sum = sum % k

        if sum in seen:
            if idx - seen[sum] > 1:
                return True
        else:
            seen[sum] = idx

    return False

# O(n) | O(n)


def test_0():
    assert check_subarray_sum([23, 2, 4, 6, 7], 6)
