"""
66. Plus One https://leetcode.com/problems/plus-one/

Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:
Input: digits = [0]
Output: [1]

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
"""

from typing import List


def plus_one(digits: List[int]) -> List[int]:
    for i in reversed(range(0, len(digits))):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits

    return [1] + digits


def test_0():
    assert plus_one([1]) == [2]


def test_1():
    assert plus_one([1, 2, 9]) == [1, 3, 0]


def test_2():
    assert plus_one([9, 9]) == [1, 0, 0]


# O(N) | O(1)