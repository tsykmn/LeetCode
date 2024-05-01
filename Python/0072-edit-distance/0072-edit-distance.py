class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1 = len(word1)
        n2 = len(word2)

        dp = [[0]*(n2+1) for _ in range(n1+1)]

        for i in range(1, n1+1):
            dp[i][0] = i
        for j in range(1, n2+1):
            dp[0][j] = j

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                # delete: dp[i-1][j]+1
                # insert: dp[i][j-1]+1
                # keep/replace: dp[i-1][j-1] + diff(i, j)

                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)

        return dp[n1][n2]