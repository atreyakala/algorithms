"""
67. Add Binary https://leetcode.com/problems/add-binary/

Given two binary strings a and b, return their sum as a binary string.

Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"

Constraints
    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.
"""


def add_binary(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    carry = 0
    result = []
    for i in reversed(range(max_len)):
        if a[i] == "1":
            carry += 1
        if b[i] == "1":
            carry += 1
        if carry % 2 == 1:
            result.append("1")
        else:
            result.append("0")
        carry //= 2

    if carry == 1:
        result.append("1")

    return "".join(reversed(result))


# O(max(a, b)) | O(max(a, b))


def add_binary(a: str, b: str) -> str:
    x = int(a, 2)
    y = int(b, 2)
    while y:
        answer = x ^ y
        carry = (x & y) << 1
        x, y = answer, carry
    return bin(x)[2:]


# O(max(a, b)) | O((a + b)
