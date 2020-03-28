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

def topKFrequent(nums, k):
    buckets = [[] for _ in range(len(nums) + 1)]
    result = []
    for num, freq in Counter(nums).items():
        buckets[freq].append(num)
    for li in reversed(buckets):
        if len(li) > 0:
            result += li
        if len(result) >= k:
            return result[:k]
