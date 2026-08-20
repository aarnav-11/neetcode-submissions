class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #start with max // 2
        
        l, r = 1, max(piles)
        best = r

        while l <= r:
            mid = (l+r) // 2
            total = sum(math.ceil(num/mid) for num in piles)
            if total > h:
                l = mid + 1
            elif total <= h:
                best = min(best, mid)
                r = mid - 1
                
        return best
                
