class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            distance = x*x + y*y
            heapq.heappush(heap, (distance, x, y))
        ans = []
        for i in range(k):
            val = heapq.heappop(heap)
            ans.append([val[1], val[2]])
        return ans

