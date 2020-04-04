def maximumSwap(num):
    digits = map(int, str(num))
    lastSeen = {digit: i for i, digit in enumerate(digits)}
    for i, digit in enumerate(digits):
        for candidate in xrange(9, digit, -1):
            if candidate > digit and candidate in lastSeen:
                indexToSwap = lastSeen[candidate]
                digits[i], digits[indexToSwap] = digits[indexToSwap], digits[i]
                return int("".join(map(str, digits)))
    return num
