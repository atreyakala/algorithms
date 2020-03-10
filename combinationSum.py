def combinationSum(candidates, target):
    if candidates is None or len(candidates) == 0:
        return []
    combinations = []
    candidates.sort()
    buildTargetSubsets(candidates, target, 0, [], combinations)
    return combinations

def buildTargetSubsets(nums, target, index, subset, combinations):
    if target == 0:
        combinations.append(subset)
        return
    for i, num in enumerate(nums):
        if num > target:
            break
        buildTargetSubsets(nums, target - num, i, subset + [num], combinations)
