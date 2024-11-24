class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dist = {')': '(', '}': '{', ']': '['}
        opens = []
        n = len(s)
        for i in range(n):
            if s[i] in dist.values():
                opens.append(s[i])
            if s[i] in dist:
                # unmatched pairing cases
                if not opens:
                    return False
                p = opens.pop()
                if dist[s[i]] != p:
                    return False
        # no open remaining if closed matched
        return len(opens) == 0