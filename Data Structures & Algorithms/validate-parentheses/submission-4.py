class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_map = {"(" : ")", "{" : "}", "[" : "]"}

        for i in range(len(s)):
            if s[i] in par_map.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                top = stack.pop()
                if par_map[top] != s[i]:
                    return False
        if stack:
            return False
        return True
            