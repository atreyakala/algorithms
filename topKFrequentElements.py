# O(n * logn) time | O(n) space
def topKFrequentElements(words, k):
    count = collections.Counter(words)
    uniqWords = count.keys()
    uniqWords.sort(key = lambda w: (-count[w], w))
    return uniqWords[:k]

# O(n + k * logn) time | O(n) space
def topKFrequentElements(words, k):
    count = collections.Counter(words)
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in xrange(k)]
