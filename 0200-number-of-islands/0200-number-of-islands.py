class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(grid, i, j):
            y = len(grid)
            x = len(grid[0])

            # Check out-of-bounds or if the cell is water ("0")
            if i < 0 or j < 0 or i >= y or j >= x or grid[i][j] == "0":
                return

            # Mark the current cell as visited
            grid[i][j] = "0"

            # Explore neighbors (up, down, left, right)
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

        if not grid:
            return 0

        total = 0
        y = len(grid)
        x = len(grid[0])

        for i in range(y):
            for j in range(x):
                # If we find an unvisited land cell, start a DFS
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    total += 1  # Increment the island count

        return total
