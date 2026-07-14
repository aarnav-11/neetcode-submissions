class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        def dfs(r,c):
            if r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c] == 0 or (r,c) in seen:
                return 0
            seen.add((r,c))
            area = 1
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                area += dfs(r + dr, c + dc)
            return area

        max_island_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_island_area = max(max_island_area, dfs(r,c))
        return max_island_area
