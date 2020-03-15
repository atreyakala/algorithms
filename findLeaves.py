def findLeaves(root):
    leaves = []
    exploreTree(root, leaves)
    return leaves

def exploreTree(node, leaves):
    if node is None:
        return -1
    currentHeight = 1 + max(exploreTree(node.left, leaves), exploreTree(node.right, leaves))
    if currentHeight == len(leaves):
        leaves.append([])
    leaves[currentHeight].append(node.val)
    return currentHeight
