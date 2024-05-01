class Solution(object):
    # memo = {}
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n==0:
        #     return 0
        # elif n == 1:
        #     return 1

        x, y = 0, 1
        for i in range(n):
            y, x = x, y + x
        return x