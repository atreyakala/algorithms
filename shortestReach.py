def buildGraph():
    graph = {}
    n, m = map(int, raw_input().split())
    for i in xrange(1, n + 1):
        graph[i] = []

    for i in xrange(m):
        u, v = map(int, raw_input().split())
        graph[u].append(v)
        graph[v].append(u)
    return n, graph

def shortestReach(G, s):
    visited = {}
    distance = {}

    for k in G.keys():
        visited[k] = False
        distance[k] = -1 if k != s else 0

    q = [s]
    while q:
        current = q.pop(0)
        for child in G[current]:
            if not visited[child] and distance is -1:
                distance[child] = distance[current] + 6
                q.append(child)
        visited[current] = True

    return distance

def main():
    q = int(raw_input())
    for i in xrange(q):
        n, G = buildGraph()

        s = raw_input().strip()
        distance = shortestReach(G, s)
        for i in xrange(1, n + 1):
            if i != s:
                print(distance[i]),
        print("")

main()
