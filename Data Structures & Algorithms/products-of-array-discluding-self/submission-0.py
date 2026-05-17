class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_zero = 0

        for num in nums:
            if num == 0:
                num_zero += 1
        
        arr_product = 1
        if num_zero > 1:
            return [0] * n
        else:
            for i in range(n):
                if nums[i] != 0:
                    arr_product *= nums[i]
            if num_zero == 1:
                for i in range(n):
                    if nums[i] == 0:
                        nums[i] = arr_product
                    else:
                        nums[i] = 0
            elif num_zero == 0:
                for i in range(n):
                    nums[i] = int(arr_product/nums[i])
        return nums