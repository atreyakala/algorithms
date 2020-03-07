def reorganizeString(string):
    charCount = getCharCount(string)
    mostFreqChar = max(charCount.keys(), key = lambda char: charCount[char])
    maxFreq = charCount[mostFreqChar]
    if maxFreq > (len(string) + 1) // 2:
        return ""
    leftOverChars = getLeftOverChars(charCount, mostFreqChar)
    organizedChars = [None] * len(string)
    for i in xrange(0, len(string), 2):
        if maxFreq > 0:
            organizedChars[i] = mostFreqChar
            maxFreq -= 1
        else:
            organizedChars[i] = leftOverChars.pop(0)
    for i in xrange(1, len(string), 2):
        organizedChars[i] = leftOverChars.pop(0)
    return "".join(organizedChars)

def getCharCount(string):
    charCount = {}
    for char in string:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1
    return charCount

def getLeftOverChars(charCount, mostFreqChar):
    leftOverChars = []
    for char, count in charCount.items():
        if char is not mostFreqChar:
            for _ in xrange(count):
                leftOverChars.append(char)
    return leftOverChars
