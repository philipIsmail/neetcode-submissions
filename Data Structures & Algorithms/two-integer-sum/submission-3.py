class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {} #hashmap to store the num as the key and the index as the value since we need to return index
        
        for i, n in enumerate(nums): #gets the index(i) and the value in that index (n)
            complement = target - n
            if complement in seen: #as soon as we have two values that equal the target we want to return the indices
                return [seen[complement], i]
            seen[n] = i #keep adding to the hashmap as long as complement is not found, reverse engineering in a way