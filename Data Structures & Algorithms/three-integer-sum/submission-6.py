class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #fix one and use 2 pointer approach to sort through the rest
        ans = []
        nums = sorted(nums)

        for i in range(len(nums)):
            target = nums[i] * -1
            l, r = i+1, len(nums) - 1

            if i > 0:
                if nums[i] == nums[i-1]:
                    continue

            while l < r:
                if nums[l] + nums[r] == target:
                    ans.append([target * -1, nums[l], nums[r]])
                    l += 1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while r > l and nums[r] == nums[r+1]:
                        r-=1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return ans
                