class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dist = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        total = 0
        pastLetter = ''
        for i in s:
            if pastLetter == 'I' and (i == 'V' or i == 'X'):
                total -= dist[pastLetter]
                total += (dist[i] - dist[pastLetter])
            elif pastLetter == 'X' and (i == 'L' or i=='C'):
                total -= dist[pastLetter]
                total += (dist[i] - dist[pastLetter])
            elif pastLetter == 'C' and (i == 'D' or i == 'M'):
                total -= dist[pastLetter]
                total += (dist[i] - dist[pastLetter])
            else:
                total += dist[i]
            pastLetter = i
        return total