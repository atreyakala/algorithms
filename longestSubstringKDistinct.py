from collections import defaultdict

def lengthOfLongestSubstringWithKDistinct(string, k):
    lastSeen = defaultdict(lambda: -1)
    leftIndex = 0
    maxLength = 0
    for rightIndex, char in enumerate(string):
        lastSeen[char] = rightIndex
        if len(lastSeen) > k:
            indexToBeRemoved = min(lastSeen.values())
            charToBeRemoved = string[indexToBeRemoved]
            del lastSeen[charToBeRemoved]
            leftIndex = indexToBeRemoved + 1
        maxLength = max(maxLength, rightIndex - leftIndex + 1)
    return maxLength
