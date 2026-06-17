class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        fresh = 0
        time = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        
        while fresh > 0 and queue:
            length = len(queue)

            for i in range(length):
                r, c = queue.popleft()
                for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]) and grid[rr][cc] == 1:
                        grid[rr][cc] = 2
                        fresh -= 1
                        queue.append((rr, cc))
            time += 1

        if fresh == 0:
            return time
        else:
            return -1 


      