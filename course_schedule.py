"""
207. Course Schedule https://leetcode.com/problems/course-schedule/
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints
    1 <= numCourses <= 105
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.
"""


from collections import defaultdict
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    num_prerequisites = defaultdict(int)
    dependents = defaultdict(list)

    for dependent, prerequisite in prerequisites:
        num_prerequisites[dependent] += 1
        dependents[prerequisite].append(dependent)

    can_take = set(range(num_courses)) - set(num_prerequisites.keys())

    while len(can_take) > 0:
        course = can_take.pop()
        num_courses -= 1
        for dependent in dependents[course]:
            num_prerequisites[dependent] -= 1
            if num_prerequisites[dependent] == 0:
                can_take.add(dependent)

    return num_courses == 0

# O(v + e) | O(v + e)


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    num_prerequisites = defaultdict(int)
    dependents = defaultdict(list)

    for dependent, prerequisite in prerequisites:
        num_prerequisites[dependent] += 1
        dependents[prerequisite].append(dependent)

    can_take = set(range(num_courses)) - set(num_prerequisites.keys())
    visited = []

    while len(can_take) > 0:
        course = can_take.pop()
        visited.append(course)
        for dependent in dependents[course]:
            num_prerequisites[dependent] -= 1
            if num_prerequisites[dependent] == 0:
                can_take.add(dependent)

    return visited if len(visited) == num_courses else []


def test_0():
    assert can_finish(2, [[1, 0]])


def test_0():
    assert not can_finish(2, [[0, 1], [1, 0]])
