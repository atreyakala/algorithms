from collections import deque

def levelOrder(root):
    if root is None:
        return []
    queue = deque([root])
    levels = []
    while len(queue) > 0:
        currentLevel = []
        currentlevelLength = len(queue)
        for _ in range(currentlevelLength):
            currentNode = queue.popleft()
            currentLevel.append(currentNode.val)
            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)
        levels.append(currentLevel)
    return levels
