def numDecodings(message):
    if message[0] == "0":
        return 0
    if len(message) < 2:
        return 1
    w1 = 1
    for i in xrange(0, len(message)):
        curr = 0 if message[i] == "0" else w1
        if i - 1 >= 0 and isValidPair(message[i], message[i - 1]):
            curr += w2
        w2 = w1
        w1 = curr
    return w1

def isValidPair(curr, prev):
    return (prev == "1") or (prev == "2" and curr <= "6")

def numDecodings(message):
    if message[0] == "0":
        return 0
    if len(message) < 2:
        return 1
    dp = [0] * (len(message) + 1)
    dp[0] = 1
    for i in xrange(0, len(message)):
        dp[i + 1] = 0 if message[i] == "0" else dp[i]
        if i - 1 >= 0 and (message[i - 1] == "1") or (message[i - 1] == "2" and message[i] <= "6"):
            dp[i + 1] += dp[i - 1]
    return dp[-1]

import pytest

def test_1():
    assert numDecodings("12") == 2

def test_2():
    assert numDecodings("223") == 3

def test_3():
    assert numDecodings("0113") == 0

def test_4():
    assert numDecodings("100") == 0

def test_5():
    assert numDecodings("1020") == 1

def test_6():
    assert numDecodings("103") == 1
