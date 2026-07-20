class Solution:
    def rob(self, nums: List[int]) -> int:
        
        two_back = 0
        best = 0

        for num in nums:
            new_best = max(best, two_back + num)
            two_back = best
            best = new_best

        return best