def lowestCommonAncestor(root, p, q):
    if root == p or root == q:
        return root
    if root.left:
        left = lowestCommonAncestor(root.left, p, q)
    if root.right:
        right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    else:
        return left or right
