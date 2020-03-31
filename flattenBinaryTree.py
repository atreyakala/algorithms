def flattenBinaryTree(root):
    leftMost, _ = flattenTree(root)
    return leftMost

def flattenTree(node):
    if node.left is None:
        leftMost = node
    else:
        leftSubTreeLeftMost, leftSubTreeRightMost = flattenTree(node.left)
        updateBindings(leftSubTreeRightMost, node)
        leftMost = leftSubTreeLeftMost

    if node.right is None:
        rightMost = node
    else:
        rightSubTreeLeftMost, rightSubTreeRightMost = flattenTree(node.right)
        updateBindings(node, rightSubTreeLeftMost)
        rightMost = rightSubTreeRightMost

    return (leftMost, rightMost)

def updateBindings(left, right):
    left.right = right
    right.left = left
