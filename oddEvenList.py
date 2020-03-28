def oddEvenList(head):
    if head is None:
        return None
    currentOddNode = head
    currentEvenNode = head.next
    evenHead = currentEvenNode
    while currentEvenNode is not None and currentEvenNode.next is not None:
        currentOddNode.next = currentEvenNode.next
        currentOddNode = currentOddNode.next
        currentEvenNode.next = currentOddNode.next
        currentEvenNode = currentEvenNode.next
    currentOddNode.next = evenHead
    return head
