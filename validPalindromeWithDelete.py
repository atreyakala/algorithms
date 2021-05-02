# 680. Valid Palindrome II https://leetcode.com/problems/valid-palindrome-ii/

# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True

# Example 2:
# Input: "abca"
# Output: True

def valid_palindrome(string: str) -> bool:
    left_idx = 0
    right_idx = len(string) - 1
    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return is_palindrome(string[left_idx: right_idx]) or is_palindrome(string[left_idx + 1: right_idx + 1])
        left_idx += 1
        right_idx -= 1
    return True


def is_palindrome(string: str) -> bool:
    left_idx = 0
    right_idx = len(string) - 1
    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    return True


def test_1():
    assert valid_palindrome("aba")


def test_2():
    assert valid_palindrome("ab")


def test_3():
    assert valid_palindrome("abca")


def test_4():
    assert not valid_palindrome("abcd")
