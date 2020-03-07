# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def rightSideView(self, root):
    if root is None: return None
    queue = [root]
    rightView = []
    while len(queue) > 0:
        for i in xrange(len(queue)):
            node = queue.pop(0)
            if i == 0: rightView.append(node.val)
            if node.right is not None: queue.append(node.right)
            if node.left is not None: queue.append(node.left)
    return rightView
