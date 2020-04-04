def kClosest(points, k):
    heap = []
    for point in points:
        x, y = point
        dist = x*x + y*y
        if len(heap) < k:
            heapq.heappush(heap, (-dist, point))
        else:
            if dist < -heap[0][0]:
                heapq.heappushpop(heap, (-dist, point))
    return [elem[1] for elem in heap]
