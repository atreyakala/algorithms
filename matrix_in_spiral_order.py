"""
54. Spiral Matrix https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List

SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))
SEEN = 101


def matrix_in_spiral_order(matrix: List[List[int]]) -> List[int]:
    rows = len(matrix)
    cols = len(matrix[0])
    direction = row = col = 0
    spiral_ordering = []

    for _ in range(rows * cols):
        spiral_ordering.append(matrix[row][col])
        matrix[row][col] = SEEN
        next_row = row + SHIFT[direction][0]
        next_col = col + SHIFT[direction][1]

        if (next_row not in range(rows)
                or next_col not in range(cols)
                or matrix[next_row][next_col] is SEEN):
            direction = (direction + 1) % 4
            next_row = row + SHIFT[direction][0]
            next_col = col + SHIFT[direction][1]

        row = next_row
        col = next_col

    return spiral_ordering


def test_0():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert matrix_in_spiral_order(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test_1():
    matrix = [
        [1, 2],
        [3, 4],
    ]
    assert matrix_in_spiral_order(matrix) == [1, 2, 4, 3]
