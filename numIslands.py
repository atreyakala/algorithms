def numIslands(grid):
    if grid is None or len(grid) == 0:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                explore(r, c, grid, dirs)
    return islands

def explore(r, c, grid, dirs):
    rows = len(grid)
    cols = len(grid[0])
    if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
        return
    grid[r][c] = '0'
    for dr, dc in dirs:
        row = r + dr
        col = c + dc
        explore(row, col, grid, dirs)
