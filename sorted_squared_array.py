# https://www.algoexpert.io/questions/Sorted%20Squared%20Array

from typing import List


def sorted_squared_array(arr: List[int]) -> List[int]:
    size = len(arr)
    squared_arr = [0 for _ in range(size)]

    left_idx = 0
    right_idx = size - 1

    for idx in reversed(range(size)):
        left_val = arr[left_idx]
        right_val = arr[right_idx]

        if abs(left_val) >= abs(right_val):
            squared_arr[idx] = left_val * left_val
            left_idx += 1
        else:
            squared_arr[idx] = right_val * right_val
            right_idx -= 1

    return squared_arr


def test_0():
    assert sorted_squared_array([-4, -2, 1, 3]) == [1, 4, 9, 16]


def test_1():
    assert sorted_squared_array([-1, 1]) == [1, 1]


def test_2():
    assert sorted_squared_array([1, 1]) == [1, 1]


