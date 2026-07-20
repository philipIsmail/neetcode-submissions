class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}

        if len(s) != len(t):
            return False

        for i in s:
            hashmap_s[i] = hashmap_s.get(i, 0) + 1
        for j in t:
            hashmap_t[j] = hashmap_t.get(j, 0) + 1

        if hashmap_s == hashmap_t:
            return True

        return False