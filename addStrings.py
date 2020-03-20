def addStrings(num1, num2):
    maxLen = max(len(num1), len(num2))
    num1 = num1.zfill(maxLen)
    num2 = num2.zfill(maxLen)
    sum = []
    carry = 0
    for i in reversed(range(maxLen)):
        digit1 = ord(num1[i]) - ord('0')
        digit2 = ord(num2[i]) - ord('0')
        currentSum = digit1 + digit2 + carry
        sum.append(currentSum % 10)
        carry = currentSum / 10
    if carry == 1:
        sum.append(carry)
    sum.reverse()
    return "".join(map(str, sum))

def addDecimalStrings(num1, num2):
    num1, num2 = normaliseNums(num1, num2)
    carry = 0
    sum = []
    for i in reversed(range(len(num1))):
        if num1[i] == '.':
            sum.append('.')
            continue
        digit1 = ord(num1[i]) - ord('0')
        digit2 = ord(num2[i]) - ord('0')
        currentSum = digit1 + digit2 + carry
        sum.append(str(currentSum % 10))
        carry = currentSum / 10
    if carry == 1:
        sum.append(str(carry))
    sum.reverse()
    if sum[-1] == '.':
        sum.pop()
    return "".join(sum).rstrip('0')

def normaliseNums(num1, num2):
    decimal1, fraction1 = splitNumAtDecimal(num1)
    decimal2, fraction2 = splitNumAtDecimal(num2)
    decimalLen = max(len(decimal1), len(decimal2))
    decimal1 = decimal1.zfill(decimalLen)
    decimal2 = decimal2.zfill(decimalLen)
    fractionLen = max(len(fraction1), len(fraction2))
    fraction1 = padTrailingZeroes(fraction1, fractionLen)
    fraction2 = padTrailingZeroes(fraction2, fractionLen)
    num1 = decimal1 + '.' + fraction1
    num2 = decimal2 + '.' + fraction2
    return num1 , num2

def splitNumAtDecimal(num):
    if '.' not in num:
        num += '.'
    decimal, fraction = num.split(".")
    return decimal, fraction

def padTrailingZeroes(fraction, requiredLen):
    if len(fraction) < requiredLen:
        trailingZeroes = ['0' for _ in range(requiredLen - len(fraction))]
        fraction += ''.join(trailingZeroes)
    return fraction

import pytest

def test_1():
    assert addDecimalStrings("13.890", "9.01") == str(13.890 + 9.01)

def test_2():
    assert addDecimalStrings("13.890", "9") == str(13.890 + 9)

def test_3():
    assert addDecimalStrings("13", "9") == str(13 + 9)
