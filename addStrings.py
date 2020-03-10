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
