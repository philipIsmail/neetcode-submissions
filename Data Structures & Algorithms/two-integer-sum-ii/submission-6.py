class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1
        while l < r:
            ding_ding = numbers[l] + numbers[r]

            if ding_ding < target:
                l += 1
            elif ding_ding > target:
                r -= 1
            else:
                return [l + 1, r + 1]