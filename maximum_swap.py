"""
670. Maximum Swap https://leetcode.com/problems/maximum-swap/

You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Input: num = 9973
Output: 9973
Explanation: No swap.
"""


def maximum_swap(num: int) -> int:
    digits = list(map(int, str(num)))
    last_seen = {digit: i for (i, digit) in enumerate(digits)}

    for i, digit in enumerate(digits):
        for candidate in reversed(range(digit + 1, 10)):
            if last_seen.get(candidate, -1) > i:
                j = last_seen[candidate]
                digits[i], digits[j] = digits[j], digits[i]
                return int("".join(map(str, digits)))

    return num


def test_0():
    assert maximum_swap(9971) == 9971


def test_1():
    assert maximum_swap(28719910) == 98719210


# O(n) | O(1)
