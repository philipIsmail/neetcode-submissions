class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #with two pointers at each index calculate the water it contains
        l, r = 0, len(heights) - 1
        result = 0

        while l < r:
            #get the min of the two numbers (l and r) and multiply by the 
            #distance from each other (l - r)
            area = min(heights[l], heights[r]) * (r - l)
            #keep track of the max
            result = max(result, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return result