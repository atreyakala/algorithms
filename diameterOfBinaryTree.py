def diameterOfBinaryTree(root):
    _, diameter = heightDiameter(root)
    return diameter

def heightDiameter(root):
    if root is None:
        return -1, 0
    leftHeight, leftDiameter = heightDiameter(root.left)
    rightHeight, rightDiameter = heightDiameter(root.right)
    currentHeight = max(leftHeight, rightHeight) + 1
    return currentHeight, max(leftHeight + rightHeight + 2, leftDiameter, rightDiameter)
