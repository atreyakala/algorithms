def nextPermutation(nums):
    for i in reversed(range(1, len(nums))):
        if nums[i] > nums[i - 1]:
            indexToSwap = findNextGreater(nums, nums[i - 1])
            nums[i - 1], nums[indexToSwap] = nums[indexToSwap], nums[i - 1]
            reverseFrom(nums, i)
            return
    reverseFrom(nums, 0)

def findNextGreater(nums, num):
    for i in reversed(range(len(nums))):
        if nums[i] > num:
            return i

def reverseFrom(nums, i):
    start = i
    end = len(nums) - 1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
