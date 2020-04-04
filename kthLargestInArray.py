import heapq

def findKthLargest(self, nums, k):
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
    return heap[0]
