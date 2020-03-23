def binaryTreePaths(root):
    if root is None:
        return ""
    paths = []
    explore(root, [], paths)
    return paths

def explore(node, currentPath, allPaths):
    if node.left is None and node.right is None:
        currentPath += [node.val]
        allPaths.append("->".join(map(str, currentPath)))
        return
    if node.left is not None:
        self.explore(node.left, currentPath + [node.val], allPaths)
    if node.right is not None:
        self.explore(node.right, currentPath + [node.val], allPaths)
