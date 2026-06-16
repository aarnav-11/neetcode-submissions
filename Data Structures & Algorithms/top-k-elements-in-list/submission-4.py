class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)

        for i in range(len(nums)):
            freq_map[nums[i]] += 1

        ans_list = [[] for _ in range(len(nums)+1)]

        for key, value in freq_map.items():
            ans_list[value].append(key)
        
        final_ans = []
        for i in range(len(nums), 0, -1):
            for j in range(len(ans_list[i])):
                if k == 0:
                    return final_ans
                final_ans.append(ans_list[i][j])
                k -= 1
        return final_ans