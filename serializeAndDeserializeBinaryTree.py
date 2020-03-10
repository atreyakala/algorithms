from collections import deque

def serialize(root):
    if root is None:
        return ""
    queue = deque([root])
    levels = []
    while len(queue) > 0:
        curr = queue.popleft()
        if curr is None:
            levels.append(None)
        else:
            levels.append(curr.val)
            queue.append(curr.left)
            queue.append(curr.right)
    while levels[-1] is None:
        levels.pop()
    return ",".join(map(str, levels))

def deserialize(data):
    if data == "":
        return None
    data = data.split(",")
    levels = deque([])
    for datum in data:
        node = TreeNode(int(datum)) if datum != "None" else None
        levels.append(node)
    root = levels.popleft()
    parents = deque([root])
    while len(levels) > 0:
        leftNode = rightNode = None
        leftNode = levels.popleft()
        if len(levels) > 0:
            rightNode = levels.popleft()
        parent = parents.popleft()
        parent.left = leftNode
        if rightNode is not None:
            parent.right = rightNode
        if leftNode is not None:
            parents.append(leftNode)
        if rightNode is not None:
            parents.append(rightNode)
    return root
