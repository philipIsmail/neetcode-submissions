class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        area = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] != 1:
                return 0

            grid[i][j] = "#"

            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j - 1) + dfs(i, j + 1)


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                area = max(area, dfs(i, j))

        return area 