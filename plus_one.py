from typing import List


def plus_one(digits: List[int]) -> List[int]:
    for i in reversed(range(0, len(digits))):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits

    return [1] + digits


def test_0():
    assert plus_one([1]) == [2]


def test_1():
    assert plus_one([1, 2, 9]) == [1, 3, 0]


def test_2():
    assert plus_one([9, 9]) == [1, 0, 0]


# O(N) | O(1)
