from collections import deque

def rightSideView(root):
    view = []
    if root is None:
        return view
    queue = deque([root])
    while len(queue) > 0:
        for i in range(len(queue)):
            node = queue.popleft()
            if i == 0:
                view.append(node.val)
            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)
    return view
