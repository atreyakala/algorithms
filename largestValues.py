from collections import deque

def largestValues(root):
    if root is None:
        return []
    values = []
    queue = deque([root])
    while len(queue) > 0:
        currentLevelLength = len(queue)
        maxSoFar = float("-inf")
        for _ in range(currentLevelLength):
            currentNode = queue.popleft()
            maxSoFar = max(currentNode.val, maxSoFar)
            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)
        values.append(maxSoFar)
    return values
