"""
438. Find All Anagrams in a String https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]

Input: s = "abab", p = "ab"
Output: [0,1,2]

Constraints
    1 <= s.length, p.length <= 3 * 104
    s and p consist of lowercase English letters.
"""

from collections import defaultdict
from typing import List


def find_anagrams(search_string: str, target_string: str) -> List[int]:
    target_string_size = len(target_string)
    search_string_size = len(search_string)

    if target_string_size > search_string_size:
        return []

    required_char_count = defaultdict(int)
    for s, t in zip(search_string[:target_string_size], target_string):
        update_char_count(required_char_count, s, -1)
        update_char_count(required_char_count, t, 1)

    anagram_start_indices = []

    for i in range(search_string_size - target_string_size):
        if len(required_char_count) == 0:
            anagram_start_indices.append(i)

        update_char_count(required_char_count, search_string[i], -1)
        update_char_count(required_char_count, search_string[i + target_string_size], 1)

    if len(required_char_count) == 0:
        anagram_start_indices.append(search_string_size - target_string_size)

    return anagram_start_indices

# O(n) | O(m)


def update_char_count(required_char_count: defaultdict, char: str, step: int) -> None:
    required_char_count[char] += step
    if required_char_count[char] == 0:
        del required_char_count[char]


def test_0():
    assert find_anagrams("abab", "ab") == [0, 1, 2]


def test_1():
    assert find_anagrams("cbaebabacd", "abc") == [0, 6]


if __name__ == "__main__":
    test_0()