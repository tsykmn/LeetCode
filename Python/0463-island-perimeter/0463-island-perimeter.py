class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        p = 0
        for i in range(n):
            m = len(grid[i])
            for j in range(m):
                if grid[i][j] == 1:
                    p +=  4
                    # up
                    if i > 0:
                        if grid[i-1][j] == 1:
                            p -= 1

                    # down
                    if i < (n-1):
                        if grid[i+1][j] == 1:
                            p -= 1
                
                    # left
                    if j > 0:
                        if grid[i][j-1] == 1:
                            p -= 1
                    
                    # right
                    if j < (m - 1):
                        if grid[i][j+1] == 1:
                            p -= 1
        return p
