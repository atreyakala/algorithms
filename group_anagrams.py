"""
49. Group Anagrams https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
"""

from collections import defaultdict
from typing import List


# O(w * n) time | O(w * n) space
def group_anagrams(words: List[str]) -> List[List[str]]:
    anagrams = defaultdict(lambda: [])
    for word in words:
        char_count = [0] * 26
        for char in word:
            char_count[ord(char) - ord('a')] += 1
        anagrams[tuple(char_count)].append(word)
    return list(anagrams.values())


# O(w * n * log(n)) time | O(w * n) space
def group_anagrams(words: List[str]) -> List[List[str]]:
    anagrams = defaultdict(lambda: [])
    for word in words:
        key = "".join(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())
