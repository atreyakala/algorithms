def addBinary(a, b):
    maxLen = max(len(a), len(b))
    a = a.zfill(maxLen)
    b = b.zfill(maxLen)

    carry = 0
    result = []
    for i in xrange(maxLen - 1, -1, -1):
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
