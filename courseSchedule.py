from collections import defaultdict

def canTake(numCourses, prerequisites):
    numOfPrereqs = defaultdict(int)
    dependents = defaultdict(list)
    for prereq, dep in prerequisites:
        numOfPrereqs[dep] += 1
        dependents[prereq].append(dep)
    canTake = set([i for i in xrange(numCourses)]) - set(numOfPrereqs.keys())
    while len(canTake) > 0:
        curr = canTake.pop()
        numCourses -= 1
        for dep in dependents[curr]:
            numOfPrereqs[dep] -= 1
            if numOfPrereqs[dep] == 0:
                canTake.add(dep)
    return numCourses == 0

def findOrder(numCourses, prerequisites):
    numOfPrereqs = defaultdict(int)
    dependents = defaultdict(list)
    for prereq, dep in prerequisites:
        numOfPrereqs[dep] += 1
        dependents[prereq].append(dep)
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
