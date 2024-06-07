class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n1 = len(s)
        n2 = len(t)
        word = ""
        target = list(t)

        if n1 > n2 or n2 > n1:
            return False

        for i in range(n1):
            if s[i] in target:
                word += s[i]
                target.remove(s[i])
        return word == s