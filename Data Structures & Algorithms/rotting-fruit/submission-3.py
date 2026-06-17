class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in [[0,1], [1,0], [-1,0], [0,-1]]:
                    rr = r + dr
                    cc = c + dc
                    if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == 1:
                        grid[rr][cc] = 2
                        fresh -= 1
                        q.append((rr,cc))
            time += 1
        if fresh == 0: 
            return time
        else:
            return -1