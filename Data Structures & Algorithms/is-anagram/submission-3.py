class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hashs, hasht = {}, {}

        for i in range(len(s)):
            if s[i] in hashs:
                hashs[s[i]] += 1
            else:
                hashs[s[i]] = 1
            
            if t[i] in hasht:
                hasht[t[i]] += 1
            else:
                hasht[t[i]] = 1

        return hashs == hasht
        