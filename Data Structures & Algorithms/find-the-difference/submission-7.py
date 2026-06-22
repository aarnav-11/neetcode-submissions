class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        seen = defaultdict(int)

        for char in s:
            seen[char] += 1
        
        for char in t:
            if seen[char] == 0:
                return char
            seen[char] -= 1