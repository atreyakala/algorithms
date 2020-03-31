def inOrderTraversal(root):
    inorder = []
    stack = []
    traverseLeftSubTree(stack, root)
    while len(stack) > 0:
        node = stack.pop()
        inorder.append(node.val)
        if node.right is not None:
            traverseLeftSubTree(node.right)

def traverseLeftSubTree(stack, node):
    while node is not None:
        stack.append(node)
        node = node.left
