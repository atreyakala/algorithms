# 344. Reverse String https://leetcode.com/problems/reverse-string/

# Write a function that reverses a string. The input string is given as an array of characters s

# Input: s = ["h", "e", "l", "l", "o"]
# Output: ["o", "l", "l", "e", "h"]
#
# Input: s = ["H", "a", "n", "n", "a", "h"]
# Output: ["h", "a", "n", "n", "a", "H"]


from typing import List


def reverse_string(string: List[str]) -> None:
    if string is None or len(string) == 0:
        return

    left_idx = 0
    right_idx = len(string) - 1

    while left_idx < right_idx:
        string[left_idx], string[right_idx] = string[right_idx], string[left_idx]
        left_idx += 1
        right_idx -= 1

    return


def test_0():
    string = None
    reverse_string(string)
    assert string is None


def test_1():
    string = []
    reverse_string(string)
    assert string == []


def test_2():
    string = ["a", "b", "c"]
    reverse_string(string)
    assert string == ["c", "b", "a"]

# O(N) | O(1)


