from collections import defaultdict
from collections import deque

def alienOrder(words):
    if len(words) == 1:
        return words[0]
    charSet, numOfPrereqs, dependents = setupGraph(words)
    canTake = deque(charSet - set(numOfPrereqs.keys()))
    alphabet = []
    while canTake:
        curr = canTake.popleft()
        alphabet.append(curr)
        for dep in dependents[curr]:
            numOfPrereqs[dep] -= 1
            if numOfPrereqs[dep] == 0:
                canTake.append(dep)
    return "".join(alphabet) if len(alphabet) == len(charSet) else ""

def setupGraph(words):
    charSet = set()
    numOfPrereqs = defaultdict(lambda: 0)
    dependents = defaultdict(lambda: [])
    for i in range(len(words) - 1):
        currWord = words[i]
        for char in currWord:
            charSet.add(char)
        nextWord = words[i + 1]
        for char in nextWord:
            charSet.add(char)
        for j in range(min(len(currWord), len(nextWord))):
            currWordChar = currWord[j]
            nextWordChar = nextWord[j]
            if currWordChar == nextWordChar:
                continue
            else:
                numOfPrereqs[nextWordChar] += 1
                dependents[currWordChar].append(nextWordChar)
                break
    return charSet, numOfPrereqs, dependents
