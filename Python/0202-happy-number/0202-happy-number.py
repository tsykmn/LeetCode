class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n != 1:
            if n in s:
                return False
            last = n % 10
            s.add(last)
            n = sum([int(i)**2 for i in str(n)])
        return True
