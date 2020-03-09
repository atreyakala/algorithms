def moveZeroes(nums):
    if nums is None:
        return None
    writeIdx = None
    for currIdx, num in enumerate(nums):
        if num == 0:
            if writeIdx is None:
                writeIdx = currIdx
            continue
        if writeIdx is not None:
            nums[writeIdx], nums[currIdx] = nums[currIdx], 0
            writeIdx += 1
    return nums

import pytest

def test_1():
    assert moveZeroes([0, 1, 2, 0, 0, 3]) == [1, 2, 3, 0, 0, 0]

def test_2():
    assert moveZeroes([1]) == [1]
