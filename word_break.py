from collections import deque
from functools import lru_cache
from typing import List, FrozenSet


def word_break(string: str, word_dict: List[str]) -> bool:
    memo = {}
    return word_break_memo(string, frozenset(word_dict), 0, memo)


def word_break_memo(string: str, word_dict: FrozenSet[str], start: int, memo: dict) -> bool:
    if start == len(string):
        return True

    if start in memo:
        return memo[start]

    for end in range(start + 1, len(string) + 1):
        if string[start: end] in word_dict and word_break_memo(string, word_dict, end, memo):
            memo[start] = True
            return True

    memo[start] = False
    return False


def word_break(string: str, word_dict: List[str]) -> bool:
    # dp[i] is True if s[0..i] can be segmented
    dp = [False] * (len(string) + 1)
    dp[0] = True
    dictionary = {}

    for word in word_dict:
        dictionary[word] = True

    for i in range(len(string)):
        if dp[i]:
            for j in range(i, len(string)):
                if string[i: j + 1] in dictionary:
                    dp[j + 1] = True

    return dp[-1]


def word_break(string: str, word_dict: List[str]) -> bool:
    @lru_cache()
    def word_break_memo(s: str, dictionary: FrozenSet[str], start: int):
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in dictionary and word_break_memo(s, dictionary, end):
                return True
        return False

    return word_break_memo(string, frozenset(word_dict), 0)


def word_break(string, word_dict):
    dictionary = {}
    for word in word_dict:
        dictionary[word] = True
    queue = deque([0])
    visited = [False] * len(string)
    while len(queue) > 0:
        start = queue.popleft()
        for end in range(start, len(string)):
            if not visited[end]:
                if string[start: end + 1] in dictionary:
                    queue.append(end)
                    if end == len(string) - 1:
                        return True
        visited[start] = True
    return False
