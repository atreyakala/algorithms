"""
139. Word Break https://leetcode.com/problems/word-break/

Given a string and a dictionary of strings word_dict. Return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.
"""

from typing import List


def word_break(string: str, word_dict: List[str]) -> bool:
    return word_break_helper(string, set(word_dict), {})


def word_break_helper(string: str, word_dict: set, memo: dict) -> bool:
    if len(string) == 0:
        return True

    if string in memo:
        return memo[string]

    for word in word_dict:
        if string.startswith(word):
            suffix = string[len(word):]
            if word_break_helper(suffix, word_dict, memo):
                return True

    memo[string] = False
    return False

# O(n^3) | O(n)
