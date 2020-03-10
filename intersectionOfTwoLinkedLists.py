def getIntersection(head1, head2):
    len1 = getLengthOf(head1)
    len2 = getLengthOf(head2)
    diff = len1 - len2
    if diff > 0:
        head1 = adjustHead(head1, diff)
    else:
        head2 = adjustHead(head2, -diff)
    while head1 is not None:
        if head1 == head2:
            return head1
        else:
            head1 = head1.next
            head2 = head2.next
    return None

def getLengthOf(head):
    length = 0
    currentNode = head
    while currentNode is not None:
        length += 1
        currentNode = currentNode.next
    return length

def adjustHead(head, skips):
    while skips > 0:
        head = head.next
        skips -= 1
    return head
