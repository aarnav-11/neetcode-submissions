class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        counter = 0

        while i < n:
            if nums[i] == val:
                nums.remove(val)
                i -= 1
                counter += 1
                nums.append("_")
            i += 1
        return n - counter
            