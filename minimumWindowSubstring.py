from collections import defaultdict
from collections import Counter

def minWindow(string, chars):
    targetCharCount = Counter(chars)
    subStringBounds = findSubStringBounds(string, targetCharCount)
    return getStringFromBounds(string, subStringBounds)

def findSubStringBounds(string, targetCharCount):
    subStringBounds = [0, float("inf")]
    subStringCharCount = defaultdict(lambda: 0)
    numOfUniqueChars = len(targetCharCount.keys())
    numOfUniqueCharsDone = 0
    leftIdx = 0
    rightIdx = 0
    while rightIdx < len(string):
        rightChar = string[rightIdx]
        if rightChar not in targetCharCount:
            rightIdx += 1
            continue
        subStringCharCount[rightChar] += 1
        if subStringCharCount[rightChar] == targetCharCount[rightChar]:
            numOfUniqueCharsDone += 1
        while numOfUniqueCharsDone == numOfUniqueChars and leftIdx <= rightIdx:
            subStringBounds = getCloserBounds(leftIdx, rightIdx, subStringBounds[0], subStringBounds[1])
            leftChar = string[leftIdx]
            if leftChar not in targetCharCount:
                leftIdx += 1
                continue
            if subStringCharCount[leftChar] == targetCharCount[leftChar]:
                numOfUniqueCharsDone -= 1
            subStringCharCount[leftChar] -= 1
            leftIdx += 1
        rightIdx += 1
    return subStringBounds

def getCloserBounds(self, currLeft, currRight, prevLeft, prevRight):
    return [currLeft, currRight] if currRight - currLeft < prevRight - prevLeft else [prevLeft, prevRight]

def getStringFromBounds(string, bounds):
    start, end = bounds
    return string[start: end + 1] if end != float("inf") else ""
