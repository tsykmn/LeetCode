class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        words = [i for i in s if i.isalpha() or i.isdigit()]
        n = len(words)
        for i in range(n//2):
            if words[i] != words[n-i-1]:
                return False
        return True