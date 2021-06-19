"""
98. Validate Binary Search Tree https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints
    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode) -> bool:
    return check_bounds(root, float('-inf'), float('+inf'))


def check_bounds(node: TreeNode, lower: float, upper: float) -> bool:
    if node is None:
        return True

    if node.val <= lower or node.val >= upper:
        return False

    return check_bounds(node.left, lower, node.val) and check_bounds(node.right, node.val, upper)


# O(n) | O(h)
