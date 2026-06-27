class Solution:
    def trap(self, height: List[int]) -> int:
        #get to first start point.
        #move r forward as long as height[r] < height [l]
        #count water while moving r forward by taking height[l] - height[r]
        #if height[l] <= height[r] we advance l to r
        l, r = 0, 1
        total_water_r_l = [0]*(len(height)+1)
        total_water_l_r = [0]*(len(height)+1)

        while r < len(height):
            while r < len(height) and height[r] < height[l]:
                total_water_r_l[r] = height[l] - height[r]
                r += 1
            l = r
            r += 1

        l, r = len(height) - 1, len(height) - 2

        while r >= 0:
            while r >= 0 and height[r] < height[l]:
                total_water_l_r[r] = height[l] - height[r]
                r -= 1
            l = r
            r -= 1
        
        ans = 0
        for i in range(len(height) + 1):
            ans += min(total_water_r_l[i], total_water_l_r[i])
        return ans
