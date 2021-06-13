"""
543. Diameter of Binary Tree https://leetcode.com/problems/diameter-of-binary-tree/
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3is the length of the path [4,2,1,3] or [5,2,1,3].

Input: root = [1,2]
Output: 1

Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""

from typing import Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root: TreeNode) -> int:
    _, diameter = get_height_diameter(root)
    return diameter


def get_height_diameter(node: TreeNode) -> Tuple[int, int]:
    if node is None:
        return -1, 0

    left_height, left_diameter = get_height_diameter(node.left)
    right_height, right_diameter = get_height_diameter(node.right)

    current_height = max(left_height, right_height) + 1
    current_diameter = max(left_diameter, right_diameter, left_height + right_height + 2)

    return current_height, current_diameter


def test_0():
    root = TreeNode(0)
    assert diameter_of_binary_tree(root) == 0


def test_1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert diameter_of_binary_tree(root) == 2


def test_2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)
    assert diameter_of_binary_tree(root) == 4

# O(n) | O(h)