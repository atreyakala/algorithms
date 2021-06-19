"""
515. Find Largest Value in Each Tree Row https://leetcode.com/problems/find-largest-value-in-each-tree-row/

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Input: root = [1,2,3]
Output: [1,3]

Constraints
The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
"""

from collections import deque
from typing import List


def largest_values(root: 'TreeNode') -> List[int]:
    if root is None:
        return []

    values = []
    queue = deque([root])

    while queue:
        size = len(queue)
        current_level_max = float('-inf')

        for _ in range(size):
            node = queue.popleft()
            if node.val > current_level_max:
                current_level_max = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        values.append(current_level_max)

    return values
