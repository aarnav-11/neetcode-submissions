class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0 , len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            val = nums[mid]
            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            elif val == target:
                return mid
        return -1