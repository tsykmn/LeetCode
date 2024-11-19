class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        c1, c2 = Counter(s), Counter(t)
        return c1 == c2