# 203. Remove Linked List Elements https://leetcode.com/problems/remove-linked-list-elements/

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: ListNode, val: int) -> ListNode:
    dummyHead = ListNode(0)
    dummyHead.next = head
    prev, curr = dummyHead, head

    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    return dummyHead.next
