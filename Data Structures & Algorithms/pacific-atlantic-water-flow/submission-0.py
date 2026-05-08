class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, ocean, previous):
            if (r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < previous or (r,c) in ocean):
                return
            ocean.add((r,c))
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                dfs(r+dr, c+dc, ocean, heights[r][c])
        
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])
        
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])

        res = []

        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
        return res

            

