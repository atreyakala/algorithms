from collections import deque

def isBipartite(graph):
    nodeColor = {}
    for node in range(len(graph)):
        if node in nodeColor:
            continue
        nodeColor[node] = 1
        queue = deque([node])
        while len(queue) > 0:
            node = queue.popleft()
            for neighbour in graph[node]:
                if neighbour not in nodeColor:
                    nodeColor[neighbour] = -nodeColor[node]
                    queue.append(neighbour)
                elif nodeColor[neighbour] == nodeColor[node]:
                    return False
    return True

def isBipartite(graph):
    nodeColor = {}
    for node in range(len(graph)):
        if node not in nodeColor and not canColor(node, 1, graph, nodeColor):
            return False
    return True

def canColor(node, color, graph, nodeColor):
    if node in nodeColor:
        return nodeColor[node] == color
    nodeColor[node] = color
    for neighbour in graph[node]:
        if not canColor(neighbour, -color, graph, nodeColor):
            return False
    return True
