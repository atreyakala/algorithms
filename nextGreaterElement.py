from collections import deque
from collections import defaultdict

def nextGreaterElement(nums1, nums2):
    stack = deque([])
    nextGreater = defaultdict(lambda: -1)
    for num in nums2:
        while len(stack) > 0 and stack[-1] < num:
            nextGreater[stack.pop()] = num
        stack.append(num)
    return [nextGreater[num] for num in nums1]
