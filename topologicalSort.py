from collections import defaultdict

def topologicalSort(numCourses, deps):
    numOfPrereqs = defaultdict(int)
    dependents = defaultdict(list)
    for preReq, dep in deps:
        numOfPrereqs[dep] += 1
        dependents[preReq].append(dep)
    canTake = set([i for i in xrange(numCourses)]) - set(numOfPrereqs.keys())
    visited = []
    while len(canTake) > 0:
        curr = canTake.pop()
        visited.append(curr)
        for dep in dependents[curr]:
            numOfPrereqs[dep] -= 1
            if numOfPrereqs[dep] == 0:
                canTake.add(dep)
    return visited if (len(visited) == numCourses) else []

import pytest

def test_1():
    assert topologicalSort(3, [[0, 1], [0, 2], [2, 1]]) == [0, 2, 1]
