def checkInclusion(chars, string):
    if len(string) < len(chars):
        return False
    targetCharCount = [0] * 26
    for char in chars:
        targetCharCount[ord(char) - ord('a')] += 1
    windowCharCount = [0] * 26
    for rightIdx in xrange(len(string)):
        rightChar = string[rightIdx]
        windowCharCount[ord(rightChar) - ord('a')] += 1
        if rightIdx >= len(chars):
            leftIdx = rightIdx - len(chars)
            leftChar = string[leftIdx]
            windowCharCount[ord(leftChar) - ord('a')] -= 1
        if windowCharCount == targetCharCount:
            return True
    return False

def checkInclusion(chars, string):
    if len(string) < len(chars):
        return False
    return stringContainsChars(string, chars)

def stringContainsChars(string, chars):
    charCount = {}
    rightIdx = 0
    for i in xrange(len(chars)):
        char = string[i]
        incrementCharCount(charCount, char)
    targetCharCount = getCharCount(chars)
    if charCount == targetCharCount:
        return True
    leftIdx = 0
    rightIdx = len(chars)
    while rightIdx < len(string):
        leftChar = string[leftIdx]
        if leftChar in charCount:
            decrementCharCount(charCount, leftChar)
            if charCount[leftChar] == 0: del charCount[leftChar]
        rightChar = string[rightIdx]
        if rightChar in targetCharCount:
            incrementCharCount(charCount, rightChar)
        if charCount == targetCharCount:
            return True
        leftIdx += 1
        rightIdx += 1
    return False

def getCharCount(chars):
    charCount = {}
    for char in chars:
        incrementCharCount(charCount, char)
    return charCount

def incrementCharCount(charCount, char):
    if char in charCount:
        charCount[char] += 1
    else:
        charCount[char] = 1

def decrementCharCount(charCount, char):
    charCount[char] -= 1

import pytest

def test_1():
    assert checkInclusion("ab", "aflafjab")

def test_3():
    assert checkInclusion("ab", "acba")

def test_2():
    assert not checkInclusion("ab", "eidboaoo")

def test_3():
    assert not checkInclusion("hello", "ooolleoooleh")
