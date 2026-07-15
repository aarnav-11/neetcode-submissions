class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        og_color = image[sr][sc]
        if og_color == color:
            return image
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != og_color:
                return
            image[r][c] = color
            for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                dfs(dr + r, dc + c)
        
        dfs(sr, sc)
        return image