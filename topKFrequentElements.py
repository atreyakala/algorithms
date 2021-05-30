from collections import Counter
from typing import List


# O(n * logn) time | O(n) space
def top_k_frequent_elements(words: List[str], k: int) -> List[str]:
    count = Counter(words)
    uniq_words = list(count.keys())
    uniq_words.sort(key=lambda w: (-count[w], w))
    return uniq_words[:k]


# O(n + k * logn) time | O(n) space
def top_k_frequent_elements(words: List[str], k: int) -> List[str]:
    count = Counter(words)
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in xrange(k)]
