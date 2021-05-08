# 953. Verifying an Alien Dictionary: https://leetcode.com/problems/verifying-an-alien-dictionary/

# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false

from typing import List


def is_alien_sorted(words: List[str], order: str) -> bool:
    char_order = {char: i for i, char in enumerate(order)}

    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]

        if not is_pair_sorted(current_word, next_word, char_order):
            return False

    return True


def is_pair_sorted(current_word: str, next_word: str, char_order: dict) -> bool:
    for i in range(min(len(current_word), len(next_word))):
        char_from_current_word = current_word[i]
        char_from_next_word = next_word[i]

        if char_from_current_word == char_from_next_word:
            continue

        return char_order[char_from_current_word] < char_order[char_from_next_word]

    return len(current_word) <= len(next_word)


def test_1():
    assert not is_alien_sorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz")


def test_2():
    assert not is_alien_sorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz")


def test_3():
    assert is_alien_sorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")

# O(N*M) | O(1) : where "N" is the number of words and "M" is the length of each word
# In worst case all the words will be the same
