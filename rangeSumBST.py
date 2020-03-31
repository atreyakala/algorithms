def rangeSumBST(root, leftBound, rightBound):
    if root is None:
        return 0
    if root.val > rightBound:
        return rangeSumBST(root.left, leftBound, rightBound)
    if root.val < leftBound:
        return rangeSumBST(root.right, leftBound, rightBound)

    return root.val + rangeSumBST(root.left, leftBound, rightBound) + rangeSumBST(root.right, leftBound, rightBound)
