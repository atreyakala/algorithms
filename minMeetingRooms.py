import heapq

def minMeetingRooms(intervals):
    intervals.sort(key = lambda x: x[0])
    endTimesHeap = []
    maxOverlappingMeetings = 0
    for start, end in intervals:
        while endTimesHeap and endTimesHeap[0] <= start:
            heapq.pop(endTimesHeap)
        heapq.heappush(endTimesHeap, end)
        maxOverlappingMeetings = max(maxOverlappingMeetings, len(endTimesHeap))
    return maxOverlappingMeetings
