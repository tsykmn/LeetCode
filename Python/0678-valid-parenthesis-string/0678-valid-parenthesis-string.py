class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftMin = 0
        leftMax = 0

        for c in s:
            if c == '(':
                leftMin += 1
                leftMax += 1
            elif c == ')':
                leftMin -= 1
                leftMax -= 1
            elif c == '*':
                leftMin -= 1
                leftMax += 1
            
            # more closing parenthesis than opening ones
            if leftMax < 0:
                return False
            elif leftMin < 0: # can't have neg open parenthesis count
                leftMin = 0

        return leftMin == 0