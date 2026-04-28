class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        num_islands = 0

        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0" or (r,c) in seen):
                return
            seen.add((r,c))
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                dfs(r + dr, c + dc)

        for i in range(rows):
            for j in range(cols):
                if ((i,j) not in seen and grid[i][j] == "1"):
                    dfs(i,j)
                    num_islands += 1
        return num_islands