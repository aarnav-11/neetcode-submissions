class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_map = defaultdict(list)
        
        for word in strs:
            sorted_word = sorted(word)
            sorted_map[tuple(sorted_word)].append(word)
        return_list = []
        for value in sorted_map.values():
            return_list.append(value)
        return return_list
        