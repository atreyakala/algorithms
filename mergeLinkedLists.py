class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n + m) time | O(n + m) space
def mergeLinkedLists(headOne, headTwo):
    if headOne is None:
        return headTwo
    if headTwo is None:
        return headOne
    if headOne.value < headTwo.value:
        headOne.next = mergeLinkedLists(headOne.next, headTwo)
        return headOne
    else:
        headTwo.next = mergeLinkedLists(headOne, headTwo.next)
        return headTwo

def mergeLinkedLists(headOne, headTwo):
    p1 = headOne
    p1Prev = None
    p2 = headTwo
    while p1 is not None and p2 is not None:
        if p1.val < p2.val:
            p1Prev = p1
            p1 = p1.next
        else:
			if p1Prev is not None:
				p1Prev.next = p2
            p1Prev = p2
            p2 = p2.next
			p1Prev.next = p1
    if p1 is None:
        p1Prev.next = p2
    return headOne if headOne.val < headTwo.val else headTwo
