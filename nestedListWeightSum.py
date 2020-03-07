def depthSum(nestedList, depth = 1):
    sum = 0
    for item in nestedList:
        if type(item) == list:
            sum += depthSum(item, depth + 1)
        else:
            sum += depth * item
    return sum

import pytest

def test_1():
    assert depthSum([1, 2, 3]) == 6

def test_2():
    assert depthSum([1, [4, [6]]]) == 27

def test_3():
    assert depthSum([[[[[1]]]], 2]) == 7

def test_4():
    assert depthSum([[1,1],2,[1,1]]) == 10
