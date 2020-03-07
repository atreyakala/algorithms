def canAttendMeetings(intervals):
    if len(intervals) == 1:
        return True
    sortedIntervals = sorted(intervals, key = lambda x: x[0])
    prevEnd = intervals[0][1]
    for start, end in sortedIntervals:
        if prevEnd > start:
            return False
        else:
            prevEnd = end
    return True
