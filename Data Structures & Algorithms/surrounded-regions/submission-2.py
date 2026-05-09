class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows, cols = len(board), len(board[0])
        seen = set()
        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O" or (r,c) in seen):
                return
            seen.add((r,c))
            board[r][c] = "S"
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                dfs(r + dr, c + dc)

        for r in range(rows):
            dfs(r, cols-1)
            dfs(r, 0)
        for c in range(cols):
            dfs(rows-1, c)
            dfs(0, c)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "S":
                    board[i][j] = "O"
        
        

                