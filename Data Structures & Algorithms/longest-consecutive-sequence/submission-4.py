class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        longest = 0
        for num in nums:
            localLength = 1
            if num - 1 not in setNums:
                while num + localLength in setNums:
                    localLength += 1
            longest = max(longest, localLength)
        return longest