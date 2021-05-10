# 56. Merge Intervals https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key = lambda x: (x[0], x[1]))
    merged_so_far = []

    for interval in intervals:
        if merged_so_far and merged_so_far[-1][-1] >= interval[0]:
            merged_so_far[-1][-1] = max(merged_so_far[-1][-1], interval[-1])
        else:
            merged_so_far.append(interval)

    return merged_so_far


def test_0():
    assert merge_intervals([[3, 4], [1, 2]]) == [[1, 2], [3, 4]]


def test_1():
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
