def rotLeft(arr, d):
    d = d % len(arr)
    return arr[d:] + arr[:d]
