from collections import Counter
from collections import deque

def reorganizeString(string):
    freq = Counter(string)
    mostFreq, maxFreq = freq.most_common(1)[0]
    if maxFreq > (len(string) + 1) // 2:
        return ""
    fillers = getFillers(freq, mostFreq)
    reorganised = [None] * len(string)
    for i in range(0, len(string), 2):
        if maxFreq > 0:
            reorganised[i] = mostFreq
            maxFreq -= 1
        else:
            reorganised[i] = fillers.popleft()
    for i in range(1, len(string), 2):
        reorganised[i] = fillers.popleft()
    return "".join(reorganised)

def getFillers(freq, mostFreq):
    fillers = deque([])
    for char, count in freq.items():
        if char == mostFreq:
            continue
        for _ in range(count):
            fillers.append(char)
    return fillers
