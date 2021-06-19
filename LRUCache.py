class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.currentSize = 0
        self.cache = {}
        self.listOfMostRecent = DoublyLinkedList()

    def getMostRecentKey(self):
        return self.listOfMostRecent.head.key

    def insertKeyValuePair(self, key, value):
        if key not in self.cache:
            if self.currentSize == self.maxSize:
                self.evictLeastRecent()
            else:
                self.currentSize += 1
            self.cache[key] = DoublyLinkedListNode(key, value)
        else:
            self.replaceKey(key, value)
        self.updateMostRecent(self.cache[key])

    def getValueFromKey(self, key):
        if key not in self.cache:
            return None
        self.updateMostRecent(self.cache[key])
        return self.cache[key].val

    def replaceKey(self, key, value):
        if key not in self.cache:
            raise Exception("Key not in cache!")
        self.cache[key].val = value

    def evictLeastRecent(self):
        keyToRemove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.removeTail()
        del self.cache[keyToRemove]

    def updateMostRecent(self, node):
        self.listOfMostRecent.setHeadTo(node)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def removeTail(self):
        if self.tail is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def setHeadTo(self, node):
        if node == self.head:
            return
        if self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if node == self.tail:
                self.removeTail()
            node.removeBindings()
            self.head.prev = node
            node.next = self.head
            self.head = node

class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

	def removeBindings(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None
        return
