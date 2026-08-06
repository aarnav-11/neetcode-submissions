class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for key, value in freq.items():
            heap.append((value, key))
        heapq.heapify_max(heap)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop_max(heap)[1])
        return ans