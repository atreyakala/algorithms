# 394. Decode String - https://leetcode.com/problems/decode-string/

# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Input: s = "3[a2[c]]"
# Output: "accaccacc"

from collections import deque

def decodeString(inputString: str) -> str:
    currentString = ""
    currentMultiplier = 0

    multiplierStack = deque([])
    decodedSoFarStack = deque([])

    for char in inputString:
        if char.isdigit():
            currentMultiplier = currentMultiplier * 10 + int(char)
        elif char.isalpha():
            currentString += char
        elif char == "[":
            multiplierStack.append(currentMultiplier)
            decodedSoFarStack.append(currentString)
            currentString = ""
            currentMultiplier = 0
        if char == "]":
            currentExpansion = multiplierStack.pop() * currentString
            currentString = decodedSoFarStack.pop() + currentExpansion

    return currentString

import pytest

def test_0():
    assert decodeString("ab") == "ab"

def test_1():
    assert decodeString("a2[b]") == "abb"

def test_2():
    assert decodeString("3[a]2[bc]") == "aaabcbc"

def test_3():
    assert decodeString("3[a2[c]]") == "accaccacc"

def test_4():
    assert decodeString("10[ab]") == "abababababababababab"
