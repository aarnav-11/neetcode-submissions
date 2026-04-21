class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_map = defaultdict(list)

        for word in strs:
            sorted_word = tuple(sorted(word))
            list_map[sorted_word].append(word)
        return_val = []
        for value in list_map.values():
            return_val.append(value)
        return return_val
            
        