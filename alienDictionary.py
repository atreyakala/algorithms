from collections import defaultdict

def alienOrder(words):
    charSet, prereqs = buildPrereqs(words)
    numOfPrereqs, dependents = buildDependents(prereqs)
    alphabet = []
    canTake = charSet - set(numOfPrereqs.keys())
    print("canTake: {}, dependents: {}, numOfPrereqs: {}".format(canTake, dependents, numOfPrereqs))
    while canTake:
        curr = canTake.pop()
        alphabet.append(curr)
        for dep in dependents[curr]:
            numOfPrereqs[dep] -= 1
            if numOfPrereqs[dep] == 0:
                canTake.add(dep)
    return "".join(alphabet) if len(alphabet) == len(charSet) else ""

def buildPrereqs(words):
    charSet = set()
    prereqs = []
    for word in words:
        seen = []
        for letter in word:
            charSet.add(letter)
            if len(seen) > 0:
                prereqs += ([s, letter] for s in seen if s is not letter and [s, letter] not in prereqs)
            seen.append(letter)
    return charSet, prereqs

def buildDependents(prereqs):
    numOfPrereqs = defaultdict(int)
    dependents = defaultdict(set)
    for prereq, dep in prereqs:
        numOfPrereqs[dep] += 1
        dependents[prereq].add(dep)
    return numOfPrereqs, dependents

import pytest

# def test_1():
#     assert alienOrder(["wrt","wrf","er","ett","rftt"]) == "ewrft"
#
# def test_2():
#     assert alienOrder(["z", "x"]) == "zx"

def test_2():
    assert alienOrder(["z", "x", "z"]) == ""
