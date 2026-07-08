class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        frac = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num
            if diff in frac:
                return [frac[diff], i]
            frac[num] = i
        return []