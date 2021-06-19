"""
19. Remove Nth Node From End of List https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_nth_node_from_end(head: 'ListNode', n: int) -> 'ListNode':
    if head is None:
        return None

    dummy = ListNode(0)
    dummy.next = head
    leader = head
    for _ in range(n):
        leader = leader.next

    follower = dummy
    while leader.next is not None:
        leader = leader.next
        follower = follower.next

    follower.next = follower.next.next
    return dummy.next


# O(n) | O(1)