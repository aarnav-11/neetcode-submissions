class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og_color = image[sr][sc]
        rows, cols = len(image), len(image[0])
        seen = set()
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != og_color or (r,c) in seen:
                return
            seen.add((r,c))
            image[r][c] = color
            for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                dfs(dr + r, dc + c)
        
        dfs(sr, sc)
        return image