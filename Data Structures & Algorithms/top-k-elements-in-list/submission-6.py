class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        length = len(nums)
        buckets = [[] for _ in range(length+1)]
        print(buckets)

        for key, value in frequency.items():
            buckets[value].append(key)
        ans = []
        
        for i in range(length, -1, -1):
            if len(ans) == k:
                break
            for j in range(len(buckets[i])):
                ans.append(buckets[i][j])
        return ans