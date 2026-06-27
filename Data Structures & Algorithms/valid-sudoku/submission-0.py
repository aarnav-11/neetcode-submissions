class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
            seen.clear()

        seen.clear()
        for c in range(cols):
            for r in range(rows):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
            seen.clear()
        
        seen.clear()
        for a in range(3):
            for i in range(3):
                for r in range(3):
                    for c in range(3):
                        if board[3*a + r][3*i + c] == ".":
                            continue
                        if board[3*a + r][3*i + c] in seen:
                            return False
                        seen.add(board[3*a + r][ 3*i + c])
                seen.clear()
        return True