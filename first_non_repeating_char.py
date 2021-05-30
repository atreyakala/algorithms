# https://www.algoexpert.io/questions/First%20Non-Repeating%20Character
from collections import Counter


def first_non_repeating_char(string: str) -> int:
    char_count = Counter(string)
    for idx, char in enumerate(string):
        if char_count[char] == 1:
            return idx
    return -1


def test_0():
    assert first_non_repeating_char("abcdcaf") == 1


def test_1():
    assert first_non_repeating_char("acac") == -1

