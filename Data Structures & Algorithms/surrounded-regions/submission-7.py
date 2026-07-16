class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "O":
                return
            grid[r][c] = "S"
            for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                dfs(r + dr, c + dc)
        
        for r in range(rows):
            if grid[r][0] == "O":
                dfs(r,0)
            if grid[r][cols-1] == "O":
                dfs(r,cols - 1)
        for c in range(cols):
            if grid[0][c] == "O":
                dfs(0,c)
            if grid[rows-1][c] == "O":
                dfs(rows-1,c)
        
        for r in range(rows):
            for c in range(cols):
                val = grid[r][c]
                if val == "S":
                    grid[r][c] = "O"
                if val == "O":
                    grid[r][c] = "X"
    

                