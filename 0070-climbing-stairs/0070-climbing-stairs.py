class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        x, y = 1, 0
        for i in range(n):
            y, x = x, x+y
        return x

        