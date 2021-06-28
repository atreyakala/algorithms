"""
133. Clone Graph https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

Constraints
    The number of nodes in the graph is in the range [0, 100].
    1 <= Node.val <= 100
    Node.val is unique for each node.
    There are no repeated edges and no self-loops in the graph.
    The Graph is connected and all nodes can be visited starting from the given node.
"""

# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: 'Node') -> 'Node':
    if node is None:
        return None

    to_clone = deque([node])
    clone = Node(node.val)
    clones = {node: clone}

    while len(to_clone) > 0:
        current_node = to_clone.popleft()
        current_clone = clones[current_node]
        for neighbor in current_node.neighbors:
            if neighbor not in clones:
                neighbor_clone = Node(neighbor.val)
                clones[neighbor] = neighbor_clone
                to_clone.append(neighbor)
            else:
                neighbor_clone = clones[neighbor]
            current_clone.neighbors.append(neighbor_clone)

    return clone


# O(v + e) | O(v + e)
