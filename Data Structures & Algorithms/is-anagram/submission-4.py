class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        smap, tmap = {}, {}

        for char in s:
            smap[char] = smap.get(char, 0) + 1
        for char in t:
            tmap[char] = tmap.get(char, 0) + 1

        return smap == tmap
        