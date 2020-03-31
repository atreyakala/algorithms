def maxPathSum(root):
    _, maxSoFar = maxGain(root)
    return maxSoFar

def maxGain(node):
    if node is None:
        return (0, float("-inf"))

    leftMaxSumAsBranch, leftMaxPathSum = maxGain(node.left)
    rightMaxSumAsBranch, rightMaxPathSum = maxGain(node.right)
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

    value = node.val
    maxSumAsBranch = maxChildSumAsBranch + value
    maxSumAsRoot = max(maxSumAsBranch, leftMaxSumAsBranch + rightMaxSumAsBranch + value)
    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRoot)

    return (maxSumAsBranch, maxPathSum)

def maxGain(node):
    leftMaxSumAsBranch = rightMaxSumAsBranch = 0
    leftMaxPathSum = rightMaxPathSum = float("-inf")

    if node.left:
        leftMaxSumAsBranch, leftMaxPathSum = maxGain(node.left)
        leftMaxSumAsBranch = max(0, leftMaxSumAsBranch)
    if node.right:
        rightMaxSumAsBranch, rightMaxPathSum = maxGain(node.right)
        rightMaxSumAsBranch = max(0, rightMaxSumAsBranch)

    sumAsRoot = leftMaxSumAsBranch + rightMaxSumAsBranch + node.val
    maxSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch) + node.val
    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, sumAsRoot)

    return (maxSumAsBranch, maxPathSum)
