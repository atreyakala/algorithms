# O(logn) time | O(1) space
def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
		potentialMatch = array[mid]
        if potentialMatch == target:
            return mid
        elif potentialMatch < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
