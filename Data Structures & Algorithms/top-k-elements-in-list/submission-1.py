class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {} #num : freq
        n = len(nums)

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        freq_list = [[] for _ in range(n+1)]
        for num, freq in freq_map.items():
            freq_list[freq].append(num)

        return_list = []
        for freq in range(n,0,-1):
            for num in freq_list[freq]:
                return_list.append(num)
            if len(return_list) == k:
                return return_list
            
