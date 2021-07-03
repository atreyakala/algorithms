"""
1428. Leftmost Column with at Least a One https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in non-decreasing order.
Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it. If such an index does not exist, return -1.
You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:
    BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
    BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements [rows, cols], which means the matrix is rows x cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.
For custom testing purposes, the input will be the entire binary matrix mat. You will not have access to the binary matrix directly.

Input: mat = [[0,0],[1,1]]
Output: 0

Input: mat = [[0,0],[0,1]]
Output: 1

Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1

Constraints
    rows == mat.length
    cols == mat[i].length
    1 <= rows, cols <= 100
    mat[i][j] is either 0 or 1.
    mat[i] is sorted in non-decreasing order.
"""


class BinaryMatrix:
    pass


def left_most_column_with_one(binary_matrix: 'BinaryMatrix') -> int:
    rows, cols = binary_matrix.dimensions()
    smallest_index = cols

    for row in range(rows):
        lo = 0
        hi = cols - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if binary_matrix.get(row, mid) == 1:
                hi = mid
            else:
                lo = mid + 1
        if binary_matrix.get(row, lo) == 1:
            smallest_index = min(lo, smallest_index)

    return smallest_index if smallest_index != cols else -1

# O(nlogm) | O(1)


def left_most_column_with_one(binary_matrix: 'BinaryMatrix') -> int:
    rows, cols = binary_matrix.dimensions()
    smallest_index = cols

    row = 0
    col = cols - 1
    while row < rows and col >= 0:
        if binary_matrix.get(row, col) == 0:
            row += 1
        else:
            smallest_index = min(smallest_index, col)
            col -= 1

    return smallest_index if smallest_index != cols else -1

# O(n + m) | O(1)


def left_most_column_with_one(binary_matrix: 'BinaryMatrix') -> int:
    rows, cols = binary_matrix.dimensions()
    left_most_column = cols

    for row in range(rows):
        lo = 0
        hi = cols - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if binary_matrix.get(row, mid) == 1:
                hi = mid
            else:
                lo = mid + 1

        if binary_matrix.get(row, lo) == 1:
            left_most_column = min(lo, left_most_column)

    return left_most_column if left_most_column != cols else -1

#  O(nlogm) | O(1)
