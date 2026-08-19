class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #fix one and use 2 pointer approach to sort through the rest
        res = []
        nums = sorted(nums)

        for i, num in enumerate((nums)):
            if num > 0:
                break
            if i >= 1 and num == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r] + num
                if total == 0:
                    res.append([num, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res
