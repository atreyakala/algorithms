"""
140. Word Break II https://leetcode.com/problems/word-break-ii/

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences in any order. Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

Constraints:
    1 <= s.length <= 20
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 10
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.
"""

from typing import List


def word_break(string: str, word_dict: List[str]) -> List[str]:
    return word_break_helper(string, set(word_dict), {})


def word_break_helper(string: str, word_dict: set, memo: dict) -> List[str]:
    if len(string) == 0:
        return [""]

    if string in memo:
        return memo[string]

    sentences = []

    for word in word_dict:
        if string.startswith(word):
            suffix = string[len(word) : ]
            suffix_sentences = word_break_helper(suffix, word_dict, memo)
            for suffix_sentence in suffix_sentences:
                optional_space = " " if len(suffix_sentence) > 0 else ""
                sentences.append(word + optional_space + suffix_sentence)

    memo[string] = sentences
    return sentences

# O(w + n^2 + 2^n) | O(2^n * n + w)


def test_0():
    assert word_break("catsanddog", ["cat","cats","and","sand","dog"]) == ["cat sand dog", "cats and dog"]
