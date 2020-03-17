import heapq

def kSmallestPairs(nums1, nums2, k):
    if len(nums1) == 0 or len(nums2) == 0:
        return []
    heap = []
    pairs = []
    for i in range(min(k, len(nums1))):
        heapq.heappush(heap, [nums1[i] + nums2[0], i, 0])
    while len(pairs) < k and len(heap) > 0:
        _, pos1, pos2 = heapq.heappop(heap)
        pairs.append([pos1, pos2])
        if pos2 + 1 < len(nums2):
            heapq.heappush(heap, [nums1[pos1] + nums2[pos2 + 1], pos1, pos2 + 1])
    return pairs
