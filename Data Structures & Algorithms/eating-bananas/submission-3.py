class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = max(piles)
        l = 1

        while l <= max_val:
            h_prac = h
            mid = int((max_val + l) // 2)
            for pile in piles:
                h_prac -= math.ceil((pile / mid))
            if h_prac < 0:
                l = mid + 1
            else:
                max_val = mid - 1

        return l