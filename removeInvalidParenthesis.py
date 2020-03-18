from collections import deque

def removeInvalidParenthesis(string):
    validRemovals = []
    if string is None:
        return validRemovals
    visited = set([string])
    queue = deque([string])
    found = False
    while len(queue) > 0:
        currentString = queue.popleft()
        if isValid(currentString):
            validRemovals.append(currentString)
            found = True
        if found:
            continue
        for i, char in enumerate(currentString):
            if char not in "()":
                continue
            nextString = currentString[:i] + currentString[i + 1:]
            if nextString not in visited:
                queue.append(nextString)
                visited.add(nextString)
    return validRemovals

def isValid(string):
    count = 0
    for char in string:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
            if count < 0:
                return False
    return count == 0
