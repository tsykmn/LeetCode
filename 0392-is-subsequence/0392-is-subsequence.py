class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        nLst = len(t)
        nSeq = len(s)
        curr = []
        n = 0
        for i in range(nSeq):
            seq = s[i]
            added = False
            for j in range(n, nLst):
                if seq == t[j] and not added:
                    curr.append(t[j])
                    n = j + 1
                    added = True
            if not curr:
                return False
        if ''.join(curr) == s:
            return True