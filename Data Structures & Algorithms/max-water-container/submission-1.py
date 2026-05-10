class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_vol = 0

        while l < r:
            temp_max = 0
            if heights[l] < heights[r]:
                temp_max = heights[l] * (r-l)
                l += 1
            else:
                temp_max = heights[r] * (r-l)
                r -= 1
            max_vol = max(temp_max, max_vol)
        return max_vol
