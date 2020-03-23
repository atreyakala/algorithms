import heapq
from collections import Counter

def topKFrequent(nums, k):
    numFreq = Counter(nums)
    maxFreqHeap = []
    for num, freq in numFreq.items():
        if len(maxFreqHeap) == k:
            heapq.heappushpop(maxFreqHeap, (freq, num))
        else:
            heapq.heappush(maxFreqHeap, (freq, num))
    return [heapq.heappop(maxFreqHeap)[1] for _ in range(k)][::-1]