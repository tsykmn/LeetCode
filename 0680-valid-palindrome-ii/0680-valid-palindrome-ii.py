class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        def palindrome(lst):
            return lst == lst[::-1]
        words = [i for i in s if i.isalpha()]
        for i in range(n):
            word = words[:i] +  words[i+1:]
            if palindrome(word):
                return True
        return False

