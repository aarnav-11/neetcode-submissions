class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_min(arr):
            l, r = 0, len(arr) - 1

            while l < r:
                mid = (l + r) // 2
                if arr[mid] > arr[r]:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        min_index = find_min(nums)
        
        def binary_search(arr, target, skew):
            def skew_index(index, skew, length):
                return (index + skew) % length

            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                val = skew_index(mid, skew, len(arr))
                if arr[val] > target:
                    r = mid - 1
                elif arr[val] < target:
                    l = mid + 1
                else:
                    return val
            return -1
        return binary_search(nums, target, min_index)
        