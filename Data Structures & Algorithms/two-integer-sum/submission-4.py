class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lookedat = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookedat:
                return [lookedat[complement], i]
            lookedat[num] = i