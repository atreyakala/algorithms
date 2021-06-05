"""
125. Valid Palindrome https://leetcode.com/problems/valid-palindrome/

Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


def is_palindrome(string: str) -> bool:
    left_idx = 0
    right_idx = len(string) - 1

    while left_idx < right_idx:
        if not string[left_idx].isalnum():
            left_idx += 1
        elif not string[right_idx].isalnum():
            right_idx -= 1
        elif string[left_idx].lower() != string[right_idx].lower():
            return False
        else:
            left_idx += 1
            right_idx -= 1

    return True


def test_0():
    assert is_palindrome("aba")


def test_1():
    assert not is_palindrome("abca")


def test_2():
    assert is_palindrome("abba")


def test_3():
    assert is_palindrome("A man, a plan, a canal: Panama")

# O(n) time | O(1) space
