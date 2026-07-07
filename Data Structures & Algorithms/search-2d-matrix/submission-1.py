class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0])*len(matrix) - 1
        rows, cols = len(matrix), len(matrix[0])
        while l <= r:
            mid = (l + r) // 2
            mid_row = mid // cols
            mid_col = mid % cols
            val = matrix[mid_row][mid_col]
            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return True
        return False