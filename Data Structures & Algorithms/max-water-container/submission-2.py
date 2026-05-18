class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_vol = 0

        while l < r:
            vol = (r-l) * min(heights[r], heights[l])
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
            max_vol = max(max_vol, vol)
        return max_vol
