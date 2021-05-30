# https://www.algoexpert.io/questions/Monotonic%20Array

from typing import List


def is_monotonic(arr: List[int]) -> bool:
    if arr is None:
        return False

    if len(arr) < 2:
        return True

    is_increasing = None
    for i in range(len(arr) - 1):
        if arr[i + 1] > arr[i]:
            if is_increasing is None:
                is_increasing = True
            elif not is_increasing:
                return False
        elif arr[i + 1] < arr[i]:
            if is_increasing is None:
                is_increasing = False
            elif is_increasing:
                return False

    return True


def test_0():
    assert is_monotonic([1, 1, 1])


def test_1():
    assert is_monotonic([-1, -1, -3, -5, -5, -10])


def test_2():
    assert not is_monotonic([1, 2, 1])