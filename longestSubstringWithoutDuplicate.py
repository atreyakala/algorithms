# O(n) time | O(min(n, a)) space
def lengthOfLongestSubstring(string):
    maxLength = float("-inf")
    lastSeen = {}
    startIndex = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            startIndex = max(startIndex, lastSeen[char] + 1)
        maxLength = max(maxLength, i + 1 - startIndex)
        lastSeen[char] = i
    return maxLength if maxLength != float("-inf") else 0
