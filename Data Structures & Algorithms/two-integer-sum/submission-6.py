class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #go thru each elem (index, value) in array
        #store elem in map key and index in value
        #then iterate checking for diff
        #if diff is in there return diff's index (value in map)
        #and current index

        elem_index = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in elem_index:
                return [elem_index[diff], i]
            elem_index[n] = i
        