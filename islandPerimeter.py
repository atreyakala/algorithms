def islandPerimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                neighbours = getNeighbours(grid, row, col, rows, cols)
                perimeter += (4 - neighbours)
    return perimeter

def getNeighbours(grid, row, col, rows, cols):
    count = 0
    adjacent = (row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)
    for r, c in adjacent:
        if r < 0 or r >= rows or c < 0 or c >= cols:
            continue
        if grid[r][c] == 1:
            count += 1
    return count
