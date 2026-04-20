class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_map = {}
        length = len(nums)

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in freq_map:
                freq_map[nums[i]] = i
            else:
                return [freq_map[diff], i]
        return []