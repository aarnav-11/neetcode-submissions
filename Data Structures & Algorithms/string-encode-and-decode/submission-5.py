class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for word in strs:
            length = len(word)
            localAdd = str(length) + "#" + word
            ret += localAdd
        return ret
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        n = len(s)
        while i < n:
            num = 0
            while i < n and s[i] != "#":
                num *= 10
                num += int(s[i])
                i += 1
            i += 1
            ans.append(s[i:i+num])
            i += num
        return ans




