from collections import deque

def findCircleNum(matrix):
    students = len(matrix)
    if matrix is None:
        return 0
    visited = set()
    count = 0
    for student in xrange(students):
        if student not in visited:
            # breadthFirstTraverse(student, matrix, visited)
            depthFirstTraverse(student, matrix, visited)
            count += 1
    return count

def depthFirstTraverse(node, matrix, visited):
    visited.add(node)
    for candidate, isFriend in enumerate(matrix[node]):
        if candidate is not node and isFriend and candidate not in visited:
            depthFirstTraverse(candidate, matrix, visited)

def breadthFirstTraverse(node, matrix, visited):
    queue = deque([node])
    while len(queue) > 0:
        curr = queue.popleft()
        for candidate in xrange(len(matrix[curr])):
            if candidate == curr:
                continue
            if matrix[curr][candidate] == 1 and candidate not in visited:
                queue.append(candidate)
        visited.add(curr)

import pytest

def test_1():
    assert findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2

def test_2():
    assert findCircleNum([[1,1,0],[1,1,1],[0,1,1]]) == 1
