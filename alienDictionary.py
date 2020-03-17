from collections import defaultdict

def alienOrder(words):
    charSet, numOfPrereqs, dependents = setupGraph(words)
    canTake = charSet - set(numOfPrereqs.keys())
    alphabet = []
    while canTake:
        curr = canTake.pop()
        alphabet.append(curr)
        for dep in dependents[curr]:
            numOfPrereqs[dep] -= 1
            if numOfPrereqs[dep] == 0:
                canTake.add(dep)
    return "".join(alphabet) if len(alphabet) == len(charSet) else ""

def setupGraph(words):
    charSet = set()
    numOfPrereqs = defaultdict(lambda: 0)
    dependents = defaultdict(lambda: [])
    for i in range(len(words) - 1):
        currWord = words[i]
        nextWord = words[i + 1]
        for j in range(min(len(currWord), len(nextWord))):
            currWordChar = currWord[j]
            nextWordChar = nextWord[j]
            charSet.add(currWordChar)
            charSet.add(nextWordChar)
            if currWordChar == nextWordChar:
                continue
            else:
                numOfPrereqs[nextWordChar] += 1
                dependents[currWordChar].append(nextWordChar)
                break
    return charSet, numOfPrereqs, dependents

import pytest

def test_1():
    assert alienOrder(["wrt","wrf","er","ett","rftt"]) == "wertf"

def test_2():
    assert alienOrder(["z", "x"]) == "zx"

def test_3():
    assert alienOrder(["z", "x", "z"]) == ""
