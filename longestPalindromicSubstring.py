# O(n^2) time | O(1) space
def longestPalindromicSubstring(string):
    longest = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPalidromeFrom(string, i - 1, i + 1)
        even = getLongestPalidromeFrom(string, i - 1, i)
        currentLongest = max(odd, even, key = lambda x: x[1] - x[0])
        longest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
    return string[longest[0] : longest[1]]

def getLongestPalidromeFrom(string, left, right):
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1
    return [left + 1, right]
