def numWays(n):
    w1 = 1
    w2 = 1
    for _ in xrange(n - 1):
        curr = w1 + w2
        w2 = w1
        w1 = curr
    return w1

import pytest

def test_1():
    assert numWays(2) == 2
