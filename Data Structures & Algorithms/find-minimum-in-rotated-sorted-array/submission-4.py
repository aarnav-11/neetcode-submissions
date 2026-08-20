class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        l, r = 1, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == nums[-1]:
                return nums[-1]
            elif nums[mid] > nums[-1]:
                l = mid + 1
            elif nums[mid] < nums[-1]:
                r = mid - 1
            if nums[mid-1] < nums[mid] < nums[mid+1]:
                continue
            else:
                return min(nums[mid], nums[mid+1])