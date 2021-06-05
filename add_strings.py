"""
415. Add Strings https://leetcode.com/problems/add-strings/

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:
1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""

def add_strings(num1, num2):
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    sum = []
    carry = 0

    for i in reversed(range(max_len)):
        digit1 = ord(num1[i]) - ord('0')
        digit2 = ord(num2[i]) - ord('0')
        current_sum = digit1 + digit2 + carry
        sum.append(current_sum % 10)
        carry = current_sum // 10

    if carry == 1:
        sum.append(carry)

    sum.reverse()
    return "".join(map(str, sum))


def add_decimal_strings(num1, num2):
    num1, num2 = format_numbers(num1, num2)
    carry = 0
    sum = []
    for i in reversed(range(len(num1))):
        if num1[i] == '.':
            sum.append('.')
            continue
        digit1 = ord(num1[i]) - ord('0')
        digit2 = ord(num2[i]) - ord('0')
        current_sum = digit1 + digit2 + carry
        sum.append(str(current_sum % 10))
        carry = current_sum / 10
    if carry == 1:
        sum.append(str(carry))
    sum.reverse()
    if sum[-1] == '.':
        sum.pop()
    return "".join(sum).rstrip('0')


def format_numbers(num1, num2):
    decimal1, fraction1 = split_number_at_decimal(num1)
    decimal2, fraction2 = split_number_at_decimal(num2)
    decimalLen = max(len(decimal1), len(decimal2))
    decimal1 = decimal1.zfill(decimalLen)
    decimal2 = decimal2.zfill(decimalLen)
    fractionLen = max(len(fraction1), len(fraction2))
    fraction1 = pad_trailing_zeroes(fraction1, fractionLen)
    fraction2 = pad_trailing_zeroes(fraction2, fractionLen)
    num1 = decimal1 + '.' + fraction1
    num2 = decimal2 + '.' + fraction2
    return num1, num2


def split_number_at_decimal(num):
    if '.' not in num:
        num += '.'
    decimal, fraction = num.split(".")
    return decimal, fraction


def pad_trailing_zeroes(fraction, requiredLen):
    if len(fraction) < requiredLen:
        trailingZeroes = ['0' for _ in range(requiredLen - len(fraction))]
        fraction += ''.join(trailingZeroes)
    return fraction


def test_1():
    assert add_decimal_strings("13.890", "9.01") == str(13.890 + 9.01)


def test_2():
    assert add_decimal_strings("13.890", "9") == str(13.890 + 9)


def test_3():
    assert add_decimal_strings("13", "9") == str(13 + 9)
