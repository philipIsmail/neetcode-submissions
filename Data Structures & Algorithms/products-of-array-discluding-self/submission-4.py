class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        """
        example: [1,2,4,6] the whole thing is 
        based on having a prefix of all the elements before
        the current index saved -> [1, 1, 2, 8] and a postfix
        which is just the same thing but backwards -> [48, 24, 6, 1]
        and then doing prefix * postfix
        """ 
        
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range((len(nums) - 1), -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result