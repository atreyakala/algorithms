"""
253. Meeting Rooms II https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1

Constraints:
1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""

import heapq
from typing import List


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[0])
    end_times_heap = []

    for start, end in intervals:
        if end_times_heap and start >= end_times_heap[0]:
            heapq.heapreplace(end_times_heap, end)
        else:
            heapq.heappush(end_times_heap, end)

    return len(end_times_heap)
