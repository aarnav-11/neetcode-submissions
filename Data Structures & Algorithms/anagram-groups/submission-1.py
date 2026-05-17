class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_map = defaultdict(list)
        return_list = []

        for string in strs:
            list_map[tuple(sorted(string))].append(string)
        
        for i in list_map.values():
            return_list.append(i)

        return return_list
            
        