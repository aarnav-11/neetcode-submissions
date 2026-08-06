class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedAnagrams = defaultdict(list)

        for word in strs:
            sortedAnagrams[tuple(sorted(word))].append(word)
        ans = []
        for value in sortedAnagrams.values():
            ans.append(value)
        return ans