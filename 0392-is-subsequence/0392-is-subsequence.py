class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # More efficient
        nT = len(t)
        nS = len(s)

        if nS > nT:
            return False
        elif nS == 0:
            return True
        subsequence = 0
        for i in range(nT):
            if subsequence <= (nS-1):
                if s[subsequence] == t[i]:
                    subsequence += 1
        return subsequence == nS
        
        # nLst = len(t)
        # nSeq = len(s)
        # curr = []
        # n = 0
        # for i in range(nSeq):
        #     seq = s[i]
        #     added = False
        #     for j in range(n, nLst):
        #         if seq == t[j] and not added:
        #             curr.append(t[j])
        #             n = j + 1
        #             added = True
        #     if not curr:
        #         return False
        # if ''.join(curr) == s:
        #     return True