from collections import deque

def rightSideView(self, root):
    if root is None:
        return None
    queue = deque([root])
    rightView = []
    while len(queue) > 0:
        for i in xrange(len(queue)):
            node = queue.popleft()
            if i == 0:
                rightView.append(node.val)
            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)
    return rightView
