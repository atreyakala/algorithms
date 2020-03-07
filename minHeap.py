class MinHeap:
    def __init__(self, array):
        self.heap = array
        self.buildHeap()

    def peek(self):
        return self.heap[0]

    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def remove(self):
        self.swap(0, len(self.heap) - 1)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1)
        return valueToRemove

    def siftDown(self, currentIdx, endIdx):
        leftChildIdx = 2 * currentIdx + 1
        while leftChildIdx <= endIdx:
            rightChildIdx = leftChildIdx + 1 if leftChildIdx + 1 <= endIdx else -1
            if rightChildIdx != -1 and self.heap[rightChildIdx] < self.heap[leftChildIdx]:
                idxToSwap = rightChildIdx
            else:
                idxToSwap = leftChildIdx
            if self.heap[idxToSwap] < self.heap[currentIdx]:
                self.swap(idxToSwap, currentIdx)
                currentIdx = idxToSwap
                leftChildIdx = 2 * currentIdx + 1
            else:
                return

    def siftUp(self, currentIdx):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and self.heap[currentIdx] < self.heap[parentIdx]:
            self.swap(currentIdx, parentIdx)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def insert(self, num):
		self.heap.append(num)
		self.siftUp(len(self.heap) - 1)

	def buildHeap(self):
        firstParentIdx = (len(self.heap) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(self.heap) - 1)
