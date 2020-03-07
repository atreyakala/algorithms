import heapq

def findKthLargest(nums, k):
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(-num)
        else:
            last = -heap[-1]
            if num > top:
                heapq.heapreplace(-num)
