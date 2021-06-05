from typing import List


def product_except_self(nums: List[int]) -> int:
    ans = [1] * len(nums)
    for i in range(1, len(nums)):
        ans[i] = nums[i - 1] * ans[i - 1]
    right_running_product = 1
    for i in reversed(range(len(nums))):
        ans[i] *= right_running_product
        right_running_product *= nums[i]
    return ans
