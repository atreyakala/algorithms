"""
408. Valid Word Abbreviation https://leetcode.com/problems/valid-word-abbreviation/

A string can be abbreviated by replacing any number of non-adjacent substrings with their lengths. For example, a string such as "substitution" could be abbreviated as (but not limited to):
    "s10n" ("s ubstitutio n")
    "sub4u4" ("sub stit u tion")
    "12" ("substitution")
    "su3i1u2on" ("su bst i t u ti on")
    "substitution" (no substrings replaced)
Note that "s55n" ("s ubsti tutio n") is not a valid abbreviation of "substitution" because the replaced substrings are adjacent.
Given a string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

Input: word = "internationalization", abbr = "i12iz4n"
Output: true

Input: word = "apple", abbr = "a2e"
Output: false

Constraints
    1 <= word.length, abbr.length <= 20
    word consists of only lowercase English letters.
    abbr consists of lowercase English letters and digits.
"""


def valid_word_abbreviation(word: str, abbr: str) -> bool:
    word_idx = 0
    abbr_idx = 0

    while abbr_idx < len(abbr) and word_idx < len(word):
        if abbr[abbr_idx].isalpha():
            if abbr[abbr_idx] != word[word_idx]:
                return False
            else:
                abbr_idx += 1
                word_idx += 1
        else:
            if abbr[abbr_idx] == "0":
                return False

            num = 0
            while abbr_idx < len(abbr) and abbr[abbr_idx].isdigit():
                num = num * 10 + int(abbr[abbr_idx])
                abbr_idx += 1
            word_idx += num

    return word_idx == len(word) and abbr_idx == len(abbr)


def test_0():
    assert not valid_word_abbreviation("apple", "a2e")


def test_1():
    assert valid_word_abbreviation("apppppppppple", "a10le")


def test_2():
    assert valid_word_abbreviation("apple", "5")


def test_3():
    assert valid_word_abbreviation("internationalization", "i5a11o1")


def test_4():
    assert not valid_word_abbreviation("a", "01")


def test_5():
    assert not valid_word_abbreviation("hi", "hi1")


# O(n) | O(1)
