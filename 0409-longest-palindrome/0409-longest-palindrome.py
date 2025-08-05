class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = {}

        for i in s:
            words[i] = words.get(i, 0)+1
        
        total = 0

        for v in words.values():
            if v % 2 == 1:
                total += (v-1)
            else:
                total += v
        return total+1 if total < len(s) else total