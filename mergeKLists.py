import heapq

def mergeKLists(lists):
    heap = [(node.val, node) for node in lists if node is not None]
    heapq.heapify(heap)
    mergedListHead = None
    lastMergedNode = None
    while len(heap) > 0:
        _, top = heapq.heappop(heap)
        if top.next is not None:
            heapq.heappush(heap, (top.next.val, top.next))
        if mergedListHead is None:
            mergedListHead = top
            lastMergedNode = top
        else:
            lastMergedNode.next = top
            lastMergedNode = top
    return mergedListHead
