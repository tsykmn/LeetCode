class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # attempt with dp
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n+1):
            num = float('inf')
            current = 1
            while current * current <= n:
                num = min(num, dp[i - current*current] + 1)
                current += 1
            dp[i] = num
        return dp[n]

        # time limit error
        # m = n
        # for i in range(1, n):
        #     sq = i*i
        #     if sq <= n:
        #         m = min(m, 1 + self.numSquares(n-sq))
        #     else:
        #         break
        # return m
        