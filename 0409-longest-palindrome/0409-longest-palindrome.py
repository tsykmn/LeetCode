class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        size = 0
        chars = {}

        if s == s[::-1]:
            return n

        for i in s:
            if chars.get(i):
                chars[i] += 1
                if chars[i] % 2 == 0:
                    size += 2
            else:
                chars[i] = 1

        return size + 1 if n - size != 0 else size
