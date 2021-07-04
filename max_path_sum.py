"""
124. Binary Tree Maximum Path Sum https://leetcode.com/problems/binary-tree-maximum-path-sum/

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path. Given the root of a binary tree, return the maximum path sum of any path.

Input: root = [1, 2, 3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Input: root = [-10, 9, 20, null, null, 15, 7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints
The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""


from typing import Tuple


class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def max_path_sum(node: Node) -> int:
    _, max_sum = max_gain(node)
    return max_sum


def max_gain(node: Node) -> Tuple[int, float]:
    if node is None:
        return 0, float('-inf')

    left_max_sum_as_branch, left_max_path_sum = max_gain(node.left)
    right_max_sum_as_branch, right_max_path_sum = max_gain(node.right)

    max_child_branch_sum = max(left_max_sum_as_branch, right_max_sum_as_branch)
    max_sum_as_branch = max(max_child_branch_sum, 0) + node.val

    max_sum_as_root = max(max_sum_as_branch, left_max_sum_as_branch + right_max_sum_as_branch + node.val)
    max_path_sum = max(left_max_path_sum, right_max_path_sum, max_sum_as_root)

    return max_sum_as_branch, max_path_sum

# O(n) | O(h)
