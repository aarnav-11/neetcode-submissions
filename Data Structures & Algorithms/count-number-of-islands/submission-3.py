class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                dfs(r + dr, c + dc)
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    ans += 1
        return ans