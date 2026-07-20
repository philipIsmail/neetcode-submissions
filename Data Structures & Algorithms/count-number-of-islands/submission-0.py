class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c): #traverses and sets anything horizontally and vertically to the island we're at to water (visited) because its part of that island
            q = deque()
            q.append((r, c))
            grid[r][c] = "0" #mark as visited
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= rows or
                    nc >= cols or grid[nr][nc] == "0"): #if below or above allocated grid or looking at a visited element or water
                        continue
                    q.append((nr, nc)) 
                    grid[nr][nc] = "0" #keep seeting it to zero until we reach water
                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
            
        return islands