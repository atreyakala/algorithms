def productExceptSelf(nums):
    ans = [1] * len(nums)
    for i in range(1, len(nums)):
        ans[i] = ans[i - 1] * nums[i - 1]
    right = 1
    for i in reversed(range(len(nums))):
        ans[i] *= right
        right *= nums[i]
    return ans
