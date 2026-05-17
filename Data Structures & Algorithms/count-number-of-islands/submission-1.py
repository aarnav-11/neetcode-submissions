class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0"):
                return
            grid[r][c]="0"
            for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                dfs(r+dr, c+dc)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    num_islands += 1
        return num_islands
                    