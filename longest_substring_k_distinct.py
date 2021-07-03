"""
340. Longest Substring with At Most K Distinct Characters https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Input: s = "eceba", k = 2
Output: 3

Input: s = "aa", k = 1
Output: 2

Constraints:
    1 <= s.length <= 5 * 104
    0 <= k <= 50
"""


from collections import defaultdict


def length_of_longest_substring_k_distinct(string: str, k: int) -> int:
    window_char_count = defaultdict(int)
    left_idx = 0
    max_length = 0

    for right_idx, right_char in enumerate(string):
        window_char_count[right_char] += 1
        if len(window_char_count) > k:
            left_char = string[left_idx]
            window_char_count[left_char] -= 1
            if window_char_count[left_char] == 0:
                del window_char_count[left_char]
            left_idx += 1
        else:
            max_length = max(max_length, right_idx - left_idx + 1)

    return max_length

# O(n) | O(k)


def test_0():
    assert length_of_longest_substring_k_distinct("eceba", 2) == 3


def test_1():
    assert length_of_longest_substring_k_distinct("aaaaa", 1) == 5


def test_2():
    assert length_of_longest_substring_k_distinct("e", 3) == 1


def test_3():
    assert length_of_longest_substring_k_distinct("abee", 1) == 2
