"""
536. Construct Binary Tree from String https://leetcode.com/problems/construct-binary-tree-from-string/

You need to construct a binary tree from a string consisting of parenthesis and integers.
The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis.
The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.
You always start to construct the left child node of the parent first if it exists.

Input: s = "-4(2(3)(1))(6(5)(7))"
Output: [-4,2,6,3,1,5,7]

Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]

Constraints:
    0 <= s.length <= 3 * 104
    s consists of digits, '(', ')', and '-' only.
"""


from typing import Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def str2tree(s: str) -> TreeNode:
    root, _ = str2tree_helper(s, 0)
    return root


def str2tree_helper(string: str, idx: int) -> Tuple[TreeNode, int]:
    if len(string) == 0:
        return None, -1

    val, idx = get_number(string, idx)
    root = TreeNode(val)

    if idx < len(string) and string[idx] == "(":
        idx += 1
        left_node, idx = str2tree_helper(string, idx)
        root.left = left_node
        idx += 1
    if idx < len(string) and string[idx] == "(":
        idx += 1
        right_node, idx = str2tree_helper(string, idx)
        root.right = right_node
        idx += 1

    return root, idx


def get_number(string: str, idx: int) -> Tuple[int, int]:
    num = 0
    is_negative = False

    if string[idx] == "-":
        is_negative = True
        idx += 1

    while idx < len(string) and string[idx].isdigit():
        num = num * 10 + int(string[idx])
        idx += 1

    num = -num if is_negative else num
    return num, idx

# O(n) | O(h)
