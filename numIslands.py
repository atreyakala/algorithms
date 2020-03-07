def numIslands(grid):
    numRows = len(grid)
    numCols = len(grid[0])
    r = 0
    c = 0
    numIslands = 0
    for r in xrange(numRows):
        for c in xrange(numCols):
            if grid[r][c] == '1':
                numIslands += 1
                self.visitNeighbours(r, c, grid)
    return numIslands

def visitNeighbours(r, c, grid):
    numRows = len(grid)
    numCols = len(grid[0])
    if r < 0 or c < 0 or r >= numRows or c >= numCols:
        return
    else:
        grid[i][j] = '0'
        self.visitNeighbours(r, c + 1, grid)
        self.visitNeighbours(r + 1, c, grid)
        self.visitNeighbours(r, c - 1, grid)
        self.visitNeighbours(r - 1, c, grid)
