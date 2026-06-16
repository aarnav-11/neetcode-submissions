class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_anagrams = defaultdict(list)

        for word in strs:
            sorted_word = sorted(word)
            sorted_anagrams[tuple(sorted_word)].append(word)

        ans = []
        for value in sorted_anagrams.values():
            ans.append(value)
        return ans