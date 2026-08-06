class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapT = Counter(s)
        mapS = Counter(t)

        if mapS != mapT:
            return False
        return True