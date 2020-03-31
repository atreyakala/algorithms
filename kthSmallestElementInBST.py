from collections import deque

def kthSmallest(root, k):
    stack = deque([])
    while True:
        appendLeftToStack(root, stack)
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right

def appendLeftToStack(node, stack):
    while node is not None:
        stack.append(node)
        node = node.left
