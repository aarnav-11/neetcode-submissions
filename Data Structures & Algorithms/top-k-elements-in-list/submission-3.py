class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        bucket_list = [[] for _ in range(len(nums)+1)]

        for key, value in freq_map.items():
            bucket_list[value].append(key)

        return_val = []
        
        for i in reversed(range(len(bucket_list))):
            for j in range(len(bucket_list[i])):
                if len(return_val) == k:
                    return return_val
                return_val.append(bucket_list[i][j])
        return return_val
