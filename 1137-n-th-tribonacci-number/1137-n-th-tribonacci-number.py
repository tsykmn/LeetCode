class Solution(object):
    # dp = {}
    # dp[1] = 1
    # dp[2] = 1
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        x, y, z = 0, 1, 1
        for i in range(2, n):
            x, y, z = y, z, x + y + z
        return z

        # Alternate solution: initialize dp/memoization
        # if n == 0:
        #     return 0
        # elif n == 1 or n == 2:
        #     return 1

        # Tn+3 = Tn + Tn+1 + Tn+2
        # Tn = Tn+3 - (Tn+1 + Tn+2) --> Tn = Tn-3 + Tn-1 - Tn-2
        if n in self.dp:
            return self.dp[n]
        self.dp[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        return self.dp[n]