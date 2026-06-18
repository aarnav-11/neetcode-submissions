class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0 
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))
        
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == 1:
                        grid[rr][cc] = 2
                        q.append((rr,cc))
                        fresh -= 1
            time += 1

        if fresh == 0:
            return time
        else:
            return -1
