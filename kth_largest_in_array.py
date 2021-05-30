import heapq
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heapreplace(heap, num)

    return heap[0]


def test_0():
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
