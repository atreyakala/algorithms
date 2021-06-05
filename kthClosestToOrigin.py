import heapq
from typing import List


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    for point in points:
        x, y = point
        dist = x * x + y * y
        if len(heap) == k:
            heapq.heappushpop(heap, (-dist, x, y))
        else:
            heapq.heappush(heap, (-dist, x, y))
    return [(x, y) for (_, x, y) in heap]


# O(N * logK) | O(k)
