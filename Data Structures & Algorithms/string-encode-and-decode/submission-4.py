class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        encoded = ""
        for string in (strs):
            encoded += (str(len(string)))
            encoded += ("#")
            encoded += (string)
        return encoded
    def decode(self, s: str) -> List[str]:
        #s = 4#abcd
        #Read the length
        #Advance to # + 1
        #decoded.append(s[from hash + 1:hash+1+length])
        #move i to hash + 1 + length
        if len(s) == 0:
            return []
        i = 0
        num = 0
        decoded = []
        while i < len(s):
            while s[i] != "#":
                num = num*10 + int(s[i])
                i += 1
            i += 1
            decoded.append(s[i:i+num])
            i = i + num
            num = 0
        return decoded



