class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #fix one and use 2 pointer approach to sort through the rest
        res = []
        nums = sorted(nums)

        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and nums[i-1] == num:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                three_sum = num + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
            



                