def validPalindrome(word):
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return isPalindrome(word[left : right]) or isPalindrome(word[left + 1: right + 1])
        left += 1
        right -= 1
    return True

def isPalindrome(word, i, j):
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

import pytest

def test_1():
    assert validPalindrome("aba")

def test_2():
    assert validPalindrome("ab")

def test_3():
    assert validPalindrome("abca")

def test_4():
    assert not validPalindrome("abcd")
