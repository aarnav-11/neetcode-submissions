class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j))

        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                rr = dr+r
                cc = dc+c
                if (0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == 2147483647):
                    grid[rr][cc] = grid[r][c] + 1
                    queue.append((rr,cc))

        
                    

        