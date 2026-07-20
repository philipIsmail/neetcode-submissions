class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        ways_to_prev = 2
        way_to_stair_before_prev = 1

        for stair in range(3, n + 1):

            curr_ways = ways_to_prev + way_to_stair_before_prev

            way_to_stair_before_prev = ways_to_prev
            ways_to_prev = curr_ways

        return ways_to_prev