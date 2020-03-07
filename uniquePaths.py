def uniquePaths(cols, rows):
    prev = [1] * (cols)
    for row in xrange(1, rows):
        for col in xrange(1, cols):
            prev[col] += prev[col - 1]
    return prev[-1]

def uniquePaths(cols, rows):
    dp = [[1] * (cols) for _ in xrange(rows)]
    for row in xrange(1, rows):
        for col in xrange(1, cols):
            dp[row][col] = dp[row][col - 1] + dp[row - 1][col]
    return dp[-1][-1]

import pytest

def test_1():
    assert uniquePaths(3, 2) == 3
