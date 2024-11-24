class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # palindrome: characters read same forward and backward
        letters = [w for w in s if (w.isalpha() or w.isnumeric())]
        word = ""
        for l in letters:
            word += l
        word = word.lower()
        return word == word[::-1]