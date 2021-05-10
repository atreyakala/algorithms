# https://www.algoexpert.io/questions/Branch%20Sums

# Return a list of branch sums ordered from leftmost branch sum to rightmost branch sum
from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sums(root: Node) -> List[int]:
    sums = []
    add_branch_sums(root, 0, sums)
    return sums


def add_branch_sums(node: Node, running_sum: int, sums: List[int]) -> None:
    if node is None:
        return

    new_running_sum = running_sum + node.value

    if node.left is None and node.right is None:
        sums.append(new_running_sum)
        return

    add_branch_sums(node.left, new_running_sum, sums)
    add_branch_sums(node.right, new_running_sum, sums)

    return

# O(N) | O(N) where N is the number of nodes
# Space complexity is combination of result array (leaf nodes) and recursive call stack
