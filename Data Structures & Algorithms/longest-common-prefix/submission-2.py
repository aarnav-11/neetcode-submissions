class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        ans = ""
        while True:
            if len(strs[0]) > i:
                init = strs[0][i]
            else:
                return ans
            for word in strs:
                if len(word) == i or word[i] != init:
                    return ans
            ans += init
            i += 1

        return i
                
