class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s 
        return res

 # "4#neet5#co#de"
    def decode(self, s: str) -> List[str]:
        res, i = [], 0 #store our result and pointer

        while i < len(s):
            j = i #another pointer to keep track of 
            #the end of the number (len of string)
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res