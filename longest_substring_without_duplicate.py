"""
3. Longest Substring Without Repeating Characters https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = ""
Output: 0

Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""


def length_of_longest_substring(string: str) -> int:
    last_seen = {}
    max_length = 0
    start_idx = 0

    for idx, char in enumerate(string):
        if char in last_seen and last_seen[char] >= start_idx:
            start_idx = last_seen[char] + 1
        else:
            max_length = max(max_length, idx - start_idx + 1)
        last_seen[char] = idx

    return max_length

# O(n) | O(len(alphabet))
