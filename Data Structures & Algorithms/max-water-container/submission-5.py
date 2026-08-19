class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(heights) - 1

        while l < r:
            total = (r - l)*min(heights[l], heights[r])
            maxWater = max(total, maxWater)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return maxWater
