class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        sizes = []

        for word in strs:
            length = len(word)
            sizes.append(length)

        encoded = ""
        for i in range(len(sizes)):
            encoded+=(str(sizes[i]) + "#" + strs[i])
        print(encoded)
        return encoded
        
    def decode(self, s: str) -> List[str]:
        #s = 4#abcd
        if len(s) == 0:
            return []
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            skip = int(s[i:j])
            i = j + 1
            decoded.append(s[i: i + skip])
            i += skip

        return decoded
