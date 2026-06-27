class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        start = []
        if len(nums) == 0:
            return 0

        for num in nums:
            if num-1 not in nums:
                start.append(num)

        res = 0
        for num in start:
            test = num
            local_res = 0
            while test+1 in nums:
                local_res += 1
                test = test + 1
            res = max(res, local_res)
        return 1 + res