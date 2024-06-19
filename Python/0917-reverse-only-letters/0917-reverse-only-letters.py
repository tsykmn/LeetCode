class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        # get all the letters w/o punctuations
        rev_word = [i for i in s[::-1] if i.isalpha()]
        for i in range(n):
            if not s[i].isalpha():
                rev_word.insert(i, s[i])
        word = ''
        for w in rev_word:
            word += w
        return word