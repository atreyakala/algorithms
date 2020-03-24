def pickRandom(nums, target):
    targetCount = nums.count(target)
    randomCount = random.randint(1, targetCount)
    count = 0
    for i, num in enumerate(nums):
        if num == target:
            count += 1
            if count == randomCount:
                return i
