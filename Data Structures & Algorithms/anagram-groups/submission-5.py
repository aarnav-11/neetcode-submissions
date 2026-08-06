class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedAnagrams = defaultdict(list)

        for word in strs:
            count = [0]*26
            for c in word:
                val = ord(c) - ord("a")
                count[val] += 1
            sortedAnagrams[tuple(count)].append(word)
        return list(sortedAnagrams.values())