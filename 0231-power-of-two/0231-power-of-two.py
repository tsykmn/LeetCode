class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        def helper(curr, target):
            if curr > target:
                return False
            elif curr == target:
                return True
            return helper(curr*2, target)
        return helper(2, n)