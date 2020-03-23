def copyRandomList(head):
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

def copyRandomList(head):
    if head is None:
        return None
    node = head
    while node is not None:
        next = node.next
        copy = Node(node.val)
        node.next = copy
        copy.next = next
        node = next
    node = head
    while node is not None:
        copy = node.next
        if node.random:
            copy.random = node.random.next
        node = copy.next
    copyHead = None
    node = head
    while node is not None:
        copy = node.next
        if copyHead is None:
            copyHead = copy
        next = copy.next
        node.next = copy.next
        if copy.next is not None:
            copy.next = copy.next.next
        node = next
    return copyHead
