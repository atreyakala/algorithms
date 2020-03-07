# O(n) | O(1)
def hasSingleCycle(array):
    numElementsVisited = 0
    currentIndex = 0
    while numElementsVisited < len(array):
        if numElementsVisited > 0 and currentIndex == 0:
            return False
        numElementsVisited += 1
        currentIndex = getNextIndex(currentIndex, array)
    return currentIndex == 0

def getNextIndex(currentIndex, array):
    jumps = array[currentIndex]
    nextIndex = (currentIndex + jumps) % len(array)
    return nextIndex if nextIndex >= 0 else nextIndex + len(array)
