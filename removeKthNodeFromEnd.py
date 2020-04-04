# O(n) | O(1)
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeKthNodeFromEnd(head, k):
    if head is None:
        return None
    leader = head
    follower = head
    for _ in range(n):
        leader = leader.next
    if leader is None:
        head = head.next
        return head
    while leader.next is not None:
        leader = leader.next
        follower = follower.next
    follower.next = follower.next.next
    return head
