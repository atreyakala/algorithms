class Node:
    def __init__(self, x, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def copyRandomList(self, head):
        map = {None: None}
        node = head
        while node is not None:
            copyNode = Node(node.val)
            map[node] = copyNode
            node = node.next
        node = head
        while node is not None:
            copyNode = map[node]
            copyNode.next = map[node.next]
            copyNode.random = map[node.random]
            node = node.next
        return map[head]
