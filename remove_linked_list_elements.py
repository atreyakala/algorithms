"""
203. Remove Linked List Elements https://leetcode.com/problems/remove-linked-list-elements/

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]


Constraints
    The number of nodes in the list is in the range [0, 104].
    1 <= Node.val <= 50
    0 <= val <= 50
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_elements(head: 'ListNode', val: int) -> 'ListNode':
    dummy_head = ListNode(0)
    dummy_head.next = head
    prev = dummy_head
    curr = head

    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    return dummy_head.next

