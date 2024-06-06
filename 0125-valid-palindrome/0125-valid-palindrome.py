class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = ''.join(filter(lambda x: x.isalpha() or x.isdigit() or x.isspace(), s))
        s = s.replace(" ", "")
        for i in range(len(s)):
            if s[i] != s[-(i+1)]:
                return False
        return True