"""
658. Find K Closest Elements https://leetcode.com/problems/find-k-closest-elements/

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:
    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:
    1 <= k <= arr.length
    1 <= arr.length <= 104
    arr is sorted in ascending order.
    -104 <= arr[i], x <= 104
"""


from typing import List


def find_closest_elements(arr: List[int], k: int, x: int) -> List[int]:
    lo = 0
    hi = len(arr) - k

    while lo < hi:
        mid = (lo + hi) // 2
        if x - arr[mid] <= arr[mid + k] - x:
            hi = mid
        else:
            lo = mid + 1

    return arr[lo:lo + k]

# O(log(n - k) + k) | O(1)
