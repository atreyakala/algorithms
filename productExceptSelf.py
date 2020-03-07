def productExceptSelf(nums):
    ans = [1] * len(nums)
    for i in xrange(1, len(nums)):
        ans[i] = ans[i - 1] * nums[i - 1]
    right = 1
    for i in xrange(size - 1, -1, -1):
        ans[i] *= right
        right *= nums[i]
    return ans
