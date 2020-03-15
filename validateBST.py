def validateBST(root):
    return checkBounds(root, float("-inf"), float("inf"))

def checkBounds(node, lower, upper):
    if node is None:
        return True
    if node.val < lower or node.val > upper:
        return False
    return checkBounds(node.left, lower, node.val) and checkBounds(node.right, node.val, upper)
