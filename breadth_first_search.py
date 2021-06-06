from collections import deque


class Node:
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add_child(self, name: str) -> 'Node':
        self.children.append(Node(name))
        return self

    def breadth_first_search(self):
        visited = []
        to_be_visited = deque([self])

        while len(to_be_visited) > 0:
            current_node = to_be_visited.popleft()
            visited.append(current_node.name)

            for child in current_node.children:
                to_be_visited.append(child)

        return visited


#       A
#     /   \
#    B     C
#   / \   /
#  D   E F
#
# [A, B, C, D, E, F]
def test_0():
    root = Node("A")
    root.add_child("B").add_child("C")
    root.children[0].add_child("D").add_child("E")
    root.children[1].add_child("F")

    assert root.breadth_first_search() == ["A", "B", "C", "D", "E", "F"]


# O(V + E) | O(V)
