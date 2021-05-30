# https://www.algoexpert.io/questions/Group%20Anagrams
# O(w * n * log(n)) time | O(w * n) space
from collections import defaultdict
from typing import List


def group_anagrams(words: List[str]) -> List[List[str]]:
    anagrams = defaultdict(lambda: [])
    for word in words:
        key = "".join(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())
