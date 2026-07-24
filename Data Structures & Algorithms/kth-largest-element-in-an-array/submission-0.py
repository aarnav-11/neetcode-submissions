class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in range(len(nums)):
            if len(heap) >= k:
                if heap[0] < nums[i]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, nums[i])
            else:
                heapq.heappush(heap, nums[i])
        return heap[0]