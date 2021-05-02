# 680. Valid Palindrome II https://leetcode.com/problems/valid-palindrome-ii/

# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True

# Example 2:
# Input: "abca"
# Output: True

def valid_palindrome(string: str) -> bool:
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return is_palindrome(string[left: right]) or is_palindrome(string[left + 1: right + 1])
        left += 1
        right -= 1
    return True


def is_palindrome(string: str) -> bool:
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


def test_1():
    assert valid_palindrome("aba")


def test_2():
    assert valid_palindrome("ab")


def test_3():
    assert valid_palindrome("abca")


def test_4():
    assert not valid_palindrome("abcd")
