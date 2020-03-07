def removeDuplicates(nums):
    if nums is None or len(nums) == 0:
        return 0
    writeIdx = 0
    for i in range(len(nums)):
        if nums[i] != nums[writeIdx]:
            writeIdx += 1
            nums[writeIdx], nums[i] = nums[i], nums[writeIdx]
    return writeIdx + 1

import pytest

def test_1():
    assert removeDuplicates([0, 0, 0, 1, 1, 2, 2, 2, 3]) == 4
