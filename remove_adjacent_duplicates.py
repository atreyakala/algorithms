# Leetcode-1047: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

# Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
# We repeatedly make duplicate removals on S until we no longer can.
# Return the final string after all such duplicate removals have been made. It is guaranteed the answer is unique.

# Input: "abbaca"
# Output: "ca"
# Explanation: For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.
# The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

from collections import deque


def remove_duplicates(string: str) -> str:
    char_stack = deque()

    for char in string:
        if char_stack and char_stack[-1] == char:
            char_stack.pop()
        else:
            char_stack.append(char)

    return "".join(char_stack)


def test_0():
    assert remove_duplicates("abbaca") == "ca"


def test_1():
    assert remove_duplicates("aaa") == "a"


def test_2():
    assert remove_duplicates("baca") == "baca"

# O(N) | O(U) where "N" is the length of the string and "U" is the number of unique chars