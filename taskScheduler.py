def leastInterval(tasks, n):
    charCount = [0] * 26
    for task in tasks:
        charCount[ord(task) - ord('A')] += 1
    maxCount = max(charCount)
    maxCountFreq = charCount.count(maxCount)
    partitions = maxCount - 1
    partitionLength = n - (maxCountFreq - 1)
    emptySlots = partitions * partitionLength
    availableTasks = len(tasks) - (maxCount * maxCountFreq)
    idleSlots = max(0, emptySlots - availableTasks)
    return idleSlots + len(tasks)

import pytest

def test_0():
    assert leastInterval(["A", "B"], 2) == 2

def test_1():
    assert leastInterval(["A", "A", "B", "B"], 2) == 5

def test_2():
    assert leastInterval(["A", "A", "A"], 2) == 7
