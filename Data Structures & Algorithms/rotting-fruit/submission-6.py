class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #keep track of fresh fruit at start
        #append all rotten to list
        #run bfs, keeping track of num cycles
        #subtract fresh everytime we hit it 
        #if fresh > 0 then return -1 else return bfs value

        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        total = 0

        for r in range(rows):
            for c in range(cols):
                val = grid[r][c]
                if val == 1:
                    fresh += 1
                elif val == 2:
                    q.append((r,c))

        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == 1:
                        q.append((rr,cc))
                        grid[rr][cc] = 2
                        fresh -= 1
            total += 1

        if fresh != 0:
            return -1
        return total