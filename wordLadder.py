from collections import deque
from collections import defaultdict

def ladderLength(beginWord, endWord, wordList):
    patternDictionary = populatePatternDictionary(wordList)
    return explore(beginWord, endWord, patternDictionary)

def explore(begin, end, patternDictionary):
    queue = deque([(begin, 1)])
    visited = set([begin])
    while len(queue) > 0:
        word, depth = queue.popleft()
        for i in range(len(word)):
            pattern = word[:i] + "_" + word[i + 1:]
            patternWords = patternDictionary[pattern]
            for patternWord in patternWords:
                if patternWord not in visited:
                    if patternWord == end:
                        return depth + 1
                    visited.add(patternWord)
                    queue.append((patternWord, depth + 1))
    return 0

def populatePatternDictionary(wordList):
    patternDictionary = defaultdict(lambda: [])
    for word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + "_" + word[i + 1:]
            patternDictionary[pattern].append(word)
    return patternDictionary
