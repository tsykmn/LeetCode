class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def isValid(num):
            if int(num) == 1:
                return True
            elif (n % 2) == 0:
                return False
            elif n == 3:
                return False
            total = 0
            for i in str(num):
                total += (int(i)**2)
            return isValid(total)
        return isValid(n)
