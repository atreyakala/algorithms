"""
314. Binary Tree Vertical Order Traversal https://leetcode.com/problems/binary-tree-vertical-order-traversal/

Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
"""

from collections import defaultdict, deque
from typing import List, Dict


def vertical_traversal(root: 'TreeNode') -> List[List[int]]:
    if root is None:
        return []

    min_x = 0
    max_x = 0

    to_visit = deque([])
    visited = defaultdict([])

    to_visit.append([root, 0])

    while len(to_visit) > 0:
        node, x = to_visit.popleft()
        visited[x].append(node.val)

        min_x = min(x, min_x)
        max_x = max(x, max_x)

        if node.left is not None:
            to_visit.append([node.left, x - 1])
        if node.right is not None:
            to_visit.append([node.right, x + 1])

    return [visited[x] for x in range(min_x, max_x + 1)]

# O(n) | O(n)


def vertical_traversal(root: 'TreeNode') -> List[List[int]]:
    if root is None:
        return []

    to_visit = deque([])
    visited = defaultdict(list)

    to_visit.append([root, 0])

    while len(to_visit) > 0:
        node, x = to_visit.popleft()
        visited[x].append(node.val)
        if node.left is not None:
            to_visit.append([node.left, x - 1])
        if node.right is not None:
            to_visit.append([node.right, x + 1])

    return visited

# O(nlogn) | O(n)


def vertical_traversal(root: 'TreeNode') -> List[List[int]]:
    if root is None:
        return []

    visited = {}
    traverse(root, visited, 0, 0)

    return [visited[x] for x in sorted(visited.keys())]


def traverse(node: 'TreeNode', traversed: Dict[int, List[int]], x: int, y: int):
    traversed[x].append([y, node.val])
    if node.left is not None:
        traverse(node.left, traversed, x - 1, y + 1)
    if node.right is not None:
        traverse(node.right, traversed, x + 1, y + 1)
