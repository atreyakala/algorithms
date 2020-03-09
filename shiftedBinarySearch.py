# O(log(n)) time |  O(1) space
def shiftedBinarySearch(array, target):
    leftIdx = 0
    rightIdx = len(array) - 1
    while leftIdx <= rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        potentialMatch = array[midIdx]
        if potentialMatch == target:
            return midIdx
        leftNum = array[leftIdx]
        rightNum = array[rightIdx]
        if leftNum <= potentialMatch:
            if leftNum <= target <= potentialMatch:
                rightIdx = midIdx - 1
            else:
                leftIdx = midIdx + 1
        else:
            if potentialMatch <= target <= rightNum:
                leftIdx = midIdx + 1
            else:
                rightIdx = midIdx - 1
    return -1
