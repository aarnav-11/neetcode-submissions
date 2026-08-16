class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #dict with sorted(word) : list(words) nlog n
        #keys (tuple())
        sortable = defaultdict(list)
        for word in strs:
            freq = [0]*26
            for char in word:
                i = ord('a') - ord(char)
                freq[i] += 1
            sortable[tuple(freq)].append(word)
        ans = []
        for values in sortable.values():
            ans.append(values)
        return ans