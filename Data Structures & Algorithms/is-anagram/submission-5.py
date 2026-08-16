class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = Counter(s)
        tCount = Counter(t)
        if len(s) != len(t):
            return False
        return sCount == tCount