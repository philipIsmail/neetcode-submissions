from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = {}
        for i in range(len(nums)):
            excluded = [nums[j] for j in range(len(nums)) if j != i]
            res[i] = prod(excluded)
        return list(res.values())