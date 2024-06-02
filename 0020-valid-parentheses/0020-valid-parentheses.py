class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dist = {'(': ')',
                '{': '}',
                '[': ']'}
        dist2 = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        n = len(s)
        # opening = []
        # closing = []

        # def getSigns():
        #     for i in range(n):
        #         if s[i] in dist.keys():
        #             opening.append(s[i])
        #         else:
        #             closing.append(s[i])
        # getSigns()

        # for i in opening:
        #     close = dist.get(i)
        #     if close in closing:
        #         opening.pop()
        #         closing.remove(close)
        #     else:
        #         return False
        # if not opening and not closing:
        #     return True
        # return False

        for i in range(n):
            curr = s[i]
            if curr in dist.keys():
                stack.append(curr)
            if curr in dist.values():
                if not stack:
                    return False
                else:
                    opens = dist2.get(curr)
                    if curr in dist.values() and stack[-1] != opens:
                        return False
                    stack.pop()
        if not stack:
            return True
        return False