# https://www.algoexpert.io/questions/First%20Duplicate%20Value

from typing import List


def first_duplicate_value(arr: List[int]) -> int:
    for val in arr:
        abs_val = abs(val)
        write_index = abs_val - 1
        if arr[write_index] < 0:
            return abs_val
        arr[write_index] *= -1
    return -1


def test_0():
    assert first_duplicate_value([2, 1, 5, 2, 3, 3]) == 2


def test_1():
    assert first_duplicate_value([2, 1, 5, 3]) == -1


def test_1():
    assert first_duplicate_value([2, 1, 5, 3, 3, 2, 4]) == 3
