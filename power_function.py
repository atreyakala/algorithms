"""
50. Pow(x, n) https://leetcode.com/problems/powx-n/

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
    -100.0 < x < 100.0
    -231 <= n <= 231-1
    -104 <= xn <= 104
"""


def pow(num, power):
    if power < 0:
        num = (1 / num)
        power = -power
    res = 1
    while power > 0:
        if power % 2 == 1:
            res = res * num
            if power == 1:
                break
        num = num * num
        power = (power // 2)
    return res

# O(logn) | O(1)


def pow(num: float, power: int) -> float:
    if power < 0:
        num = (1 / num)
        power = -power

    return pow_helper(num, power)

# O(logn) | O(logn)


def pow_helper(num: int, power: int) -> int:
    if power == 0:
        return 1.0

    half = pow_helper(num, power // 2)
    res = half * half

    return res if power % 2 == 0 else res * num
