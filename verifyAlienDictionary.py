# O(N * M) or O(C) Time | O(1) Space
def isAlienSorted(words, order):
    charOrder = {char: i for i, char in enumerate(order)}
    for i in xrange(len(words) - 1):
        first = words[i]
        second = words[i + 1]
        if not isPairSorted(first, second, charOrder):
            return False
    return True

def isPairSorted(first, second, order):
    for i in xrange(min(len(first), len(second))):
        charFromFirst = first[i]
        charFromSecond = second[i]
        if charFromFirst == charFromSecond:
            continue
        else:
            return order[charFromFirst] < order[charFromSecond]
    return len(first) < len(second)

import pytest

def test_1():
    assert not isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")

def test_2():
    assert isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
