class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        at each index do a dfs to see if the island continues
        if it does change it to #, otherwise terminate
        
        """

        def dfs(i, j):

            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] != "1":
                return None

            grid[i][j] = "#"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count += 1

        return count