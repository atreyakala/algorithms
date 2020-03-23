from collections import deque

def wallsAndGates(rooms):
    if rooms is None or len(rooms) == 0 or rooms[0] is None or len(rooms[0]) == 0:
        return
    INF = 2 ** 31 - 1
    rows = len(rooms)
    cols = len(rooms[0])
    gates = deque([(r, c) for r in range(rows) for c in range(cols) if rooms[r][c] == 0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while len(gates) > 0:
        r, c = gates.popleft()
        for dr, dc in directions:
            row = r + dr
            col = c + dc
            if row >= 0 and row < rows and col >= 0 and col < cols and rooms[row][col] == INF:
                rooms[row][col] = rooms[r][c] + 1
                gates.append((row, col))
