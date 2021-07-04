"""
43. Multiply Strings https://leetcode.com/problems/multiply-strings/

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Input: num1 = "2", num2 = "3"
Output: "6"

Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
    1 <= num1.length, num2.length <= 200
    num1 and num2 consist of digits only.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    res = [0] * (len(num1) + len(num2))

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            res[i + j + 1] += int(num1[i]) * int(num2[j])
            res[i + j] += res[i + j + 1] // 10
            res[i + j + 1] %= 10

    i = 0
    while i < len(res) and res[i] == 0:
        i += 1

    return "".join(map(str, res[i:]))

# O(n*m) | O(n + m)


def test_0():
    assert multiply("903", "15") == str(903 * 15)

