class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #keep track of count of elements for both then compare

        return Counter(s) == Counter(t)