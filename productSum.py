# O(n) | O(n) where n is number of elements including subarrays
def productSum(array, multiplier = 1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier
