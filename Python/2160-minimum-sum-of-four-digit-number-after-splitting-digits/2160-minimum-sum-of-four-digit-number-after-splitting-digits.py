class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = sorted(str(num))
        return int(s[0]+s[2])+int(s[1]+s[3])