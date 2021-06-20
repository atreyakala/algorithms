"""
199. Binary Tree Right Side View https://leetcode.com/problems/binary-tree-right-side-view/

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Input: root = [1,null,3]
Output: [1,3]

Input: root = []
Output: []

Constraints
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
"""


from collections import deque


def right_side_view(root):
    view = []
    if root is None:
        return view
    queue = deque([root])
    while len(queue) > 0:
        for i in range(len(queue)):
            node = queue.popleft()
            if i == 0:
                view.append(node.val)
            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)
    return view


# O(n) | O(w)