class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = defaultdict(list)
        for i, num in enumerate(nums):
            count[num].append(i)
        print(count)
        total = 0
        for value in count.values():
            n = len(value)
            total += n * (n - 1) // 2
        return total