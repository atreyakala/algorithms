from typing import List


class Node:
    def __init__(self, name: str):
        self.children = []
        self.name = name

    def add_child(self, name):
        child_node = Node(name)
        self.children.append(child_node)
        return self

    def depth_first_search(self, arr: List[str] = []) -> List[str]:
        if self is None:
            return []
        arr.append(self.name)
        for child in self.children:
            child.depth_first_search(arr)
        return arr


#       A
#     /   \
#    B     C
#   / \   /
#  D   E F
#
# [A, B, D, E, C, F]
def test_0():
    root = Node("A")
    root.add_child("B").add_child("C")
    root.children[0].add_child("D").add_child("E")
    root.children[1].add_child("F")
    assert root.depth_first_search() == ["A", "B", "D", "E", "C", "F"]

# O(V + E) | O(V)
