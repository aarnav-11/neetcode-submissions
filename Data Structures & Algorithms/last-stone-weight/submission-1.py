class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            x, y = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if x == y:
                continue
            else:
                heapq.heappush_max(stones, abs(y-x))
        if len(stones) == 1:
            return stones[0]
        return 0
            