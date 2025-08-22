class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        y = len(mat)
        x = len(mat[0])

        dp = [[float('inf') for j in range(x)] for i in range(y)]

        for i in range(y):
            for j in range(x):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if j > 0:
                        dp[i][j] = min(dp[i][j-1]+1, dp[i][j])
                    if i > 0:
                        dp[i][j] = min(dp[i-1][j]+1, dp[i][j])
        
        for i in reversed(range(y)):
            for j in reversed(range(x)):
                if (i+1) < y:
                    dp[i][j] = min(dp[i+1][j]+1, dp[i][j])

                if (j+1) < x:
                    dp[i][j] = min(dp[i][j+1]+1, dp[i][j])
            
        return dp