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
