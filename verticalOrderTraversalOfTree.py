from collections import defaultdict

def verticalTraversal(root):
    traversed = defaultdict(lambda: [])
    traverse(root, traversed, 0, 0)
    # traverse(root, traversed)
    order = []
    for x in sorted(traversed.keys()):
        traversed[x].sort(key = lambda v: (v[0], v[1]))
        order.append(item[1] for item in traversed[x])
    return order

def traverse(node, traversed, x, y):
    traversed[x].append([y, node.val])
    if node.left is not None:
        traverse(node.left, traversed, x - 1, y + 1)
    if node.right is not None:
        traverse(node.right, traversed, x + 1, y + 1)

def traverse(root, traversed):
    if root is None:
        return
    queue = deque()
    queue.append([root, (0, 0)])
    while len(queue) > 0:
        node, (x, y) = queue.popleft()
        traversed[x].append([y, node.val])
        if node.left is not None:
            queue.append([node.left, (x - 1, y + 1)])
        if node.right is not None:
            queue.append([node.right, (x + 1, y + 1)])
