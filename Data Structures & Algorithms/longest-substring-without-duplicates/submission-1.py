class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        l = 0
        count = 0

        for r in range(len(s)):
            while s[r] in myset:
                myset.remove(s[l])
                l += 1
            myset.add(s[r])
            count = max(count, r - l + 1)
        return count