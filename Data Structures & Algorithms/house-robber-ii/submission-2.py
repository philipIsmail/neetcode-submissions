class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def rob_line(nums):
            
            two_back = 0
            best = 0

            for money in nums:
                new_best = max(best, two_back + money)
                two_back = best
                best = new_best

            return best

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))