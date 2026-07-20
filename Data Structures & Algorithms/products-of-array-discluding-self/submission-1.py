class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zero_count = nums.count(0)
        output = [0] * len(nums) #output to be returned
        product = 1
        for num in nums:
            if num != 0:
                product *= num

        i = 0
        for i, num in enumerate(nums):
            if zero_count > 1:
                output[i] = 0
            elif zero_count == 1:
                output[i] = product if num == 0 else 0
            else:
                output[i] = product // num
            i += 1

        return output