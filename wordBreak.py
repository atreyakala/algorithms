def wordBreak(string, wordDict):
    dp = [False] * (len(string) + 1)
    dp[0] = True
    dictionary = {}
    for word in wordDict:
        dictionary[word] = True
    for i in range(len(string)):
        for j in range(i, len(string)):
            if dp[i] and string[i : j + 1] in dictionary:
                dp[j + 1] = True
    return dp[-1]

from collections import deque

# "aaaaa", ["aa", "aaa"]
def wordBreak(string, wordDict):
    dictionary = {}
    for word in wordDict:
        dictionary[word] = True
    queue = deque([0])
    visited = [False] * len(string)
    while len(queue) > 0:
        start = queue.popleft()
        for end in range(start, len(string)):
            if end not in visited:
                if string[start : end + 1] in dictionary:
                    queue.append(end)
                    if end == len(string) - 1:
                        return True
        visited[start] = True
    return False
