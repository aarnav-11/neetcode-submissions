class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        seen = set()

        for r in range(rows):
            for c in range (cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    seen.add((r,c))
        distance = 1
        while q:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()
                for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                    rr, cc = r + dr, c + dc 
                    if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] != -1 and (rr,cc) not in seen:
                        q.append((rr,cc))
                        seen.add((rr,cc))
                        if grid[rr][cc] == 2147483647:
                            grid[rr][cc] = distance
            distance += 1
                        
        
                    
                

            

        
                    

        