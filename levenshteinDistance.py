# O(N * M) | O(N * M)
def levenshteinDistance(source, target):
    rows = len(source) + 1
    cols = len(target) + 1
    dist = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(1, rows):
        dist[i][0] = i
    for i in range(1, cols):
        dist[0][i] = i
    for col in range(1, cols):
        for row in range(1, rows):
            if source[row - 1] == target[col - 1]:
                dist[row][col] = dist[row - 1][col - 1]
            else:
                dist[row][col] = 1 + min(dist[row - 1][col - 1], dist[row][col - 1], dist[row - 1][col])
    return dist[-1][-1]
