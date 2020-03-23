def orangesRotting(grid):
    rows = len(grid)
    cols = len(grid[0])
    fresh = set()
    rotten = set()
    for row in rows:
        for col in cols:
            if grid[row][col] == 1:
                fresh.add((row, col))
            elif grid[row][col] == 2:
                rotten.add((row, col))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    min = 0
    while len(fresh) > 0:
        nextRotten = set()
        for r, c in rotten:
            for dr, dc in directions:
                neighbour = ((r + dr), (c + dc))
                if neighbour in fresh:
                    nextRotten.add(neighbour)
        if len(nextRotten) == 0:
            return -1
        rotten = nextRotten
        fresh -= nextRotten
        min += 1
    return min
