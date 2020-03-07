# iterative
# O(n) time | O(1) space
def reverseLinkedList(head):
    prevNode = None
    currentNode = head
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = nextNode
    return prevNode

# recursive
# O(n) time | O(n) space
def reverseLinkedList(head):
    if head is None or head.next is None:
        return head
    remainingReversed = reverseLinkedList(head.next)
    head.next.next = head
    head.next = None
    return remainingReversed
