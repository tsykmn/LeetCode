class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        words = "".join(lower(char) for char in s if char.isalpha() or char.isnumeric())
        return words[::] == words[::-1]