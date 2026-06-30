class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {'(':')', '{':'}', '[':']'}
        open = []
        for b in s:
            if b in brackets.keys():
                open.append(b)
            # elif b in brackets.keys() and open != []:
            #     return False
            elif b in brackets.values() and open == []:
                return False
            elif b in brackets.values():
                last = open.pop()
                if brackets[last] != b:
                    return False
        return len(open) == 0