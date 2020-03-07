class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

    def height(self, node):
        if self is None:
            return -1
        if self.left is None and self.right is None:
            return 0
        return 1 + max(self.height(self.left), self.height(self.right))
