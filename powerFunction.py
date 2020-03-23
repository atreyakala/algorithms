def myPow(num, power):
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
        power = (power / 2)
    return res
