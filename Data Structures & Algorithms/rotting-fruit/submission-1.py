class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        fresh = 0
        queue = deque()
        time = 0 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i,j))

        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr = r + dr
                    nc = c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr,nc) not in seen):
                        seen.add((nr,nc))
                        queue.append((nr,nc))
                        fresh -= 1
            time+=1
            
        if fresh != 0:
            return -1
        return time
