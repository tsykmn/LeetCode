class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n1 = len(s)
        n2 = len(t)

        if n1 > n2:
            return False
        elif n1 == 0:
            return True
        
        pt1 = 0
        pt2 = 0

        while pt1 <= len(s) and pt2 < len(t):
            if s[pt1] == t[pt2]:
                pt1 += 1
            pt2 += 1
        return pt1 == len(s)