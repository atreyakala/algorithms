def mergeIntervals(intervals):
    intervals.sort(key = lambda x: x[0])
    merged = []
    for interval in intervals:
        if merged and merged[-1][-1] >= interval[0]
            merged[-1][-1] = max(merged[-1][-1], interval[1])
        else:
            merged.append(interval)
    return merged
