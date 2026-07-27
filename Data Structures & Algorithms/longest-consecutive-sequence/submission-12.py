class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        count = 0

        longest = 0
        for num in nums:

            if num - 1 not in nums:
                length = 0
                while num + length in nums:
                    length += 1
                
                longest = max(longest, length)

        return longest