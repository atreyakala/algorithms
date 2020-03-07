def addStrings(num1, num2):
    sum = ""
    carry = 0
    pos1 = len(num1) - 1
    pos2 = len(num2) - 1
    while pos1 >= 0 or pos2 >= 0:
        currentSum = carry
        if pos1 >= 0: currentSum += ord(num1[pos1]) - ord('0')
        if pos2 >= 0: currentSum += ord(num2[pos2]) - ord('0')
        digit = currentSum % 10
        carry = currentSum / 10
        sum += str(digit)
        pos1 -= 1
        pos2 -= 1
    if carry == 1: sum += '1'
    return sum[::-1]
