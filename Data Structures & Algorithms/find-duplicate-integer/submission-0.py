class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq_table = Counter(nums)

        for key, value in freq_table.items():
            if value > 1:
                return key
        
        return -1