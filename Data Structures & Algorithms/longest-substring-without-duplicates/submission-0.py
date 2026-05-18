class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char_seen = set()
        result = 0
        n = len(s)

        for r in range(n):
            while s[r] in char_seen:
                char_seen.remove(s[l])
                l += 1
            char_seen.add(s[r])
            result = max(result, r - l + 1)
        return result
            