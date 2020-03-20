from collections import deque

def isComplete(root):
    queue = deque([root])
    seenNull = False
    while len(queue) > 0:
        node = queue.popleft()
        if node is None:
            if not seenNull:
                seenNull = True
            continue
        elif seenNull:
            return False
        queue.append(node.left)
        queue.append(node.right)
    return True
