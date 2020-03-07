def subsets(nums):
    powerset = [[]]
    for num in nums:
        powerset += [subset + [num] for subset in powerset]
    return powerset

def powerset(array):
    subsets = [[]]
    for ele in array:
        for i in xrange(len(subsets)):
            currentSubset = subset[i]
            subsets.append(currentSubset)
    return subsets
